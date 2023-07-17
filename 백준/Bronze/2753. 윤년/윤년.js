const fs = require("fs");
const inputData = fs.readFileSync('/dev/stdin').toString().trim()

if (inputData % 4 == 0 && (inputData % 100 != 0 || inputData % 400 == 0)) {
  console.log(1);
} else {
  console.log(0);
}
