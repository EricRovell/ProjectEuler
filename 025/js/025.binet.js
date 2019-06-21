// returns the 1st fibonacci number that contain desired number of digits
// using the Binet formula approximation
function fibonacciDigits(digits) {
  let phi = (1 + 5 ** 0.5) / 2;
  return Math.ceil( ((digits - 1) + 0.5 * Math.log10(5)) / Math.log10(phi) );
}

// tests
console.log(fibonacciDigits(3));
console.log(fibonacciDigits(1000));