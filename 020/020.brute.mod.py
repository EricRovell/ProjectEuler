# Brute-force solution, still works fast.
# The factorial is calculated using for-loop.
# The digits were got by modulo operator.

def digits(number: int) -> int:
  """ 
  Generates the digits of the number from right to the left. \n
    Args: \n
      number: integer to generate digits from. \n
    Yields: \n
      Digits from right to the left. 
  """
  while number:
    yield number % 10
    number //= 10

def factorial(number: int) -> int:
  """ Calculates the factorial. Non-recursive. """
  if number < 1: return None
  product = 1
  for num in range(1, number + 1):
    product *= num
  return product 

# Calculating the sum of the digits
def digitsum(func, arg):
  value = func(arg)
  return sum(digit for digit in digits(value))

# results
print(digitsum(factorial, 100))