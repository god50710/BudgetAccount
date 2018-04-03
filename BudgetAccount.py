class BudgetAccount(object):

    def __init__(self, *params):
        self.budgets = params

    def total_amount(self, period):
        if not self.budgets:
            return 0
        effective_amount = 0
        for budget in self.budgets:
            print(budget.amount)
            if period.start_date < budget.first_day():
                period.start_date = budget.first_day()
            if period.end_date > budget.last_day():
                period.end_date = budget.last_day()
            effective_amount += period.days() * budget.amount_of_day()
        return effective_amount


