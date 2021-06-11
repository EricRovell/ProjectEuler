// filesystem
const fs = require('fs');

fs.readFile("../013_data.txt", "utf8", (error, data) => {
  if (error) throw error;
  
  // fileData -> string -> split by newline
  const fileData = data
    .toString()
    .split("\n");
  // find a sum by converting every string to BigInt
  const total = fileData
    .reduce((acc, number) => acc + BigInt(number), 0n);
  // convert the sum to String and slice out first 10 characters
  const first10digits = total
    .toString()
    .slice(0, 10);
  
  // answer
  console.log(first10digits);
});
