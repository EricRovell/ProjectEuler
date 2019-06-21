substitution = {
  'IIII'  : 'IV', # -> (4)
  'VIIII' : 'IX', # -> (9)
  'XXXX'  : 'XL', # -> (40)
  'LXXXX' : 'XC', # -> (90)
  'CCCC'  : 'CD', # -> (400)
  'DCCCC' : 'CM'  # -> (900)  
}

roman = {
    'I': '1',
    'V': '5',
    'X': '10',
    'L': '50',
    'C': '100',
    'D': '500',
    'M': '1000'
}

arabic = {
    '1'    : 'I',
    '5'    : 'V',
    '10'   : 'X',
    '50'   : 'L',
    '100'  : 'C',
    '500'  : 'D',
    '1000' : 'M'
}

from re import compile, match

pattern = r'^M{0,4}(CM|CD|DC{0,3}?)(XC|XL|LX{0,3}?)(IX|IV|V?I{0,3}?)'

numeral = 'III'

if match(pattern, numeral):
  print(1)
else:
  print(0)