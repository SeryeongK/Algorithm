const fs = require("fs");
const inputData = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

for (let i = 1; i <= Number(inputData[0]); i++) {
  const [A, B] = inputData[i].trim().split(" ").map(Number);
  console.log(A + B);
}
