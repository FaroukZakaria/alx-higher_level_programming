#!/usr/bin/node
exports.converter = function (base) {
  if (base === 0) {
  return (0);
  }

  let result = '';
  while (num > 0) {
    const remainder = number % base;
    result = remainder.toString() + result;
    number = Math.floor(number / base);
  }
  return (result);
}
