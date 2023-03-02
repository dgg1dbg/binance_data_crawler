import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Actor:
    def __init__(self, data, timestep, trigger, ohlcvm):
        self.data = data
        self.timestep = timestep
        self.trigger = trigger
        self.ohlcvm = ohlcvm

    def get_action(self):
        target = pd.DataFrame()
        result = pd.DataFrame()
        if self.ohlcvm == "mean":
            target = pd.DataFrame((self.data['low'] + self.data['high'])/2, columns = ['target'])
        else:
            target = pd.DataFrame(self.data[self.ohlcvm])
            target.rename(columns={self.ohlcvm:'target'}, inplace=True)
        target = target.pct_change(periods=self.timestep) * 100
        plt.plot(target, label="percent_change")
        conditionlist = [(target['target'] >= self.trigger), (target['target'] > -1 * self.trigger) & (target['target'] < self.trigger), (target['target'] <= -1 * self.trigger)]
        choicelist = [1, 0, -1]
        self.data['action'] = np.select(conditionlist, choicelist)
        plt.plot(self.data['action'], label="action")
        plt.savefig('result.png')
        return self.data


            