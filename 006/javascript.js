function sqSumDifference(numbers) {
  let [sumSq, sqSum] = [0, 0];
  for (let number = 1; number <= numbers; number++)
  {
    sumSq += number ** 2;
    sqSum += number;
  }
  return sqSum ** 2 - sumSq;
}

// tests
console.log(sqSumDifference(10));
console.log(sqSumDifference(100));