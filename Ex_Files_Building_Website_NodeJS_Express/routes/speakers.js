const express = require('express');
// This is a routing module
const router = express.Router();

module.exports = () => {
  // Routing middleware (actual)
  router.get('/', (request, response) => {
    return response.send('Speakers list');
  });
  router.get('/:shortname', (request, response) => {
    return response.send(`Detailed page of ${request.params.shortname}`));
  });
  return router;
};
