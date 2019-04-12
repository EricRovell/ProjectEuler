_path = '022/data.txt'

def get_data(path: str):
  with open(path) as file:
    file = file.read().split(',')
    return sorted(file)
    
# ord() -> A-Z -> 65-90
def scores(path: str, names = get_data(_path)):
  name_score = lambda name: sum(ord(letter) - 64 for letter in name)
  names = map(name_score, names)
  return sum((index + 1) * score for index, score in enumerate(names))
  
print(scores(_path))