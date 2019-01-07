# returns a sum of digits of the factorial(number)
def factorial_digit_sum(number):
  factorial = 1
  while number != 1:
    factorial *= number
    number -= 1
  return sum([int(digit) for digit in str(factorial)])

# tests
print(factorial_digit_sum(10))
print(factorial_digit_sum(100))