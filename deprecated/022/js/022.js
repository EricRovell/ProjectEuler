const { readFileSync } = require("fs");

const path = "../022_data.txt";

const namesScores = path => {
  // getting alphabet score for a letter
  // charCodeAt: A - Z -> 65 - 90
  const charScore = char => char.charCodeAt() - 64;

  // read file
  // -> split a string by comma
  // -> get a copy of the sorted array
  // -> break every name into array of letters
  // -> find a score from every letter and get a sum
  // -> get a sum of multiplied name's score by it's index
  const score = readFileSync(path, "utf8")
    .split(",")
    .slice().sort()
    .map(name => Array.from(name))
    .map(word => word.reduce((a, b) => a + charScore(b), 0))
    .reduce((acc, score, index) => acc + (index + 1) * score, 0);
  
  return score; 
};

namesScores(path);