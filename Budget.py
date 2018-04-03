from datetime import datetime
import calendar


class Budget(object):
    def __init__(self, year_month, amount):
        self.year_month = year_month
        self.amount = amount

    def first_day(self):
        return datetime.strptime(self.year_month+"01", '%Y%m%d')

    def last_day(self):
        return datetime.strptime(
            self.year_month+str(calendar.monthrange(
                int(self.year_month[0:3]), int(self.year_month[4:]))[1]), '%Y%m%d')

    def amount_of_day(self):
        return self.amount / int(self.last_day().day)
