#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import argparse
import sys

import settings
from meican import Session
from utils import json_dump


def execute(argv=None):
    if argv is None:
        argv = sys.argv[1:] or ["-h"]
    parser = argparse.ArgumentParser(description="order meican meal from command line")
    parser.add_argument("-u", "--username", help="meican username (phone or email)")
    parser.add_argument("-p", "--password", help="meican password")
    parser.add_argument("-o", "--order", help="order meal")
    args = parser.parse_args(argv)
    username = args.username or settings.username
    password = args.password or settings.password

    s = Session(username, password)
    dish_list = s.list_dish()
    if args.order:
        order = args.order.decode('utf8')
        dish_list = filter(lambda x: order in x['name'], dish_list)
        if len(dish_list) == 1:
            s.order(int(dish_list[0].get('id')))
            print("done!")
        else:
            print("error! you should specify an only one matching pattern")
    print(json_dump([_.get('name') for _ in dish_list]))


if __name__ == '__main__':
    execute()
