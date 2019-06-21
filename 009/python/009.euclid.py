def gcd(a, b):
  if a < b: return gcd(b, a)
  while b:
    a, b = b, a % b
  return a


def triplet(perimeter):
  a, b, c = 0, 0, 0
  m, k, n, d = 0, 0, 0, 0
  isfound = False
  
  mlimit = int(perimeter ** 0.5)
  for m in range(2, mlimit):
    if perimeter / 2 % m == 0:
      if m % 2 == 0:
        k = m + 1
      else:
        k = m + 2
      while k < 2 * m and k <= perimeter / (2 * m):
        if perimeter / (2 * m) % k == 0 and gcd(k, m) == 1:
          d = perimeter / 2 / (k * m)
          n = k - m
          a = d * (m ** 2 - n ** 2)
          b = 2 * d * n * m
          c = d * (m ** 2 + n ** 2)
          isfound = True
          break
        k += 2
    if isfound: break

  return tuple(map(int, (a, b, c)))

print(triplet(1000))