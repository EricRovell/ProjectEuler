function squareDifference(limit) {
  let squareSum  = x => (1 + limit) * limit / 2;
  let sumSquares = x => (2 * x**3 + 3 * x**2 + x) / 6;
  return squareSum(limit) ** 2 - sumSquares(limit);
}

console.log(squareDifference(100));