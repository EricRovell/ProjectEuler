// endless primes generator
function* primes() {
  yield 2;
  let possiblePrime = 3;
  while (true)
  {
    let isPrime = true;
    let searchLimit = Math.floor(Math.sqrt(possiblePrime) + 1);
    for (divisor = 2; divisor < searchLimit; divisor++)
    {
      if (possiblePrime % divisor == 0) {
        isPrime = false;
        break;
      } 
    }
    if (isPrime) {
      yield possiblePrime;
    }
    possiblePrime += 2;  
  }
}

// returns a sum of all primes within a limit
function primeSum(limit) {
  let sum = 0;
  let prime = primes();
  let number = prime.next().value;
  while (number < limit)
  {
    sum += number;
    number = prime.next().value;
  }
  return sum;
}

// tests
console.log(primeSum(10));
console.log(primeSum(2000000));