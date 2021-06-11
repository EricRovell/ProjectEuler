from math import floor

phi = (1 + 5 ** 0.5) / 2
psi = (1 - 5 ** 0.5) / 2
sq5 = 5 ** 0.5

binet = lambda n: floor((phi ** n - psi ** n) / sq5)
  
def even_fib_sum(limit: int) -> int:
  index, total = 3, 0
  while True:
    fibonacci = binet(index)
    if fibonacci < limit:
      total += fibonacci
      index += 3
    else:
      break
  return total