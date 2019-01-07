function primeSum(limit) {
  let total = 0;
  let isPrime

  let possiblePrime = 2;
  while (possiblePrime < limit) {

    isPrime = true;
    let boundary = Math.floor(Math.sqrt(possiblePrime) + 1);

    for (let divisor = 2; divisor < boundary; divisor++) {
      if (possiblePrime % divisor == 0) {
        isPrime = false;
        possiblePrime++;
        break;
      }
    }

    if (isPrime) {
      total += possiblePrime;
      possiblePrime++;
    }
  }

  return total;
}

// tests
console.log(primeSum(10))
console.log(primeSum(2000000))