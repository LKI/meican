#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import argparse
import sys

from tools import MeiCan
from settings import MeiCanSetting
from utils import json_dump


def execute(argv=None):
    if argv is None:
        argv = sys.argv[1:] or []
    parser = argparse.ArgumentParser(description='order meican meal from command line')
    parser.add_argument('-o', '--order', help='order meal')
    args = parser.parse_args(argv)

    settings = MeiCanSetting()
    settings.load_credentials()
    meican = MeiCan(settings.username, settings.password)

    try:
        dish_list = meican.list_dish()
    except IndexError:
        print('there is no available order to make!')
        return
    if args.order:
        order = args.order.decode('utf8')
        dish_list = filter(lambda x: order in x['name'], dish_list)
        if len(dish_list) == 1:
            meican.order(int(dish_list[0].get('id')))
            print('done!')
        else:
            print('error! you should specify an only one matching pattern')
    print(json_dump([_.get('name') for _ in dish_list]))


if __name__ == '__main__':
    execute()
