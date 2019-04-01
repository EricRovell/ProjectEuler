_path = '083/_083_data.txt'
_test = '083/_083_data_test.txt'

def get_data(path: str):
  ''' getting data from file as matrix \n
      parameter: path to the file '''
  matrix = []
  with open(path) as file:
    for line in file.readlines():
      line = line.split(',')
      line = list(map(int, line))
      matrix.append(line)
  return matrix

def dijkstra(path: str):
  ''' Dijkstra algorithm, returns the min value path
      from the left top corner to the right bottom. '''
  infinity = float('inf')
  matrix   = get_data(path)
  size     = len(matrix)

  visited   = [ [False] * size for _ in range(size) ]
  distances = [ [infinity] * size for _ in range(size)]
  distances[0][0] = matrix[0][0]
  queue = [(0, 0)]

  # generating neighbours indexes as tuple
  neighbours = lambda i, j: ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1))

  while len(queue) > 0:
    row, col = min(queue, key = lambda v: distances[v[0]][v[1]])
    queue.remove((row, col))
    visited[row][col] = True

    for nrow, ncol in neighbours(row, col):

      if ( 0 <= nrow < size and
           0 <= ncol < size and
           not visited[nrow][ncol] ):

            distances[nrow][ncol] = min(
              distances[nrow][ncol],
              distances[row][col] + matrix[nrow][ncol]
              )

            if (nrow, ncol) not in queue:
              queue.append((nrow, ncol))

  return distances[-1][-1]

print(dijkstra(_path))