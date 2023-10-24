#!/usr/bin/node
const req = require('request');
const url = process.argv[2];

req(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const jsonbody = JSON.parse(body);
  const result = {};
  for (const task of jsonbody) {
    if (task.completed === true) {
      if (result[task.userId] === undefined) {
        result[task.userId] = 0;
      }
      result[task.userId] += 1;
    }
  }
  console.log(result);
});
