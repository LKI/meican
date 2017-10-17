# MeiCan 美餐点菜
[![PyPI](https://img.shields.io/pypi/v/meican.svg)](https://pypi.python.org/pypi/meican)
[![Travis](https://img.shields.io/travis/hui-z/meican.svg)](https://travis-ci.org/hui-z/meican)

**非官方的Python包，支持命令行调用。**

山上的朋友！
树上的朋友！
有选择困难症的朋友！
每周都忘记点饭的朋友！
每天都想点同一个套餐的朋友！

:ghost: 懒人们！
快快解放双手来点美餐吧~


## 代码调用（推荐）

通过pip安装：

```bash
pip install meican
```

样例Python代码（想实现更多操作请读源码）：

```python
from meican import MeiCan,MeiCanError,NoOrderAvailable

try:
    meican = MeiCan('username@domain', 'hunter2')  # login
    dishes = meican.list_dishes()
    if any(dish for dish in dishes if dish.name == '香酥鸡腿'):
        print('今天有香酥鸡腿 :happy:')
    else:
        print('今天没有香酥鸡腿 :sad:')
except NoOrderAvailable:
    print('今天没有开放点餐')
except MeiCanError:
    print('用户名或者密码不正确')
```


## 命令行调用

```bash
git clone git@github.com:hui-z/meican.git ~/.meican && cd ~/.meican && pip install -r requirements.txt  # 用git把项目克隆到本地并且安装项目依赖
alias meican="python ~/.meican/meican/cmdline.py"
```

装好以后，
就可以直接通过命令行调用了~

```bash
meican  # 查询下次点啥菜
meican -o 香酥  # 点包含 香酥 关键字的菜，比如香酥鸡腿
```
