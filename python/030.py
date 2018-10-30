"""
Problem #030: Digit fifth powers

Surprisingly there are only three numbers that can be written as the sum
of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.
"""

# returns all numbers that can be written as the sum of "power" powers of their digits
def digit_power(power):
  numbers = []

  powers = {}
  for digit in range(0, 10):
    powers[digit] = digit ** power

  # limit of one digit
  digit_max = 9 ** power
  # we can get a n-digit number from that
  limit_digits = len(str(digit_max)) * digit_max
  # so, the limit is:
  limit = len(str(limit_digits)) * digit_max

  for number in range(2, limit):
    total = 0
    for digit in str(number):
      total += powers[int(digit)]
    if number == total:
      numbers.append(number)

  return numbers

# tests
print(digit_power(4))
print(digit_power(5))