# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from distutils.core import setup

setup(
    name='meican',
    version='0.0.1',
    description='UNOFFICIAL meican command line / sdk',
    author='Lirian Su',
    author_email='liriansu@gmail.com',
    url='https://github.com/hui-z/mcm',
    license='WTFPL',
    long_description=open('README.rst').read(),
    entry_points={
        'console_scripts': ['mcm = mcm.cmdline:execute']
    },
    packages=['mcm'],
)
