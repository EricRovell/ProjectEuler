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