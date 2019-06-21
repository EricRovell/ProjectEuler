# Brute-force solution
# It is fast -> still the approach is straightforward:
#   1. Convert the resulting integer to digit sum
#     1.1 The numeric aproach was used with mod operator.
#         Interestingly enough, the string reverse was faster.
#         And still, I decided to use numeric one.
#   2. Find the maximum digit sum.

def digits(number: int) -> int:
  """ 
  Calculates the digits sum of the given integer. \n
    Args: \n
      number: the integer to find digits sum for. \n
    Returns: \n
      The digits sum value.
  """
  while number:
    yield number % 10
    number //= 10

def powerful_digit_sum(limit):
  """
  Searches for the largest digits sum value for numbers in form of a ^ b. \n
    Args:
      limit: defines the search limit for a, b <- [1, limit).
    Returns:
      The largest digits sum value.
  """
  largest = 0
  for a in range(1, limit):
    for b in range(1, limit):
      digitsum = sum(digits(a ** b))
      largest = max(largest, digitsum)
  return largest

# results
print(powerful_digit_sum(100))

# Actually, this is the number with the largest number of digits!
# print(sum(digits(99 ** 95)))