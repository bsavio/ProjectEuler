"""
Counting Sundays
Problem 19
You are given the following information, but you may prefer to do some research for yourself.

 - 1 Jan 1900 was a Monday.
 - Thirty days has September,
   April, June and November.
   All the rest have thirty-one,
   Saving February alone,
   Which has twenty-eight, rain or shine.
   And on leap years, twenty-nine.
 - A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""


class CountingSundaysDate(object):
    months_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_of_week = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']

    def __init__(self, year, month, day, day_of_week_index):
        self.year = year
        self.month = month
        self.day = day
        self.day_of_week_index = day_of_week_index

    def get_last_day_of_month(self, month, year):
        if month == 1 and ((year % 100 != 0 and year % 4 == 0) or (year % 100 == 0 and year % 400 == 0)):
                return 29
        return self.months_days[month]

    def next_day(self):
        last_day_of_current_month = self.get_last_day_of_month(self.month, self.year)
        self.day += 1
        if self.day > last_day_of_current_month:
            self.day -= last_day_of_current_month
            self.month += 1
            if self.month == len(self.months_days):
                self.month = 0
                self.year += 1
        self.day_of_week_index += 1
        if self.day_of_week_index == len(self.days_of_week):
            self.day_of_week_index = 0

    def print_date(self):
        print('{0}-{1}-{2} {3}'.format(str(self.year), str(self.month + 1), str(self.day),
                                       self.days_of_week[self.day_of_week_index]))

cs_date = CountingSundaysDate(1900, 0, 1, 0)
sundayCount = 0
while cs_date.year <= 2000:
    sundayCount += int(cs_date.year > 1900 and cs_date.day == 1 and cs_date.day_of_week_index == 6)
    cs_date.next_day()
print(sundayCount)

