-- returns a sum of all mutiples of 3 and 5 under a given limit [1, limit]
sumMult3and5 :: Int -> Int
sumMult3and5 limit = sum [num | num <- [1 .. limit], mod num 3 == 0 || mod num 5 == 0] 