"""
Problem #020: Factorial digit sum

n! means n × (n − 1) × ... × 3 × 2 × 1
For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

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