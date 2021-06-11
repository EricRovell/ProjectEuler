function* primes({ limit }) {
  // infinite integers generator
  function* infiniteCounter({ start = 2, step = 1, limit }) {
    while (true) {
      yield start;
      start += step;
      if (limit !== undefined && start >= limit) break;
    }
  }
  // yield 2 as the only one even prime
  // this way it is easier to check only odd numbers
  yield 2;
  const naturalNumbers = infiniteCounter({ start: 3, step: 2, limit });
  for (let possiblePrime of naturalNumbers) {
    let boundary = Math.floor(possiblePrime ** 0.5 + 1);
    divCheck: {
      for (let divisor = 2; divisor < boundary; divisor++) {
        if (possiblePrime % divisor === 0) break divCheck; 
      }
      yield possiblePrime;
    }
  }

}

const primeSummations = target => {
  // this solution uses infinite primes generator because the limit is unknown
  // every necessary prime is generated and pushed to array after every unsuccesful loop
  let number = 2;
  primesIter = primes({});
  primesArr = [ primesIter.next().value ];
  while (true) {
    const ways = [ 1, ...Array(number).fill(0) ];
    for (let prime of primesArr) {
      for (let integer = prime; integer <= number; integer++) {
        ways[integer] += ways[integer - prime];
      }
    }
    if (ways[number] > target) {
      // arr index represents the checked number
      return ways.length - 1;
    }
    number++;
    primesArr.push(primesIter.next().value);
  } 
};

//console.log(primeSummations(5000));
