"""
Problem #015: Lattice paths

Starting in the top left corner of a 2×2 grid (/files/015.gif),
and only being able to move to the right and down,
there are exactly 6 routes to the bottom right coner.

How many such routes are there through a 20×20 grid?
"""

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