# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


class MeiCanError(Exception):
    """ MeiCan 包产生的错误 """


class MeiCanKeyError(MeiCanError):
    """ MeiCan 接口更改导致的 Dict Key 错误 """


class NoOrderAvailable(MeiCanError):
    """ 目前还点不了餐 """
