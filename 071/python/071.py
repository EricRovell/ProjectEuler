""" def stern_brocot(length):
  seq, i = [1, 1], 0
  while len(seq) < length:
    seq += [sum(seq[i: i + 2]), seq[i + 1]]
    i += 1
  return seq

print(list(stern_brocot(20))) """

def lneighbour(fraction, denominator):
  