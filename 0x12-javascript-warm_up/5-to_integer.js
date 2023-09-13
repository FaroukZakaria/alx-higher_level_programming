#!/usr/bin/node

const arg = process.argv[2];

const value = parseInt(arg, 10);

if (!(isNaN(value)) && Number.isInteger(value)) {
  console.log(`My number: ${value}`);
} else {
  console.log('Not a number');
}
