import time

from unicorn_binance_rest_api import BinanceRestApiManager

try:
    with BinanceRestApiManager() as ubra:
        while True:
            print(f"{ubra.get_used_weight()}")
            time.sleep(1)

except KeyboardInterrupt:
    pass
print(f"\r\nStopping ...")