#!/usr/bin/node
const req = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

req(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const MovieCharacters = JSON.parse(body).characters;
  for (const character of MovieCharacters) {
    req(character, (error, response, body) => {
      if (error) {
        console.log(error);
      }
      const CharacterName = JSON.parse(body).name;
      console.log(CharacterName);
    });
  }
});
