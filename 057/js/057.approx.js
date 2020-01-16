/*
  This is an approximate solution to the problem.
  More details and explanation check in analysis folder.

  The idea is that space between the convergents index we are looking for
    has a pattern, however not completely regular: 8, 5, 8, 5, 8...
    The trend is 13 solutions per 13 expansions.

  This solution (for the problems boundary = 1000):
    - hits the target in 60.9%;
    - +1 value error in 34.8%;
    - -1 value error in 4.3%.
*/

const sq2Convergents = bound => {
  const limit = 2 * Math.floor(bound / 13);
  return (bound % 13 < 8)
    ? limit
    : limit + 1;
};

//console.log(sq2Convergents(1000));
