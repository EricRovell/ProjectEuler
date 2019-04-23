# Optimized solution
# 1. Seraching from the end -> largest numbers first.
# 2. In order not to check the same numbers twice:
#   2nd number >= 1st number while search.
# 3. If the next found palindrome product is less than we presently have:
#   ! No reason to search further.
#   ! Remember, we are checking the largest numbers first.

def reverse(number: int) -> int:
  ''' Reversing an integer. '''
  inversed = 0
  while number:
    inversed = 10 * inversed + number % 10
    number //= 10
  return inversed

def largest_palindrome_product(a: int, b: int) -> int:
  """ Getting the largest palindrome product for two integers.
    Args:
      a (int): The number of digits in the first number.
      b (int): The number of digits in the second number.
    Returns:
      int: the largest palindrome product.
  """
  largest = 0
  for num1 in range(10 ** a, 10 ** (a - 1), -1):
    for num2 in range(10 ** b, num1, -1):
      product = num1 * num2
      if product <= largest:
        break
      if product == reverse(product):
        largest = max(largest, product)
  return largest

# results
print(largest_palindrome_product(2, 2))
print(largest_palindrome_product(3, 3))