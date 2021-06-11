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