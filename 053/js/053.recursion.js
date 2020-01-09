// This solution uses recursive factorial function with memoization

const inMemory = func => {
  // memoization decorator
  const history = {
    0: 1,
    1: 1,
  };

  return (...args) => {
    const number = args[0];

    if (number in history) return history[number];
    const result = func(number);
    history[number] = result;

    return result;
  }  
};

const factorial = inMemory(
  // factorial recursive function
  // wrapped in memoization decorator
  number => {
    if (number === 0) return 1;
    return number * factorial(number - 1);
  }
);

const combinations = (n, r) => {
  return factorial(n) / factorial(r) / factorial(n - r);
};

const overLimit = ({ a, b, limit }) => {
  // calculates how many values of (r n) of combinations
  // are greater than limit in [a, b]
  let counter = 0;

  for (let n = a; n <= b; n++) {
    for (let r = a; r <= n; r++) {
      if (combinations(n, r) > limit) counter++;
    }
  }

  return counter;
};


// assert -> 4075
console.log(overLimit({
  a: 1,
  b: 100,
  limit: 1000000,
}));