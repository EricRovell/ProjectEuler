_path = '042_data.txt' # -> path to data file

def get_data(path: str):
  ''' Reading and getting data from a file. '''
  with open(path) as file:
    # read -> remove quotes -> split by commas
    return file.read().replace(r'"', '').split(',')

# triangle number check
istriangle = lambda index: float.is_integer(-0.5 + (0.25 + 2 * index) ** 0.5)

def search(path: str, data_getter_func):
  # get data ->
  #   -> word to alphabet score
  #   -> filter non-triangles
  #   -> length of iterable means how many triangles
  words = data_getter_func(path)
  words = map(lambda word: sum(ord(letter) - 64 for letter in word), words)
  words = filter(istriangle, words)
  return len(list(words))

# results
print(search(_path, get_data))