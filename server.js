// Import required packages
const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');

// Create express app
const app = express();
const PORT = 5000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// In-memory "database"
let items = [];
let idCounter = 1;

// ➕ Route: GET /
app.get('/', (req, res) => {
  res.send('Backend server is running!');
});

// 📄 Route: GET all items
app.get('/items', (req, res) => {
  res.json(items);
});

// ➕ Route: POST new item
app.post('/items', (req, res) => {
  const newItem = { id: idCounter++, name: req.body.name };
  items.push(newItem);
  res.status(201).json(newItem);
});

// ✏️ Route: PUT (update item)
app.put('/items/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const item = items.find(i => i.id === id);
  if (item) {
    item.name = req.body.name;
    res.json(item);
  } else {
    res.status(404).json({ error: 'Item not found' });
  }
});

// ❌ Route: DELETE item
app.delete('/items/:id', (req, res) => {
  const id = parseInt(req.params.id);
  items = items.filter(i => i.id !== id);
  res.status(204).end();
});

// Start server
app.listen(PORT, () => {
  console.log(`✅ Server running at http://localhost:${PORT}`);
});
