const express = require('express');
const http = require('http');
const { Server } = require('socket.io');
const path = require('path');

const app = express();
const server = http.createServer(app);
const io = new Server(server);

const PORT = process.env.PORT || 3000;

app.use(express.static(path.join(__dirname)));

io.on('connection', (socket) => {
  console.log('socket connected:', socket.id);

  // Relay position/state updates to other clients
  socket.on('state:update', (data) => {
    socket.broadcast.emit('state:update', { id: socket.id, ...data });
  });

  // Relay shoot events
  socket.on('shoot', (data) => {
    socket.broadcast.emit('shoot', { id: socket.id, ...data });
  });

  socket.on('disconnect', () => {
    console.log('socket disconnected:', socket.id);
    socket.broadcast.emit('player:disconnect', { id: socket.id });
  });
});

server.listen(PORT, () => console.log(`Server running on http://localhost:${PORT}`));
