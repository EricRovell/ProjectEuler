"""
Problem #006: Sum square difference

The sum of the squares of the first ten natural numbers is:

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the
first one hundred natural numbers and the square of the sum.
"""

def sumSquareDiff(n, m = 1):

  if not isinstance(n, int) or not isinstance(m, int) or n < 0 or m < 0:
    return "Argument should be a positive integer"
  
  if m == 1 and n > m:
    m = n
    n = 1

  # sum of the squares
  sumSquares = 0
  # square of the sum
  squareSum = 0

  for number in range(n, m + 1):
    sumSquares += number ** 2
    squareSum += number
  
  squareSum = squareSum ** 2
  
  return squareSum - sumSquares
  
# test
print(sumSquareDiff(1, 10))
print(sumSquareDiff(1, 100))