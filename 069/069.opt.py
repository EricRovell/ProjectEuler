# The optimized solution
# The value of n / phi(n) is only dependent on the number of unique prime factors.
# (1 - 1 / p) will be minimal for a small p
# taking the product of the smalles primes is the only resonable thing to do

def primes():
  """ Generates prime numbers indefinetly.
  Uses trial division algorithm. """
  def infinity(start = 3, step = 2):
    """ Infinite counter generator. """
    while True:
      yield start
      start += 1
  # yielding 2 as the only even prime number
  # so we can check only odd numbers instead
  yield 2
  for number in infinity():
    if number % 2 == 0: continue
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