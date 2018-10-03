"""
Problem #010: Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

# returns the sum of all primes below given limit value
def primes_sum(limit):
  
  if not isinstance(limit, int):
    return "Number must be an integer."

  if limit == 2:
    return None
    
  sum = 0
    
  for possiblePrime in range(2, limit + 1):

    isPrime = True

    for number in range(2, int(possiblePrime ** 0.5 + 1)):
      if possiblePrime % number == 0:
        isPrime = False
        break

    if isPrime:
      sum += possiblePrime
      
  return sum

# tests
print(primes_sum(10))
print(primes_sum(2000000))