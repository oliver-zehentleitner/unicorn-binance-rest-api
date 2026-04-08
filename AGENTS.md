# AGENTS.md — UNICORN Binance REST API

## Planning & Backlog

Open development tasks and decisions are tracked in **[TASKS.md](TASKS.md)**.

---

## Project Overview

Python SDK (MIT License) for the Binance REST APIs. Covers Spot, Margin, Isolated Margin, Futures (USDT-M & Coin-M), Testnet variants, Binance.US and TRBinance.com. Forked from python-binance (Sam McHardy), heavily extended and maintained by Oliver Zehentleitner.

**Current Version:** 2.9.0.dev  
**Next Release:** 2.9.0  
**Python Compatibility:** 3.8 – 3.13  
**Author:** Oliver Zehentleitner  
**PyPI:** `unicorn-binance-rest-api`  
**Part of:** [UNICORN Binance Suite](https://github.com/oliver-zehentleitner/unicorn-binance-suite)

---

## Directory Structure

```
unicorn_binance_rest_api/
    manager.py          # Core class BinanceRestApiManager — all REST endpoints
    enums.py            # Exchange constants (order types, intervals, sides, etc.)
    exceptions.py       # Custom exceptions
    helpers.py          # Utility functions (date_to_milliseconds, interval_to_milliseconds)
    __init__.py         # Exports BinanceRestApiManager + enums + exceptions + helpers

unittest_binance_rest_api.py   # Unit tests (run in CI)
dev/                           # Local dev/integration tests — NOT run in CI
examples/                      # Usage examples
docs/                          # Pre-built HTML documentation (Sphinx)
dev/sphinx/                    # Sphinx source for rebuilding docs
```

---

## Supported Exchanges

| Exchange String | Description |
|---|---|
| `binance.com` | Binance.com Spot (default) |
| `binance.com-testnet` | Binance.com Spot Testnet |
| `binance.com-margin` | Binance.com Cross Margin |
| `binance.com-margin-testnet` | Binance.com Cross Margin Testnet |
| `binance.com-isolated_margin` | Binance.com Isolated Margin |
| `binance.com-isolated_margin-testnet` | Binance.com Isolated Margin Testnet |
| `binance.com-futures` | Binance.com USDT-M Futures |
| `binance.com-futures-testnet` | Binance.com USDT-M Futures Testnet |
| `binance.com-coin_futures` | Binance.com Coin-M Futures |
| `binance.us` | Binance.US |
| `trbinance.com` | TRBinance.com |

---

## Dependencies

Managed in `requirements.txt`, `setup.py`, `pyproject.toml`, `environment.yml`, and `meta.yaml` — **all five must be kept in sync manually**:

- `requests>=2.31.0` — HTTP client
- `ujson` — fast JSON parsing
- `certifi>=2023.7.22` — TLS certificates
- `cryptography>=42.0.4` — signature/encryption
- `pyOpenSSL` — SSL support
- `service-identity` — SSL identity verification
- `colorama` — colored terminal output
- `dateparser` — date string parsing
- `regex` — regex utilities
- `PySocks` — SOCKS5 proxy support
- `pytz` — timezone handling
- `Cython` — C extension compilation (release builds only)

---

## Workflow

Every change must be accompanied by updates to **all affected locations**:
- `README.md` — Python version range, feature descriptions, endpoint lists
- `docs/` — pre-built Sphinx HTML; rebuild via `dev/sphinx/create_docs.sh` if content changed
- `CHANGELOG.md` — entry for every user-visible change
- Dependency files — `requirements.txt`, `setup.py`, `pyproject.toml`, `environment.yml`, `meta.yaml` (all five in sync)

Never open a PR without checking README.md and docs for stale information.

---

## Running Tests

```bash
# Unit tests with coverage (this is what CI runs)
coverage run --source unicorn_binance_rest_api unittest_binance_rest_api.py

# Unit tests without coverage
python unittest_binance_rest_api.py
```

Tests in `dev/` are local integration tests that require live Binance credentials — they are **not run in CI**.

---

## Build & Packaging

Development and testing use **plain Python** — no Cython compilation needed during development.

Cython compilation only happens for **release builds**:

```bash
python setup.py bdist_wheel
```

`setup.py` also auto-generates `.pyi` stub files via `stubgen` and moves them into the package directory.

**Version bump** — done **manually** before each release. Update the version string in all three locations:
1. `setup.py`
2. `pyproject.toml`
3. `unicorn_binance_rest_api/manager.py` (`__version__`)

**CI/CD:** GitHub Actions in `.github/workflows/`
- `unit-tests.yml` — Python matrix on Ubuntu, Codecov upload
- `build_wheels.yml` — Manual trigger, builds wheels for Linux/macOS/Windows, PyPI release
- `codeql-analysis.yml` — Security scanning
- `build_conda.yml` — Conda package build

---

## Code Conventions

- **File header:** Always include the full MIT license block with dual copyright (2017-2021 Sam McHardy + 2021-2025 Oliver Zehentleitner)
- **Encoding:** UTF-8, UNIX line endings
- **Logging:** `logging.getLogger("unicorn_binance_rest_api")`
- **JSON:** `ujson` — do not switch to stdlib `json` or `simplejson`
- **Cython:** Core module compiles to C extension for releases — no `#cython:` directives needed in source
- **Versioning:** Keep version in sync across `setup.py`, `pyproject.toml`, and `manager.py` manually

---

## Key Classes & Modules

| Module | Purpose |
|---|---|
| `manager.py` | `BinanceRestApiManager` — all REST endpoints, request signing, exchange routing |
| `enums.py` | Constants for order types, kline intervals, sides, time-in-force, response types |
| `exceptions.py` | Custom exception classes |
| `helpers.py` | `date_to_milliseconds()`, `interval_to_milliseconds()` |

---

## Usage Pattern (Quick Reference)

```python
from unicorn_binance_rest_api import BinanceRestApiManager

ubra = BinanceRestApiManager(api_key="key", api_secret="secret", exchange="binance.com")

# Public endpoint
ticker = ubra.get_symbol_ticker(symbol="BTCUSDT")

# Authenticated endpoint
order = ubra.create_order(symbol="BTCUSDT", side="BUY", type="MARKET", quantity=0.001)

# Futures
ubra_futures = BinanceRestApiManager(exchange="binance.com-futures")
```

---

## Integration with UNICORN Binance Suite

`unicorn-binance-rest-api` is used by:
- `unicorn-binance-websocket-api` — for listen key management and REST fallbacks
- `unicorn-binance-trailing-stop-loss` — for order placement and account queries
- `unicorn-binance-local-depth-cache` — for initial snapshot fetching
