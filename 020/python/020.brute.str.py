# Brute-force solution, still works fast.
# The factorial is calculated using for-loop
# The digits were got by string conversion.

def factorial_digit_sum(number: int) -> int:
  """ Calculates the sum of digits of factorial. """
  factorial = 1
  for mult in range(2, number + 1):
    factorial *= mult
  return sum([int(digit) for digit in str(factorial)])

# results
print(factorial_digit_sum(100))