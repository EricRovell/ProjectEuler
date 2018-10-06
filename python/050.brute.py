'''
Problem #050: Consecutive prime sum

The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
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

# returns
def most_consecutive_sum(limit):

  primes = primesList(limit)
  primes_sum = {}
  
  for index in range(int(limit ** 0.5)):

    sum = 0
    counter = 0

    while True:

      sum += primes[index]
      counter += 1

      if sum in primes:
        primes_sum[counter] = sum
      if sum > limit:
        break

      index += 1

  most = max(primes_sum.keys())
  value = primes_sum[most]
  return f"The highest sum is {value} from {most} consequtive primes."

# tests
print(most_consecutive_sum(100))
print(most_consecutive_sum(1000))
print(most_consecutive_sum(10000))
print(most_consecutive_sum(100000))
print(most_consecutive_sum(1000000))