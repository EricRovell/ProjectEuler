import matplotlib.pyplot as plt

def brute(limit):
  # num/den - numerator/denominator
  num, den = 3, 2
  counter = 0
  for _ in range(1, limit + 1):
    yield counter
    if len(str(num)) > len(str(den)):
      counter += 1
    num, den = (num + 2 * den, den + num)

def approximate(limit):
  for index in range(1, limit + 1):
    bound = 2 * (index // 13)
    if index % 13 < 8:
      yield bound
    else:
      yield bound + 1


def plot_error(limit):
  x = list(range(1, limit + 1))

  errors = [exact - approx for exact, approx in zip(brute(limit), approximate(limit))]

  print(errors)

  print(errors.count(-1) / 1000, errors.count(0) / 1000, errors.count(1) / 1000)

  plt.scatter(x, errors, color="blue", alpha=0.5, s=1)
  plt.xlabel('some numbers')
  plt.show()

plot_error(1000)