"""
Problem #038: Pandigital multiples

Take the number 192 and multiply it by each of 1, 2, and 3:
  192 × 1 = 192
  192 × 2 = 384
  192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576.
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
giving the pandigital, 918273645, which is the concatenated product of 9
and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed
as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

# checks if the given number is pandigital for the given range of numbers [left, right]
def is_pandigital(number, left, right):
  digits = {str(digit) for digit in range(left, right + 1)}
  for digit in str(number):
    if digit in digits: digits.remove(digit)
    else: return False
  return True if len(digits) == 0 else False

# n > 1 -> we need to concatenate at least 2 numbers and still get a 9-digit number
# => the number should be 5-digit or less (5 + 5 = 10 but we need 9)!

# if fixed number = 2-digit -> can't generate 9-digit since:
#   n = 3 -> 99 * 1 + 99 * 2 + 99 * 3 = 1-digit + 3-digit + 3-digit = 8-digit
#   n = 4 -> ... + 99 * 4 = ... + 3-digit = 11-digit

# same for 3-digit numbers:
# 3-digit + 4-digit -> 7-digit (n = 2)
# ... + 3-or-4-digit -> 11-digit (n = 3)

# hence we start with 4-digit that starts with '9'
# both limits consists of the different digits: 9123 and 9876 (all differs)

# if the second digit is > 4, then we will get while multiplying by 2:
# 2 numbers as 19xxx (instead of 19xxx and 18xxx)
# new limit: 9123 and 9487

def pandigital_multiples():
  pandigitals = set()
  for number in range(9123, 9487 + 1):
    possible_pandigital = int(f'{number}{number * 2}')
    if is_pandigital(possible_pandigital, 1, 9):
      pandigitals.add(possible_pandigital)
  return max(pandigitals)

# tests
print(pandigital_multiples())