"""
Problem #032: Pandigital products

We shall say that an n-digit number is pandigital if it makes use of all the digits
1 to n exactly once;
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254,
containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure
to only include it once in your sum.
"""

# checks if the given number is pandigital for the given range of numbers [left, right]
def is_pandigital(number, left, right):
  digits = {str(digit) for digit in range(left, right + 1)}
  for digit in str(number):
    if digit in digits: digits.remove(digit)
    else: return False
  return True if len(digits) == 0 else False


def pandigital_products():
  result = set()
  
  for multiplicand in range(2, 100):
    start = 123 if multiplicand > 9 else 1234
    end = 10000 // multiplicand + 1
    for multiplier in range(start, end):

      number = int(f'{multiplicand}{multiplier}{multiplicand * multiplier}')
      if is_pandigital(number, 1, 9):
        result.add(multiplicand * multiplier)

  return sum(result)

# tests
print(pandigital_products())