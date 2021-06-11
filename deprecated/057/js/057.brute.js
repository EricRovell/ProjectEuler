/*
  It is a brute force solution, still very fast.
  This solution uses BigInt primitive.

  Steps:

  1. Initialize generator function:
    1.1. The initial convergent is constructed with
    numerator, denominator and convergent's index.
    1.2. The "for" loop initialized to check all indexes up to the limit:
      - The convergent yilded from the generator function.
      - Next convergent is being constructed and overrides the previous one.
  2. Initialize a function for searching the solution.
    2.1. Initialize counter to zero.
    2.2. Using loop iterate over values from generator.
      - Destruct values from the generated object.
      - Compare number of digits.
      - If the numerator has more -> update the counter.
    2.3. Return the counter. It is the answer.  
*/

function* sq2rootConvergents({ limit }) {
  let convergent = {
    n: 3n,
    d: 2n,
    index: 1,
  };

  for (let index = 1; index <= limit; index++) {
    yield convergent;

    convergent = {
      ...convergent,
      n: convergent.n + 2n * convergent.d,
      d: convergent.n + convergent.d,
      index,
    }    
  }
}

const search = ({ limit }) => {
  let counter = 0;
  const convergents = sq2rootConvergents({ limit });

  for (let convergent of convergents) {
    const { n, d } = convergent;
    if (n.toString().length > d.toString().length) {
      counter++;
    }
  }

  return counter;
};


// assert: limit = 1000, answer: 153
// console.log(search({ limit: 1000 }));
