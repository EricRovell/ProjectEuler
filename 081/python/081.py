# data file path
path = '081/_081_data.txt'
start = (0, 0)

# getting tha data
def get_data(path: str):
  matrix = []
  with open(path) as file:
    for line in file.readlines():
      line = line.split(',')
      line = list(map(int, line))
      matrix.append(line)
    return matrix

def minimal_path_sum_2(path, start):
  ''' returns the minimum path from starting point to the right bottom '''
  matrix = get_data(path)        # getting data as matrix
  size = len(matrix)             # grid size -> should be square
   
  # bottom and right
  for index in range(size - 2, -1 , -1):
    matrix[index][-1] += matrix[index + 1][-1] # right
    matrix[-1][index] += matrix[-1][index + 1] # bottom

  for i in range(size - 2, -1, -1):
    for j in range(size - 2, -1, -1):
     matrix[i][j] += min( matrix[i + 1][j], matrix[i][j + 1] )

  return matrix[start[0]][start[0]]
  

# tests
print(minimal_path_sum_2(path, start))