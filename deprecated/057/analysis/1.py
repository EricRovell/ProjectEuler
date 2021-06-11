import matplotlib.pyplot as plt



def sq2convergents(limit):
  # num/den - numerator/denominator
  num, den = 3, 2
  for index in range(1, limit + 1):
    yield (index, num, den)
    num, den = (num + 2 * den, den + num)

def search(limit):
  convergents = sq2convergents(limit)
  for convergent in convergents:
    index, num, den = convergent
    if len(str(num)) > len(str(den)):
      yield index


def plot():
  more_digits = list(search(1000))
  diff = [more_digits[i+1] - more_digits[i] for i in range(len(more_digits) - 1)]

  print(diff)

  """ plt.plot(more_digits)
  plt.xlabel('some numbers')
  plt.show() """

  num_bins = 3
  n, bins, patches = plt.hist(diff, num_bins, facecolor='blue', alpha=0.5)
  plt.show()

plot()
