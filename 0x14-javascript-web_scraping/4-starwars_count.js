#!/usr/bin/node
const req = require('request');
const url = process.argv[2];
const wedge = '/people/18/';

req(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const count = (body.split(wedge).length - 1);
  console.log(count);
});
