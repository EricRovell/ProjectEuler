const powerDigitSum = (base, power) => {
  // calculates a digits sum of the number: base^number
  
  // digits generator
  function* digits(number) {
    while (number) {
      yield number % 10n;
      number = number / 10n;
    }
  }
  
  // init generator
  const numDigits = digits(
    BigInt(base ** power)
  );

  let sum = 0n;
  for (let digit of numDigits) {
    sum += digit;
  }
  
  return sum;
};


// asserts
powerDigitSum(2, 15);    // -> 26
powerDigitSum(2, 1000);  // -> 1366
