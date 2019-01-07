def sum_of_multiples(limit, *multiples):
  total = 0

  for number in range(1, limit):
    for multiple in multiples:  

      if number % multiple == 0:
        total += number
        break

  return total

# tests
print(sum_of_multiples(10, 3, 5))
print(sum_of_multiples(1000, 3, 5))