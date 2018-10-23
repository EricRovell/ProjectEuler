"""
Problem #027: Quadratic primes

Euler discovered the remarkable quadratic formula: n^2 + n + 41
It turns out that the formula will produce 40 primes for the consecutive integer
values 0 ≤ n ≤ 39.

However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41,
and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula n^2 − 79n + 1601 was discovered, which produces
80 primes for the consecutive values 0 ≤ n ≤ 79.
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:
n^2 + an + b, where |a| < 1000 and |b| ≤ 1000,
where |n| is the modulus/absolute value of n (e.g. |11| = 11 and |−4| = 4).

Find the product of the coefficients, a and b, for the quadratic expression that
produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""

# getting primes set from a file
def data():
  with open('_files/primes_list_10e6.txt') as primes:
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
  
  for a in range(-a_limit + 1, a_limit):
    for b in range(-b_limit + 1, b_limit):

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