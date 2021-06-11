# returns a list of the sums of divisors for the numbers: [0, number)
# if propers = True -> returns sum of proper divisors
# algorithm itself works as sieve:
# according to prime factorization
# sum of divisors = (1 + 2 + 2^2 ...)(1 + 3 + 3^2...)(1 + 5 + 5^2...)
# so we updating the sum of the number gradually
# for example: num % 4 == 0 has (1 + 2 + 2^2), but 8 does (1 + 2 + 2^2 + 2^3)
def divisorsum(limit, propers = False):
  sums = [0] + [1] * (limit - 1)
  # we are 'sieving' numbers,
  # if it is still 1 - it is prime
  for prime in range(2, limit):
    if sums[prime] == 1:
      current = 1
      factor = prime
      while factor < limit:
        # (1 + prime + prime ^ 2 + prime ^ 3 ...)
        multiple = current + factor
        # sieving numbers that are divisible by
        # current prime factor: p, p**2, p**3...
        for number in range(factor, limit, factor):
          sums[number] //= current
          sums[number] *= multiple
        current = multiple
        factor *= prime

  if propers:
    return [total - index for index, total in enumerate(sums)]
  else:
    return sums

# returns all amicable pairs within a dictionary within a given limit
# {number: sum of it's proper divisors}
def amicables(limit):
  amicable_pairs = {}
  proper = divisorsum(limit, True)

  for number in range(2, limit):
    a = proper[number]  # possible pair
    if a > len(proper) - 1:
      continue
    b = proper[a]       # reverse check
    # number == b  -> amicable pair
    # number != a  -> no self-made pairs {number: number}
    # number < a   -> no mirrored dublicates
    if number == b and number != a and number < a:
      amicable_pairs[number] = a   
  
  return amicable_pairs

# returns sum of all amicable numbers within given interval: [1, limit)
def amicables_sum(limit):
  total = 0
  for key, value in amicables(limit).items():
    total += (key + value)
  return total

# tests
print(amicables_sum(10000))