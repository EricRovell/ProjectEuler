target = 200
coin_sizes = { 1, 2, 5, 10, 20, 50, 100, 200 }
changes = [0] * (target + 1)
changes[0] = 1

for coin in coin_sizes:
  for change in range(coin, target + 1):
    changes[change] += changes[change - coin]

print(changes[-1])