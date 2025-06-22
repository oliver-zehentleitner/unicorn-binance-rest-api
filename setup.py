#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: setup.py
#
# Part of ‘UNICORN Binance REST API’
# Project website: https://github.com/oliver-zehentleitner/unicorn-binance-rest-api
# Github: https://github.com/oliver-zehentleitner/unicorn-binance-rest-api
# Documentation: https://oliver-zehentleitner.github.io/unicorn-binance-rest-api
# PyPI: https://pypi.org/project/unicorn-binance-rest-api
#
# License: MIT
# https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/blob/master/LICENSE
#
# Author: Oliver Zehentleitner
#
# Copyright (c) 2017-2021, MIT License, Sam McHardy (https://github.com/sammchardy)
# Copyright (c) 2021-2025, Oliver Zehentleitner (https://about.me/oliver-zehentleitner)
#
# All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from Cython.Build import cythonize
from setuptools import setup, find_packages, Extension
import os
import shutil
import subprocess

name = "unicorn-binance-rest-api"
source_dir = "unicorn_binance_rest_api"

stubs_dir = "stubs"
extensions = [
    Extension("*", [f"{source_dir}/*.py"]),
]

# Setup
print("Generating stub files ...")
os.makedirs(stubs_dir, exist_ok=True)
for filename in os.listdir(source_dir):
    if filename.endswith('.py'):
        source_path = os.path.join(source_dir, filename)
        subprocess.run(['stubgen', '-o', stubs_dir, source_path], check=True)
for stub_file in os.listdir(os.path.join(stubs_dir, source_dir)):
    if stub_file.endswith('.pyi'):
        source_stub_path = os.path.join(stubs_dir, source_dir, stub_file)
        if os.path.exists(os.path.join(source_dir, stub_file)):
            print(f"Skipped moving {source_stub_path} because {os.path.join(source_dir, stub_file)} already exists!")
        else:
            shutil.move(source_stub_path, source_dir)
            print(f"Moved {source_stub_path} to {source_dir}!")
shutil.rmtree(os.path.join(stubs_dir))
print("Stub files generated and moved successfully.")

with open("README.md", "r") as fh:
    print("Using README.md content as `long_description` ...")
    long_description = fh.read()

setup(
     name=name,
     version="2.8.0",
     author="Oliver Zehentleitner",
     url="https://github.com/oliver-zehentleitner/unicorn-binance-rest-api",
     description="A Python SDK to use the Binance REST API`s (com+testnet, com-margin+testnet, "
                 "com-isolated_margin+testnet, com-futures+testnet, us, tr) in a simple, fast, flexible, robust and "
                 "fully-featured way.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     license='MIT',
     install_requires=['certifi>=2023.7.22', 'colorama', 'cryptography>=42.0.4', 'dateparser', 'pyOpenSSL',
                       'requests>=2.31.0', 'service-identity', 'ujson', 'regex', 'PySocks', 'Cython'],
     keywords='',
     project_urls={
         'Howto': 'https://github.com/oliver-zehentleitner/unicorn-binance-rest-api#howto',
         'Documentation': 'https://oliver-zehentleitner.github.io/unicorn-binance-rest-api',
         'Changes': 'https://oliver-zehentleitner.github.io/unicorn-binance-rest-api/changelog.html',
         'License': 'https://oliver-zehentleitner.github.io/unicorn-binance-rest-api/license.html',
         'Issue Tracker': 'https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/issues',
         'Wiki': 'https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/wiki',
         'Author': 'https://www.linkedin.com/in/oliver-zehentleitner',
         'Telegram': 'https://t.me/unicorndevs',
     },
     packages=find_packages(exclude=[f"dev/{source_dir}"], include=[source_dir]),
     ext_modules=cythonize(extensions, compiler_directives={'language_level': "3"}),
     python_requires='>=3.8.0',
     package_data={'': ['*.so', '*.dll', '*.py', '*.pyd', '*.pyi']},
     include_package_data=True,
     classifiers=[
         "Development Status :: 5 - Production/Stable",
         "Programming Language :: Python :: 3.8",
         "Programming Language :: Python :: 3.9",
         "Programming Language :: Python :: 3.10",
         "Programming Language :: Python :: 3.11",
         "Programming Language :: Python :: 3.12",
         "Programming Language :: Python :: 3.13",
         "License :: Other/Proprietary License",
         'Intended Audience :: Developers',
         "Intended Audience :: Financial and Insurance Industry",
         "Intended Audience :: Information Technology",
         "Intended Audience :: Science/Research",
         "Operating System :: OS Independent",
         "Topic :: Office/Business :: Financial :: Investment",
         'Topic :: Software Development :: Libraries :: Python Modules',
     ],
)

