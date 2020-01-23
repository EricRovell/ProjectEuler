def summations(value: int):
  ''' Calculates how many different ways can number be written
  as a sum of at least two positive integers \n
    Args:
      value: integer to find number of summations for
    Returns:
      number of summations, int '''

  ways = [1] + [0 for _ in range(value)]
  for number in range(1, value):
    for addend in range(number, value + 1):
      ways[addend] += ways[addend - number]
  # the last element is the answer
  return ways[-1]

# print(summations(5))