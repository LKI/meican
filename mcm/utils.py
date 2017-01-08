# coding=utf-8 #
from __future__ import unicode_literals

import datetime
import json


def milli_to_datetime(milliseconds):
    return datetime.date(1970, 1, 1) + datetime.timedelta(milliseconds=int(milliseconds))


def json_dump(data):
    return json.dumps(data, ensure_ascii=False, indent=2)
