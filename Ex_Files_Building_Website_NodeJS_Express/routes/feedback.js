const express = require('express');
// This is a routing module
const router = express.Router();

module.exports = (params) => {
  // Routing middleware (actual)
  const { feedbackService } = params;

  router.get('/', async (request, response) => {
    // "return" keyword ends the request-response cycle
    const feedback = await feedbackService.getList();
    return response.json(feedback);
  });

  router.post('/', (request, response) => {
    return response.send('Feedback form posted');
  });

  return router;
};
