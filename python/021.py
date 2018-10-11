"""
Problem #021: Amicable numbers

Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).

If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

# returns all proper divisors of given number
def divisors(number):
  divisors = {1}
  
  for divisor in range(2, number // 2 + 1):
    if number % divisor == 0:
      divisors.add(divisor)
      divisors.add(number // divisor)

  return divisors

# returns the dictionary for interval [start ; end[
# number: sum of all proper divisors of this number
def divisors_dict_sum(start, end):
  divisors_dict = {}

  for number in range(start, end):
    total = sum(divisors(number))
    divisors_dict[number] = total

  return divisors_dict

# return all pair of amicable numbers inside given interval [start, end[
def amicable_numbers(start, end):

  dictionary = divisors_dict_sum(start, end)

  amicable_numbers = set()

  for one_key in dictionary:
    for another_key in dictionary:
      if one_key != another_key:
      
        if one_key == dictionary[another_key]:
          if another_key == dictionary[one_key]:

            pair = frozenset({dictionary[one_key], dictionary[another_key]})
            amicable_numbers.add(pair)

  return amicable_numbers

# returns the sum of all amicable numbers
def answer_sum(start, end):
  total = 0
  amicables = amicable_numbers(start, end)

  for amicable in amicables:
    total += sum(amicable)

  return total


# tests
print(amicable_numbers(2, 300))
print(amicable_numbers(2, 10000))

# answer
print(answer_sum(2, 10000))