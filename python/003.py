'''
Problem #3: Largest prime factor
 
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

# returns the primes list witin given interval
def primesList(n, m):

  if not isinstance(n, int) or not isinstance(m, int) or n < 0 or m < 0:
    return "Argument should be a positive integer"

  if n > m:
    n, m = m, n
    print("I think you gave the interval in reverse order, I fixed it!")

  primes = []

  for possiblePrime in range(n, m + 1):

    isPrime = True

    for number in range(2, int(possiblePrime ** 0.5 + 1)):
      if possiblePrime % number == 0:
        isPrime = False
        break

    if isPrime:
      primes.append(possiblePrime)

  return primes

print(primesList(20, 30))

    



