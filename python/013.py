"""
Problem #013: Large sum

Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
(_files/013.txt)
"""

sum = 0

with open("_files/013.txt") as data:
  for line in data.readlines():
    sum += int(line)

sum = str(sum)
print(sum[:10])
  