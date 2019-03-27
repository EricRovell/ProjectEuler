# path to the data file
path = '067/_067_data.txt'

def get_data(path: str):
  ''' getting data from file '''
  data = []
  with open(path) as file:
    for line in file.readlines():    # reading line by line
      line = line.replace('\n', '')  # - replace escape symbols 
      line = line.split(' ')         # - split line by whitespaces
      line = list(map(int, line))    # - convert all strings to integers
      data.append(line)              # - adding list of integers to data
    return data

# get_data('067/_067_data.txt')
def pairwise(iterable):
  ''' (a, b, c, d) -> (a, b), (b, c), (c, d) '''
  a = iterable[:-1]      # all but the last
  b = iterable[1:]       # all but the first
  for pair in zip(a, b):
    yield pair

def max_path_sum(path):
  data = get_data(path)
  data = data[::-1]
  # we had to reverse the data order, we will woks from the bottom instead
  # -> taking two last rows at the same time
  for row, prevrow in pairwise(data):
    # getting:
    #  pair  -> two numbers from bottom row
    #  index -> value from upper row, we add the biggest number from pair
    # so the biggest sum will appear at the top eventually
    for pair, index in zip( pairwise(row), range(len(prevrow)) ):
      prevrow[index] += max(pair)
  return data[-1]

# getting the result
print(max_path_sum(path))