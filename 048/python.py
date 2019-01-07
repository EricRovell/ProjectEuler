# returns the sum of self-power number for given interval
# n^n + (n + 1)^(n + 1) + ... + m^m
def powerSeries(n, m):

  sum = 0

  for number in range(n, m + 1):
    sum += number ** number
  
  return sum

# test 1
print(powerSeries(1, 10))
# text 2
number = str(powerSeries(1, 1000))
print(number[-10:])