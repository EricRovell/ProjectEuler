# data files: problem case and test example
_path = '082/_082_data.txt'
_test = '082/_082_data_test.txt'

def get_data(path: str):
  ''' reading file -> getting data '''
  matrix = []
  with open(path) as file:
    for line in file.readlines():
      line = line.split(',')
      line = list(map(int, line))
      matrix.append(line)
  return matrix

def min_path_sum_III(path):
  ''' returns the minimum path sum from left to the right columns '''
  matrix = get_data(path)  # getting data from file
  size   = len(matrix)     # assert: it is squre matrix
  
  # starting with the rightmost column
  result = [matrix[i][size - 1] for i in range(size)]
  for col in range(size - 2, -1, -1):
    # just turning right
    result[0] += matrix[0][col]
    # traverse down
    for row in range(1, size):
      down  = result[row - 1] + matrix[row][col]
      right = result[row] + matrix[row][col]
      result[row] = min(down, right)
    # traverse up
    for row in range(size - 2, -1, -1):
      up = result[row + 1] + matrix[row][col]
      result[row] = min(up, result[row])
  
  return min(result)

# tests
print(min_path_sum_III(_test))