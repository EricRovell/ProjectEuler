def distinct_powers(a, b):
  distinct_terms = set()

  for a in range(a, b + 1):
    for b in range(a, b + 1):
      distinct_terms.add(a ** b)
      distinct_terms.add(b ** a)

  return len(distinct_terms)

# tests
print(distinct_powers(2, 5))
print(distinct_powers(2, 100))
