def is_bouncy(number: int) -> bool:
  """ Evaluates if the given integer is bouncy. """

  increasing, decreasing = False, False
  last_digit = number % 10
  number //= 10

  while number:
    next_digit = number % 10
    number //= 10

    if next_digit < last_digit:
      increasing = True
    elif next_digit > last_digit:
      decreasing = True

    last_digit = next_digit

    if increasing and decreasing:
      return True
  
  return decreasing and increasing


# getting the least integer for which the proportion of bouncy numbers first reaches 'percent' value
def bouncy_proportion(percent):
  bouncy = 0
  number = 1
  while True:
    if is_bouncy(number):
      bouncy += 1
      if 100 * bouncy == percent * number: break
    number += 1
  return number

# result
print(bouncy_proportion(99))