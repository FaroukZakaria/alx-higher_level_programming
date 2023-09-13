#!/usr/bin/node

function factorial (n) {
  if (isNaN(n)) {
    return (1);
  }
  if (n <= 1) {
    return (1);
  } else {
    return (n * factorial (n - 1));
  }
}
const n = parseInt(process.argv[2]);
const result = factorial (n);
console.log(result);
