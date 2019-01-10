# in order for recursion to run fast we cache the results
cache = { 0: 0, 1: 1, }
def fibonacci(number):
  if number in cache:
    return cache[number]
  else:
    cache[number] = fibonacci(number - 1) + fibonacci(number - 2)
    return cache[number]

# getting the sum of even fibonacci numbers below the given limit value
def even_sum(limit):
  total, term = 0, 0
  while True:
    number = fibonacci(term)
    if number > limit: break
    if number % 2 == 0: total += number
    term += 1
  return total

# tests
print(even_sum(4000000))