# returns the continued expansion of the number's square root
# does not work for perfect squares -> raises ValueError
# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion
def expansion(number):
  # sqrt integer solution
  def isqrt(number):
    initial = number
    seed = (initial + 1) // 2
    while seed < initial:
      initial = seed
      seed = (initial + number // initial) // 2
    return initial
  # validation
  if number == isqrt(number) ** 2:
    raise ValueError('The square root of the number should be irrational.')
  
  # m, d, a - in algorithm description
  complement = 0
  denominator = 1
  addendum = isqrt(number)

  sequence = [addendum]
  while addendum != sequence[0] * 2:
    complement = denominator * addendum - complement
    denominator = (number - complement ** 2) // denominator
    addendum = (sequence[0] + complement) // denominator
    sequence.append(addendum)

  return sequence


def odd_periods(limit):
  counter = 0
  for number in range(2, limit + 1):
    try:
      sequence = expansion(number)
    except ValueError:
      continue
    if (len(sequence) - 1) % 2 == 1: counter += 1

  return counter

# tests
print(odd_periods(10000))
