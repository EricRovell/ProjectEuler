# returns next lexicographic permutation of given iterable
def lexicographic_permutation(iterable):

  # non-increasing element search
  # search from the end
  index = len(iterable) - 1
  while index > 0 and iterable[index - 1] >= iterable[index]:
    index -= 1
    if index <= 0: return None
  pivot = index - 1

  # find successor to the pivot
  index = len(iterable) - 1
  while iterable[index] < iterable[pivot]:
    index -= 1
  
  # swap them
  iterable[pivot], iterable[index] = iterable[index], iterable[pivot]

  # reverse suffix
  iterable[pivot + 1 :] = iterable[len(iterable) - 1 : pivot : -1]

  return iterable


# test
counter = 1
iterable = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
while counter != 10e5:
  iterable = lexicographic_permutation(iterable)
  counter += 1
print(iterable)