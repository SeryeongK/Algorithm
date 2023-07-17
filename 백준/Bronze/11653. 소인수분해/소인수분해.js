const fs = require("fs");
let inputData = Number(fs.readFileSync("/dev/stdin").toString().trim());

// 에라토스테네스의 체
function findPrimes(N) {
  let isPrime = new Array(N + 1).fill(true);
  isPrime[0] = false;
  isPrime[1] = false;

  for (let i = 2; i * i <= N; i++) {
    if (isPrime[i]) {
      for (let j = i * i; j <= N; j += i) {
        isPrime[j] = false;
      }
    }
  }

  let primes = [];
  for (let i = 2; i <= N; i++) {
    if (isPrime[i]) {
      primes.push(i);
    }
  }

  return primes;
}

let primes = findPrimes(inputData);
let output = [];

if (inputData > 1) {
  while (inputData > 1) {
    primes.forEach((i) => {
      if (inputData % i == 0) {
        output.push(i);
        inputData = inputData / i;
      }
    });
  }
}

// output.sort();
output.sort(function (a, b) {
  return a - b;
});

output.forEach((i) => {
  console.log(i);
});
