import Data.Char

factorialDigitsSum :: Integer -> Int
factorialDigitsSum n = sum $ map digitToInt $ show $ product [1..n]

-- solution: factorialDigitsSum 100
