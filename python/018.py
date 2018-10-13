"""
Problem #018: Maximum path sum I

By starting at the top of the triangle below and moving to adjacent numbers
on the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below (_files/018.txt).
"""

def get_data():
  with open('_files/018.txt') as numbers:
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