"""
Problem #036: Double-base palindromes

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million,
which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base,
may not include leading zeros.)
"""

# convert a positive 'number' to it's digit representation in 'base'
def to_base(number, base):
  digits = []
  while number > 0:
    digits.insert(0, str(number % base))
    number //= base
  return ''.join(digits)

# palindrome (recusive) test
def is_palindrome(number):

  # validation
  if isinstance(number, int):
    number = [digit for digit in str(number)]
  elif isinstance(number, str):
    number = [digit for digit in number]

  # base case
  if len(number) <= 1:
    return True
  if number[0] != number[-1]:
    return False
  
  del number[0], number[-1]
  return is_palindrome(number)

# solving the problem
def search(limit):
  total = 0
  for number in range(1, limit + 1):
    if is_palindrome(number) and is_palindrome(to_base(number, 2)):
      total += number
  return total


# tests
print(search(1000000))