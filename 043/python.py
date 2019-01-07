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