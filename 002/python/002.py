# returns the n-th fibonacci number in sequance
def fibonacci(n):
  if n == 0 or n == 1:
    return 1
  elif n == 2:
    return 2
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

# returns the list of all fibonacci numbers below n-value
def fibList(n):
  array = []
  item = 0

  isBigger = False

  while not isBigger:
    number = fibonacci(item)
    if number < n:
      array.append(number)
      item += 1
    else:
      isBigger = True
  
  return array

# returns the sum of all even numbers in a list
def evenSum(n):
  sum = 0
  array = fibList(n)

  for number in array:
    if number % 2 == 0:
      sum += number
  
  return sum

print(evenSum(4000000))