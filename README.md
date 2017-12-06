# MeiCan 美餐
[![PyPI](https://img.shields.io/pypi/v/meican.svg)](https://pypi.python.org/pypi/meican)
[![Travis](https://img.shields.io/travis/hui-z/meican.svg)](https://travis-ci.org/hui-z/meican)

**兼容Python各版本+命令行调用的美餐非官方库**

山上的朋友！
树上的朋友！
有选择困难症的朋友！
每周都忘记点饭的朋友！
每天都想点同一个套餐的朋友！

:ghost: 懒人们！
快快解放双手来点美餐吧~


## 安装

通过pip:

```bash
pip install meican
```

## 代码调用

```python
from meican import MeiCan, MeiCanLoginFail, NoOrderAvailable

try:
    meican = MeiCan('username@domain', 'hunter2')  # login
    dishes = meican.list_dishes()
    if any(dish for dish in dishes if dish.name == '香酥鸡腿'):
        print('今天有香酥鸡腿 :happy:')
    else:
        print('今天没有香酥鸡腿 :sad:')
except NoOrderAvailable:
    print('今天没有开放点餐')
except MeiCanLoginFail:
    print('用户名或者密码不正确')
```


## 命令行调用

```bash
meican  # 查询下次点啥菜
meican -o 香酥  # 点包含 香酥 关键字的菜，比如香酥鸡腿
```


## 其它

最开始是因为[我司](http://www.kezaihui.com/#!/join)用的美餐服务，所以就写个简单脚本内部点餐用。

License 就是宽松的 MIT 协议，欢迎各种 Fork + PR.

各家美餐服务都有不同，也欢迎看看 [wujiyu115](https://github.com/wujiyu115/meican) 的实现。

:wink: 最后欢迎各种 PR
