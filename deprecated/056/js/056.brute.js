// Brute force solution using BigInt primitives.
// Converting the number to string in order to find the digit sum
//  was faster than numeric method.

const digitSum = (number) => {
  /**
   * Returns the digits sum of the integer.
   * @param {int} number - to find the sum of digits for.
   * @returns {int} - the digits sum.
   */
  digits = number.toString().split('').map(Number);
  return digits.reduce((a, b) => a + b, 0);
}

const powerfulDigitSum = (limit) => {
  /**
   * Searches for the largest digit sum for numbers in the form of a ^ b.
   * @param {int} limit - the search interval, where a. b in [1, limit).
   * @returns {int} - the largest digits sum.
   */
  let largest = 0n;
  for (let a = 1n; a < limit; a++) {
    for (let b = 1n; b < limit; b++) {
      sum = digitSum(BigInt(a ** b));
      if (largest < sum) { largest = sum; }
    }
  }
  return largest;
}

// results
console.log(powerfulDigitSum(100));