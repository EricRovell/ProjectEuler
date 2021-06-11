# prime numbers generator: [a, b] interval of search
# if only one parameter given:
# primes(100) -> [2, 100] interval will be set
def primes(a, b = 2):
  if a < 2: a = 2
  if b == 2: a, b = 2, a
  for possible_prime in range(a, b + 1):
    for number in range(2, int(possible_prime ** 0.5 + 1)):
      if possible_prime % number == 0:
        break
    else:
      yield possible_prime

# returns the largest prime factor of the given number
def largest_prime_factor(number):
  record = 0
  for prime in primes(int(number ** 0.5 + 1)):
    if number % prime == 0:
      record = max(record, prime)
  return record


# test
print(largest_prime_factor(600851475143))