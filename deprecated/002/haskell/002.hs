-- Project Euler #002
-- Returns sum of even fibonacci numbers under specified limit
evenFibSum :: Int -> Int
evenFibSum limit = sum [ x | x <- takeWhile (<= limit) fibs, even x]
  where
    fibs = 0 : 1 : zipWith (+) fibs (tail fibs)
