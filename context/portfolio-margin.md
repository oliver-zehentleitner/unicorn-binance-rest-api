# Portfolio Margin support

## Deliberately minimal: just enough for UBWA's listenKey needs

**Status:** active
**Confirmed** (CHANGELOG, 2.11.0.dev entry; issue [#452](https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/issues/452))

This repo's Portfolio Margin (PAPI) support is scoped to the `portfolio_margin_stream_*` listenKey lifecycle methods — just what `unicorn-binance-websocket-api` needs to open a Portfolio Margin user-data stream (see UBWA's own `context/portfolio-margin.md` for the WS-side design).

**Rejected alternative:** implementing broader Portfolio Margin REST coverage (account info, positions, orders, etc.) alongside the listenKey methods, while already touching this code.

**Reason:** broader Portfolio Margin REST coverage is deferred to the planned UBRA rewrite (see the suite's `unicorn-binance-rest-api` v3.0.0 rewrite plan) rather than bolted onto the current architecture piecemeal. The listenKey methods were the minimum needed to unblock UBWA's issue #452.
