# test_rate_strategies.py

from re import S
import unittest
from unittest.mock import Mock

from paystation.domain import LinearRateStrategy, progressive_rate_strategy, AlternatingRateStrategy, is_weekend


class TestLinearRate(unittest.TestCase):

    def test_correct_value_for_100_cents(self):
        lrs = LinearRateStrategy(150)
        self.assertEqual(100 // 5 * 2, lrs(100))

    def test_150_equals_60_mins(self):
        prs = progressive_rate_strategy
        self.assertEqual(150 // 5 * 2, prs(150))

    def test_350_equals_120_mins(self):
        prs = progressive_rate_strategy
        self.assertEqual((150 // 5 * 2)+(200 // 5 * 1.5), prs(350))

    def test_650_equals_180_mins(self):
        prs = progressive_rate_strategy
        self.assertEqual((150 // 5 * 2)+(200 // 5 * 1.5)+(300 // 5 * 1), prs(650))

    def test_950_equals_240_mins(self):
        prs = progressive_rate_strategy
        self.assertEqual((150 // 5 * 2)+(200 // 5 * 1.5)+(600 // 5 * 1), prs(950))

    def test_160_equals_63_mins(self):
        prs = progressive_rate_strategy
        self.assertEqual((150 // 5 * 2)+(10 // 5 * 1.5), prs(160))

    def test_355_equals_121_mins(self):
        prs = progressive_rate_strategy
        self.assertEqual((150 // 5 * 2)+(200 // 5 * 1.5)+1, prs(355))

class TestAlternatingRateStrategy(unittest.TestCase):

    def fake_rate_strat_30(self, amount):
        return 30

    def fake_rate_strat_60(self, amount):
        return 60

    """class FakeDecisionStrategy:
        def __call__(self):
            return self.return_value"""

    def setUp(self):
        self.decision_strategy = Mock()
        self.ars = AlternatingRateStrategy(self.decision_strategy, self.fake_rate_strat_30, self.fake_rate_strat_60)

    def test_uses_correct_strategy_on_weekend(self):
        self.decision_strategy.return_value = True
        self.assertEqual(30, self.ars(500))

    def test_uses_correct_strategy_on_weekday(self):
        self.decision_strategy.return_value = False
        self.assertEqual(60, self.ars(500))

    def test_is_weekend_returns_boolean(self):
        self.assertIn(is_weekend(), [True, False])

