# returns the number of divisors for a given number
def divisors(number):

  factors = 0

  # factors come in pairs, for example 28: 1/28; 2/14, 4/7 
  for divisor in range(1, int(number ** 0.5 + 1)):
    if number % divisor == 0:
      factors += 2
    if number == divisor ** 2:
      factors -= 1
  
  return factors

# returns the the n-index triangle number
def triangle_number(index):
  number = index * (index + 1) / 2
  return int(number)

# returns the first triangle number with more the "threshold" number of divisors
def more_divisors(threshold):

  i = 2
  
  while True:

    number = triangle_number(i)
    factors = divisors(number)

    if factors > threshold:
      return number
    else:
      i += 1

# test
print(more_divisors(5))
print(more_divisors(500))