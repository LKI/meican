# -*- coding: utf-8 -*-

================
MeiCan Meal 美餐点菜
================

山上的朋友！
树上的朋友！
有选择困难症的朋友！
每周都忘记点饭的朋友！
每天都想点同一个套餐的朋友！
:ghost: 懒人们！

快快使用本Python脚本解放双手来美餐点餐吧~

===============
Installation 安装
===============

通过pip安装：
::

    pip install meican

或者是命令行安装：
::

    git clone git@github.com:hui-z/mcm.git ~/.mcm && cd ~/.mcm && pip install -r requirements.txt
    ln -sf ~/.mcm/mcm/cmdline.py /usr/bin/mcm

=======
目前支持的命令
=======

::

    mcm -u <me@liriansu.com> -p <hunter2>  # 查询下次可以点的菜
    mcm -u <me@liriansu.com> -p <hunter2> -o 香酥  # 点香酥鸡腿

=======
License
=======

WTFPL
http://www.wtfpl.net
简单来说就是你想干啥都行...

有个小伙伴基于本repo开发了更高端的功能，
各位也可以去参考下：
https://github.com/wujiyu115/meican
