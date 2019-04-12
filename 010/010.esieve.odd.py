def esieve(limit: int):
  ''' Prime numbers generator, sieve of Erathosthenes algorithm. \n
  Uses less memory, odd indexes version of algorithm.
    Args:
      limit: the last exclusive integer to generate primes before
    Returns:
      yields prime numbers
  '''
  boundary = int(limit ** 0.5) + 1
  # we start sieve from 3, all numbers assumed to be odd
  # [0 -> 3, 1 -> 5, 2 -> 7, ...]
  size = (limit // 2 - 1)
  sieve = size * [1]
  # index to number: i -> 2i + 3
  # we start to sieve from the prime^2, so:
  #   starting point: index + prime
  #   jump: prime
  yield 2
  for index, isprime in enumerate(sieve):
    if isprime:
      prime = 2 * index + 3
      yield prime
      if prime > boundary: continue
      for multiple in range(index + prime, size, prime):
        sieve[multiple] = 0

def primesum(limit: int):
  ''' Calculates the sum of all primes below the given limit value. \n
    Args:
      limit: the exclusive boundary integer
    Returns:
      The sum of all prime numbers. '''
  return sum(list(esieve(limit)))

# tests
# print(primesum(10))
# print(primesum(2000000))