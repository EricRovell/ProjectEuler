# returns the largest prime factor of the given number
def largest_prime_factor(number):
  # the greatest prime factor is less or equal than sqrt(number)
  max_factor = int(number ** 0.5 + 1)

  # 2 - is the only even prime
  # factorizing it out will allow us to increase
  # factor by 2 each time after
  while number % 2 == 0:
    number //= 2

  factor = 3
  last_factor = 3
  while number > 1 and factor < max_factor:

    while number % factor == 0:
      last_factor = factor
      number //= factor

    last_factor = factor
    factor += 2

  return last_factor

# tests
print(largest_prime_factor(600851475143 )) 