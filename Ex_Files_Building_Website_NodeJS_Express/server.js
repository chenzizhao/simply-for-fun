const path = require('path');
const express = require('express');

const app = express();

// Usually 8080 for web servers, 3000 for express servers
const port = 3000;

// Set EJS as the template engine
// (no need to require EJS as express will discover it)
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, './views'));

// Global middleware (used for every function call)
app.use(express.static(path.join(__dirname, './static')));

// Routing middleware
app.get('/', (request, response) => {
  response.sendFile(path.join(__dirname, './static/index.html'));
  response.render('pages/index', { pageTitle: 'Welcome' });
});

app.get('/speakers', (request, response) => {
  response.sendFile(path.join(__dirname, './static/speakers.html'));
});

app.listen(port, () => {
  console.log(`Express server listening on port ${port}`);
});
