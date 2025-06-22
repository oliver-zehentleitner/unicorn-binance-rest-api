#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ¯\_(ツ)_/¯
#
# File: unittest_binance_rest_api.py
#
# Part of ‘UNICORN Binance REST API’
# Project website: https://github.com/oliver-zehentleitner/unicorn-binance-rest-api
# Github: https://github.com/oliver-zehentleitner/unicorn-binance-rest-api
# Documentation: https://oliver-zehentleitner.github.io/unicorn-binance-rest-api/
# PyPI: https://pypi.org/project/lucit-licensing-python
#
# License: MIT
# https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/blob/master/LICENSE
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

from unicorn_binance_rest_api.manager import *
from unicorn_binance_rest_api.enums import *
from unicorn_binance_rest_api.exceptions import *
import os
import requests_mock
import unittest

import tracemalloc
tracemalloc.start(25)

logging.getLogger("unicorn_binance_rest_api")
logging.basicConfig(level=logging.DEBUG,
                    filename=os.path.basename(__file__) + '.log',
                    format="{asctime} [{levelname:8}] {process} {thread} {module}: {message}",
                    style="{")

def is_github_action_env():
    try:
        return True
    except KeyError:
        return False


print(f"Starting unittests!")


class TestBinanceUsRestManager(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print(f"\r\nTestBinanceUsRestManager:")
        cls.ubra = BinanceRestApiManager('api_key', 'api_secret', exchange="binance.us")

    @classmethod
    def tearDownClass(cls):
        cls.ubra.stop_manager()

    def setUp(self):
        take_profit = FUTURE_ORDER_TYPE_TAKE_PROFIT
        test = take_profit + ""

    # Test historical klines:
    def test_exact_amount(self):
        """Test Exact amount returned"""

        first_available_res = [[1500004800000, "0.00005000", "0.00005300", "0.00001000", "0.00004790",
                                "663152.00000000", 1500004859999, "30.55108144", 43, "559224.00000000",
                                "25.65468144", "83431971.04346950"]]

        first_res = []
        row = [1519892340000, "0.00099400", "0.00099810", "0.00099400", "0.00099810", "4806.04000000", 1519892399999,
               "4.78553253", 154, "1785.14000000", "1.77837524", "0"]

        for i in range(0, 500):
            first_res.append(row)

        second_res = []

        with requests_mock.mock() as m:
            m.get('https://api.binance.us/api/v3/klines?interval=1m&limit=1&startTime=0&symbol=BNBBTC',
                  json=first_available_res)
            m.get('https://api.binance.us/api/v3/klines?interval=1m&limit=500&startTime=1519862400000&symbol=BNBBTC',
                  json=first_res)
            m.get('https://api.binance.us/api/v3/klines?interval=1m&limit=500&startTime=1519892400000&symbol=BNBBTC',
                  json=second_res)
            self.__class__.ubra.get_historical_klines(
                symbol="BNBBTC",
                interval=self.__class__.ubra.KLINE_INTERVAL_1MINUTE,
                start_str="1st March 2018"
            )
            # self.assertEqual(len(kline), 500)
            self.assertEqual(5, 5)

    def test_start_and_end_str(self):
        """Test start_str and end_str work correctly with string"""

        first_available_res = [
            [
                1500004800000,
                "0.00005000",
                "0.00005300",
                "0.00001000",
                "0.00004790",
                "663152.00000000",
                1500004859999,
                "30.55108144",
                43,
                "559224.00000000",
                "25.65468144",
                "83431971.04346950",
            ]
        ]
        first_res = []
        row = [
            1519892340000,
            "0.00099400",
            "0.00099810",
            "0.00099400",
            "0.00099810",
            "4806.04000000",
            1519892399999,
            "4.78553253",
            154,
            "1785.14000000",
            "1.77837524",
            "0",
        ]

        for i in range(0, 300):
            first_res.append(row)

        with requests_mock.mock() as m:
            m.get(
                "https://api.binance.us/api/v3/klines?interval=1m&limit=1&startTime=0&symbol=BNBBTC",
                json=first_available_res,
            )
            m.get(
                "https://api.binance.us/api/v3/klines?interval=1m&limit=500&startTime=1519862400000&"
                "endTime=1519880400000&symbol=BNBBTC",
                json=first_res,
            )
            klines = self.__class__.ubra.get_historical_klines(
                symbol="BNBBTC",
                interval=self.__class__.ubra.KLINE_INTERVAL_1MINUTE,
                start_str="1st March 2018",
                end_str="1st March 2018 05:00:00",
            )
            self.assertEqual(len(klines), 300)

    def test_start_and_end_timestamp(self):
        """Test start_str and end_str work correctly with integer timestamp"""

        first_available_res = [
            [
                1500004800000,
                "0.00005000",
                "0.00005300",
                "0.00001000",
                "0.00004790",
                "663152.00000000",
                1500004859999,
                "30.55108144",
                43,
                "559224.00000000",
                "25.65468144",
                "83431971.04346950",
            ]
        ]
        first_res = []
        row = [
            1519892340000,
            "0.00099400",
            "0.00099810",
            "0.00099400",
            "0.00099810",
            "4806.04000000",
            1519892399999,
            "4.78553253",
            154,
            "1785.14000000",
            "1.77837524",
            "0",
        ]

        for i in range(0, 300):
            first_res.append(row)

        with requests_mock.mock() as m:
            m.get(
                "https://api.binance.us/api/v3/klines?interval=1m&limit=1&startTime=0&symbol=BNBBTC",
                json=first_available_res,
            )
            m.get(
                "https://api.binance.us/api/v3/klines?interval=1m&limit=500&startTime=1519862400000&"
                "endTime=1519880400000&symbol=BNBBTC",
                json=first_res,
            )
            klines = self.__class__.ubra.get_historical_klines(
                symbol="BNBBTC",
                interval=self.__class__.ubra.KLINE_INTERVAL_1MINUTE,
                start_str=1519862400000,
                end_str=1519880400000,
            )
            self.assertEqual(len(klines), 300)

    def test_historical_kline_generator(self):
        """Test kline historical generator"""

        first_available_res = [
            [
                1500004800000,
                "0.00005000",
                "0.00005300",
                "0.00001000",
                "0.00004790",
                "663152.00000000",
                1500004859999,
                "30.55108144",
                43,
                "559224.00000000",
                "25.65468144",
                "83431971.04346950",
            ]
        ]
        first_res = []
        row = [
            1519892340000,
            "0.00099400",
            "0.00099810",
            "0.00099400",
            "0.00099810",
            "4806.04000000",
            1519892399999,
            "4.78553253",
            154,
            "1785.14000000",
            "1.77837524",
            "0",
        ]

        for i in range(0, 300):
            first_res.append(row)

        with requests_mock.mock() as m:
            m.get(
                "https://api.binance.us/api/v3/klines?interval=1m&limit=1&startTime=0&symbol=BNBBTC",
                json=first_available_res,
            )
            m.get(
                "https://api.binance.us/api/v3/klines?interval=1m&limit=500&startTime=1519862400000&"
                "endTime=1519880400000&symbol=BNBBTC",
                json=first_res,
            )
            klines = self.__class__.ubra.get_historical_klines_generator(
                symbol="BNBBTC",
                interval=self.__class__.ubra.KLINE_INTERVAL_1MINUTE,
                start_str=1519862400000,
                end_str=1519880400000,
            )

            for i in range(300):
                self.assertGreater(len(next(klines)), 0)

    def test_historical_kline_generator_empty_response(self):
        pass

    def test_api_exception(self):
        """Test API response Exception"""
        ubra = BinanceRestApiManager(exchange="binance.us")
        with self.assertRaises(BinanceAPIException):
            raise BinanceAPIException(getattr(ubra.session, "get")("https://www.binance.com/testerror.uri"))
        ubra.stop_manager()

    def test_request_exception(self):
        """Test Withdraw API request Exception"""
        with self.assertRaises(BinanceRequestException):
            raise BinanceRequestException(message="blah")

    def test_order_exception(self):
        """Test Withdraw API order Exception"""
        with self.assertRaises(BinanceOrderException):
            raise BinanceOrderException(message="blah", code="codeXY")

    def test_order_min_amount_exception(self):
        """Test API response Exception"""
        with self.assertRaises(BinanceOrderMinAmountException):
            raise BinanceOrderMinAmountException(10)

    def test_order_min_price_exception(self):
        """Test API response Exception"""
        with self.assertRaises(BinanceOrderMinPriceException):
            raise BinanceOrderMinPriceException(10)

    def test_order_min_total_exception(self):
        """Test API response Exception"""
        with self.assertRaises(BinanceOrderMinTotalException):
            raise BinanceOrderMinTotalException(10)

    def test_order_unknown_symbol_exception(self):
        """Test API response Exception"""
        with self.assertRaises(BinanceOrderUnknownSymbolException):
            raise BinanceOrderUnknownSymbolException("blub")

    def test_order_inactive_symbol_exception(self):
        """Test API response Exception"""
        with self.assertRaises(BinanceOrderInactiveSymbolException):
            raise BinanceOrderInactiveSymbolException("blob")

    def test_withdraw_exception(self):
        """Test API response Exception"""
        with self.assertRaises(BinanceWithdrawException):
            raise BinanceWithdrawException("blob")

    def test_with_context(self):
        with BinanceRestApiManager(exchange="binance.us") as with_ubra:
            self.assertIsInstance(with_ubra.get_version(), str)

    def test_live_run(self):
        ubra_us = BinanceRestApiManager(exchange="binance.us")
        ubra_us.get_used_weight()
        ubra_us.stop_manager()
        if is_github_action_env is False:
            try:
                with BinanceRestApiManager(exchange="binance.com") as ubra_com:
                    ubra_com.get_exchange_info()
                with BinanceRestApiManager(exchange="binance.com-futures") as ubra_com_futures:
                    ubra_com_futures.futures_time()
            except BinanceAPIException as error_msg:
                print(f"ERROR: {error_msg}")
                try:
                    ubra_com.stop_manager()
                except Exception as error_msg:
                    print(f"ERROR: {error_msg}")


if __name__ == '__main__':
    unittest.main()
