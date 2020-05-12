const express = require("express");

const app = express();

// Usually 8080 for web servers, 3000 for express servers
const port = 3000;

// Get route
app.get('/', (request, response)=>{
    response.send('Hello Express');
});

app.listen(port, ()=>{
    console.log(`Express server listening on port ${port}`);
});