# sqrt by subtraction method
# http://www.afjarvis.staff.shef.ac.uk/maths/jarvisspec02.pdf
def sqrt(number, precision):
  limit = 10 ** (precision + 1)
  a, b = 5 * number, 5
  while b < limit:
    if a >= b:
      a, b = a - b, b + 10
    else:
      a, b = a * 100, (b - 5) * 10 + 5
  return b

# digits generator
# number -> digit by digit
def digits(number):
  while number:
    yield number % 10
    number //= 10

# solving the problem
def decimalsum():
  total = 0
  squares = {number ** 2 for number in range(1, 10)}
  for number in range(2, 100):
    if number in squares: continue
    root = sqrt(number, 100)
    # digits generator works from the last digits
    # so we take 100 digits from end
    total += sum( list(digits(root))[-100:] )
  return total

# tests
print(decimalsum())