const path = require('path');
const express = require('express');

const app = express();

// Usually 8080 for web servers, 3000 for express servers
const port = 3000;

// Middle ware
app.use(express.static(path.join(__dirname, './static')));

// Get route, send html files
app.get('/', (request, response)=>{
    response.sendFile(path.join(__dirname, './static/index.html'));
});

app.get('/speakers', (request, response)=>{
    response.sendFile(path.join(__dirname, './static/speakers.html'));
});

app.listen(port, ()=>{
    console.log(`Express server listening on port ${port}`);
});