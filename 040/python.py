# returns the digit with index of Champernowne's constant
def champernowne_digit(index):
  
  if 0 < index <= 9:
    return index
  
  # returns the digit length of the given generation (series)
  def generation(k):
    return 9 * k * 10 ** (k - 1)

  # getting the series of given index
  k = 1
  while index > generation(k):
    index -= generation(k)
    k += 1
  
  # (index - 1): series begins with 0 (10, 11, 12 ... 100, 101, 102...)
  # location is the number itself,
  # we divide the residual value of index and divide it by k - number of digits in this series
  # adding the starting value of the series
  # shift (remainder) means the digit in location number [0, 1, 2...]
  location = (index - 1) // k + 10 ** (k - 1)
  shift = (index - 1) % k

  return str(location)[shift]


# test
def answer():
  indexes = [(10 ** x) for x in range(7)]
  
  product = 1
  for index in indexes:
    product *= int(champernowne_digit(index))
    
  return product

print(answer())