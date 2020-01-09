const PATH = "../data.txt";

const { readFileSync } = require("fs");

const largestProduct = ({ filePath, adjacentDigits }) => {
  const data = readFileSync(filePath, { encoding: "utf8" });
  const digits = data.split("").map(Number);
  
  let largestProduct = 0;
  for (let index = 0; index <= digits.length - adjacentDigits; index++) {
    const product = digits
      .slice(index, index + adjacentDigits)
      .reduce((acc, value) => acc * value);

    largestProduct = Math.max(
      product,
      largestProduct
    );
  }

  return largestProduct;
};


// assert -> 5832
console.log(largestProduct({
  filePath: PATH,
  adjacentDigits: 4,
}));

// assert -> 23514624000
console.log(largestProduct({
  filePath: PATH,
  adjacentDigits: 13,
}));