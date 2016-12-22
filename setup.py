# -*- coding: utf-8 -*-
# @Author: darkshadows123
# @Last Modified by:   darkshadows123


from distutils.core import setup
from setuptools import find_packages

setup(
    name='ipAddressExtractor',
    version='0.3.2',
    description='ipAddressExtractor',
    author='Rishit Jain',
    author_email='rishitja@usc.edu',
    url='https://github.com/darkshadows123/ip-address-extractor',
    download_url='https://github.com/darkshadows123/ip-address-extractor',
    packages=find_packages(),
    keywords=['ip address', 'extractor'],
    install_requires=['digExtractor']
)
