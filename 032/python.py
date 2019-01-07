# checks if the given number is pandigital for the given range of numbers [left, right]
def is_pandigital(number, left, right):
  digits = {str(digit) for digit in range(left, right + 1)}
  for digit in str(number):
    if digit in digits: digits.remove(digit)
    else: return False
  return True if len(digits) == 0 else False

# limititng the search space:
# you can get 9-digit number only by:
# (1-digit * 4-digit) OR (2-digit * 3-digit) => both need 4-digit product
# so: multiplicand * multiplier < 10 000
def pandigital_products():
  result = set()
  
  for multiplicand in range(2, 100):
    start = 123 if multiplicand > 9 else 1234
    end = 10000 // multiplicand + 1
    for multiplier in range(start, end):

      number = int(f'{multiplicand}{multiplier}{multiplicand * multiplier}')
      if is_pandigital(number, 1, 9):
        result.add(multiplicand * multiplier)

  return sum(result)

# tests
print(pandigital_products())