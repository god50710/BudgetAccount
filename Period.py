class Period(object):
    def __init__(self, start_date, end_date):
        if start_date > end_date:
            raise Exception()
        self.start_date = start_date
        self.end_date = end_date

    def days(self):
        return (self.end_date - self.start_date).days + 1

    def effective_days(self, budget):
        effective_start_date = self.start_date
        if self.start_date < budget.first_day():
            effective_start_date = budget.first_day()

        effective_end_date = self.end_date
        if self.end_date > budget.last_day():
            effective_end_date = budget.last_day()

        return (effective_end_date - effective_start_date).days + 1
