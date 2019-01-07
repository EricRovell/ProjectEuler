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