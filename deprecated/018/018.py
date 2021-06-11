def get_data():
  with open('018/data.txt') as numbers:
    data = []
    for line in numbers.readlines():
      line = line.split(' ')
      line = list(map(int, line))
      data.append(line)

  return data

# algorithm evaluates the highest sum from bottom
def max_path_sum(data):

  while len(data) != 1:

    for index in range(len(data[-2])):

      neighbour_left = data[-1][index]
      neighbour_right = data[-1][index + 1]

      if neighbour_left > neighbour_right:
        data[-2][index] += neighbour_left
      else:
        data[-2][index] += neighbour_right

    del data[-1]
         
  return data

# test
print(max_path_sum(get_data()))