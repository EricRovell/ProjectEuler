const fs = require("fs");
const readline = require("readline");

const myInterface = readline.createInterface({
  input: fs.createReadStream("../013_data.txt")
});

let total = 0n;
myInterface.on("line", line => {
  total += BigInt(line);
  console.log(total);
});

