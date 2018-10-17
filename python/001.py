'''
Problem #1: Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

def sum_of_multiples(limit, *multiples):
  total = 0

  for number in range(1, limit):
    for multiple in multiples:  

      if number % multiple == 0:
        total += number
        break

  return total

# tests
print(sum_of_multiples(10, 3, 5))
print(sum_of_multiples(1000, 3, 5))
