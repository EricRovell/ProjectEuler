// returns a boolean if the given integer is Lychrel number or not
// within given number of iterations
function isLychrel(number, iterations) {
  // returns a reversed integer
  function reverse(number) {
    number = number.toString().split("").reverse().join("");
    return parseInt(number, 10);
  }

  for (let iteration = 0; iteration < iterations; iteration++) {
    number += reverse(number);
    if (number == reverse(number)) {
      return false;
    } 
  }
  return true;
}

// returns a number of Lychrel sequence within an [a, b) interval
function lychrelSequence(a, b) {
  let numbers = 0;
  for (let number = a; number < b; number++) {
    if (isLychrel(number, 50)) {
      numbers++;
    }
  }
  return numbers;
}

// tests
console.log(lychrelSequence(1, 10000))