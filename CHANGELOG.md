# unicorn-binance-rest-api Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/) and this project adheres to 
[Semantic Versioning](http://semver.org/).

[Discussions about unicorn-binance-rest-api releases!](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/discussions/categories/releases)

[How to upgrade to the latest version!](https://oliver-zehentleitner.github.io/unicorn-binance-rest-api/readme.html#installation-and-upgrade)

## 2.8.1.dev (development stage/unreleased/unstable)

## 2.8.1
### Added
- Python 3.13 support

## 2.8.0
### Changed
- Moved from https://github.com/LUCIT-Systems-and-Development/ to https://github.com/oliver-zehentleitner
### Removed
- LUCIT Licensing Manager

## 2.6.1
### Fixed
- TypeError: unsupported operand type(s) for -: 'float' and 'NoneType' in `get_used_weight()`

## 2.6.0
### Added
- `cached_timeout` parameter to `_save_used_weight()`
### Fixed
- `_save_used_weight()` - Exception: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'

## 2.5.1
### Changed
- Returned type of `get_used_weight()['weight']` to int

## 2.5.0
### Added
- `_save_used_weight()` to cache the used weight on every request.
- Updated `get_used_weight()` and added parameter `cached=False`.
### Changed
- `type(start_str) == int` to `type(start_str) is int` a couple of times.

## 2.4.0
Exclude known security vulnerabilities in dependencies by increasing the minimum version numbers of the dependencies.
### Changed
- Updated description text in all files.
- Update of `get_used_weight()`, removed parameter `make_new_request`, it is now allways using `ping()` to get the 
  current used weight. 
- https://pypi.org/project/requesocks/ has been discontinued and socks support is now provided directly by `requests`.
### Fixed
- Import in `licensing_manager.py`.
- Type of global `logger` variable.
### Security
- Set higher minimum version `2023.7.22` for `certifi`, as vulnerabilities were found in earlier versions:
  - CVE-2023-37920, Score: 9.8 (High)
    - Certifi is a curated collection of Root Certificates for validating the trustworthiness of SSL certificates while 
      verifying the identity of TLS hosts. Certifi 1.0.1 through 2023.5.7 recognizes "e-Tugra" root certificates. 
      e-Tugra's root certificates were subject to an investigation prompted by reporting of security issues in their 
      systems. Certifi 2023.07.22 removes root certificates from "e-Tugra" from the root store.
    - https://devhub.checkmarx.com/cve-details/CVE-2023-37920/
- Set higher minimum version `42.0.4` for `cryptography`, as vulnerabilities were found in earlier versions:
  - CVE-2023-38325, Score: 7.5 (High)
    - The cryptography package versions prior to 41.0.2 for Python mishandles SSH certificates that have critical 
      options.
    - https://devhub.checkmarx.com/cve-details/CVE-2023-38325/
  - CVE-2023-49083, Score: 7.5 (High)
    - Cryptography is a package designed to expose cryptographic primitives and recipes to Python developers. Calling 
      `load_pem_pkcs7_certificates` or `load_der_pkcs7_certificates` could lead to a NULL-pointer dereference and 
      segfault. Exploitation of this vulnerability poses a serious risk of Denial of Service (DoS) for any application 
      attempting to deserialize a PKCS7 blob/certificate. The consequences extend to potential disruptions in system 
      availability and stability. This issue affects versions 3.1 through 41.0.5.
    - https://devhub.checkmarx.com/cve-details/CVE-2023-49083/
  - CVE-2023-50782, Score: 7.5 (High)
    - A flaw was found in the python cryptography package versions prior to 42.0.0. This issue may allow a remote 
      attacker to decrypt captured messages in TLS servers that use RSA key exchanges, which may lead to exposure of 
      confidential or sensitive data. This issue is an incomplete fix of CVE-2020-25659.
    - https://devhub.checkmarx.com/cve-details/CVE-2023-50782/
  - CVE-2024-26130, Score: 7.5 (High)
    - cryptography is a package designed to expose cryptographic primitives and recipes to Python developers. Starting 
      in version 38.0.0 and prior to version 42.0.4, if `pkcs12.serialize_key_and_certificates` is called with both a 
      certificate whose public key did not match the provided private key and an `encryption_algorithm` with `hmac_hash` 
      set (via `PrivateFormat.PKCS12.encryption_builder().hmac_hash(...)`, then a NULL pointer dereference would occur, 
      crashing the Python process. This has been resolved in version 42.0.4, the first version in which a `ValueError` 
      is properly raised.
    - https://devhub.checkmarx.com/cve-details/CVE-2024-26130/
- Set higher minimum version `2.31.0` for `requests`, as vulnerabilities were found in earlier versions:
  - CVE-2023-32681, Score: 6.1 (Medium)
    - Requests is a HTTP library. Requests has been leaking Proxy-Authorization headers to destination servers when 
      redirected to an HTTPS endpoint. This is a product of how we use `rebuild_proxies` to reattach the 
      `Proxy-Authorization` header to requests. For HTTP connections sent through the tunnel, the proxy will identify 
      the header in the request itself and remove it prior to forwarding to the destination server. However when sent 
      over HTTPS, the `Proxy-Authorization` header must be sent in the CONNECT request as the proxy has no visibility 
      into the tunneled request. This results in Requests forwarding proxy credentials to the destination server 
      unintentionally, allowing a malicious actor to potentially exfiltrate sensitive information. This issue affects 
      versions 2.3.0 through 2.30.0.
    - https://devhub.checkmarx.com/cve-details/CVE-2023-32681/

## 2.3.0
### Added
- Parameter `version` to `_request_futures_api()`, `_create_futures_coin_data_api_url()` and `_create_futures_api_uri()`
- Since UBRA is delivered as a compiled C extension, IDEs such as Pycharm and Visual Code cannot use information about 
  available methods, parameters and their types for autocomplete and other intellisense functions. As a solution, from 
  now on stub files (PYI) will be created in the build process and attached to the packages. The IDEs can automatically 
  obtain the required information from these.
### Changed
- Renamed `binance.com-coin-futures` to `binance.com-coin_futures`.
### Fixed
- `futures_account()`, `futures_account_balance()` and `futures_position_information()`  [issue#65](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/issues/65)
- Projects `__init__.py` - did not correct import.

## 2.2.1
`unicorn-binance-rest-api` can now also be installed on all architectures on which there are no precompiled packages from 
LUCIT. PIP now automatically recognises whether there is a suitable precompiled package and if not, the source is 
automatically compiled on the target system during the installation process with Cython. Even if you don't have to do 
anything special, please note that this process takes some time!

## 2.2.0
### Added
- Support of `params` in `manager.py`:
  - `get_exchange_info()`
  - `futures_exchange_info()`
  - `futures_coin_exchange_info()`

## 2.1.2
### Added 
- Typing for a few more parameters.
### Fixed
- Fixed handling of `tld` in `manager.__init__()`.
### Removed
- `version=1` parameter in `manager._create_futures_coin_data_api_url()`.

## 2.1.1
### Fixed
- Used `False` instead of `None` in `manager.__init__()` parameter `tld`.

## 2.1.0
### Adding
- Support of multiple tenants with `kwargs['api_key']` and `kwargs['api_secret']` in `manager._request()` - every 
  private rest call now supports specific `api_key` and `api_secret` values via `**kwargs`.
- Support of `**params` in:
    - `manager.stream_get_listen_key()`
    - `manager.stream_keepalive()`
    - `manager.stream_close()`
    - `manager.margin_stream_get_listen_key()`
    - `manager.margin_stream_keepalive()`
    - `manager.margin_stream_close()`
    - `manager.isolated_margin_stream_get_listen_key()`
    - `manager.isolated_margin_stream_keepalive()`
    - `manager.isolated_margin_stream_close()`
    - `manager.futures_stream_get_listen_key()`
    - `manager.futures_stream_keepalive()`
    - `manager.futures_stream_close()`
    - `manager.futures_coin_stream_get_listen_key()`
    - `manager.futures_coin_stream_keepalive()`
    - `manager.futures_coin_stream_close()`
### Changed
- Using types in `manager.__init__()`.

## 2.0.5
- Building conda packages and distribute them via https://anaconda.org/lucit

## 2.0.4
- Same as 2.0.2, error during github upload.

## 2.0.3
- Same as 2.0.2, error during pypi upload.

## 2.0.2
### Changed
- Replaced URLs
### Fixed
- Stopping manager automatically if an unknown exchange string was used before the exception gets raised.

## 2.0.1
### Fixed
- New exception `AlreadyStoppedError` is thrown if a stopped instance gets used.
- Memory leak with implementation of `manager.stop_manager()`.

## 2.0.0
### Added
- Support for Python 3.11 and 3.12
- Integration of the `lucit-licensing-python` library for verifying the UNICORN Binance Suite license. A license can be 
  purchased in the LUCIT Online Shop: https://shop.lucit.services/software/unicorn-binance-suite
- License change from MIT to LSOSL - LUCIT Synergetic Open Source License:
  https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/LICENSE
- Conversion to a C++ compiled Cython package with precompiled as well as PyPy and source code wheels.
- Setup of a "Trusted Publisher" deployment chain. The source code is transparently packaged into wheels directly from
  the GitHub repository by a GitHub action for all possible platforms and published directly as a new release on GitHub
  and PyPi. A second process from Conda-Forge then uploads it to Anaconda. Thus, the entire deployment process is
  transparent and the user can be sure that the compilation of a version fully corresponds to the source code.
- `manager.stop_manager()`
- Support for `with`-context

## 1.10.0
### Added
- `"s": 1,` to helpers.py to fix kline_1s support
- `create_margin_oco_order()`, `cancel_margin_oco_order()`, `get_margin_oco_order()`, `get_open_margin_oco_orders()`

## 1.9.0
### Added
- `futures_stream_get_listen_key()`, `futures_stream_keepalive()` and `futures_stream_close()`
- `futures_coin_stream_get_listen_key()`, `futures_coin_stream_keepalive()` and `futures_coin_stream_close()`
### Removed
- jex.com support

## 1.8.1
### Fixing
- `requests.exceptions.InvalidHeader`: Header part (False) from {'X-MBX-APIKEY': False} must be of type str or bytes, not <class 'bool'>

## 1.8.0
### Added 
- `output="value"` and `throw_exception=True` to: `stream_get_listen_key()`, `margin_stream_get_listen_key()`, `isolated_margin_stream_get_listen_key()`
- `throw_exception=True` to: `_request()`, `_request_api()`, `_request_margin_api()`, `_request_website()`, `_request_futures_api()`, `_request_futures_data_api()`, `_request_futures_coin_api()`, `_request_futures_coin_data_api()`, `_handle_response()`, `stream_keepalive()`, `stream_close()`, `margin_stream_keepalive()`, `margin_stream_close()`, `isolated_margin_stream_keepalive()`, `isolated_margin_stream_close()`
### Fixing 
- Issue in `get_used_weight()`

## 1.7.0
### Added
- SOCKS5 proxy support to [`BinanceRestApiManager()`](https://oliver-zehentleitner.github.io/unicorn-binance-rest-api/unicorn_binance_rest_api.html#unicorn_binance_rest_api.manager.BinanceRestApiManager) - 
  New parameter: `socks5_proxy_server`, `socks5_proxy_user`, `socks5_proxy_pass`, `socks5_proxy_ssl_verification`

## 1.6.0
### Added
- New kline interval: 1s `KLINE_INTERVAL_1SECOND`
- `futures_place_batch_order()` - Placing batch orders for USD-M API. Thx [@hawkeye-bot](https://github.com/hawkeye-bot) 
[PR#42](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/pull/42)
### Changed
- Dependency regex no specific version anymore

## 1.5.0
### Added 
- `cancel_all_open_margin_orders()`
- `futures_auto_cancel_all_open_orders()`

## 1.4.3
Codebase equal to 1.4.2, testing azure pipe

## 1.4.2
### Changed 
- Dependency regex to <= 2022.3.2 [issue#24](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/issues/24)

## 1.4.1
### Fixed
- Binance Futures Testnet URL [issue#20](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/issues/20)

## 1.4.0
### Adding
- `futures_commission_rate()` [issue#18](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/issues/18)
### Changed
- Moved from https://github.com/oliver-zehentleitner to https://github.com/oliver-zehentleitner/
- removed "unicorn_binance_rest_api_"-part of the module file names (more info: [Discussions](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/discussions/19))
- Correctly scope loggers so that it plays nicely with others. [PR#17](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/pull/17)
- renamed logger name of all modules to "unicorn_binance_rest_api", in the implementation of 
[PR#17](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/pull/17) every module has had 
its own logger name.

## 1.3.0
### Added
- `exchange` parameter to manager class to replace `tld` parameter
- support for new endpoints: trbinance.com 
- `disable_colorama` parameter to manager class
- `cancel_all_open_orders()` to cancel all orders of a symbol with one request. Thx @mfurlend 
[issue#3](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/issues/3)
### Changed
- `tld` is now obsolete
### Fixed
- ValueError in `get_used_weight()`
- get_open_margin_orders()
### Removed
- double definition of `make_universal_transfer()`
- binance.je support (Binance Jersey has ceased operations.)

## 1.2.0
### Added
- get_used_weight()
- futures_coin_place_batch_order() 
### Changed
- Migrate from WAPI to SAPI [issue#7](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/issues/7)
- URLs to Biannce Docs

## 1.1.1
### Fixed
- changed FUTURES_COIN_URL [PR#5](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/pull/5) - 
Thanks to [flo-rian](https://github.com/flo-rian)

## 1.1.0
### Added
- logging
- update check

## 1.0.0
forked from Sam McHardy [python-binance v0.7.10](https://github.com/sammchardy/python-binance)
### Added
- get_latest_release_info()
- get_latest_version()
- is_update_availabe()
- get_version()
- get_user_agent()
- colorama as requirement
### Removed
- Websocket support from python-binance and dependencies
