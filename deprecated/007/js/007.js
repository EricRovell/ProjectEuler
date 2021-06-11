/* 
Problem #007: 10001st prime

By listing the first six prime numbers:
2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
*/

function prime(index) {
  let primes = [];

  let possiblePrime = 2;
  while (primes.length < index) {

    let isPrime = true;
    let boundary = Math.floor(Math.sqrt(possiblePrime) + 1);

    for (let divisor = 2; divisor < boundary; divisor++) {

      if (possiblePrime % divisor == 0) {
        isPrime = false;
        possiblePrime++;
        break;
      }
    }

    if (isPrime) {
      primes.push(possiblePrime);
      possiblePrime++
    }
  }

  return primes[primes.length - 1]
}

// tests
console.log(prime(6))
console.log(prime(10001))