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