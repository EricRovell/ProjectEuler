"""
Problem #016: Power digit sum

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

# returns the sum of the digits of number ^ power
def power_digit_sum(number, power):

  sum = 0
  number = str(number ** power)

  for digit in number:
    sum += int(digit)

  return sum

# tests
print(power_digit_sum(2, 15))
print(power_digit_sum(2, 1000))


