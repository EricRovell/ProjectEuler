// sieve of Eratosthenes generator
function* sieve(limit) {
  // creating an array where index means actual number
  // 0 and 1 - are not primes
  // assuming that all others - are primes
  let numbers = [0, 0].concat(new Array(limit - 2).fill(1));
  
  for (let index = 2; index < numbers.length; index++)
  {
    let prime = index;
    if (numbers[index]) {      
      yield prime;
    }
    // we mark all multiples of the last prime number as non-prime
    for (let number = index ** 2; number < numbers.length; number += prime)
    {
      numbers[number] = 0;
    }
  }
}

// returns a sum of all primes below the given limit
function primeSum(limit) {
  let sum = 0;
  let primes = sieve(limit);
  for (prime of primes) {
    sum += prime;
  }
  return sum;
}

// tests
console.log(primeSum(2000000));