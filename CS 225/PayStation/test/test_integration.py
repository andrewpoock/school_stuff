# test_integration.py

import unittest

from paystation.domain import PayStation, LinearRateStrategy, progressive_rate_strategy, AlternatingRateStrategy, is_weekend

def insert_coins(ps, coins):
        for coin in coins:
            ps.add_payment(coin)

class TestTownIntegrations(unittest.TestCase):

    def test_paystation_linear_rate(self):
        ps = PayStation(LinearRateStrategy(150))
        ps.add_payment(25)
        self.assertEqual(25 // 5 * 2, ps.read_display())

    def test_paystation_progressive_rate_for_3_hours(self):
        ps = PayStation(progressive_rate_strategy)
        insert_coins(ps, [25]*26)
        self.assertEqual((150 // 5 * 2)+(200 // 5 * 1.5)+(300 // 5 * 1), ps.read_display())

    def test_paystation_alternating_rate(self):
        lrs = LinearRateStrategy(150)
        ps = PayStation(AlternatingRateStrategy(is_weekend, progressive_rate_strategy, lrs))
        insert_coins(ps, [25]*12)
        if is_weekend():
            self.assertEqual(progressive_rate_strategy(25*12), ps.read_display())
        else:
            self.assertEqual(lrs(300), ps.read_display())

