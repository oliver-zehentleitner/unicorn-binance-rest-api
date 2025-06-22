#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: example_buy_and_sell_oco_order_isolated_margin.py
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
import logging
import os

# https://docs.python.org/3/library/logging.html#logging-levels
logging.getLogger("unicorn_binance_rest_api")
logging.basicConfig(level=logging.DEBUG,
                    filename=os.path.basename(__file__) + '.log',
                    format="{asctime} [{levelname:8}] {process} {thread} {module}: {message}",
                    style="{")

# Define API Key and Secret
API_KEY = ""
API_SECRET = ""

# Define quantity in USDT to buy
BUY_QUANTITY_USDT = 15

# Define number of decimal places to round prices
ROUND_DECIMAL_PLACES = 2

# Define the time in force for the stop limit order
STOP_LIMIT_TIME_IN_FORCE = "GTC"  # ENUM: GTC, FOK, IOC - https://www.delta.exchange/blog/support/time-in-force-flags-on-delta-exchange-fok-ioc-gtc

# Define the percentage gap between the buy price and the stop loss price
STOP_LOSS_GAP_TO_BUY_PRICE_IN_PERCENT = 2

# Define the gap in USDT between the stop loss trigger and the stop loss price
STOP_LOSS_TRIGGER_GAP_USDT = 0.01

# Define the percentage gap between the buy price and the take profit price
TAKE_PROFIT_GAP_TO_BUY_PRICE_IN_PERCENT = 2

# Create a BinanceRestApiManager instance with the exchange and API credentials
# To use this library you need a valid UNICORN Binance Suite License: https://technopathy.club/87b0088124a8
ubra = BinanceRestApiManager(exchange="binance.com-isolated_margin", api_key=API_KEY, api_secret=API_SECRET)

# Buy BTC with a market order using the specified USDT quantity
buy_order = ubra.create_margin_order(symbol="BTCUSDT",
                                     isIsolated="TRUE",
                                     side="BUY",
                                     type="MARKET",
                                     quoteOrderQty=BUY_QUANTITY_USDT)
print(f"Buy Order Result: {buy_order}")

# If the buy order was filled
if buy_order['status'] == "FILLED":
    # Calculate prices
    buy_price = float(buy_order['fills'][0]['price'])
    take_profit_price = buy_price * (100+TAKE_PROFIT_GAP_TO_BUY_PRICE_IN_PERCENT) / 100
    stop_loss_price = buy_price * (100-STOP_LOSS_GAP_TO_BUY_PRICE_IN_PERCENT) / 100
    stop_loss_price_trigger = stop_loss_price + STOP_LOSS_TRIGGER_GAP_USDT

    # Sell BTC with TakeProfit or StopLoss (oco order)
    oco_sell_order = ubra.create_margin_oco_order(symbol="BTCUSDT",
                                                  isIsolated="TRUE",
                                                  price=round(take_profit_price, ROUND_DECIMAL_PLACES),
                                                  quantity=buy_order['executedQty'],
                                                  side="SELL",
                                                  stopPrice=round(stop_loss_price_trigger, ROUND_DECIMAL_PLACES),
                                                  stopLimitPrice=round(stop_loss_price, ROUND_DECIMAL_PLACES),
                                                  stopLimitTimeInForce=STOP_LIMIT_TIME_IN_FORCE)
    print(f"OCO Order Result: {oco_sell_order}")