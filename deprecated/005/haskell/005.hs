divisible :: Int -> Int
divisible limit = foldr1 lcm [1..limit]
