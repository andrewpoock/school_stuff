# paystation.py

from datetime import datetime

class IllegalCoinException(Exception):
    pass

class PayStation:
    """Implements the 'business logic' of a parking pay  station.
    """

    LEGAL_COINS = [5, 10, 25]

    def __init__(self, rate_strategy_fn):
        self._calculate_time = rate_strategy_fn
        self._reset()

    def add_payment(self, coinvalue):
        """Adds coinvalue in payment to the pay station
     
        pre: coinvalue is an int representing a legal coin
        note: raises IllegalCoinException if coinvalue invalid
        """
        if coinvalue not in self.LEGAL_COINS:
            raise IllegalCoinException(f"Bad coin: {coinvalue}")
        self._coins_inserted += coinvalue

    def read_display(self):
        """returns current number of minutes purchased"""
        return self._time_bought()

    def buy(self):
        """Terminates transaction and returns Receipt"""
        
        receipt = Receipt(self._time_bought())
        self._reset()
        return receipt
    
    def cancel(self):
        """Terminates the transaction (resets machine)"""

        self._reset()

    def _time_bought(self):
        return self._calculate_time(self._coins_inserted)
        # return self._coins_inserted // 5 * 2

    def _reset(self):
        self._coins_inserted = 0
        

class Receipt:

    def __init__(self, value, barcode=False):
        self.value = value
        self.time = datetime.now().strftime("%H:%M")
        self.barcode = barcode

    def print(self, file):
        f = open(file, "w")
        f.write("------------------------------------------------\n")
        f.write("--------------- PARKING RECIEPT ----------------\n")
        f.write(f"--------------- Value: {self.value} minutes --------------\n")
        f.write(f"------------- Car parked at {self.time} --------------\n")
        if self.barcode:
            f.write("------------------------------------------------\n")
            f.write("|| ||||| | || ||| || || ||| | || |||| | || |||| \n")
        f.write("------------------------------------------------\n")
        f.close()

# Rate Strategies

class LinearRateStrategy:

    def __init__(self, cents_per_hour=150):
        self.cents_per_hour = cents_per_hour
    
    def __call__(self, amount):
        return amount / (self.cents_per_hour/60)

def progressive_rate_strategy(amount):
    if amount <= 150:
        return amount // 5 * 2
    if 350 >= amount > 150:
        return (150 // 5 * 2) + ((amount-150) // 5 * 1.5)
    if amount > 350:
        return (150 // 5 * 2) + (200 // 5 * 1.5) + ((amount-350) // 5 * 1)

def is_weekend():
    today = datetime.now()
    return today.weekday() > 4

class AlternatingRateStrategy:

    def __init__(self, dec_strat, weekend_rate, weekday_rate):
        self._is_weekend = dec_strat
        self._weekend_rate_strat = weekend_rate
        self._weekday_rate_strat = weekday_rate

    def __call__(self, amount):
        if self._is_weekend():
            return self._weekend_rate_strat(amount)
        else:
            return self._weekday_rate_strat(amount)

class AlphaTownFactory:
    
    def __init__(self):
        self.create_rate_strategy = LinearRateStrategy(150)
        self.receipt = Receipt(self.create_rate_strategy)

class BetaTownFactory:
    
    def __init__(self):
        self.create_rate_strategy = progressive_rate_strategy(150)
        self.receipt = Receipt(self.create_rate_strategy, True)
        
class GammaTownFactory:
    
    def __init__(self):
        self.create_rate_strategy = AlternatingRateStrategy(is_weekend, progressive_rate_strategy(150), LinearRateStrategy(150))
        self.receipt = Receipt(self.create_rate_strategy)

class TripoliFactory:
    
    def __init__(self):
        self.create_rate_strategy = LinearRateStrategy(200)
        self.receipt = Receipt(self.create_rate_strategy, True)