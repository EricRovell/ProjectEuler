def search(target):
  closest_area = 0
  error = target
  x, y = 2000, 1
  while x >= y:
    rects = x * (x + 1) * y * (y + 1) / 4
    if error > abs(rects - target):
      closest_area = x * y
      error = abs(rects - target)
    if rects > target:
      x -= 1
    else:
      y += 1

  return closest_area

print(search(2000000))