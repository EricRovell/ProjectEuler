def cache(function):
  history = {0: 0, 1: 2}
  def decorated(*args):
    if args in history:
      return history[args]
    else:
      value = function(*args)
      history[args] = value
      return value
  return decorated

# even fibonacci sequence generator
# using cashe from previous calculations
@cache
def evenfib(index):
  if index == 0: return 0
  if index == 1: return 2
  return 4 * evenfib(index - 1) + evenfib(index - 2)

# solving the problem
def evensum(limit, index = 1):
  total = 0
  fib = evenfib(index)
  while fib < limit:
    total += fib
    index += 1
    fib = evenfib(index)
  return total

print(evensum(4000000))