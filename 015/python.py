# returns the number of possible path for [x, y] grid
def lattice_paths(x, y):
  possible_paths = (factorial(x + y)) / (factorial(x) * factorial(y))
  return int(possible_paths)

# factorial function
def factorial(number):
  if number == 0 or number == 1:
    return 1
  else:
    return number * factorial(number - 1)

# tests
print(lattice_paths(2, 2))
print(lattice_paths(20, 20))