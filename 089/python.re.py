from re import compile, sub

patterns = compile(r'IIII|VIIII|XXXX|LXXXX|CCCC|DCCCC')

# tracking the length before substitution and after
before, after = 0, 0
with open('089/data.txt') as numerals:
  for numeral in numerals.readlines():
    numeral = numeral.replace('\n', '')
    before += len(numeral)
    # all needed substitutions have the length of 2
    # so we don't actually make the correct numeral
    # just getting the right track of removed digits
    numeral = sub(patterns, 'KK', numeral)
    after += len(numeral)
# the overall difference
print(before - after)

""" substitution = {
  'IIII'  : 'IV', # -> (4)
  'VIIII' : 'IX', # -> (9)
  'XXXX'  : 'XL', # -> (40)
  'LXXXX' : 'XC', # -> (90)
  'CCCC'  : 'CD', # -> (400)
  'DCCCC' : 'CM'  # -> (900)  
} """