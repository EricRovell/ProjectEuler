// brute force solution
// palindrome check via string reverse

function largestPalindromeProduct(a, b) {
  /**
   * Searches for the largest palindrome product from two integers.
   * @param {int} a - the number of digits in the first number.
   * @param {int} b - the number of digits in the second number.
   * @returns {int} - the largest found palindrome product.
   */
  let largest = 0;
  for (let num1 = 10 ** (a - 1); num1 < 10 ** a; num1++) {
    for (let num2 = 10 ** (b - 1); num2 < 10 ** b; num2++) {
      let product = num1 * num2;
      if (product == product.toString().split("").reverse().join("")) {
        largest = Math.max(largest, product);
      }
    }
  }
  return largest;
}

// results
console.log(largestPalindromeProduct(2, 2));
console.log(largestPalindromeProduct(3, 3));