sum = 0

with open("013/data.txt") as data:
  for line in data.readlines():
    sum += int(line)

sum = str(sum)
print(sum[:10])
  