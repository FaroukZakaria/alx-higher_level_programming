#!/usr/bin/node
const req = require('request');
const url = process.argv[2];
const wedge = 'https://swapi-api.alx-tools.com/api/people/18/';

req(url, (error, response, body) => {
  if (error) {
    console.error(`${error.messaage}`);
    return;
  }
  const data = JSON.parse(body);
  let count = 0;
  for (const key of data.results) {
    count += key.characters.filter(char => char === wedge).length;
  }
  console.log(count);
});
