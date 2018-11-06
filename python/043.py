"""
Problem #043: Sub-string divisibility
 
The number, 1406357289, is a 0 to 9 pandigital number because it is made up
of each of the digits 0 to 9 in some order, but it also has a rather interesting
sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on.
In this way, we note the following:

d2 d3 d4= 406 is divisible by 2
d3 d4 d5 = 063 is divisible by 3
d4 d5 d6 = 635 is divisible by 5
d5 d6 d7 = 357 is divisible by 7
d6 d7 d8 = 572 is divisible by 11
d7 d8 d9 = 728 is divisible by 13
d8 d9d 10 = 289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

# returns a list of all permutation of the given iterable
# works as generator -> use list() or set()
def permutations(iterable): 
  
  if len(iterable) == 0: return None
  if len(iterable) == 1: return iterable[0]
  
  permutated = [] 
  
  for index in range(len(iterable)): 
    seed = iterable[index]
    remaining = iterable[ : index] + iterable[index + 1 : ] 
  
    for permutation in permutations(remaining): 
      permutated.append(seed + permutation)

  return permutated

def sub_string_divisibility():
  total = 0

  pandigitals = set(permutations('0123456789'))

  # 'p' as pandigital
  for p in pandigitals:
    
    indexes = [1, 2, 3, 4, 5, 6, 7]
    divisors = [2, 3, 5, 7, 11, 13, 17]

    if p[0] != 0:
      if all( int(p[index] + p[index + 1] + p[index + 2]) % divisor == 0 for index, divisor in zip(indexes, divisors) ):
        total += int(p)

  return total

# tests
print(sub_string_divisibility())