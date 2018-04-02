class Period(object):
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def days(self):
        return (self.end_date - self.start_date).days + 1