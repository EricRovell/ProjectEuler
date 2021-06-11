"""
  This is an approximate solution to the problem.
  More details and explanation check in analysis folder.

  The idea is that space between the convergents index we are looking for
    has a pattern, however not completely regular: 8, 5, 8, 5, 8...
    The trend is 13 solutions per 13 expansions.

  This solution (for the problems boundary = 1000):
    - hits the target in 60.9%;
    - +1 value error in 34.8%;
    - -1 value error in 4.3%.
"""

def sq2convergents(bound):
  limit = 2 * (bound // 13)
  return limit if (bound % 13 < 8) else limit + 1

#print(sq2convergents(1000))
