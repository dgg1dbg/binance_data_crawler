import os
import json
import ccxt

from Downloader import Downloader
from Actor import Actor

cwd = os.getcwd()
with open(cwd + "/binance_data_crawler/config.json") as f:
    config = json.load(f)

binance = ccxt.binance(config={
    'apiKey': config['key']['api_key'], 
    'secret': config['key']['secret'],
    'enableRateLimit': True,
    'options': {
        'defaultType': 'future'
    }
})

downloader = Downloader(binance=binance, **config['data'])
data = downloader.download()

actor = Actor(data=data, **config['policy'])
data = actor.get_action()

symbol = config['data']['symbol'].replace('/', '-')

data.to_csv(cwd + f"/binance_data_crawler/{symbol}: from {config['data']['since']}.csv")





