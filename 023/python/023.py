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