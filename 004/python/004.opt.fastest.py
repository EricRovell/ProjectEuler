# The best optimization solution
# ! This approach is worked only for the 3 x 3 digits numbers the problems asks for.
# ! Not flexible, can't use any digit numbers.
# TODO: A flexible version of this aproach.
# We are still using the same optimization tricks from optimized approach.
# Now, if we consider the largest product of the 3 x 3 numbers:
#   it is a 6-digit number.
# If it is a palindrome, then is has a form:
#   100 000 x + 10 000 y + 1 000 z + 100 z + 10 y + x
# In the simplest form:
#   100 001 x + 10 010 y + 1 100 z -> 11 (9091 x + 910 y + 100 z)
# We found out that the palindrome must have a multiple 11,
# So the 1st number of the 2nd number should be divisible by 11.

def reverse(number: int) -> int:
  ''' Reversing an integer. '''
  inversed = 0
  while number:
    inversed = 10 * inversed + number % 10
    number //= 10
  return inversed

def largest_palindromic_product() -> int:
  largest = 0
  for a in range(999, 99, -1):
    # at least one number should have multiple 11
    begin, step = (999, 1) if a % 11 == 0 else (990, 11)
    for b in range(begin, 99, -step):
      product = a * b
      if product <= largest:
        break
      if product == reverse(product):
        largest = product
  return largest

# results
print(largest_palindromic_product())