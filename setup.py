# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from setuptools import setup

import meican


def get_long_description(readme_file='README.md'):
    with open(readme_file, 'rb') as f:
        return f.read().decode('utf-8')


setup(
    name='meican',
    version=meican.__version__,
    description='UNOFFICIAL meican command line / sdk',
    long_description=get_long_description(),
    author='Lirian Su',
    author_email='liriansu@gmail.com',
    url='https://github.com/hui-z/meican',
    license='MIT License',
    entry_points={
        'console_scripts': ['meican = meican.cmdline:execute']
    },
    packages=['meican'],
)
