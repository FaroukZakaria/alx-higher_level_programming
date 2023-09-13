#!/usr/bin/node
exports.esrever = function (list) {
  let i = list.length - 1;
  const tsil = [];
  while (i >= 0) {
    tsil.push(list[i]);
    i--;
  }
  return (tsil);
};
