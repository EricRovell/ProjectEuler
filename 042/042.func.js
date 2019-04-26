// data location
const _path = '042_data.txt';

function getData(path = _path) {
  // reading data and making it manageable
  const fs = require('fs');
  let data = fs.readFileSync(path, "utf-8");
  data = data.replace(/"/g, "").split(',');
  return data;
}

// triangle number check
const isTriangle = num => Number.isInteger((-0.5 + (0.25 + 2 * num) ** 0.5));
// alphabet order for letters
const order = char => char.charCodeAt() - 64;
// word score: split -> each letter to order -> sum of orders
const score = word => word.split('').map(order).reduce((a, b) => a + b);

function triangleWords(words = getData()) {
  // every word -> score -> is this a triangle number?
  // how many triangle number? -> length
  return words.map(score).filter(isTriangle).length;
}

// results
console.log(triangleWords());