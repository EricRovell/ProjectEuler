# returns Ulam's spiral as list of lists
# direction: 1 for clockwise and -1 for anti-clockwise
# show = True => prints spiral into console and returns None
# show = False => returns spiral as list
def ulams_spiral(size, direction = -1, show = False):
  if size % 2 == 0: raise ValueError
  
  spiral = [ [None] * size for _ in range(size) ]
  step = 1

  # position
  x, y = size // 2, size // 2
  spiral[y][x] = step

  for i in range(1, size // 2 + 1):
  
    # right, one time (1)
    x += 1
    step += 1
    spiral[y][x] = step

    # up/down one time (1, 3, 5)
    for _ in range(i * 2 - 1):
      if direction == 1: y += 1
      elif direction == -1: y -= 1
      step += 1
      spiral[y][x] = step

    # left, down, right: complete the square (2, 4, 6, 8)
    for _ in range(i * 2):
      x -= 1
      step += 1
      spiral[y][x] = step
    for _ in range(i * 2):
      if direction == 1: y -= 1
      elif direction == -1: y += 1
      step += 1
      spiral[y][x] = step
    for _ in range(i * 2):
      x += 1
      step += 1
      spiral[y][x] = step

  if show == True:
    for row in spiral: print(row)
    else:
      return None

  return spiral

# returns sum of both diagonals of the given matrix
def diagonal_sum(matrix):
  size = len(matrix)
  total = 0

  for i in range(size):
    for j in range(size):

      if i == j or i + j == size - 1:
        total += matrix[i][j]
  
  return total

# tests
print(diagonal_sum(ulams_spiral(5)))
print(diagonal_sum(ulams_spiral(1001)))