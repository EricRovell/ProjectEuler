// returns the largest prime factor of the given number
function greatestPrimeFactor(number) {
  // the greatest prime factor is less or equal than sqrt(number)
  let searchLimit = Math.floor(number ** 0.5 + 1);

  // 2 - is the only even prime
  // factorizing it out will allow us to increase
  // factor by 2 each time after
  while (number % 2 == 0) {
    number /= 2;
  }

  let factor = 3;
  let greatestFactor = 3;
  while (number > 1 && factor < searchLimit) {
    while (number % factor == 0) {
      number /= factor;
    }
    greatestFactor = factor;
    factor += 2;
  }
  return greatestFactor;
}

// tests
console.log(greatestPrimeFactor(13195));
console.log(greatestPrimeFactor(600851475143));