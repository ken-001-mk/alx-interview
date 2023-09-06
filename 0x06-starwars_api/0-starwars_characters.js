const request = require('request');

// Function to fetch characters from the Star Wars API for a specific movie
function getCharacters(movieId) {
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
  
  request(apiUrl, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const filmData = JSON.parse(body);
      const characters = filmData.characters;

      console.log(`Characters in ${filmData.title}:`);
      
      // Function to print characters one by one
      function printCharacters(index) {
        if (index < characters.length) {
          request(characters[index], (error, response, characterData) => {
            if (!error && response.statusCode === 200) {
              const character = JSON.parse(characterData);
              console.log(character.name);
              printCharacters(index + 1);
            } else {
              console.error(`Error fetching character data: ${error}`);
            }
          });
        }
      }

      printCharacters(0);
    } else {
      console.error(`Error fetching movie data: ${error}`);
    }
  });
}

// Usage: Pass the Movie ID as a command-line argument (e.g., 3 for "Return of the Jedi")
const movieId = process.argv[2];

if (!movieId) {
  console.error("Please provide a valid Movie ID as a command-line argument.");
} else {
  getCharacters(movieId);
}
