#!/usr/bin/bash

rm *.log
rm dev/*.log

rm build -r
rm dist -r
rm *.egg-info -r
rm stubs -r
rm out -r

rm unicorn_binance_rest_api/*.c
rm unicorn_binance_rest_api/*.html
rm unicorn_binance_rest_api/*.dll
rm unicorn_binance_rest_api/*.so
rm unicorn_binance_rest_api/*.pyi