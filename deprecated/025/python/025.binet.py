from math import log10, ceil

# using the approximate version of Binet formula
def fibonacci_digits(digits):
  phi = (1 + 5 ** 0.5) / 2
  return ceil( ((digits - 1) + 0.5 * log10(5)) / log10(phi) )

# tests
print(fibonacci_digits(3))
print(fibonacci_digits(1000))