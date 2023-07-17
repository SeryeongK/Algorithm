const fs = require("fs");
const inputData = fs.readFileSync("/dev/stdin").toString().trim()

for (let i = 1; i <= inputData; i++) {
  console.log("*".repeat(i));
}
