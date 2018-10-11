"""
Problem #014: Longest Collatz sequence

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

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