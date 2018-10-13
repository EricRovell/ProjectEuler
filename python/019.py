"""
Problem #019: Counting Sundays

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September, April, June and November.
All the rest have thirty-one, saving February alone,
  which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4,
  but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century
  (1 Jan 1901 to 31 Dec 2000)?
"""

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
  if year % 4 == 0:
    if year % 400 == 0:
      if year % 100 != 0:
        return True
  else:
    return False

def counting_sundays():
  counter = 0
  day = 0

  for year in range(1901, 2001):

    if not is_leap(year):
      month_days[1] = 28
    else:
      month_days[1] = 29

    for days in month_days:

      day += days
      if day % 7 == 0:
        counter += 1

  return counter

# test
print(counting_sundays())