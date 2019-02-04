# sieve of Eratosthenes
def sieve(limit):
  primes_list = []
  # 0 and 1 -> False + all other numbers
  primes = [False] * 2 + [True] * (limit - 2)
  # index -> holds the number value
  for number, is_prime in enumerate(primes):
    if is_prime:
      primes_list.append(number)
      for multiple in range(number * number, limit, number):
        primes[multiple] = False
  return primes_list

# using prime factorization we can find the sum factors
def proper_divisors_sum(number, primes):
  initial_number = number
  total, i = 1, 0
  
  if number in primes: return 1
  while number > 1 and i < len(primes):
    power = 1
    if number % primes[i] == 0:
      while number % primes[i] == 0:
        number //= primes[i]
        power += 1
      total *= (primes[i] ** power - 1) // (primes[i] - 1)
    i += 1

  return total - initial_number

# getting all amicable numbers below the given limit
def amicables(limit):
  primes = sieve(limit)
  amicable_pairs = {}

  for number in range(2, limit):
    a = proper_divisors_sum(number, primes)  # possible pair
    b = proper_divisors_sum(a, primes)       # reverse check
    # number == b  -> amicable pair
    # number != a  -> no self-made pairs {number: number}
    # number < a   -> no mirrored dublicates
    if number == b and number != a and number < a:
      amicable_pairs[number] = a      
  
  return amicable_pairs

# tests
print(amicables(10000))