# returns the desired rational approximation of sqrt(number)
def econvergents(order):
  # creating a list of [2, 1, 1, 1, 1 ...]
  # slice assignment -> [2; (1, 2 * mult, 1)] where mult [1, 2, 3 ...]
  addenda = [2] + [1] * (order - 1)
  addenda[2::3] = [2 * mult for mult in range(1, len(addenda[2::3]) + 1)]
  # reversing a list because we calculate from the end
  seed, *addenda = addenda[::-1]
  numerator, denominator = 1, seed 
  for addendum in addenda:
    numerator += addendum * denominator
    denominator = denominator
    # get the reciprocal
    numerator, denominator = denominator, numerator

  # to get the final answer we should get the reciprocal
  return denominator, numerator

# generates the sum of digits (reverse order)
def digitsum(number):
  while number:
    yield number % 10
    number //= 10


# solving the problem
def numerator_sum():
  numerator = econvergents(100)[0]
  return sum(digitsum(numerator))
# tests
print(numerator_sum())