const express = require('express');
// This is a routing module
const router = express.Router();
// Use Express "router" object instead of "app" object

const speakersRoute = require('./speakers');
const feedbackRoute = require('./feedback');

module.exports = (params) => {
  // Routing middleware (actual)
  router.get('/', (request, response) => {
    response.render('pages/index', { pageTitle: 'Welcome' });
  });
  router.use('/speakers', speakersRoute(params));
  router.use('/feedback', feedbackRoute(params));
  return router;
};
