// returns the n-fibonacci number
// starts from 0, 1, 1, 2, 3, 5...
function fibonacci(index) {
  if (index == 0) {
    return 0;
  } else if (index == 1 || index == 2) {
    return 1;
  } else {
    return fibonacci(index - 1) + fibonacci(index - 2);
  }
}

// returns the array of the entire fibonacci sequence up till the limit number
function fibSequence(limit) {
  let fibList = new Array();
  let index = 0;
  
  while (true) {
    let number = fibonacci(index);
    if (number < limit) {
      fibList.push(number);
    } else {
      break;
    }
    index++;    
  }

  return fibList;
}

// returns the sum of all even-valued terms of the given array
function evenSum(array) {
  let sum = 0;
  for (let item = 0; item < array.length; item++) {
    if (array[item] % 2 == 0) {
      sum += array[item];
    }
  }
  return sum;
}

// tests
console.log(evenSum(fibSequence(4000000)));