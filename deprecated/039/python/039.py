# returns all primitive (as tuples) or non-primitive too (as lists)
# pythagorean triplets for a given limit
def pythagorian_triplets(limit, primitive = False):

  def children(parent):
    a, b, c = parent[0], parent[1], parent[2]
    children = []

    children.append((a - 2*b + 2*c, 2*a - b + 2*c, 2*a - 2*b + 3*c))
    children.append((a + 2*b + 2*c, 2*a + b + 2*c, 2*a + 2*b + 3*c))
    children.append((-a + 2*b + 2*c, -2*a + b + 2*c, -2*a + 2*b + 3*c))

    return children
    
  primitives = [(3, 4, 5)]

  seed = primitives[0]
  genetation = children(seed)
  
  while len(genetation) != 0:

    genetation = [triplet for triplet in genetation if all(side < limit for side in triplet)]
    primitives.extend(genetation)

    new_generation = []
    for triplet in genetation:
      new_generation.extend(children(triplet))

    genetation = new_generation
  
  if primitive == True:
    return primitives
  else:

    for triplet in primitives:
      k = 2
      
      while True:
        non_primitive = [k * side for side in triplet]
        
        if all(side < limit for side in non_primitive):
          if non_primitive not in primitives:
            primitives.append(non_primitive)
        else:
          break
        
        k += 1
    
  return primitives

# returns the perimeter with the greatest number of triplets associated with it
def triplet_perimeter_dict(perimeter):
  # usually the hypotenuse is a bit less than half of perimeter
  # generating triplets up to perimeter / 2 as side length limit
  triplets = pythagorian_triplets(perimeter/2)
  perimeter_dict = {}

  for triplet in triplets:
    P = sum(triplet)
    if P <= perimeter:
      if P not in perimeter_dict:
        perimeter_dict[P] = 1
      else:
        perimeter_dict[P] += 1

  greatest_P = max(perimeter_dict, key = perimeter_dict.get)
  triplets_P = perimeter_dict[greatest_P]
  return f'Perimeter with value of {greatest_P} has the greatest number of triplets: {triplets_P}.'

# tests
print(triplet_perimeter_dict(1000))