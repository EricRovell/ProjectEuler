def sqdiff(left: int, right: int):
  ''' Calculates the difference between sum of squares
  and square of sum for all natural numbers in closed interval. \n
    Args:
      left: the beggining of the interval,
      right: the end of the interval.
    Returns:
      An integer.  '''

  sumsq = sum(x ** 2 for x in range(left, right + 1))  # sum of squares
  sqsum = sum(x for x in range(left, right + 1)) ** 2  # square of sum
  return sqsum - sumsq

# tests
print(sqdiff(1, 100))