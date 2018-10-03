/*
Problem #001: Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
*/

// returns the sum of all multiples of the given numbers from the given interval
function multiplesSum(left, right, multiples) {

  if (left == undefined & right == undefined) {return "No limits are given."}
  if (arguments.length < 3) {return "No multiples are given"}

  let sum = 0;
  
  for (let number = left; number < right; number++) {
    for (let i = 2; i < arguments.length; i++) {
      if (number % arguments[i] == 0) {
        sum += number;
        break;
      }
    }    
  }

  return sum;
}

// tests
console.log(multiplesSum(1, 10, 3, 5));
console.log(multiplesSum(1, 1000, 3, 5));