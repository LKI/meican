# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


class MeiCanError(Exception):
    """
    啊，又出错了
    """
    pass


class MeiCanKeyError(MeiCanError):
    """
    MeiCan 接口改了

    要么就是哪里写了屎代码

    反正就是 dict key 不对
    """
    pass


class NoOrderAvailable(MeiCanError):
    """ 目前还点不了餐 """
    pass
