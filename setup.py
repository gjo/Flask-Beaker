#! /usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='Flask-Beaker',
    version='0.1',
    author='OCHIAI, Gouji',
    author_email='gjo.ext@gmail.com',
    url='http://github.com/gjo/Flask-Beaker',
    description='flask extension for beaker',
    long_description=open('README.rst').read(),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools', 'Flask', 'Beaker'],
    )
