// The optimized solution.
// The value of n / phi(n) is only dependent on the number of unique prime factors.
// So, to solve the problem, the inversed totient function should be minimized.
//   Inversed totient function has a (1 - 1 / p) in the denominator.
//   (1 / p) -> smaller the prime factors, more is subtracted from 1 in...
//   ... (1 - 1 / p) -> it will be minimal for a small prime factors,
// then we should be taking the product of the smalles primes to get the answer.

function* primes() {
  /**
   * ! Infinite prime numbers generator.
   */ 

  function* infinite(start = 3, step = 2) {
    /**
     * Infinite generator of integer numbers.
     * @param {int} start - the first value to generate.
     * @param {int} step - the step between generated integers.
     * @yields {int} - yields the integers indefinetly.
     */
    while (true) {
      yield start;
      start += step;
    }
  }

  function* range(start, stop, step) {
    /**
     * Generator of integer sequence, both ends are inclusive.
     * @param {int} start - the first value to generate.
     * @param {int} stop - the last value to generate, inclusive
     * @param {int} step - the step between generated integers.
     * @yields {int} - yields the integer.
     */
    let number = start;
    while (number <= stop) {
      yield number;
      number += step;
    }
  }

  yield 2;
  for (number of infinite()) {
    let isPrime = true;
    for (factor of range(3, Math.floor(number ** 0.5) + 1, 2)) {
      if (number % factor == 0) {
        isPrime = false;
        break;
      }
    }
    if (isPrime) {
      yield number;
    }
  }
}

function totientMaximum(limit) {
  let result = 1;
  let prime = primes();
  let nextPrime = prime.next().value;
  while (result * nextPrime <= limit) {
    result *= nextPrime;
    nextPrime = prime.next().value;
  }
  return result;
}

// results
console.log(totientMaximum(1000000));