// function for a pair of numbers
/* function gcd(a, b) {
  return (a < b) ? gcd(b, a)
       : (a % b == 0) ? b
       : gcd(b, a % b)
} */

function gcd(...numbers) {
  // returns the greatest common divisor
  // of given numbers
  return numbers.reduce((a, b) => {
    return (a < b) ? gcd(b, a)
         : (a % b == 0) ? b
         : gcd(b, a % b)
  });
}

function lcm(...numbers) {
  // returns the largest common multiple
  // of given numbers
  return numbers.reduce((a, b) => {
    return (a * b) / gcd(a, b);
  });
}


// tests
let numbers = [... Array(20).keys()].slice(1);  // [1, 2, ... 20]
console.log(lcm(...numbers));