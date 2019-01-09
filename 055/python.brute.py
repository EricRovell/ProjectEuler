# returns True / False if the given number is Lychrel number
def lychrel(number):
  for _ in range(50):
    number += int( str(number)[::-1] )
    if str(number) == str(number)[::-1]:
      return False
  return True

# returns a number of Lychrel numbers below given limit
def lychrel_numbers(limit):
  numbers = set()
  for number in range(1, limit):
    if lychrel(number):
      numbers.add(number)

  return len(numbers)

# tests
print(lychrel_numbers(10000))