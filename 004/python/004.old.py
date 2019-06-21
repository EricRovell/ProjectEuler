# My first solution.
# It is really bad designed and poorly written.
# I am leaving it to see from time to time how I was coding in the past.

# returns the set of all products from n-digit and m-digit numbers
def productsSet(n, m):
  if n == 0 or m == 0:
    return 0
  elif n < 0 or m < 0:
    return None
  
  products = set()

  # for n = 1, 2, 3: (1, 9), (10, 99), (100, 999)
  for i in range(10 ** (n - 1), 10 ** n):
    for j in range(10 ** (m - 1), 10 ** m):
      products.add(i * j)

  return products

# returns the palindromes from a given list
# optional parameter: 1 => returns the biggest
def palindromes(list, maximum = 0):
  palindromeSet = set()
  for number in list:
    if str(number) == str(number)[::-1]:
      palindromeSet.add(number)
  if maximum == 0:
    return palindromeSet
  else:
    return max(palindromeSet)

# results
print(palindromes(productsSet(2, 2), 1))
print(palindromes(productsSet(3, 3), 1))