!/usr/bin/node

const fetch = require('node-fetch'); // Node.js environment, or you can use the browser's fetch

function getMovieCharacters(movieId) {
  const baseUrl = 'https://swapi-api.hbtn.io/api/films/';

  // Make a request to the SWAPI API to get information about the specified movie
  fetch(`${baseUrl}${movieId}/`)
    .then((response) => {
      if (!response.ok) {
        throw new Error(`Failed to fetch movie data for Movie ID ${movieId}`);
      }
      return response.json();
    })
    .then((filmData) => {
      const charactersUrls = filmData.characters;

      // Iterate through the character URLs and fetch character data
      charactersUrls.forEach((characterUrl) => {
        fetch(characterUrl)
          .then((response) => {
            if (!response.ok) {
              console.log(`Failed to fetch character data from ${characterUrl}`);
              return;
            }
            return response.json();
          })
          .then((characterData) => {
            const characterName = characterData.name;
            console.log(characterName);
          })
          .catch((error) => {
            console.error(error);
          });
      });
    })
    .catch((error) => {
      console.error(error);
    });
}

const movieId = process.argv[2]; // Get the Movie ID from the command line arguments
if (!movieId) {
  console.log('Usage: node star_wars_characters.js <Movie ID>');
} else {
  getMovieCharacters(movieId);
}
