// returns the largest collatz sequence of all integers less than given limit
function collatzMaxLength(limit) {
  // we will step into the same numbers over and over
  let cached = {1: 1};
  // returns the next collatz number of given argument
  let collatz = (num) => (num % 2 == 0) ? (num / 2) : (3 * num + 1);
  
  for (let integer = 2; integer < limit; integer++)
  {
    // storing integer because we need to modify it
    let [number, length] = [integer, 1];
    while (number > 1)
    {
      number = collatz(number);
      if (number in cached) {
        length += cached[number];
        break;
      } else {
        length++;
      } 
    }
    cached[integer] = length;
  }
  
  // the largest key value in cached object
  return Object.keys(cached).reduce((a, b) => cached[a] > cached[b] ? a : b);
}

// tests
console.log(collatzMaxLength(1000000))