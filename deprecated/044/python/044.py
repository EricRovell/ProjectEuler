# checks if the given number is Pentagonal-number
# it is just an inverse function of the Pentagonal-formula
# index must be an integer if the given number is a Pentagonal number
def is_pentagonal(number):
  index = ( 1 + (1 + 24 * number) ** 0.5 ) / 6
  return True if float.is_integer(index) else False

# search
def answer():
  i = 1
  while True:
    i += 1
    one_pentagonal = i * (3 * i - 1) * 0.5

    for j in range(i - 1, 0, -1):
      another_pentagonal = j * (3 * j - 1) * 0.5

      if is_pentagonal(one_pentagonal + another_pentagonal):
        if is_pentagonal(one_pentagonal - another_pentagonal):

          return one_pentagonal - another_pentagonal

# test
print(answer())