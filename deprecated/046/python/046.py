# the idea is to transform the conjecture a bit:
# ( odd_composite - prime ) / 2 => must be a square

# updating a primes list using a generator
# issue: after update we always have one greater prime than that we need
# so, we make a check only up to the last element in the prime list [:-1]

# primes generator
def primes():
  
  def count():
    n = 2
    while True:
      yield n
      n += 1
  
  for possiblePrime in count():
    for number in range(2, int(possiblePrime ** 0.5 + 1)):
      if possiblePrime % number == 0:
        break
    else:
      yield possiblePrime


def goldbach_conjecture_breaker():
  prime = primes()
  primes_list = [next(prime)]

  def is_square(number):
    number = number ** 0.5
    return True if float.is_integer(number) else False
  
  answer = 9
  while True:

    # updating prime list
    while True:
      if primes_list[-1] <= answer:
        primes_list.append(next(prime))
      else: break

    # answer must be a composite odd number
    if answer in primes_list:
      answer += 2
      continue
    
    if any( is_square((answer - number) / 2) for number in primes_list[:-1] ):
      answer += 2
      continue
    else:
      return answer
    
# test
print(goldbach_conjecture_breaker())