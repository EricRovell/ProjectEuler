# returns the n-th prime number
def primeNumber(n):

  if not isinstance(n, int) or n <= 0:
    return "Argument should be a positive integer greater than 0."

  primes = []
  possiblePrime = 2

  while len(primes) != n:
    
    for number in range(2, int(possiblePrime ** 0.5 + 1)):
      if possiblePrime % number == 0:
        break
    else:
      primes.append(possiblePrime)
    
    possiblePrime += 1

  return primes[-1]

# test
print(primeNumber(6))
print(primeNumber(10001))  