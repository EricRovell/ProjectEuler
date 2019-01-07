from functools import reduce

def get_data():
  with open('011/data.txt') as data:
    grid = []
    for line in data.readlines():
      line = line.split(' ')
      line = list(map(int, line))
      grid.append(line)

  return grid

def max_grid(grid, adjacent):

  columns = len(grid)
  rows = len(grid[0])
  border = adjacent - 1

  greatest = 0

  for row in range(rows):
    for column in range(columns):

      if column < columns - border:
        # right / left
        elements = [grid[row][column + index] for index in range(adjacent)]
        product = reduce((lambda x, y: x * y), elements)
        greatest = max(greatest, product)

      if row < rows - border:
        # down / up
        elements = [grid[row + index][column] for index in range(adjacent)]
        product = reduce((lambda x, y: x * y), elements)
        greatest = max(greatest, product)

        if column < columns - border:
          # diagonal main
          elements = [grid[row + index][column + index] for index in range(adjacent)]
          product = reduce((lambda x, y: x * y), elements)
          greatest = max(greatest, product)

        if column > border:
          # diagonal reverse
          elements = [grid[row + index][column - index] for index in range(adjacent)]
          product = reduce((lambda x, y: x * y), elements)
          greatest = max(greatest, product)

  return greatest

# tests
print(max_grid(get_data(), 2))
print(max_grid(get_data(), 3))
print(max_grid(get_data(), 4))