"""
Problem #041: Pandigital prime

We shall say that an n-digit number is pandigital if it makes use
of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from itertools import permutations

# returns all pandigital primes for a given number of digits
def pandigital_primes(digits):
  if digits == 1: return [1]

  pandigitals = []
    
  template = [str(digit) for digit in range(1, digits + 1)]
  permutated = [int("".join(string)) for string in permutations(template)]

  # if-prime check
  for possible_pandigital in permutated:
    is_prime = True

    for divisor in range(2, int(possible_pandigital ** 0.5 + 1)):

      if possible_pandigital % divisor == 0:
        is_prime = False
        break
    
    if is_prime:
      pandigitals.append(possible_pandigital)

  return pandigitals

# searching for the largest pandigital
def largest_pandigital():
  pandigitals = []

  for digit in range(1, 10):
    pandigitals.extend(pandigital_primes(digit))

  return max(pandigitals)

# tests
print(largest_pandigital())