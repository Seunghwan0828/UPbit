import pyupbit

access = "He3C69CTNB7OJ1H4vx0b07wLArly8AeB7zMltBrz"
secret = "OdOgYm00kwKPjERpaHoUufGe1sCEo2WA57jz0RQD"
upbit = pyupbit.Upbit(access, secret)

btc = upbit.get_balance("KRW-BTC")
btg = upbit.get_balance("KRW-BTG")
eth = upbit.get_balance("KRW-ETH")
etc = upbit.get_balance("KRW-ETC")
krw = upbit.get_balance("KRW")

print(f'BTC = {btc}\nBTG = {btg}\nETH = {eth}\nETC = {etc}\nKRW = {krw}')