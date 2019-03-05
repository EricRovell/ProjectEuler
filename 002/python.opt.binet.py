from math import floor, sqrt

# generates even fibonacci numbers using Binet's formula with floor
def evenfib(limit, index = 1):
  phi = (1 + sqrt(5)) / 2
  while True:
    fib = floor(phi ** (3 * index) / sqrt(5) + 0.5)
    if fib < limit: yield fib
    else: break
    index += 1

# solving the problem
total = sum(number for number in evenfib(4000000))
print(total)