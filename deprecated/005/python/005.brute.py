def smallestMultiple(n, m = 1):

  if not isinstance(n, int) or not isinstance(m, int) or n < 0 or m < 0:
    return "Argument should be a positive integer"
  
  if m == 1 and n > m:
    m = n
    n = 1
  
  multiple = m
  isFinished = False

  while not isFinished:
    for factor in range(n, m + 1):
      if multiple % factor != 0:
        multiple += 1
        break
      elif factor == m and multiple % m == 0:
        isFinished = True
  
  return multiple

# tests
print(smallestMultiple(1, 10))
print(smallestMultiple(9, 11))