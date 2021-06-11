"""
  It is a brute force solution, still very fast.
  
  Steps:

  1. Initialize generator function:
    1.1. The initial convergent is constructed with numerator, denominator.
    1.2. The "for" loop initialized to check all indexes up to the limit:
      - The convergent yilded from the generator function.
      - Next convergent is being constructed and overrides the previous one.
  2. Initialize a function for searching the solution.
    2.1. Initialize counter to zero or use counter parameter with default value.
    2.2. Using loop iterate over values from generator.
      - Destruct values from the generated object.
      - Compare number of digits.
      - If the numerator has more -> update the counter.
    2.3. Return the counter. It is the answer.
"""  

def sq2convergents(limit):
  # num/den - numerator/denominator
  num, den = 3, 2
  for _ in range(1, limit + 1):
    yield (num, den)
    num, den = (num + 2 * den, den + num)

def search(limit, counter = 0):
  convergents = sq2convergents(limit)
  for convergent in convergents:
    num, den = convergent
    if len(str(num)) > len(str(den)):
      counter += 1
  return counter


#print(search(1000))
