const fs = require("fs");
const readline = require("readline");

const rl = readline.createInterface({
  input: fs.createReadStream('/dev/stdin'),
  output: process.stdout,
  terminal: false,
});

let lineCount = 0;

rl.on("line", function (line) {
  if (lineCount === 0) {
    lineCount = Number(line);
  } else {
    const numbers = line.trim().split(" ").map(Number);
    console.log(numbers[0] + numbers[1]);
    lineCount--;
    if (lineCount === 0) {
      rl.close();
    }
  }
});
