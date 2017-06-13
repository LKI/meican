# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from setuptools import setup

setup(
    name='meican',
    version='0.1.0',
    description='UNOFFICIAL meican command line / sdk',
    author='Lirian Su',
    author_email='liriansu@gmail.com',
    url='https://github.com/hui-z/meican',
    license='WTFPL',
    entry_points={
        'console_scripts': ['meican = cmdline:execute']
    },
    packages=['meican'],
)
