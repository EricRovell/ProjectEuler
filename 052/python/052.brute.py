def is_permuted_multiples(generation):

  number = 1
  while True:

    # the largest multiple must have the same number of digits
    if len(str(number)) != len(str(number * generation)):
      number += 1
      continue

    # genereting a sorted list of digits for all multiples
    # generation -> how many multiples
    digits = [ sorted(list(str(number * multiple))) for multiple in range(1, generation + 1)]
    
    # comparing initial number as sorted list of digits
    # to the list of digits of multiples
    initial = sorted(list(str(number)))
    if all(initial == multiple for multiple in digits):
      return number
    else:
      number += 1
      continue

# we can't use sets!
# if we do -> we will get 10255 as answer
# 10 255 * 2 = 20 510  => set(0, 1, 2, 5), two zeros makes answer incorrect

# tests
print(is_permuted_multiples(2))
print(is_permuted_multiples(6))