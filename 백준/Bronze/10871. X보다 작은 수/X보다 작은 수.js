const fs = require("fs");
const inputData = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [N, X] = inputData[0].split(" ").map(Number);
const nums = inputData[1].split(" ").map(Number);

const answers = nums.filter((num) => num < X);
console.log(answers.join(" "));
