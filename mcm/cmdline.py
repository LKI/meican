#!/usr/bin/env python
# coding=utf-8 #

import sys
import argparse

from meican import Session, Formatter


def execute(argv=None):
    if argv is None:
        argv = sys.argv[1:] or ["-h"]
    parser = argparse.ArgumentParser(description="order meican meal from command line")
    parser.add_argument("-u", "--username", help="meican username (phone or email)", required=True)
    parser.add_argument("-p", "--password", help="meican password", required=True)
    args = parser.parse_args(argv)
    username = args.username
    password = args.password
    print Formatter.json_data(Session(username, password).calendar_items())


if __name__ == '__main__':
    execute()
