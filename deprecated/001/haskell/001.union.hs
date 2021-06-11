import Data.List (union)

solution :: Int -> Int
solution limit = sum $ union [3,6..limit] [5,10..limit]
