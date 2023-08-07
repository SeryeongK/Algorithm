// 히든 넘버
const fs = require("fs");
let inputData = fs.readFileSync("/dev/stdin").toString().split("\n");
const N = Number(inputData[0]);
let word = inputData[1];
// 문자 구별
let number = "";
let numbers = [];
for (let i = 0; i <= N; i++) {
  if (isNaN(word[i])) {
    numbers.push(number);
    number = "";
  } else {
    number += word[i];
  }
}
// 합 구하기
answer = 0;
numbers.map((w) => {
  answer += Number(w);
});
console.log(answer);
