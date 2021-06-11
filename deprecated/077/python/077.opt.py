def primes_generator(limit=None):
  # infinite integers generator
  def inf_counter(start=1, step=1):
    while True:
      yield start
      start += step

  natural_numbers = inf_counter(3, 2)
  # yield 2 as the only one even prime
  # this way it is easier to check only odd numbers
  yield 2
  for number in natural_numbers:    
    for divisor in range(2, int(number ** 0.5 + 1)):
      if not number % divisor: break      
    else:
      if limit != None and number > limit: return
      yield number
      

def prime_summations(target):
  # this solution uses infinite primes generator because the limit is unknown
  # every necessary prime is generated and pushed to array after every unsuccesful loop
  number = 2 
  primes_gen = primes_generator()
  primes = [ next(primes_gen) ]

  while True:
    ways = [1] + [0 for _ in range(number)]
    for prime in primes:
      for integer in range(prime, number + 1):
        ways[integer] += ways[integer - prime]
    
    if ways[number] > target:
      # arr index represents the checked number
      return len(ways) - 1

    number += 1
    primes.append(next(primes_gen))


#print(prime_summations(5000))
