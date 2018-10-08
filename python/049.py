'''
Problem #049: Prime permutations

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways:
  1. each of the three terms are prime,
  2. each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

'''

# returns the primes list within given interval
def primesList(n, m = 2):

  if m == 2 and n > m:
    m = n
    n = 2

  if not isinstance(n, int) or not isinstance(m, int) or n < 0 or m < 0:
    return "Argument should be a positive integer"

  primes = []

  for possiblePrime in range(n, m + 1):

    isPrime = True

    for number in range(2, int(possiblePrime ** 0.5 + 1)):
      if possiblePrime % number == 0:
        isPrime = False
        break

    if isPrime:
      primes.append(possiblePrime)

  return primes

def sequence():

  primes = primesList(1000, 9999)
  primes_seq = []

  for i in range(len(primes)):
    for j in range(len(primes)):

      if i == j:
        break

      for k in range(len(primes)):

        if j == k:
          break

        first = primes[i]
        second = primes[j]
        third = primes[k]

        if third - second == second - first:
          first_symbols = set(str(first))
          second_symbols = set(str(second))
          third_symbols = set(str(third))

          if first_symbols == second_symbols == third_symbols:
            primes_seq.append((first, second, third))

  return primes_seq

# test
print(sequence())