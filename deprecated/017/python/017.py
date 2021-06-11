number_word = {
  1: 'One',
  2: 'Two',
  3: 'Three',
  4: 'Four',
  5: 'Five',
  6: 'Six',
  7: 'Seven',
  8: 'Eight',
  9: 'Nine',
  10: 'Ten',
  11: 'Eleven',
  12: 'Twelve',
  13: 'Thirteen',
  14: 'Fourteen',
  15: 'Fifteen',
  16: 'Sixteen',
  17: 'Seventeen',
  18: 'Eighteen',
  19: 'Nineteen',
  20: 'Twenty',
  30: 'Thirty',
  40: 'Forty',
  50: 'Fifty',
  60: 'Sixty',
  70: 'Seventy',
  80: 'Eighty',
  90: 'Ninety',
  100: "One hundred",
  200: "Two hundred",
  300: "Three hundred",
  400: "Four hundred",
  500: "Five hundred",
  600: "Six hundred",
  700: "Seven hundred",
  800: "Eight hundred",
  900: "Nine hundred",
  1000: "One thousand"
  }

def number_to_word(n):

  def tens(n):
    tens = number_word[n - n % 10]
    digit = number_word[n % 10].lower()
    return f"{tens} {digit}"

  def hundreds(n):
    hundreds = number_word[n - n % 100]

    # case: [101:110]
    if n % 100 < 10:
      digit = number_word[n % 100].lower()
      return f"{hundreds} and {digit}"
    # case hundreds + teens [113:119]
    elif 10 < n % 100 < 21:
      digit = number_word[n % 100].lower()
      return f"{hundreds} and {digit}"
    # case hundreds + tens [110, 120...]
    elif n % 10 == 0:
      decade = number_word[n % 100].lower()
      return f"{hundreds} and {decade}"

    tens_and_digits = (tens(n % 100)).lower()
    return f"{hundreds} and {tens_and_digits}"

  try:
    return(number_word[n])

  except KeyError:
    try:
      if 20 < n < 100:
        return tens(n)
      elif 100 <= n < 1000:
        return hundreds(n)
    except KeyError:
      return('Number out of range')

# count symbols from "n" till "m"
def count_symbols(n, m = 1):
  if m == 1 and n > m:
    m = n
    n = 1
  string = ""
  for i in range(n, m + 1):
    string += number_to_word(i)
  string = string.replace(" ", "")
  return len(string)

# tests
print(count_symbols(5))
print(count_symbols(1000))

# test the translation
# print(number_to_word(1000))