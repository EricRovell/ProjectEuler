from math import log

_path = '099/_099_data.txt'

def get_data(path: str):
  ''' Reading data from file. '''
  exponents = []
  with open(path) as file:
    for line in file.readlines():
      line = line.replace('\n', '').split(',')
      line = list(map(int, line))
      exponents.append(line)
  return exponents

def exp_max(path: str):
  data = get_data(path)
  # (pair) <-> (number, power)
  data = list(map(lambda pair: pair[1] * log(pair[0]), data))
  return data.index(max(data)) + 1

# tests
print(exp_max(_path))