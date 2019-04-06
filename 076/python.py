def counting_paths(number: int):
  ''' Finds the number of ways you can get a number
  by sum of two integers. '''
  sums = [1] + [0 for _ in range(number)]
  for integer in range(1, number):
    for addend in range(integer, number + 1):
      sums[addend] += sums[addend - integer]
  return sums[-1]

# tests
print(counting_paths(100))