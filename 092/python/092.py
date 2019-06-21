# reversed digits from the number generator
def digits(number):
  while number:
    yield number % 10
    number //= 10

# returns the sum of squared digits of the given number
sqdigitsum = lambda number: sum(digit ** 2 for digit in digits(number))

def loop89(limit):
  terminated89 = {89}              # storing numbers that stuck in 89 loop
  terminated01 = {1}               # storing numbers that stuck in  1 loop
  for number in range(1, limit):
    sequent = sqdigitsum(number)
    chain = {number, sequent} 
    while True:         
      if sequent in terminated01:
        terminated01 |= chain
        break
      elif sequent in terminated89:
        terminated89 |= chain
        break
      else:
        sequent = sqdigitsum(sequent)
        chain.add(sequent)
  return len(terminated89)

# tests
print(loop89(10**7))     