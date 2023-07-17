const fs = require("fs");
let inputData = fs.readFileSync("/dev/stdin").toString().trim();
let answer = 0;
if (inputData[0] == 0) {
  if (inputData[1] == "x") {
    // 16진수
    let number = inputData.slice(2, inputData.length).split("");
    for (let i = 0; i < number.length; i++) {
      num = 0;
      if (number[i] == "a") {
        num = 10;
      } else if (number[i] == "b") {
        num = 11;
      } else if (number[i] == "c") {
        num = 12;
      } else if (number[i] == "d") {
        num = 13;
      } else if (number[i] == "e") {
        num = 14;
      } else if (number[i] == "f") {
        num = 15;
      } else {
        num = Number(number[i]);
      }
      answer += num * 16 ** (number.length - (i + 1));
    }
    console.log(answer);
  } else {
    // 8진수
    let number = inputData.slice(1, inputData.length).split("").map(Number);
    for (let i = 0; i < number.length; i++) {
      answer += number[i] * 8 ** (number.length - (i + 1));
    }
    console.log(answer);
  }
} else {
  // 10진수
  console.log(inputData);
}
