solution = do
  xs <- fmap (map read . lines) (readFile "../013_data.txt")
  print . take 10 . show . sum $ xs