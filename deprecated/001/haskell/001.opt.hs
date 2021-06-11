-- sum of all multiples for mult below given limit
multSum limit a b = sumStep a limit + sumStep b limit - sumStep (a * b) limit
  where
    sumStep s n = s * sumOnetoN (n `div` s)
    sumOnetoN n = n * (n + 1) `div` 2 