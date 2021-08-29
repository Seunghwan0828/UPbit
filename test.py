import pyupbit

access = "access"
secret = "secret"
upbit = pyupbit.Upbit(access, secret)

btc = upbit.get_balance("KRW-BTC")
btg = upbit.get_balance("KRW-BTG")
eth = upbit.get_balance("KRW-ETH")
etc = upbit.get_balance("KRW-ETC")
xrp = upbit.get_balance("KRW-XRP")
xrp_now = pyupbit.get_orderbook(tickers="KRW-XRP")[0]["orderbook_units"][0]["ask_price"]
krw = upbit.get_balance("KRW")

print(f'BTC = {btc}\nBTG = {btg}\nETH = {eth}\nETC = {etc}\nKRW = {krw}\nXRP = {xrp}\nXRP_now = {xrp_now}')
