const express = require('express');
// This is a routing module
const router = express.Router();

module.exports = (params) => {
  // Routing middleware (actual)
  const { speakerService } = params;

  router.get('/', async (request, response) => {
    const speakers = await speakerService.getList();
    return response.json(speakers);
  });

  router.get('/:shortname', (request, response) => {
    return response.send(`Detailed page of ${request.params.shortname}`);
  });

  return router;
};
