# brute force solution
# palindrome check via string reverse

def largest_palindrome_product(a: int, b: int) -> int:
  """ Getting the largest palindrome product for two integers.
    Args:
      a (int): The number of digits in the first number.
      b (int): The number of digits in the second number.
    Returns:
      int: the largest palindrome product.
  """
  largest = 0
  for num1 in range(10 ** (a - 1), 10 ** a):
    for num2 in range(10 ** (b - 1), 10 ** b):
      product = num1 * num2
      if product == int(str(product)[::-1]):
        largest = max(largest, product)
  return largest

# results
print(largest_palindrome_product(2, 2))
print(largest_palindrome_product(3, 3))