"""
Problem #025: 1000-digit Fibonacci number

The Fibonacci sequence is defined by the recurrence relation:
Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

# returns the first fibonacci number with "digits" number of digits
def fibonacci(digits):
  array = [0, 1]

  while len(str(array[-1])) != digits:
    array.append(array[-1] + array[-2])
  
  # because of zero included
  return len(array) - 1

# tests
print(fibonacci(3))
print(fibonacci(1000))