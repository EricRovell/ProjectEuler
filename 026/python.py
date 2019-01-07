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