const fs = require("fs");
let inputData = fs.readFileSync("/dev/stdin").toString().trim();
let answer = 0;

if (inputData[0] === "0") {
  if (inputData[1] === "x") {
    // 16진수
    console.log(parseInt(inputData, 16));
  } else {
    // 8진수
    console.log(parseInt(inputData, 8));
  }
} else {
  // 10진수
  console.log(inputData);
}
