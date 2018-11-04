"""
Problem #042: Coded triangle numbers

The n-th term of the sequence of triangle numbers is given by,
t(n) = 0.5 * n * (n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical
position and adding these values we form a word value.
For example, the word value for SKY is 19 + 11 + 25 = 55 = t(10).
If the word value is a triangle number then we shall call the word a triangle word.

Using _files/042.txt, a 16K text file containing nearly two-thousand common
English words, how many are triangle words?
"""

def data():
  with open('_files/042.txt') as data:
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