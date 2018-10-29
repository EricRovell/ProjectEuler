"""
Problem #037: Truncatable primes

The number 3797 has an interesting property. Being prime itself,
it is possible to continuously remove digits from left to right,
and remain prime at each stage: 3797, 797, 97, and 7.

Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right
and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes (for this problem).
"""

# primes generator [left_limit; right_limit]
def prime(left, right):
  for possiblePrime in range(left, right + 1):
    for number in range(2, int(possiblePrime ** 0.5 + 1)):
      if possiblePrime % number == 0:
        break
    else:
      yield possiblePrime

# returns a list of all truncation of the given number
# direction: -1 - for left truncation; 1 - for right only; 0 - for both
def truncate(number, direction = 0):
  if 0 <= number <= 9: return [number]

  number = str(number)

  left = [int(number[index:]) for index in range(len(number))]
  if direction == -1: return left
  right = [int(number[:index]) for index in range(1, len(number) + 1)]
  if direction == 1: return right

  left.extend(right)
  return left
  
# returns the list of the first "amount" of truncatable primes
def truncatable_primes(amount):
  primes = set()
  truncatable_primes = set()

  while True:
    for prime_number in prime(2, 10 ** 9):
      primes.add(prime_number)
      truncated = set(truncate(prime_number))

      if truncated.issubset(primes):
        truncatable_primes.add(prime_number)

      if len(truncatable_primes) == amount:
        return truncatable_primes

# tests
print(truncatable_primes(15))