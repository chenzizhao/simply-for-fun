const express = require('express');
// This is a routing module
const router = express.Router();

module.exports = () => {
  // Routing middleware (actual)
  router.get('/', (request, response) => {
    // "return" keyword ends the request-response cycle
    return response.send('Feedback page');
  });
  router.post('/:shortname', (request, response) => {
    return response.send('Feedback form posted');
  });
  return router;
};
