# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')

# get version from __version__ variable in cloudcentrics/__init__.py
from cloudcentrics import __version__ as version

setup(
    name='cloudcentrics',
    version=version,
    description='ERPNext Cloudcentrics',
    author='Cloud Centrics',
    author_email='learn.with.bilal@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
