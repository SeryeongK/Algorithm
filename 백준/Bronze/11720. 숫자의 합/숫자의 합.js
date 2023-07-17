const fs = require("fs");
let inputData = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const nums = inputData[1].split("");
let answer = 0;
nums.forEach((i) => {
  answer += Number(i);
});
console.log(answer);
