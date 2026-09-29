import Candle

#### IT WILL BE IMPOSSIBLE TO FULLY CODE THIS UNTIL THE HLOC DATA STRUCTURE IS PROPERLY UNDERSTOOD ####

Class Atr():
    
    def _init_(self, period:int):
        self.period = period
        self.previous_atr = None
        self.truerange = None
        self.today_high = None
        self.today_low = None
        self.yesterday_closing_price = None

    # when the program starts this method calculates the first tr from historical data
    # streamed from the IG API
    def warmup(self,candles):
        rolling_window = []
        tr = 0

        # checks that the amount of candles and the ATR period are consistent
        if len(rolling_window) != self.period:
            Error("Rolling Window and Period values differ")
        
        # for each candle, calculate the TR
        for candle in rolling_window:
            hml = candle["high"] - candle["low"]
            hmc = candle["high"] - self.yesterday_closing_price
            lmc = candle["low"] - self.yesterday_closing_price
            
            # store the averaged tr
            tr += (1/self.period) * max(hml,hmc,lmc) 

        return tr

    # calculate the true range for each candle POST WARMUP
    def true_range(): int
        hml = self.today_high - self.today_low
        hmc = self.today_high - self.yesterday_closing_price
        lmc = self.today_low - self.yesterday_closing_price
        new_tr = max(hml,hmc,lmc)
        self.truerange = new_tr
        return 0

    
    # receive each new candle and update the ATR value with its data
    def update(candle):
        if self.previous_atr is None:
            # calculate first atr
            self.truerange = self.warmup()
            return 0

        elif self.previous_atr is not None:
            # calculate regular atr
            self.previous_atr = ((self.previous_atr*(self.period - 1)) + self.truerange)/self.period
            return 0

