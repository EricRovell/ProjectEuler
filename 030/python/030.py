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