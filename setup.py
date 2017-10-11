# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from setuptools import setup

import meican

setup(
    name='meican',
    version=meican.__version__,
    description='UNOFFICIAL meican command line / sdk',
    author='Lirian Su',
    author_email='liriansu@gmail.com',
    url='https://github.com/hui-z/meican',
    license='WTFPL',
    entry_points={
        'console_scripts': ['meican = meican.cmdline:execute']
    },
    packages=['meican'],
)
