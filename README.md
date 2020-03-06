# MeiCan 美餐
[![PyPI](https://img.shields.io/pypi/v/meican.svg)](https://pypi.python.org/pypi/meican)
[![Build](https://github.com/LKI/LKI/workflows/Build/badge.svg)](https://github.com/LKI/meican)

> 同时支持 Python 3.5+ 与命令行调用的美餐点餐非官方库

山上的朋友！
树上的朋友！
有选择困难症的朋友！
每周都忘记点饭的朋友！
每天都想点同一个套餐的朋友！

:ghost: 懒人们！
快快解放双手来点美餐吧~


## 背景

最开始是因为[我司](https://www.lagou.com/gongsi/j86312.html)用的美餐服务，
所以就写了个命令行脚本内部点餐用。

后来发现其实大家会有自己动手实现点单逻辑的需求，
就做成了这个开源库啦。


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


## 贡献

不论是任何疑问、想要的功能~~还是想吃的套餐~~都欢迎[直接提 issue](https://github.com/LKI/meican/issues/new)

假如你们公司是用熙香点餐的，
[隔壁也有熙香的库噢~](https://github.com/LKI/xixiang)

:wink: 欢迎各种 PR


## 协议

宽松的 [MIT](https://github.com/LKI/meican/blob/master/LICENSE) 协议：

- ✔ 支持各种改写
- ✔ 支持你把代码作者都改成自己
- ✖ 不支持每天中午免费吃西贝莜面村
- ✖ 也不支持点大羊腿、掌中宝
