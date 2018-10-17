"""
Problem #035: Circular primes

The number, 197, is called a circular prime because all rotations of the digits:
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100:
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

# getting primes set from a file
def data():
  with open('_files/primes_list_10e6.txt') as primes:
    primes = primes.read()
    primes = primes.replace('\n', '')
    primes = primes.split(',')
    # primes = list(map(int, primes))
  return set(primes)

def cyclic_permutation(string):
  permutations = {string}

  string = [char for char in string]
  for _ in range(len(string) - 1):
    string.append(string.pop(0))
    permutations.add("".join(string))

  return permutations

def circular_primes(primes):
  circular_primes = set()
  
  for prime in primes:
    permutation = cyclic_permutation(prime)

    is_circular = True
    for number in permutation:
      if number not in primes:
        is_circular = False
        break
    
    if is_circular:
      circular_primes.add(frozenset(permutation))

  # count
  counter = 0
  for element in circular_primes:
    for _ in element:
      counter += 1

  return counter, circular_primes

# test
print(circular_primes(data()))