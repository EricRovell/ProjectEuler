var fs = require('fs');

let data = fs.readFileSync('013/data.txt', 'utf8');
data = data.toString().split('\n');

let sum = data.reduce((acc, string) => acc + parseInt(string, 10), 0);
sum = sum.toString().slice(0, 11).replace('.', '');
console.log(sum);