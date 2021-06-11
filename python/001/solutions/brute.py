def multiples_sum(limit: int) -> int:
  total: int = 0
  for number in range(limit):
    if number % 3 == 0 or number % 5 == 0:
      total += number
  return total