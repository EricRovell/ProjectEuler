maximum_sum = 0

for a in range(1, 100):
  for b in range(1, 100):
    digits_sum = sum( [int(digit) for digit in str(a ** b)] )
    maximum_sum = max(maximum_sum, digits_sum)

print(maximum_sum)