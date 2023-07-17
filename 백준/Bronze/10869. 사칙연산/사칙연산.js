const fs = require("fs");
const inputData = fs.readFileSync('/dev/stdin').toString().trim().split(" ");
const A = Number(inputData[0]);
const B = Number(inputData[1]);

console.log(A + B);
console.log(A - B);
console.log(A * B);
console.log(parseInt(A / B));
console.log(A % B);
