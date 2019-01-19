// this solution has flaw: problems if the number has zeros inside the number

// returns the least integer value that has permutated multiples
// times -> how many [2, times]
// 5 -> [number * 2, number * 3, number * 4, number * 5]
function permutedMultiples(times) {
  let number = 1;
  // checks if two given sets are equal
  let isSetsEqual = (a, b) => a.size === b.size && [...a].every(value => b.has(value));

  while (true)
  {
    let numbers = Array.from(Array(times - 1).keys(), (i) => number * (i + 2));
    let initialNumber = new Set(number.toString());
    numbers = new Set(numbers.join(''));
    if (isSetsEqual(initialNumber, numbers)) {
      return number;
    }
    number++;
  }  
}

// tests
console.log(permutedMultiples(6));