import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--limit", type=int, default=1000, help="Limit to find a sum of divisors")
parser.add_argument("--divs", nargs="+", type=int, default="3 5", help="Array of divisors")

args = parser.parse_args()

limit = args.limit
divs = args.divs

# The solution
def multsum(limit, *divs):
  assert len(divs) == 2
  # returns the sum of all divs in [1, limit)
  def divsum(divisor):
    lastmult = (limit - 1) // divisor
    return divisor * (1 + lastmult) * lastmult // 2

  return divsum(divs[0]) + divsum(divs[1]) - divsum(divs[0] * divs[1])

#run
print(multsum(limit, *divs))

# tests
#print(multsum(1000, 3, 5))