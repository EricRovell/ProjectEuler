# returns a list of sum of divisors as [index -> sum of it's divisors]
# propers = True -> calculating sum of proper divisors instead:
# sum of proper divisors = sum of divisors - number itself
# returns a list for numbers under the given limit as [0; limit)
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

# returns the longest amicable chain under the given limit
def longest_amicable_chain(limit):
  longest = []                     # updating the answer
  sums = divisorsum(limit, True)   # getting proper sums for all numbers at once
  visited = {0, 1}                 # if number don't get in cycle -> forget it
  
  for number in range(1000, limit):
    if number in visited: continue
    chain, cycled = [], True
    connector = sums[number]

    while not connector in chain:
      chain.append(connector)
      try:
        connector = sums[connector]
      except IndexError:
        cycled = False
        break
      if connector > limit or connector in visited:
        cycled = False
        break

    if cycled:
      if len(longest) < len(chain):
        longest = chain

    visited.update(chain)

  # 1st number in chain is not part of Amicable chain
  # it is the seed number from where it grows
  return longest


# tests
print(longest_amicable_chain(1000000))