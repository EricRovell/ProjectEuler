# returns the greatest product of n-adjacent digits in the number
def maxProduct(n, number):
 
  i = 0
  number = str(number)

  record = 0
  
  for array in range(len(number) - n):

    product = 1
    for digit in number[i: i + n]:
      product *= int(digit)
  
    if product > record:
      record = product
    
    i += 1
  
  return record

# working with external file where the number is stored
with open('008/data.txt') as number:
  number = number.read()
  # test
  print(maxProduct(4, number))
  print(maxProduct(13, number))