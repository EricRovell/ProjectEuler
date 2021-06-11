# Division primality check

# side length: numbers -> (1, 1), (3, 9), (5, 25), (7, 49)
#   side -> length: length = side ^ 2
#   length -> side: side = sqrt(length)
# Generating corner numbers:
# ! bottom part of the main diagonal contain perfect squares -> check 3 corners
#   3  ->  5 ->  7  -> (+2) [+6]
#   13 -> 17 -> 21  -> (+4) [+10]
#   31 -> 37 -> 43  -> (+6) [+14]
#   57 -> 65 -> 73  -> (+8) [+18]

def corners():
  start, length = 3, 9
  step, jump = 2, 6
  while True:
    yield start
    for _ in range(2):
      start += step
      yield start, length
    step += 2
    start += jump
    jump += 4
    length += 2

# ! count length of the spiral!


def diagonal_prime_ratio(limit):
  spiral_length = 9
  primes = 0
  while primes / spiral_length > limit:
    for number, length in corners():
      if is_prime(number):
        primes += 1
    