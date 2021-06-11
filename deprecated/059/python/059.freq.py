# Frequency analysis approach:
#   1. -> Grab the data.
#   2. -> Analyse the massage:
#     2.1 -> key length -> break message into three parts;
#     2.2 -> find the most occuring element in each part;
#     2.3 -> more likely to be a 'space' character ord = 32;
#     2.4 -> get key parts using XOR on each most common element.
#   3. -> decrypt the message using found key and convert to characters.
#   4. -> to get the answer sum the decrypted message without converting to text.

_path = "059_data.txt"

def get_data(path = _path):
  ''' Reading and getting manageable data. '''
  with open(path) as file:
    # read -> split -> str to int
    file = file.read().split(',')
    return list(map(int, file))

def analysis(message = get_data(), key_length = 3):
  """ Searches for a key using frequency analysis. """
  space_char = 32 # -> most common character

  def most_occuring(iterable):
    """ Gets the most occuring element/s from the list. """
    elements = {}
    for element in iterable:
      if elements.get(element, None) != None:
        elements[element] += 1
      else:
        elements[element] = 1
    return max(elements, key=elements.get)
  # breaking into parts -> get the most occuring element -> XOR it as the most common
  thirds = [message[begin::key_length] for begin in range(key_length)]
  key = [most_occuring(part) ^ space_char for part in thirds]
  return ''.join([chr(num) for num in key])


def encrypt(message = get_data(), key = analysis()):
  """ Encrypt / Decrypt the message with XOR. """
  def cycle(key: str) -> str:
    """ Infinite cycle generator. """
    while True:
      for char in key: yield char
  message = [code ^ ord(key) for code, key in zip(message, cycle(key))]
  return ''.join(map(chr, message))


# results
message = encrypt()
score = sum(ord(char) for char in message)
# -> answer for a problem
print(f'The score for the message is: {score}.')
# -> decrypted message itself
print(message)   