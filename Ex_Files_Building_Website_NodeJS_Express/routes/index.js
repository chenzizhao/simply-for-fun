const express = require('express');
// This is a routing module
const router = express.Router();
// Use Express "router" object instead of "app" object

module.exports = () => {
  // Routing middleware
  router.get('/', (request, response) => {
    response.render('pages/index', { pageTitle: 'Welcome' });
  });
  return router;
};
