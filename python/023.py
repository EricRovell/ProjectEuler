"""
Problem #023: Non-abundant sums

A perfect number is a number for which the sum of its proper divisors is exactly equal
to the number. For example, the sum of the proper divisors of 28 would be:
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two abundant numbers is 24.

By mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though
it is known that the greatest number that cannot be expressed as
the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as
the sum of two abundant numbers.
"""

# returns the sum of all numbers under the given limit that cannot be
# written as the sum of two abundant numbers
def abundant_sum_limit(limit):

  def is_abundant(number):
    divisors = {1}
    for divisor in range(2, int(number ** 0.5) + 1):
      if number % divisor == 0: divisors.update({divisor, number // divisor})
    return True if sum(divisors) > number else False

  abundants = []
  for number in range(1, limit + 1):
    if is_abundant(number): abundants.append(number)
  
  numbers = [False] * (limit + 1)
  for abundant in abundants:
    for another in abundants:

      total = abundant + another
      if abundant + another <= limit:
        numbers[total] = True
      else:
        break
    
  non_abundant = [index for index in range(len(numbers)) if numbers[index] == False]

  return sum(non_abundant)

# tests
print(abundant_sum_limit(28123))