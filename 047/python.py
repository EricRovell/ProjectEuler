# loading primes from the file, up to the 100 000
with open("_files/primes_list_10e5.txt") as data:
  primes_list = []
  for line in data.readlines():
    primes_list.append(int(line))

# returns the "n" numbers with "m" distinct factors
def factoring(number, primes):
  factors = {}

  for prime in primes:

    power = 1

    while number != 1:

      if number % prime == 0:

        if prime in factors:
          factors[prime] += power
          
        else: 
          factors[prime] = power
        
        number = number // prime

      else:
        break      

  return factors

# checks if two given dictionaties have different keys OR values if the keys are equal
def completely_different(dictionary_one, dictionary_another):
        
  for one_key in dictionary_one.keys():
    for another_key in dictionary_another.keys():
      if one_key == another_key:
        if dictionary_one[one_key] != dictionary_another[another_key]:
          return False  

  return True

# returns the "consecutive" number of integers that have "distinct" prime factors each
def distinct_primes(consecutive, distinct):
  
  start = 2
  
  while True:

    factors = {}

    numbers = [number for number in range(start, start + consecutive)]
    
    for number in numbers:
      factors[number] = factoring(number, primes_list)

    if all(len(factors[element]) == distinct for element in factors):

      for one_element in factors:
        for another_element in factors:
          if one_element != another_element:

            if completely_different(factors[one_element], factors[another_element]):
              return factors
  
    start += 1  

# tests
print(distinct_primes(2, 2))
print(distinct_primes(3, 3))
print(distinct_primes(4, 4))