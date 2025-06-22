[![GitHub Release](https://img.shields.io/github/release/oliver-zehentleitner/unicorn-binance-rest-api.svg?label=github&color=blue)](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/releases)
[![GitHub Downloads](https://img.shields.io/github/downloads/oliver-zehentleitner/unicorn-binance-rest-api/total?color=blue)](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/releases)
[![PyPi Release](https://img.shields.io/pypi/v/unicorn-binance-rest-api?color=blue)](https://pypi.org/project/unicorn-binance-rest-api/)
[![PyPi Downloads](https://pepy.tech/badge/unicorn-binance-rest-api)](https://pepy.tech/project/unicorn-binance-rest-api)
[![License](https://img.shields.io/github/license/oliver-zehentleitner/unicorn-binance-rest-api.svg?color=blue)](https://oliver-zehentleitner.github.io/unicorn-binance-rest-apilicense.html)
[![Supported Python Version](https://img.shields.io/pypi/pyversions/unicorn_binance_rest_api.svg)](https://www.python.org/downloads/)
[![PyPI - Status](https://img.shields.io/pypi/status/unicorn_binance_rest_api.svg)](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/issues)
[![codecov](https://codecov.io/gh/oliver-zehentleitner/unicorn-binance-rest-api/graph/badge.svg?token=P7XILPPSLU)](https://codecov.io/gh/oliver-zehentleitner/unicorn-binance-rest-api)
[![CodeQL](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/actions/workflows/codeql-analysis.yml)
[![Unittests](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/actions/workflows/unit-tests.yml)
[![Build and Publish GH+PyPi](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/actions/workflows/build_wheels.yml/badge.svg)](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/actions/workflows/build_wheels.yml)
[![Read the Docs](https://img.shields.io/badge/read-%20docs-yellow)](https://oliver-zehentleitner.github.io/unicorn-binance-rest-api/)
[![Read How To`s](https://img.shields.io/badge/read-%20howto-yellow)](https://technopathy.club)
[![Github](https://img.shields.io/badge/source-github-cbc2c8)](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api)
[![Telegram](https://img.shields.io/badge/community-telegram-41ab8c)](https://t.me/unicorndevs)

[![LUCIT-UBRA-Banner](https://raw.githubusercontent.com/oliver-zehentleitner/unicorn-binance-rest-api/master/images/logo/LUCIT-UBRA-Banner-Readme.png)](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api)

# UNICORN Binance REST API

[Description](#description) | [Installation](#installation-and-upgrade) | [How To](#howto) |
[Documentation](#documentation) | [Examples](#examples) | [Change Log](#change-log) | [Wiki](#wiki) | [Social](#social) |
[Notifications](#receive-notifications) | [Bugs](#how-to-report-bugs-or-suggest-improvements) | 
[Contributing](#contributing) | [Disclaimer](#disclaimer)

A Python SDK to use the Binance REST API`s (com+testnet, com-margin+testnet, com-isolated_margin+testnet, 
com-futures+testnet, us, tr) in a simple, fast, flexible, robust and fully-featured way. 

Part of ['UNICORN Binance Suite'](https://github.com/oliver-zehentleitner/unicorn-binance-suite).

## Receive Data from Binance REST API Endpoints

### Initiate `BinanceRestApiManager()`
```
from unicorn_binance_rest_api import BinanceRestApiManager

ubra = BinanceRestApiManager(api_key="YOUR_BINANCE_API_KEY", 
                             api_secret="YOUR_BINANCE_API_SECRET", 
                             exchange="binance.com")
```

### Print a snapshot of an order book
```
print(f"BNBBTC order book: {ubra.get_order_book(symbol='BNBBTC')}")
```

### Get all symbol prices
```
print(f"All tickers:\r\n{ubra.get_all_tickers()}")
```

### Get the used weight 
***Please Note:*** 
https://github.com/binance-us/binance-official-api-docs/blob/master/rest-api.md#limits

```
print(f"Used weight: {ubra.get_used_weight()}")
```

## Send data to Binance REST API Endpoints
### Initiate `BinanceRestApiManager()`

```
ubra = BinanceRestApiManager(api_key="YOUR_BINANCE_API_KEY", 
                             api_secret="YOUR_BINANCE_API_SECRET", 
                             exchange="binance.com-isolated_margin")
```

### Buy BTC with a market order using 100 USDT
```
buy_order = ubra.create_margin_order(symbol="BTCUSDT",
                                     isIsolated="TRUE",
                                     side="BUY",
                                     type="MARKET",
                                     quoteOrderQty=100)
print(f"Buy Order Result: {buy_order}")
```

## Stop `ubra` after usage to avoid memory leaks

When you instantiate UBRA with `with`, `ubra.stop_manager()` is automatically executed upon exiting the `with`-block.

```
with BinanceRestApiManager() as ubra:
    depth = ubra.get_order_book(symbol='BNBBTC')
```

Without `with`, you must explicitly execute `ubra.stop_manager()` yourself.

```
ubra.stop_manager()
```

## More?
[Discover even more possibilities](https://oliver-zehentleitner.github.io/unicorn-binance-rest-api/unicorn_binance_rest_api.html) 
or try our [examples](#examples)!

## Description
The Python module [UNICORN Binance REST API](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api) 
provides an API to the Binance REST API`s of 
[Binance](https://github.com/binance-exchange/binance-official-api-docs) 
([+Testnet](https://testnet.binance.vision/)), 
[Binance Margin](https://binance-docs.github.io/apidocs/spot/en/#user-data-streams) 
([+Testnet](https://testnet.binance.vision/)), 
[Binance Isolated Margin](https://binance-docs.github.io/apidocs/spot/en/#listen-key-isolated-margin)
([+Testnet](https://testnet.binance.vision/)), 
[Binance Futures](https://binance-docs.github.io/apidocs/futures/en/#websocket-market-streams) 
([+Testnet](https://testnet.binancefuture.com)), 
[Binance COIN-M Futures](https://binance-docs.github.io/apidocs/delivery/en/#change-log),
[Binance US](https://github.com/binance-us/binance-official-api-docs) and
[Binance TR](https://www.trbinance.com/apidocs) and needs to be used with a valid 
[api_key and api_secret](https://technopathy.club/how-to-create-a-binance-api-key-and-api-secret-3bb5f47e360d)
from the Binance Exchange 
[www.binance.com](https://www.binance.com/userCenter/createApi.html), 
[testnet.binance.vision](https://testnet.binance.vision/) or
[www.binance.us](https://www.binance.us/userCenter/createApi.html).

Be aware that the Binance REST API is request based. if you want to send and receive high frequency and high volume 
data, you can use the [UNICORN Binance Websocket API](https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api) in 
combination. 

### What are the benefits of the UNICORN Binance REST API?
- Supported exchanges:

| Exchange                                                           | Exchange string                       |
|--------------------------------------------------------------------|---------------------------------------|
| [Binance](https://www.binance.com)                                 | `binance.com`                         |
| [Binance Testnet](https://testnet.binance.vision/)                 | `binance.com-testnet`                 |
| [Binance Margin](https://www.binance.com)                          | `binance.com-margin`                  |
| [Binance Margin Testnet](https://testnet.binance.vision/)          | `binance.com-margin-testnet`          |
| [Binance Isolated Margin](https://www.binance.com)                 | `binance.com-isolated_margin`         |
| [Binance Isolated Margin Testnet](https://testnet.binance.vision/) | `binance.com-isolated_margin-testnet` |
| [Binance USD-M Futures](https://www.binance.com)                   | `binance.com-futures`                 |
| [Binance USD-M Futures Testnet](https://testnet.binancefuture.com) | `binance.com-futures-testnet`         |
| [Binance Coin-M Futures](https://www.binance.com)                  | `binance.com-coin_futures`            |
| [Binance US](https://www.binance.us)                               | `binance.us`                          |
| [Binance TR](https://www.trbinance.com)                            | `trbinance.com`                       |

- Helpful management features like 
[`get_used_weight()`](https://oliver-zehentleitner.github.io/unicorn-binance-rest-api/unicorn_binance_rest_api.html#unicorn_binance_rest_api.manager.BinanceRestApiManager.get_used_weight), 

- Available as a package via `pip` and `conda` as precompiled C extension with stub files for improved Intellisense 
  functions and source code for easier debugging of the source code. [To the installation.](#installation-and-upgrade)

- Integration of [test cases](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/actions/workflows/unit-tests.yml) and [examples](#examples).

- Customizable base URL and request timeout.

- *Socks5 Proxy* support:
  ```
  ubra = BinanceRestApiManager(exchange="binance.com", socks5_proxy_server="127.0.0.1:9050") 
  ```
  Read the [docs](https://oliver-zehentleitner.github.io/unicorn-binance-rest-api/unicorn_binance_rest_api.html#unicorn_binance_rest_api.manager.BinanceRestApiManager)
  or this [how to](https://medium.com/@oliverzehentleitner/how-to-connect-to-binance-com-rest-api-using-python-via-a-socks5-proxy-638dbbecacfd) 
  for more information or try 
  [example_socks5_proxy.py](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/blob/master/examples/_archive/example_socks5_proxy.py).

- Excessively tested on Linux, Mac and Windows

If you like the project, please [![star](https://raw.githubusercontent.com/oliver-zehentleitner/unicorn-binance-rest-api/master/images/misc/star.png)](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/stargazers) it on 
[GitHub](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api)!

## Installation and Upgrade
The module requires Python 3.8 and runs smoothly up to and including Python 3.13.

[There is no conda support until the migration to conda-forge.](https://github.com/oliver-zehentleitner/unicorn-binance-suite/issues/17)

For the PyPy interpreter we offer packages only from Python version 3.9 and higher.

The current dependencies are listed 
[here](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/blob/master/requirements.txt).

If you run into errors during the installation take a look [here](https://github.com/oliver-zehentleitner/unicorn-binance-suite/wiki/Installation).

### Packages are created automatically with GitHub Actions
When a new release is to be created, we start two GitHubActions: 

- [Build and Publish Anaconda](https://github.com/oliver-zehentleitner/unicorn-binance-suite/issues/17)
- [Build and Publish GH+PyPi](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/actions/workflows/build_wheels.yml) 

Both start virtual Windows/Linux/Mac servers provided by GitHub in the cloud with preconfigured environments and 
create the respective compilations and stub files, pack them into wheels and conda packages and then publish them on 
GitHub, PYPI and Anaconda. This is a transparent method that makes it possible to trace the source code behind a 
compilation.

### A Cython binary, PyPy or source code based CPython wheel of the latest version with `pip` from [PyPI](https://pypi.org/project/unicorn-binance-rest-api/)
Our [Cython](https://cython.org/) and [PyPy](https://www.pypy.org/) Wheels are available on [PyPI](https://pypi.org/), 
these wheels offer significant advantages for Python developers:

- ***Performance Boost with Cython Wheels:*** Cython is a programming language that supplements Python with static typing and C-level performance. By compiling 
  Python code into C, Cython Wheels can significantly enhance the execution speed of Python code, especially in 
  computationally intensive tasks. This means faster runtimes and more efficient processing for users of our package. 

- ***PyPy Wheels for Enhanced Efficiency:*** PyPy is an alternative Python interpreter known for its speed and efficiency. It uses Just-In-Time (JIT) compilation, 
  which can dramatically improve the performance of Python code. Our PyPy Wheels are tailored for compatibility with 
  PyPy, allowing users to leverage this speed advantage seamlessly.

Both Cython and PyPy Wheels on PyPI make the installation process simpler and more straightforward. They ensure that 
you get the optimized version of our package with minimal setup, allowing you to focus on development rather than 
configuration.

On Raspberry Pi and other architectures for which there are no pre-compiled versions, the package can still be 
installed with PIP. PIP then compiles the package locally on the target system during installation. Please be patient, 
this may take some time!

#### Installation
`pip install unicorn-binance-rest-api`

#### Update
`pip install unicorn-binance-rest-api --upgrade`

### A Conda Package of the latest version with `conda` from [Anaconda](https://anaconda.org/lucit)
[There is no conda support until the migration to conda-forge.](https://github.com/oliver-zehentleitner/unicorn-binance-suite/issues/17)

The `unicorn-binance-rest-api` package is also available as a Cython version for the `linux-64`, `osx-64` 
and `win-64` architectures with [Conda](https://docs.conda.io/en/latest/) through the 
[`lucit` channel](https://anaconda.org/lucit). 

For optimal compatibility and performance, it is recommended to source the necessary dependencies from the 
[`conda-forge` channel](https://anaconda.org/conda-forge). 

#### Installation
[There is no conda support until the migration to conda-forge.](https://github.com/oliver-zehentleitner/unicorn-binance-suite/issues/17)

```
conda config --add channels conda-forge
conda config --add channels lucit
conda install -c lucit unicorn-binance-rest-api
```

#### Update
[There is no conda support until the migration to conda-forge.](https://github.com/oliver-zehentleitner/unicorn-binance-suite/issues/17)

`conda update -c lucit unicorn-binance-rest-api`

### From source of the latest release with PIP from [GitHub](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api)
#### Linux, macOS, ...
Run in bash:

`pip install https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/archive/$(curl -s https://api.github.com/repos/oliver-zehentleitner/unicorn-binance-rest-api/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")').tar.gz --upgrade`

#### Windows
Use the below command with the version (such as 2.8.0) you determined 
[here](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/releases/latest):

`pip install https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/archive/2.8.0.tar.gz --upgrade`

### From the latest source (dev-stage) with PIP from [GitHub](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api)
This is not a release version and can not be considered to be stable!

`pip install https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/tarball/master --upgrade`

### [Conda environment](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html), [Virtualenv](https://virtualenv.pypa.io/en/latest/) or plain [Python](https://www.python.org)
Download the [latest release](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/releases/latest) 
or the [current master branch](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/archive/master.zip)
 and use:
 
- ./environment.yml
- ./meta.yaml
- ./pyproject.toml
- ./requirements.txt
- ./setup.py

## Change Log
[https://oliver-zehentleitner.github.io/unicorn-binance-rest-api/changelog.html](https://oliver-zehentleitner.github.io/unicorn-binance-rest-api/changelog.html)

## Documentation
- [General](https://oliver-zehentleitner.github.io/unicorn-binance-rest-api/)
- [Modules](https://oliver-zehentleitner.github.io/unicorn-binance-rest-api/modules.html)

## Examples
- [Look here!](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/tree/master/examples/)

## Howto
- [Restful Binance Requests in Python with UNICORN Binance REST API](https://technopathy.club/restful-binance-requests-in-python-with-unicorn-binance-rest-api-288f364e92a8)
- [How to Download Klines from Binance using Python?](https://technopathy.club/how-to-download-data-from-binance-using-python-8f1b6e8f19f3)
- [How to Connect to binance.com REST API using Python via a SOCKS5 Proxy](https://technopathy.club/how-to-connect-to-binance-com-rest-api-using-python-via-a-socks5-proxy-638dbbecacfd)
- [Buy an Asset and instantly create a Take Profit and Stop Loss OCO Sell Order using Python in Binance Isolated Margin](https://technopathy.club/buy-an-asset-and-instantly-create-a-take-profit-and-stop-loss-oco-sell-order-using-python-in-5d68a5d22a9b)

## Project Homepage
[https://github.com/oliver-zehentleitner/unicorn-binance-rest-api](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api)

## Wiki
[https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/wiki](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/wiki)

## Social
- [Discussions](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/discussions)
- [https://t.me/unicorndevs](https://t.me/unicorndevs)
- [https://dev.binance.vision](https://dev.binance.vision)
- [https://forum.bnbchain.org/](https://forum.bnbchain.org/)

## Receive Notifications
To receive notifications on available updates you can 
[![watch](https://raw.githubusercontent.com/oliver-zehentleitner/unicorn-binance-rest-api/master/images/misc/watch.png)](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/watchers) 
the repository on [GitHub](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api), write your 
[own script](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/blob/master/examples/_archive/example_version_of_this_package.py) 
with using 
[`is_update_availabe()`](https://oliver-zehentleitner.github.io/unicorn-binance-rest-api/unicorn_binance_rest_api.html?highlight=is_update_availabe#unicorn_binance_rest_api.manager.BinanceRestApiManager.is_update_availabe).

To receive news (like inspection windows/maintenance) about the Binance API`s subscribe to their telegram groups: 

- [https://t.me/binance_api_announcements](https://t.me/binance_api_announcements)
- [https://t.me/binance_api_english](https://t.me/binance_api_english)
- [https://t.me/Binance_USA](https://t.me/Binance_USA)
- [https://t.me/TRBinanceTR](https://t.me/TRBinanceTR)
- [https://t.me/BinanceDEXchange](https://t.me/BinanceDEXchange)
- [https://t.me/BinanceExchange](https://t.me/BinanceExchange)

## How to report Bugs or suggest Improvements?
[List of planned features](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement) - 
click ![thumbs-up](https://raw.githubusercontent.com/oliver-zehentleitner/unicorn-binance-rest-api/master/images/misc/thumbup.png) if you need one of them or suggest a new feature!

Before you report a bug, [try the latest release](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api#installation-and-upgrade). If the issue still exists, provide the error trace, OS 
and Python version and explain how to reproduce the error. A demo script is appreciated.

If you don't find an issue related to your topic, please open a new [issue](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/issues)!

[Report a security bug!](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/security/policy)

## Contributing
[UNICORN Binance REST API](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api) is an open 
source project which welcomes contributions which can be anything from simple documentation fixes and reporting dead links to new features. To 
contribute follow 
[this guide](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/blob/master/CONTRIBUTING.md).
 
### Contributors
[![Contributors](https://contributors-img.web.app/image?repo=oliver-zehentleitner/unicorn-binance-rest-api)](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/graphs/contributors)

We ![love](https://raw.githubusercontent.com/oliver-zehentleitner/unicorn-binance-rest-api/master/images/misc/heart.png) open source!

## Disclaimer
This project is for informational purposes only. You should not construe this information or any other material as 
legal, tax, investment, financial or other advice. Nothing contained herein constitutes a solicitation, recommendation, 
endorsement or offer by us or any third party provider to buy or sell any securities or other financial instruments in 
this or any other jurisdiction in which such solicitation or offer would be unlawful under the securities laws of such 
jurisdiction.

### If you intend to use real money, use it at your own risk!

Under no circumstances will we be responsible or liable for any claims, damages, losses, expenses, costs or liabilities 
of any kind, including but not limited to direct or indirect damages for loss of profits.

### SOCKS5 Proxy / Geoblocking
We would like to explicitly point out that in our opinion US citizens are exclusively authorized to trade on Binance.US 
and that this restriction must not be circumvented!

The purpose of supporting a SOCKS5 proxy in the UNICORN Binance Suite and its modules is to allow non-US citizens to use 
US services. For example, GitHub actions with UBS will not work without a SOCKS5 proxy, as they will inevitably run on 
servers in the US and be blocked by Binance.com. Moreover, it also seems justified that traders, data scientists and 
companies from the US analyze binance.com market data - as long as they do not trade there.
