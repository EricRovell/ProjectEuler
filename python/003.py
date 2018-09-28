'''
Problem #3: Largest prime factor
 
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

# returns the primes list within given interval
def primesList(n, m = 2):

  if m == 2 and n > m:
    m = n
    n = 2

  if not isinstance(n, int) or not isinstance(m, int) or n < 0 or m < 0:
    return "Argument should be a positive integer"

  primes = []

  for possiblePrime in range(n, m + 1):

    isPrime = True

    for number in range(2, int(possiblePrime ** 0.5 + 1)):
      if possiblePrime % number == 0:
        isPrime = False
        break

    if isPrime:
      primes.append(possiblePrime)

  return primes

# returns all the prime factors for a given number "n"
# optional argument
def factorsList(n, maximum = False):

  primes = primesList(int(n ** 0.5) + 1)
  factors = set()

  # we don't need primes that are bigger than sqrt(n)
  # primes = list(filter(lambda x: x < n ** 0.5 + 1, primes))

  for prime in primes:
    if n % prime == 0:
      factors.add(prime)
  
  if maximum == False:
    return factors
  else:
    return max(factors)

# test
print(factorsList(13195, maximum = True))
print(factorsList(600851475143, maximum = True))