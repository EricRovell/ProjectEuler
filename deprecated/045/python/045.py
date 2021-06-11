# hexagonals are subset for triangle numbers
# substitute 'n' as '2m - 1' in triangle formula to get hexagonal formula

# to get the answer we need to generate hexagonal numbers
# and check them if they are pentagonal

def is_pentagonal(number):
  index = ( 1 + (1 + 24 * number) ** 0.5 ) / 6
  return True if float.is_integer(index) else False

# returns the first 'amount' of numbers as list
# that are triangle, pentagonal and hexagonal at the same time
def ternary_search(amount):
  numbers = []
  n = 1
  
  while len(numbers) < amount:
    hex_number = n * (2 * n - 1)

    if is_pentagonal(hex_number):
      numbers.append(hex_number)
    
    n += 1
  
  return numbers

# tests
print(ternary_search(3))