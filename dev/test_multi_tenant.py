from unicorn_binance_rest_api import BinanceRestApiManager
import asyncio
import logging
import os

api_key = ""
api_secret = ""


async def main(ubra):
    kwargs = {'api_key': api_key,
              'api_secret': api_secret}

    listen_key = ubra.stream_get_listen_key(**kwargs)
    print(f"{listen_key=:}")

    stream_keepalive = ubra.stream_keepalive(listenKey=listen_key, **kwargs)
    print(f"{stream_keepalive=:}")

    stream_close = ubra.stream_close(listenKey=listen_key, **kwargs)
    print(f"{stream_close=:}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        filename=os.path.basename(__file__) + '.log',
                        format="{asctime} [{levelname:8}] {process} {thread} {module}: {message}",
                        style="{")

    try:
        with BinanceRestApiManager(exchange="binance.com") as ubra_manager:
            asyncio.run(main(ubra_manager))
    except Exception as error_msg:
        print(f"ERROR: {error_msg}")
