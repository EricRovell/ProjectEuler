def multiples_sum(limit: int) -> int:
  def divsum(divisor):
    lastmult = (limit - 1) // divisor
    return divisor * (1 + lastmult) * lastmult // 2
  return divsum(3) + divsum(5) - divsum(3 * 5)