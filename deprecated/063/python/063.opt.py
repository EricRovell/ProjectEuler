from math import ceil

result = 0

for x in range(1, 10):
  result += 10 - int(10 ** (1 - 1/x))

print(result)

