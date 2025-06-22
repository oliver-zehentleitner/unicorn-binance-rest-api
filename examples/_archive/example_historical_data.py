#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: example_historical_data.py
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

api_key = "*"
api_secret = "*"

# To use this library you need a valid UNICORN Binance Suite License: https://technopathy.club/87b0088124a8
ubra = BinanceRestApiManager(api_key, api_secret)

# Retrieve 1-minute klines for the last day so far
klines_1m = ubra.get_historical_klines("BTCUSDT", ubra.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")
print(f"klines_1m:\r\n{klines_1m}")

# Retrieve 30-minute klines for the last month of 2021
klines_30m = ubra.get_historical_klines("BTCUSDT", "30m", "1 Dec, 2021", "1 Jan, 2022")
print(f"klines_30m:\r\n{klines_30m}")

# Retrieve weekly klines since they are listed
klines_1w = ubra.get_historical_klines("BNBBTC", "1w", "1 Jan, 2017")
print(f"klines_1w:\r\n{klines_1w}")

ubra.stop_manager()
