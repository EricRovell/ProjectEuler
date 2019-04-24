# Not the best approach if asked the result itself.
# Can be done more straightforwards actually.
# Still, it was interesting to write (the ratio -> the decimal) converter.

def decimal(numerator: int, denominator: int, limit = None, get_period = False):
  '''
  converts ratio to it's decimal form.
    Args:
      limit: how many decimal digits to get.
              default value: None -> get full decimal. 
      get_period: returns period of ratio instead if needed (True)
    Returns:
      str   -> if the decimal is reccuring: '1.02(345)',
      float -> if the decimal is non-reccuring: 1.25,
      str   -> if get_period = True and the ratio has a period: '0235',
               if no period is present, returns '0'
  '''
  unit = numerator // denominator
  divident = 10 * (numerator - unit * denominator)
  # long division:
  #   intermediate divident: index of the string
  #   first state index begins from 2 (after zero and dot)
  #   same divident means repetition  
  #   from the last index that divident was encountered at
  states = {}
  decimal = f'{unit}.'
  # while:
  #   divident is present
  #   limit is not required OR still not met
  while divident and (limit == None or limit):
    previous_index = states.get(divident, None)
    if previous_index != None:
      period_start = previous_index
      non_periodic = decimal[ : period_start]
      period       = decimal[period_start : ]
      if get_period: return f'{period}'
      return f'{non_periodic}({period})'

    states[divident] = len(decimal)
    unit = divident // denominator
    decimal += str(unit)
    divident = 10 * (divident - unit * denominator)
    if limit: limit -= 1
  
  # if divident > 0: return float(decimal)  # limited decimal
  if get_period: return '0'                   # no period -> 0
  return float(decimal)

# decorator -> gives human answer
def informative(func):
  def func_wrapper(limit):
    denominator, period = func(limit)
    return f'The longest period length {period} has the fraction 1/{denominator}.'
  return func_wrapper

# search
@informative
def longest_period(limit):
  """
  Searches for the denominator with the longest period of the form 1/d.
    Args:
      limit: defines the search space, where denominator is in [1, limit)
    Returns
      A fraction and ith longest period: (denominator, period_length).
  """
  # dict -> denominator: length of the period for 1 / denominator
  periods = { d: len(decimal(1, d, get_period = True)) for d in range(1, limit) }
  denominator = max(periods, key = periods.get)
  return denominator, periods[denominator]

# results
print(longest_period(1000))