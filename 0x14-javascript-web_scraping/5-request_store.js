#!/usr/bin/node
const req = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];

req(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const content = body;
  fs.writeFile(file, content, error => {
    if (error) {
      console.log(error);
    }
  });
});
