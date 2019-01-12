function champernowneDigit(index) {
  // returns the desired digit of the Champernowne's constant
  // 0.123456789101112131415...
  // int : int

  if (index > 0 && index <= 9) { return index; }

  // returns the number of digits of k-term
  let digits = (term) => 9 * term * 10 ** (term - 1)

  // getting the:
  // 1. term where index resides
  // 2. position of the digit in this term (updated index value)
  // 3. index is decremented by 1 -> because terms begin from 0 values
  //    example: 10, 11, 12... or 100, 101, 102... etc.
  let term = 1;
  while (index > digits(term))
  {
    index -= digits(term);
    term++;
  }
  index--;

  // number where index resides:
  // number = x + y
  // x = 'starting number from previous term' : 10 ** (term - 1)
  // y = index / (digits of this term)        : Math.ceil(index / term)
  // shift (remainder) means the digit in location number [0, 1, 2...]
  let number = 10 ** (term - 1) + Math.ceil(index / term)
  let shift = index % term;

  let digit = number.toString()[shift];

  return parseInt(digit, 10);
}

// solving the problem
function search() {
  let answer = 1;
  for (let digit = 1; digit <= 1000000; digit *= 10) {
    answer *= champernowneDigit(digit);
  }
  return answer;
}

// tests
console.log(search());