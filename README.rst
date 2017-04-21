===========
MeiCan 美餐点菜
===========

非官方的Python包 / 命令行。

山上的朋友！
树上的朋友！
有选择困难症的朋友！
每周都忘记点饭的朋友！
每天都想点同一个套餐的朋友！
:ghost: 懒人们！
快快解放双手来点美餐吧~

===============
Installation 安装
===============

通过pip安装：
::

    pip install meican

或者是命令行安装：
::

    git clone git@github.com:hui-z/meican.git ~/.meican && cd ~/.meican && pip install -r requirements.txt  # 用git把项目克隆到本地并且安装项目依赖
    alias meican="python ~/.meican/meican/cmdline.py"

装好以后，
就可以直接通过命令行调用了~

::

    meican  # 查询下次点啥菜
    meican -o 香酥  # 点包含 香酥 关键字的菜，比如香酥鸡腿

=======
License
=======

WTFPL
http://www.wtfpl.net
简单来说就是你想干啥都行...

有个小伙伴基于本repo开发了更高端的功能，
各位也可以去参考下：
https://github.com/wujiyu115/meican
