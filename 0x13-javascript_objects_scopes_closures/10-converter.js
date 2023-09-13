#!/usr/bin/node
exports.converter = function (base) {
  return function (num) {
    if (base === 0) {
      return (0);
    }

    let result = '';
    while (num > 0) {
      const remainder = num % base;
      result = remainder.toString() + result;
      num = Math.floor(num / base);
    }
    return (result);
  };
};
