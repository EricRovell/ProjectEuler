"""
Problem #007: 10001st prime

By listing the first six prime numbers:
2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

# returns the n-th prime number
def primeNumber(n):

  if not isinstance(n, int) or n <= 0:
    return "Argument should be a positive integer greater than 0."

  primes = []
  possiblePrime = 2

  while len(primes) != n:
    
    isPrime = True

    for number in range(2, int(possiblePrime ** 0.5 + 1)):
      if possiblePrime % number == 0:
        isPrime = False
        break

    if isPrime:
      primes.append(possiblePrime)
    
    possiblePrime += 1

  return primes[-1]

# test
print(primeNumber(6))
print(primeNumber(10001))  