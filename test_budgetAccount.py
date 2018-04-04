from unittest import TestCase
from BudgetAccount import BudgetAccount
from Period import Period
from Budget import Budget
from datetime import datetime


class TestBudgetAccount(TestCase):
    def test_no_budget(self):
        ba = BudgetAccount()
        period = Period(datetime(2017, 3, 1), datetime(2017, 3, 15))
        self.amount_should_be(ba, period, 0)

    def test_half_month_period_has_budget(self):
        ba = BudgetAccount(Budget('201703', 31))
        period = Period(datetime(2017, 3, 1), datetime(2017, 3, 15))
        self.amount_should_be(ba, period, 15)

    def test_one_day_period_before_budget(self):
        ba = BudgetAccount(Budget('201703', 31))
        period = Period(datetime(2017, 2, 27), datetime(2017, 2, 28))
        self.amount_should_be(ba, period, 0)

    def test_one_day_period_after_budget(self):
        ba = BudgetAccount(Budget('201703', 31))
        period = Period(datetime(2017, 4, 1), datetime(2017, 4, 2))
        self.amount_should_be(ba, period, 0)

    def test_one_overlapping_period_cross_budget_last_day(self):
        ba = BudgetAccount(Budget('201703', 31))
        period = Period(datetime(2017, 3, 30), datetime(2017, 4, 2))
        self.amount_should_be(ba, period, 2)

    def test_one_overlapping_period_cross_budget_first_day(self):
        ba = BudgetAccount(Budget('201703', 31))
        period = Period(datetime(2017, 2, 28), datetime(2017, 3, 5))
        self.amount_should_be(ba, period, 5)

    def test_invalid_period(self):
        self.assertRaises(Exception, Period, self, datetime(2017, 3, 20), datetime(2017, 3, 19))

    def test_amount_is_100(self):
        ba = BudgetAccount(Budget('201703', 3100))
        period = Period(datetime(2017, 3, 1), datetime(2017, 3, 5))
        self.amount_should_be(ba, period, 500)

    def test_multiple_budgets_with_overlapping_days(self):
        ba = BudgetAccount(Budget('201703', 3100), Budget('201704', 30))
        period = Period(datetime(2017, 3, 29), datetime(2017, 4, 2))
        self.amount_should_be(ba, period, 302)

    def amount_should_be(self, ba, period, expect_amount):
        self.assertEqual(ba.total_amount(period), expect_amount)




