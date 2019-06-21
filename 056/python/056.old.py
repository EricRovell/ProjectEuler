# My 1st solution for this problem I wrote 4 monthes ago.
# Works fine, but I don't like it now.
# Leaving as it is to watch my progress.

maximum_sum = 0

for a in range(1, 100):
  for b in range(1, 100):
    digits_sum = sum( [int(digit) for digit in str(a ** b)] )
    maximum_sum = max(maximum_sum, digits_sum)

# result
print(maximum_sum)