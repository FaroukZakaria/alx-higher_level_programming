#!/usr/bin/node

if (!process.argv[2]) {
  console.log('Missing number of occurrences');
}
const i = process.argv[2];

for (let j = 0; j < i; j++) {
  console.log('C is fun');
}
