const fs = require("fs");
const inputData = fs.readFileSync('/dev/stdin').toString().trim().split(" ").map(Number);

const [x, y, w, h] = inputData;

const answer = Math.min(x, y, w - x, h - y);
console.log(answer);
