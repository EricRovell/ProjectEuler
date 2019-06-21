# returns the number of factorial digits chains 
# with desired length that occurs under the given limit
def factorial_chains(limit, length = 60):
  # pre-calculated factorials for all digits
  factorial = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800)

  # generates digits: int of given number
  # yields in reverse order: 123 -> 3, 2, 1
  def digits(number):
    while number:
      yield number % 10
      number //= 10

  # returns the sum of digit factorials of the given number
  factsum = lambda number: sum(factorial[num] for num in digits(number))
  
  # every starting number will stuck in the loop:
  chains = {
    69:  5,
    78:  4,
    169: 3,
    540: 2,
    871: 2,
    872: 2
  }

  for number in range(2, limit):
    chain = [number]
    connector = factsum(number)
    while True:
      chain.append(connector)
      connector = factsum(connector)
      
      # use cached result: additional length + future length
      if connector in chains:
        chains[number] = chains[connector] + len(chain)
        break

      # defence from such cases like 1 and 2
      if chain[-1] == connector: break
  
  # count the desired lengths
  result = 0
  for chain_length in chains.values():
    if chain_length == length: result +=1
  
  return result


# tests
print(factorial_chains(1000000))