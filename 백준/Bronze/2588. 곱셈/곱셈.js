const fs = require("fs");
const inputData = fs.readFileSync('/dev/stdin').toString().trim().split("\n");
const A = inputData[0];
const B = inputData[1];

console.log(Number(A) * Number(B[2]));
console.log(Number(A) * Number(B[1]));
console.log(Number(A) * Number(B[0]));
console.log(Number(A) * Number(B));
