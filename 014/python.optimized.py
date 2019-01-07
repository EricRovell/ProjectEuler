# optimization: we do not recalculate the sequence again and again
# 26 -> 13, so we already know the sequence for "13",
# just adding the history to existing counter

# returns the dictionary with "number" = "length_of_chain" for Collatz sequence
def collatz_sequence(limit):
  
  sequence_length = {1:1}

  for number in range(2, limit):

    counter = 0
    untouched = number
    while True:      

      if number in sequence_length:
        counter += sequence_length[number]
        break
      
      if number % 2 == 0:
        number //= 2
      else:
        number = 3 * number + 1

      counter += 1
  
    sequence_length[untouched] = counter

  return sequence_length

# returns the number with the longest chain from Collatz sequence
def longest_chain(limit):
  dictionary = collatz_sequence(limit)
  number = max(dictionary, key = dictionary.get)
  
  return f"The longest chain has the {number} with {dictionary[number]} terms."

# test
print(longest_chain(1000000))