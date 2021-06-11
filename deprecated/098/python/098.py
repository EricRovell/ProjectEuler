_path = '098/_098_data.txt'

def get_data(path: str):
  anagrams = {}
  with open(path) as file:
    file = file.read().replace('"', r'').split(',')
    file = set(filter(lambda x: x != x[::-1], file)) # -> no palindromes
    for word in file:
      sorted_word = ''.join(sorted(word))
      if sorted_word not in anagrams:
        anagrams[sorted_word] = {word}
      else:
        anagrams[sorted_word].add(word)

    # getting anagrams only
    anagrams = [value for key, value in anagrams.items() if len(value) > 1]
    return anagrams

print(get_data(_path))
