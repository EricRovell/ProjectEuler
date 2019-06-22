def is_bouncy(number: int) -> int:
  """ Evaluates if the given integer is:
        - increasing -> returns 1
        - decreasing -> returns -1
        - bouncy     -> returns 0
  """

  # ! only integer can be evaluated
  if not isinstance(number, int):
    raise TypeError('Only integer can be evaluated.')

  def digits(number: int) -> int:
    """ Generates the digits of the integer from right-to-left. """
    while number:
      yield number % 10
      number //= 10

  # if the integer is 'increasing':
  # all the digits become smaller or equal from the end:
  # 134468 -> 1 < 3 < 4 <= 4 < 6 < 8
  def is_increasing(number: int) -> bool:
    """ 'Increasing' integer test. """
    last = number % 10
    for digit in digits(number):
      if digit <= last:
        last = digit
        continue
      else:
        return False
    return True

  # if the integer is 'descreasing':
  # all the digits become smaller or equal from the end:
  # 66420 -> 6 >= 6 > 4 > 2 > 0
  def is_decreasing(number: int) -> bool:
    """ 'Decreasing' integer test. """
    last = number % 10
    for digit in digits(number):
      if digit >= last:
        last = digit
        continue
      else:
        return False
    return True

  # if the number not increasing nor decreasing -> it's bouncy
  if is_increasing(number): return 1
  if is_decreasing(number): return -1
  return 0

# ! tests

# checking some known integers:
def test_numbers():
  numbers = [134468, 66420, 155349]
  cases = {
    1: 'increasing',
    0: 'bouncy',
    -1: 'decreasing'
  }
  for number in numbers:
    case = is_bouncy(number)
    print(f'The number {number} is {cases[case]}.')

# checking how many bouncy number there are up the given limit
def how_many_are_bouncy(limit: int, bouncy = 0):
  for number in range(100, limit + 1):
    if not is_bouncy(number):
      bouncy += 1
  print(bouncy)

# checking what propotion does bouncy numbers up below given limit
def proprotion_of_bouncy(limit: int, bouncy = 0):
  for number in range(100, limit + 1):
    if not is_bouncy(number):
      bouncy += 1
  print(bouncy / limit)

# getting the least integer for which the proportion of bouncy numbers first reaches 'percent' value
def bouncy_proportion(percent):
  bouncy = 0
  number = 1
  while True:
    if not is_bouncy(number):
      bouncy += 1
      if 100 * bouncy == percent * number: break
    number += 1
  return number

# result
print(bouncy_proportion(99))