class MeiCanError(Exception):
    """MeiCan 包产生的错误"""


class MeiCanKeyError(MeiCanError):
    """MeiCan 接口更改导致的 Dict Key 错误"""


class MeiCanLoginFail(MeiCanError):
    """用户名或密码错误，导致的登录失败"""


class NoOrderAvailable(MeiCanError):
    """目前还点不了餐"""
