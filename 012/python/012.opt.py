# esieve of eratosthenes generator
def esieve(limit):
  # 0 and 1 -> non-primes + all other possible primes
  sieve = [0] * 2 + [1] * (limit - 2)
  # index -> holds the number value
  for number, isprime in enumerate(sieve):
    if isprime: 
      yield number
      for multiple in range(number ** 2, limit, number):
        sieve[multiple] = 0

# returns the number of divisors for a given number
# prime factorization -> product of (powers + 1) of each prime gives the answer
def divisors(number, primelist):
  divisors = 1
  for prime in primelist:
    if number == 1: break
    power = 0
    while number % prime == 0:
      number //= prime
      power += 1
    divisors *= (power + 1)
  # divisors is still 1 -> it is prime
  # prime has 2 divisors: 1 and itself
  return divisors if divisors > 1 else 2

# returns the first triangle number with the greater than 'number' of divisors
# primeslimit -> how many primes do we need?
def triangle_divisors(number, primeslimit):
  # returns triangle number
  triangle = lambda index: index * (index + 1) // 2
  # is this number even or not?
  is_even = lambda number: number % 2 == 0

  primelist = list(esieve(primeslimit))  # generating prime list
  index = 1                             # index for the triangular number

  while True:
    # triangle number is product of -> index and (index + 1) // 2 -> coprimes
    # so we can find number of divisors part by part
    # it is fast because parts are much less than triangle number itself
    if is_even(index):
      divs = divisors(index // 2, primelist) * divisors(index + 1, primelist)
    else:
      divs = divisors(index, primelist) * divisors((index + 1) // 2, primelist)
    
    if divs >= number: return triangle(index)
    index += 1

# tests
print(triangle_divisors(5, 10))
print(triangle_divisors(500, 1000))