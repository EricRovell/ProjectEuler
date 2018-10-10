"""
Problem #012: Highly divisible triangular number

The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

1: 1
3: 1,3
6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

# returns the number of divisors for a given number
def divisors(number):

  factors = 0

  # factors come in pairs, for example 28: 1/28; 2/14, 4/7 
  for divisor in range(1, int(number ** 0.5 + 1)):
    if number % divisor == 0:
      factors += 2
    if number == divisor ** 2:
      factors -= 1
  
  return factors

# returns the the n-index triangle number
def triangle_number(index):
  number = index * (index + 1) / 2
  return int(number)

# returns the first triangle number with more the "threshold" number of divisors
def more_divisors(threshold):

  i = 2
  
  while True:

    number = triangle_number(i)
    factors = divisors(number)

    if factors > threshold:
      return number
    else:
      i += 1

# test
print(more_divisors(5))
print(more_divisors(500))