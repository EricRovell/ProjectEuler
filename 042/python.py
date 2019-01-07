def data():
  with open('042/data.txt') as data:
    words = data.read()
    words = words.replace('"', '')
    words = words.split(',')
  return words

letters = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
           'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17,
           'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
           'Z': 26}

# checks if the given number is Triangle-number
# it is just an inverse function of the Triangle-formula
# index must be an integer if the given number is a Triangle number
def is_triangle(number):
  index = ( -1 + (1 + 8 * number) ** 0.5 ) / 2
  return True if float.is_integer(index) else False

# search for triangle words
def triangle_words(words):
  triangle_words = 0

  for word in words:

    score = 0
    for char in word:
      score += letters[char]

    if is_triangle(score):
      triangle_words += 1

  return triangle_words

# test
print(triangle_words(data()))