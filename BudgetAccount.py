class BudgetAccount(object):

    def __init__(self, params=[]):
        self.budgets = params

    def total_amount(self, period):
        if not self.budgets:
            return 0
        if period.start_date < self.budgets.first_day():
            period.start_date = self.budgets.first_day()
        if period.end_date > self.budgets.last_day():
            period.end_date = self.budgets.last_day()
        return period.days()


