def digits(number: int, length: int):
  ''' Retuns integer that consists of the digits from it's tail. \n
    Args:
      number: the number to get digits from,
      length: the number of digits to get.
    Returns:
      integer fron last length-digits in natural order. '''
  return number % 10 ** length

prime = 28433 * 2 ** 7830457 + 1
prime_last_digits = digits(prime, 10)

# test
print(prime_last_digits)