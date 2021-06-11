def rectangles(x, y):
  rects = 0
  for i in range(x):
    for j in range(y):
      rects += (x - i) * (y - j)
  return rects

def search(target):
  closest_area_rects = 0
  closest_area = 0
  
  for x in range(1, 2000):
    for y in range(1, 2000):
      rects = rectangles(x, y)
      if abs(closest_area_rects - target) > abs(rects - target):
        closest_area = x * y
        closest_area_rects = rects
      if rects > target: break
  
  return closest_area

print(search(2000000))
