# MeiCan 美餐点菜
[![Package](https://img.shields.io/pypi/v/meican.svg)](https://pypi.python.org/pypi/meican)

**非官方的Python包 / 命令行点美餐工具（首先你要有一个账号）。**

山上的朋友！
树上的朋友！
有选择困难症的朋友！
每周都忘记点饭的朋友！
每天都想点同一个套餐的朋友！
:ghost: 懒人们！
快快解放双手来点美餐吧~


## 安装 / 使用

通过pip安装：

```bash
pip install meican
```

或者是命令行安装：

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
