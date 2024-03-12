import express from "express";

const app = express();
const port = 3000;
const { Server } = require('socket.io');

app.get('/', (req, res) => {
    res.send('<h1>Hello world</h1>');
});

io.on('connection', (socket) => {
    console.log('a user connected');
  });

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});