_path = '102_data.txt'

def get_data(path = _path):
  ''' Reading data from a file: path. \n
  Returns:
    list of tuples with coordinates \n
    ((int, int), (int, int), (int, int))'''
  with open(path) as file:
    file = file.read().replace('\n', ',').split(',')
    file.remove('')
    file = map(int, file)
    file = [(x, y) for x, y in zip(*[iter(file)] * 2)]
    return [(a, b, c) for a, b, c in zip(*[iter(file)] * 3)]

def area(a, b, c):
  """ Calculates the area of the triangle in Cartesian system. \n
    Args: \n
      a, b, c: points with (x, y) coordinates. \n
    Returns: \n
      Area of the given triangle. """
  return abs((a[0] * (b[1] - c[1]) +
              b[0] * (c[1] - a[1]) +
              c[0] * (a[1] - b[1])) / 2)

def origin(triangle, point = (0, 0)) -> bool:
  '''
  Checks if the given point is located inside the triangle. \n
  Args: \n
    triangle: tuple of points of the triangle each with (x, y) coordinates.
              tuple: ((int, int), (int, int), (int, int)).
    point: (x, y) to check location against the triangle,
           if not specified -> (0, 0) \n
  Returns: \n
    bool: does this point located inside the triangle or not.
  '''
  a, b, c = triangle
  full = area(a, b, c)
  part1 = area(a, b, point)
  part2 = area(b, c, point)
  part3 = area(c, a, point)
  return full == (part1 + part2 + part3)

# searching for the number triangles that has the origin in the interior
def is_origin(triangles = get_data()):
  triangles = list(filter(origin, triangles))
  return len(triangles)

# tests
print(is_origin())