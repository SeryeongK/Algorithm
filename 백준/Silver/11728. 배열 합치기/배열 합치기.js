// 배열 합치기
const fs = require("fs");
let inputData = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
let one = inputData[1].split(" ").map((n) => {
  return Number(n);
});
let two = inputData[2].split(" ").map((n) => {
  return Number(n);
});
let answer = one.concat(two);
answer = answer.sort((a, b) => {return a - b});
console.log(answer.join(" "));