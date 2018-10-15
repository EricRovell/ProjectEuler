"""
Problem #022: Names scores

Using ('_files/022.txt'), a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order.

Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.
What is the total of all the name scores in the file?
"""

def get_data():
  with open('_files/022.txt') as names_book:
    names_book = names_book.read()
    names_book = names_book.replace('"', r'')
    names_book = names_book.split(',')
    names_book.sort()    
  return names_book

letter_digit = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 
                'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 
                'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21,
                'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

def score(data, dictionary):
  score = 0
  for name in data:

    name_score = 0
    for letter in name:
      if letter in dictionary:
        name_score += dictionary[letter]

    score += name_score * (data.index(name) + 1)

  return score

# test
print(score(get_data(), letter_digit))