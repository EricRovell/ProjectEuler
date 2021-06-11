fibs :: [Integer]
fibs = 0 : 1 : (zipWith (+) fibs $ tail fibs)

fibDigits :: Int -> Int
fibDigits d = length $ takeWhile ( < digits ) fibs
  where digits = 10 ^ (d - 1)