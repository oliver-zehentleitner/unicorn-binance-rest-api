#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# File: pypi/upload_wheel.sh
#
# Part of ‘UNICORN Binance WebSocket API’
# Project website: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api
# Github: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api
# Documentation: https://unicorn-binance-websocket-api.docs.lucit.tech
# PyPI: https://pypi.org/project/unicorn-binance-websocket-api
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
#
# create this file:
# ~/.pypirc

python3 -m twine upload dist/*
