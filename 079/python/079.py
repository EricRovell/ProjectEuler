path = '079/data.txt'  # path to dataset
passlength = 7         # estimated password's length

def passderivation(path, passlength):
  # getting logging data -> (digit, digit, digit...)
  logs = set()
  with open(path) as data:
    for line in data.readlines():
      line = line.replace('\n', '')
      if not line in logs:
        logs.add(line)

  # making up pairs of each log
  # to track the following digits
  # (digit1, digit2, digit3) -> (digit1, digit2), (digit2, digit3)
  pairs = set()
  for log in logs:
    for digit1, digit2 in zip(log[:-1], log[1:]):
      pairs.add( (int(digit1), int(digit2)) )
  # no need of logs anymore
  del logs

  # here we will got the answer
  lastdigit = []
  # how long the password?
  for _ in range(7):
    # finding the digit that never occurs at the start of the pair
    # it should be the last digit in the password
    digits = {digit for pair in pairs for digit in pair}
    for pair in pairs:
      if pair[0] in digits:
        digits.remove(pair[0])

    # assuming that the only one unused digit left -> the last one
    # updating answer
    assert len(digits) == 1
    lastdigit.insert(0, *digits)

    # to get the last digit when 1 pair of digits left
    if len(pairs) == 1:
      last = set(*pairs) - set(digits)
      lastdigit.insert(0, *last)

    # removing pairs that has the last found following digit   
    pairs = [pair for pair in pairs if pair[1] not in digits]

  return lastdigit

# tests
print(passderivation(path, passlength))