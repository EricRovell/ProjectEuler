# brute-force solution
# palindrome check by using arithmetics 

def reverse(number: int) -> int:
  """ Reverses an integer. \n
    Args: \n
      number (int): integer to reverse. \n
    Returns: \n
      A reversed integer. \n
  """
  inversed = 0
  while number:
    inversed = 10 * inversed + number % 10
    number //= 10
  return inversed

# palindrome integer check
is_palindrome = lambda number: number == reverse(number)

# search
def largest_palindrome_product(a: int, b: int) -> int:
  largest = 0
  for num1 in range(10 ** (a - 1), 10 ** a):
    for num2 in range(10 ** (b - 1), 10 ** b):
      product = num1 * num2
      if is_palindrome(product):
        largest = max(largest, product)
  return largest

# results
print(largest_palindrome_product(2, 2))
print(largest_palindrome_product(3, 3))