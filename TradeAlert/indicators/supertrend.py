

class Supertrend():
    def _init_(self, period, multiplier,hloc,atr: ATR):
        self.period = period
        self.multiplier = multiplier
        self.hloc = hloc
        self.atr = atr

    
    @staticmethod
    def calculate_upper_band(hloc):
        high = hloc["high"]
        low = hloc["low"]
