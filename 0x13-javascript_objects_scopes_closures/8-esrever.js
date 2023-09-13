#!/usr/bin/node
let i = 0;
exports.esrever = function (list) {
  if (i < list.length) {
    const item = list[i++];
    exports.esrever(list);
    console.log(item);
  }
};
