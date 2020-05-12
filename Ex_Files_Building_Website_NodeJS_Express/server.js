const path = require('path');
const express = require('express');
const cookieSession = require('cookie-session');
const routes = require('./routes');

const app = express();

const FeedbackService = require('./services/FeedbackService');
const SpeakerService = require('./services/SpeakerService');

const feedbackService = new FeedbackService('./data/feedback.json');
const speakerService = new SpeakerService('./data/speakers.json');

// Usually 8080 for web servers, 3000 for express servers
const port = 3000;

app.set('trust proxy', 1);

// Use cookie session
app.use(
  cookieSession({
    name: 'session',
    keys: ['happy', 'happier', 'happiest'],
  })
);

// Set EJS as the template engine
// (no need to require EJS as express will discover it)
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, './views'));

// Global middleware (used for every function call)
app.use(express.static(path.join(__dirname, './static')));
app.use(
  '/',
  routes({
    feedbackService,
    speakerService,
  })
);

app.listen(port, () => {
  console.log(`Express server listening on port ${port}`);
});
