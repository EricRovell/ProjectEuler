def sqdiff(limit):
  ''' Calculates the difference between sum of squares
  and square of sum for all natural numbers in closed interval. \n
    Args:
      limit: the end of the interval, [1, limit]
    Returns:
      An integer.  '''

  sumsq = lambda limit: (2 * limit**3 + 3 * limit**2 + limit) / 6  # sum of squres  
  sqsum = lambda limit: ((1 + limit) * limit / 2) ** 2             # squre of sum
  return int(sqsum(limit) - sumsq(limit))

# tests
# print(sqdiff(100))