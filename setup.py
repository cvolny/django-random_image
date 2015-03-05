#!/usr/bin/env python

from setuptools import setup

setup(
    name='RandomDick',
    version='1.0',
    description='RandomDick.pics',
    author='Christopher J. Volny',
    author_email='cvolny@gmail.com',
    url='http://www.thevolny.net/',
    install_requires=['Django==1.7', 'Pillow==2.7.0', 'sorl-thumbnail==12.2', 'mysqlclient']
)
