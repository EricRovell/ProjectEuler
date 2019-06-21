# returns the number of term in the collatz sequence for a given number
def collatz_sequence(number):
  if number == 1:
    return 1

  # 1 is counted too
  counter = 1

  while number != 1:

    if number % 2 == 0:
      number //= 2
    else:
      number = 3 * number + 1
    
    counter += 1

  return counter

# returns the longest chain of the collatz sequence in the given interval
def longest_collatz_sequence(start, limit = 1):
  if limit == 1 and start > limit:
    limit = start
    start = 1

  record_num = 0
  record_length = 0

  for number in range(start, limit):
    
    length = collatz_sequence(number)
    if record_length < length:
      record_num = number
      record_length = length

  return f"The longest sequence gives number {record_num} with {record_length} terms."

# tests
print(longest_collatz_sequence(1000000))