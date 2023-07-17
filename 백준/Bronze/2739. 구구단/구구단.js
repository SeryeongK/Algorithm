const fs = require("fs");
const inputData = fs.readFileSync('/dev/stdin').toString().trim();

for (let i = 1; i < 10; i++) {
  console.log(`${inputData} * ${i} = ${inputData * i}`);
}
