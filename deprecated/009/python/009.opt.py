def pytriples(perimeter, primitives_only = False):
  ''' Generates all integer pythagorian triplets within given perimeter limit. \n
    Args:
      perimeter: limit value for perimeter the triplets can have,
      primitives_only: generate only primitive tripltes ot not. \n
    Returns:
      Set with triplets as tuples -> { (int, int, int) }.  '''

  primitives = {(3, 4, 5)} # seed triplet
  def children(parent):
    '''
    Berggren's Linear Transformations algortithm. \n
    Calculates 3 children Pythagorian triples for the given parent triple. \n
      Args:
        parent: primitive Pythagorian triple in the form (a: int, b: int, c: int). \n
      Returns:
        A set of 3 children primitive Pythagorian triples in the form: \n
        set: (a: int, b: int, c: int). '''
    a, b, c = parent
    return {
            ( a - 2*b + 2*c,   2*a - b + 2*c,   2*a - 2*b + 3*c),
            ( a + 2*b + 2*c,   2*a + b + 2*c,   2*a + 2*b + 3*c),
            (-a + 2*b + 2*c,  -2*a + b + 2*c,  -2*a + 2*b + 3*c) }

  # generating elementary triplets recursively
  def triples(primitives, seed):
    generation = children(seed)
    for triplet in filter(lambda x: sum(x) <= perimeter, generation):
      primitives.add(triplet)
      triples(primitives, triplet)

  # generating non-primitive triples
  def multiples(primitives):
    non_primitives = set()
    for triplet in primitives:
      k = 2
      while True:
        multiple = tuple(side * k for side in triplet)
        if sum(multiple) <= perimeter:
          non_primitives.add(multiple)
          k += 1
        else:
          break
    primitives |= non_primitives

  triples(primitives, *primitives)  # -> generating primitives first       
  if not primitives_only:            # -> generating non-primitives (default) if needed
    multiples(primitives)
  # returning the set of Pythagorian triples
  return primitives

# solving the problem
def perimeter_pytriple(perimeter, generator):
  ''' Returns all the Pythagorian triples with fixed perimeter. '''
  triples = generator(perimeter)
  primitives = set(filter(lambda x: sum(x) == perimeter, triples))
  return primitives

# tests
print(perimeter_pytriple(1000, pytriples))