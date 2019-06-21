def multsum(limit, *divs):
  assert len(divs) == 2
  # returns the sum of all divs in [1, limit)
  def divsum(divisor):
    lastmult = (limit - 1) // divisor
    return divisor * (1 + lastmult) * lastmult // 2

  return divsum(divs[0]) + divsum(divs[1]) - divsum(divs[0] * divs[1])

# tests
print(multsum(1000, 3, 5))