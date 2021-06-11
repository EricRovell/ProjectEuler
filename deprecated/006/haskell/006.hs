sqDiff :: Int -> Int
sqDiff limit = sqSum - sumSq
  where
    sqSum = sum [1..limit] ^ 2
    sumSq = sum $ map (^2) [1..limit]
