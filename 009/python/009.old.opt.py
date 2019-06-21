# My 1st solution. Was writtend some time ago.
# Poorly written, but still effective.
# Leaving it to watch my progress from time to time.

# returns all pythagorean triplets with desired perimeter
def pythagorean_triplets(perimeter):
  # parent / child triplets algorithm
  def children(parent):
    a, b, c = parent[0], parent[1], parent[2]
    children = []

    children.append((a - 2*b + 2*c, 2*a - b + 2*c, 2*a - 2*b + 3*c))
    children.append((a + 2*b + 2*c, 2*a + b + 2*c, 2*a + 2*b + 3*c))
    children.append((-a + 2*b + 2*c, -2*a + b + 2*c, -2*a + 2*b + 3*c))

    return children
  
  # (3, 4, 5) - seed for all primitive triplets
  primitives = [(3, 4, 5)] 
  # 1st generetaion
  genetation = children(primitives[0])
  
  # generating primitive triplets
  while len(genetation) != 0:

    genetation = [triplet for triplet in genetation if all(side < perimeter/2 for side in triplet)]
    primitives.extend(genetation)

    new_generation = []
    for triplet in genetation:
      new_generation.extend(children(triplet))

    genetation = new_generation
  
  # generating non-primitive triplets
  for triplet in primitives:
    k = 2
    while True:
      non_primitive = [k * side for side in triplet]
      if all(side < perimeter/2 for side in non_primitive):
        if non_primitive not in primitives:
          primitives.append(non_primitive)
      else:
        break
      k += 1
  
  # filters triplets => only with desired perimeters stays
  triplets_with_perimeter = [triplet for triplet in primitives if sum(side for side in triplet) == perimeter]
  return triplets_with_perimeter

# results
print(pythagorean_triplets(1000))