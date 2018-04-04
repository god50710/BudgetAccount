class BudgetAccount(object):

    def __init__(self, *params):
        self.budgets = params

    def total_amount(self, period):
        if self.budgets:
            effective_amount = 0
            for budget in self.budgets:
                effective_amount += budget.effective_amount(period)
            return effective_amount
        else:
            return 0
