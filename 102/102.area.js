// import fs from 'fs';
const fs = require('fs');

// reading the data 
const data = fs.readFileSync("102_data.txt", "utf-8")
  .split(/\n|,/) // -> split by \n and comma
  .map(Number);  // -> convert to Integers

// remove the last odd element, the file has empty \n in the end
if (!data[data.length - 1]) { data.pop() };

function area(x1, y1, x2, y2, x3, y3) {
  /**
   * Calculates the area of a triangle by it's coordinates.
   * @param {Number} - x1, y1, x2, y2, x3, y3 -> cartesian coordinates.
   * @returns {Number} - the area value.
   */
  return 0.5 * Math.abs(
    x1 * (y2 - y3) +
    x2 * (y3 - y1) +
    x3 * (y1 - y2)
  )
}

function originContainment(x1, y1, x2, y2, x3, y3) {
  /**
   * Evaluates if the given triangle contains the origin.
   * @param {Number} - x1, y1, x2, y2, x3, y3 -> cartesioan coordinates.
   * @returns {Bool}
   */
  let full  = area(x1, y1, x2, y2, x3, y3);
  let part1 = area(x1, y1, x2, y2, 0, 0);
  let part2 = area(x1, y1, 0, 0, x3, y3);
  let part3 = area(0, 0, x2, y2, x3, y3);
  return (full == part1 + part2 + part3);
}

// reading cartesioan coordinates from a data
// and counting how many triangles contain the origin
function countingTriangles(triangles = data) {
  let contains = 0;
  for (let i = 0; i < triangles.length; i += 6)
  {
    let coordinates = triangles.slice(i, i + 6);
    if (originContainment(...coordinates)) {
      contains++;
    }
  }
  return contains;
}

// results
console.log(countingTriangles())