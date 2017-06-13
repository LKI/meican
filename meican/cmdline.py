#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import argparse
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from meican.exceptions import NoOrderAvailable
from meican.settings import MeiCanSetting
from meican.tools import MeiCan


def initialize_meican():
    settings = MeiCanSetting()
    settings.load_credentials()
    return MeiCan(settings.username, settings.password)


def execute(argv=None):
    if argv is None:
        argv = sys.argv[1:] or []
    parser = argparse.ArgumentParser(description='命令行点美餐的工具')
    parser.add_argument('-o', '--order', help='order meal')
    args = parser.parse_args(argv)

    meican = initialize_meican()

    try:
        dishes = meican.list_dishes()
    except NoOrderAvailable:
        print('别急，下一顿还没开放订餐')
        return
    if args.order:
        keyword = args.order.decode('utf-8')
        dishes = [_ for _ in dishes if keyword in _.name]
        if len(dishes) == 1:
            meican.order(dishes[0])
            print('done!')
        elif not dishes:
            print('没有找到 {} 的对应菜品'.format(keyword))
        else:
            print('找到多于一个菜品，请指定更详细的关键词')
            print('\n'.join(['{}'.format(_) for _ in dishes]))


if __name__ == '__main__':
    execute()
