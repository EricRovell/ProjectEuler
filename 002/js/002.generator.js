// endless fibonacci number generator
function* fibonacci() {
  [a, b] = [0, 1]
  while (true)
  {
    yield a;
    [a, b] = [b, a + b];
  }
}

// returns sum of even fibonacci number under the given limit
function fibEvenSum(limit) {
  let sum = 0;
  let number = fibonacci();
  let fib = number.next().value;
  while (fib < limit)
  {
    sum += (fib % 2 == 0) ? fib : 0;
    fib = number.next().value; 
  }
  return sum;
}

// tests
console.log(fibEvenSum(4000000))