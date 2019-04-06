# brute force solution
# don't have flexibility
# for learning purposes only

value = 200  # how many we want to collect
ways  = 0    # how many ways to collect the target

for coin200 in range(value, -1, -200):
  for coin100 in range(coin200, -1, -100):
    for coin50 in range(coin100, -1, -50):
      for coin20 in range(coin50, -1, -20):
        for coin10 in range(coin20, -1, -10):
          for coin5 in range(coin10, -1, -5):
            for coin2 in range(coin5, -1, -2):
              ways += 1

print(ways)