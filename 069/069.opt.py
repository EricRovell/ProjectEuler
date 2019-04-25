# The optimized solution.
# The value of n / phi(n) is only dependent on the number of unique prime factors.
# So, to solve the problem, the inversed totient function should be minimized.
#   Inversed totient function has a (1 - 1 / p) in the denominator.
#   (1 / p) -> smaller the prime factors, more is subtracted from 1 in...
#   ... (1 - 1 / p) -> it will be minimal for a small prime factors,
# then we should be taking the product of the smalles primes to get the answer.

def primes():
  """ Generates prime numbers indefinetly.
  Uses trial division algorithm. """
  def infinity(start = 3, step = 2):
    """ Infinite counter generator. """
    while True:
      yield start
      start += step
  # yielding 2 as the only even prime number
  # so we can check only odd numbers instead
  yield 2
  for number in infinity():
    for factor in range(3, int(number ** 0.5) + 1, 2):
      if number % factor == 0:
        break
    else:
      yield number

def totient_max(limit):
  result = 1
  prime = primes()
  next_prime = next(prime)
  while result * next_prime <= limit:
    result *= next_prime
    next_prime = next(prime)
  return result

# results
print(totient_max(1000000))