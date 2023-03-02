import pandas as pd

class Downloader:
    def __init__(self, binance, symbol, timeframe, since):
        self.binance = binance
        self.symbol = symbol
        self.timeframe = timeframe
        self.since = binance.parse8601(since)
    
    def download(self):
        y = []
        while True:
            x = self.binance.fetch_ohlcv(symbol=self.symbol, timeframe=self.timeframe, since=self.since, limit=None)
            y.extend(x[1:])
            self.since = x[-1][0]
            if len(x) < 500:
                break
        df = pd.DataFrame(y, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
        df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
        df.set_index('datetime', inplace=True)
        return df

