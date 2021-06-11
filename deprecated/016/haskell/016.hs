import Data.Char

digitsSum :: (Show a) => a -> Int
digitsSum num = sum $ map digitToInt $ show num

-- to get the result: digitsSum (2^1000)
