-- sum of all multiples for mult below given limit
sumMult :: Integer -> Integer -> Integer
sumMult limit mult =
  let lastMult = div (limit - 1) mult
  in  div (mult * (1 + lastMult) * lastMult) 2

-- sum of 2 multiples combined
sumMults :: Integer -> Integer -> Integer -> Integer
sumMults limit mult1 mult2 =
  let sum1 = sumMult limit mult1
      sum2 = sumMult limit mult2
      both = sumMult limit (mult1 * mult2)
  in  sum1 + sum2 - both