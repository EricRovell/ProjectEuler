"""
Problem #005: Smallest multiple

2520 is the smallest number that can be divided
by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
"""

from functools import reduce

# returns the Greatest Common Divisor for "a" and "b"
def gcd(a, b):

  if b > a:
    return gcd(b, a)
  
  if a % b == 0:
    return b
  
  return gcd(b, a % b)

# returns the Least Common Multiple of "a" and "b"
def lcm(a, b):
  return a * b / gcd(a, b)

# return the GCD or LCM for a list of numbers
def lcm_(*args):
  return reduce(lcm, args)
def gcd_(*args):
  return reduce(gcd, args)

# test
print(lcm_(*range(1, 11)))
print(lcm_(*range(1, 21)))