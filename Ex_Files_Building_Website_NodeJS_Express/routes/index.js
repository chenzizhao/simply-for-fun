const express = require('express');
// This is a routing module
const router = express.Router();
// Use Express "router" object instead of "app" object

const speakersRoute = require('./speakers');
const feedbackRoute = require('./feedback');

module.exports = () => {
  // Routing middleware (actual)
  router.get('/', (request, response) => {
    response.render('pages/index', { pageTitle: 'Welcome' });
  });
  router.use('/speakers', speakersRoute());
  router.use('/feedback', feedbackRoute());
  return router;
};
