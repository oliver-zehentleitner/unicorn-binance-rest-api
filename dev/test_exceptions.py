#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: dev/test_exceptions.py
#
# Part of ‘UNICORN Binance REST API’
# Project website: https://github.com/oliver-zehentleitner/unicorn-binance-rest-api
# Github: https://github.com/oliver-zehentleitner/unicorn-binance-rest-api
# Documentation: https://oliver-zehentleitner.github.io/unicorn-binance-rest-api/
# PyPI: https://pypi.org/project/lucit-licensing-python
#
# License: LSOSL - LUCIT Synergetic Open Source License
# https://github.com/oliver-zehentleitner/lucit-licensing-python/blob/master/LICENSE
#
# Author: Oliver Zehentleitner
#
# Copyright (c) 2017-2021, Sam McHardy (https://github.com/sammchardy)
# Copyright (c) 2021-2023, LUCIT Systems and Development (https://www.lucit.tech)
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

from unicorn_binance_rest_api.manager import BinanceRestApiManager
from unicorn_binance_rest_api.exceptions import AlreadyStoppedError, UnknownExchange
from lucit_licensing_python.exceptions import NoValidatedLucitLicense
import logging
import os

# https://docs.python.org/3/library/logging.html#logging-levels
logging.getLogger("unicorn_binance_rest_api")
logging.basicConfig(level=logging.DEBUG,
                    filename=os.path.basename(__file__) + '.log',
                    format="{asctime} [{levelname:8}] {process} {thread} {module}: {message}",
                    style="{")

api_key = "aaa"
api_secret = "bbb"

try:
    # To use this library you need a valid UNICORN Binance Suite License:
    # https://technopathy.club/87b0088124a8
    with BinanceRestApiManager(api_key, api_secret, lucit_license_profile="LUCIT") as ubra:
        print(ubra.get_version())
        print(ubra.get_server_time())
        print(ubra.get_ticker(symbol="BNBUSDT"))

    print(f"Leaving ubra context manager")
    print(ubra.get_ticker(symbol="BNBUSDT"))
except NoValidatedLucitLicense as error_msg:
    print(f"ERROR LEVEL 1: {error_msg}")
except AlreadyStoppedError as error_msg:
    print(f"ERROR LEVEL 1: {error_msg}")

try:
    # To use this library you need a valid UNICORN Binance Suite License:
    # https://technopathy.club/87b0088124a8
    with BinanceRestApiManager(api_key, api_secret, exchange="test-error") as ubra:
        print(ubra.get_version())
        print(ubra.get_server_time())
        print(ubra.get_ticker(symbol="BNBUSDT"))

    print(f"Leaving ubra context manager")
    print(ubra.get_ticker(symbol="BNBUSDT"))
except NoValidatedLucitLicense as error_msg:
    print(f"ERROR LEVEL 1: {error_msg}")
except UnknownExchange as error_msg:
    print(f"ERROR LEVEL 1: {error_msg}")
except AlreadyStoppedError as error_msg:
    print(f"ERROR LEVEL 1: {error_msg}")
