// -> returns the difference between:
//   squared sum of natural numbers
//   sum of squares of naturals numbers
// argument <- the last natural number, [1, N]
const difference = x => x * (x**2 - 1) * (3 * x + 2) / 12

// console.log(difference(100))