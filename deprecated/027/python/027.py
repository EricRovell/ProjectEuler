# getting primes set from a file
def data():
  with open('_data/primes_list_10e6.txt') as primes:
    primes = primes.read()
    primes = primes.replace('\n', '')
    primes = primes.split(',')
    primes = list(map(int, primes))
  return set(primes)

# returns the coefficients a,b and the greatest number of consecutive primes
# for equation(n) => prime number
def quadratic_primes(a_limit, b_limit, primes_list):
  record = {'a': 0, 'b': 0, 'n': 0}

  def equation(n, a, b):
    return n ** 2 + a * n + b
  
  # 'b' can't be even, equation(0) = b, so 'b' should be a prime
  # incrementing 'b_limit' to assure the step = 2
  
  for a in range(-a_limit + 1, a_limit):
    for b in range(-b_limit, b_limit + 1):

      if b % 2 == 0: continue

      n = 0
      while True:
        if equation(n, a, b) not in primes_list: break
        if n > record['n']: record = {'a': a, 'b': b, 'n': n}
        n += 1

  return record

# tests
print(quadratic_primes(2, 42, data()))
print(quadratic_primes(80, 1602, data()))
print(quadratic_primes(1000, 1000, data()))