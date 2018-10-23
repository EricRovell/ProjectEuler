"""
Problem #026: Reciprocal cycles

A unit fraction contains 1 in the numerator.
The decimal representation of the unit fractions with denominators 2 to 10 are given:
1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part. """

# converts the rational fraction to decimal
# limit => limits the number of digits
# repetition => should we detect repetition or not
# period => returns period (if presented) or None
def rational_to_decimal(numerator, denominator, period = False, limit = None, repetition = True):

  digit = numerator // denominator

  numerator = 10 * (numerator - digit * denominator)
  decimal = f'{digit}.'
    
  # long division
  # intermediate numerator : index of the string
  # first state index begins from 2 (after zero and dot)
  # same numerator means repetition  
  # from the last index that numerator was enciuntered at
  states = {}
    
  while numerator > 0 and (limit == None or limit > 0):
       
    if repetition:

      previous_index = states.get(numerator, None)
      if previous_index != None:

        repeat_begin = previous_index
        repeat_not = decimal[ :repeat_begin]
        repeat = decimal[repeat_begin: ]

        if period: return f'{repeat}'

        return f'{repeat_not}({repeat})'

      states[numerator] = len(decimal)
                    
    digit = numerator // denominator
    decimal += str(digit)
    numerator = 10 * (numerator - digit * denominator)

    if limit != None: limit -= 1
    
  if numerator > 0: return f'{decimal}...'
  if period: return None
  
  return decimal

#
def longest_period():

  periods = {}

  for denominator in range(1, 1000):
    period = rational_to_decimal(1, denominator, period = True)

    if period == None:
      periods[denominator] = 0
    else:
      periods[denominator] = int(period)
  
  number = max(periods, key = periods.get)
  period = len(str(periods[number]))

  return f'The longest period has number {number} with {period} period length.'

# test
print(longest_period())