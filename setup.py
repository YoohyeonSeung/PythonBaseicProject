# -*- coding : utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='sample',
    version='0.1.0',
    description='Sample package',
    author='Hyeon-seung Yoo',
    packages=find_packages(exclude=('tests', ))

)