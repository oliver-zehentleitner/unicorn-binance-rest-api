# Testing

## CI initializes against `binance.us`, not `binance.com`

**Status:** active
**Confirmed** (commit `050284a`)

`BinanceRestApiManager.__init__()` makes a live `get_server_time()` call against Binance for every exchange. Test classes that need to exercise a `binance.com`-specific endpoint initialize the manager with `exchange="binance.us"` and then manually override the relevant URL constants (e.g. `PAPI_URL`, `OPTIONS_URL`) for the endpoint actually under test, instead of initializing with `exchange="binance.com"` directly.

**Reason:** GitHub Actions runners are US-based, and Binance blocks `binance.com` API access from restricted (US) locations — a direct `binance.com` init would fail in CI (though it may work fine locally, outside the US). This is the same workaround pattern used in UBWA's and UBTSL's unit tests, for the same reason.

**How to apply:** don't "fix" a test by switching its init back to `binance.com` because it looks more correct — it will pass locally and fail in CI.

## `colorama.init(wrap=False)`

**Status:** active
**Confirmed** (commit `f8bb80c`)

`colorama.init()` is called with `wrap=False`.

**Reason:** `colorama.init()` wraps `sys.stdout`/`sys.stderr` with `AnsiToWin32`, which overrides `isatty()`. If `BinanceRestApiManager` is instantiated more than once in the same process (e.g. in tests, or a host app creating multiple managers), the stream gets wrapped again on each init, and `isatty()` ends up calling itself recursively until `RecursionError`. `wrap=False` avoids the repeated wrapping.
