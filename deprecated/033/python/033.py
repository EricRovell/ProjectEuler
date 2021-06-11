from fractions import Fraction

fractions = set()
for denominator in range(11, 100):
  for numerator in range(12, 100):

    if numerator < denominator:
      if numerator != 10 and denominator != 10:
        fractions.add((numerator, denominator))
      else:
        continue

solution = set()
for fraction in fractions:
  numerator, denominator = str(fraction[0]), str(fraction[1])

  if denominator[0] == '0' or denominator[1] == '0': continue
  
  index = [(0, 0), (1, 0), (0, 1), (1, 1)]

  for i, j in index:
    if numerator[i] == denominator[j]:
      i = 0 if i == 1 else 0
      j = 0 if j == 1 else 0
      if Fraction(int(numerator), int(denominator)) == Fraction(int(numerator[i]), int(denominator[j])):
        solution.add((numerator, denominator))
  """ elif numerator[0] == denominator[1]:
    if Fraction(int(numerator), int(denominator)) == Fraction(int(numerator[1]), int(denominator[0])):
      solution.add((numerator, denominator))
  elif numerator[1] == denominator[0]:
    if Fraction(int(numerator), int(denominator)) == Fraction(int(numerator[0]), int(denominator[1])):
      solution.add((numerator, denominator))
  elif numerator[1] == denominator[1]:
    if Fraction(int(numerator), int(denominator)) == Fraction(int(numerator[0]), int(denominator[0])):
      solution.add((numerator, denominator)) """

product = [1, 1]
for fraction in solution:
  product[0] *= int(fraction[0])
  product[1] *= int(fraction[1])

print(Fraction(product[0], product[1]))