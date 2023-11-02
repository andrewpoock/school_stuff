# test_paystation.py

import unittest
from datetime import datetime

from paystation.domain import (PayStation,
                               IllegalCoinException,
                               Receipt,
                               )


def one_to_one_rate_strategy(amount):
    return amount


class TestPayStation(unittest.TestCase):

    def setUp(self):
        self.ps = PayStation(one_to_one_rate_strategy)

    def _insert_coins(self, coins):
        for coin in coins:
            self.ps.add_payment(coin)

    def test_displays_proper_time_for_5_cents(self):
        self.ps.add_payment(5)
        self.assertEqual(5, self.ps.read_display())

    def test_displays_time_for_25_cents(self):
        self.ps.add_payment(25)
        self.assertEqual(25, self.ps.read_display())

    def test_displays_time_for_5_and_25_cents(self):
        self._insert_coins([5, 25])
        self.assertEqual(5+ 25, self.ps.read_display())   

    def test_reject_illegal_coin(self):
        with self.assertRaises(IllegalCoinException):
            self.ps.add_payment(17)

    def test_buy_gives_valid_receipt(self):
        self._insert_coins([5, 10, 25])
        receipt = self.ps.buy()
        self.assertIsInstance(receipt, Receipt)
        self.assertEqual(5+10+25, receipt.value)

    def test_receipt_stores_value(self):
        receipt = Receipt(30)
        self.assertEqual(30, receipt.value) 

    def test_correct_receipt_for_100_cents(self):
        self._insert_coins([25, 25, 25, 10, 10, 5])
        rec = self.ps.buy()
        self.assertEqual(25*3+10*2+5, rec.value)

    def test_clears_after_buy(self):
        self.ps.add_payment(25)
        self.ps.buy()
        self.assertEqual(0, self.ps.read_display())
        self._insert_coins([5, 25])
        self.assertEqual(5+25, self.ps.read_display())

    def test_clears_on_cancel(self):
        self.ps.add_payment(25)
        self.ps.cancel()
        self.assertEqual(0, self.ps.read_display())
        self._insert_coins([5, 25])
        self.assertEqual(5+25, self.ps.read_display())

class TestReceipt(unittest.TestCase):
    
    def setUp(self):
        self.file = "receipt.txt"

    def test_value(self):
        r = Receipt(30)
        self.assertEqual(r.value, 30)

    def test_print(self):
        r = Receipt(30)
        r.print(self.file)
        f = open(self.file, "r")
        lines = [line for line in f]
        self.assertEqual(lines[0], "------------------------------------------------\n")
        self.assertEqual(lines[1], "--------------- PARKING RECIEPT ----------------\n")
        self.assertEqual(lines[2], f"--------------- Value: {r.value} minutes --------------\n")
        self.assertEqual(lines[3], f"------------- Car parked at {r.time} --------------\n")
        self.assertEqual(lines[4], "------------------------------------------------\n")


    def test_barcode(self):
        r = Receipt(30, True)
        r.print(self.file)
        f = open(self.file, "r")
        lines = [line for line in f]
        self.assertEqual(lines[0], "------------------------------------------------\n")
        self.assertEqual(lines[1], "--------------- PARKING RECIEPT ----------------\n")
        self.assertEqual(lines[2], f"--------------- Value: {r.value} minutes --------------\n")
        self.assertEqual(lines[3], f"------------- Car parked at {r.time} --------------\n")
        self.assertEqual(lines[4], "------------------------------------------------\n")
        self.assertEqual(lines[5], "|| ||||| | || ||| || || ||| | || |||| | || |||| \n")
        self.assertEqual(lines[6], "------------------------------------------------\n")



if __name__ == "__main__":
    unittest.main()
