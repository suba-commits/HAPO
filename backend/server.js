const express = require('express');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3001;

// Middleware
app.use(cors());
app.use(express.json());

// In-memory data store for habits
let habits = [
  {
    id: 1,
    name: 'Morning Exercise',
    description: 'Exercise for 30 minutes every morning',
    frequency: 'daily',
    completed: false,
    createdAt: new Date().toISOString()
  },
  {
    id: 2,
    name: 'Read Books',
    description: 'Read for at least 20 minutes',
    frequency: 'daily',
    completed: false,
    createdAt: new Date().toISOString()
  }
];

let nextId = 3;

// Routes

// Get all habits
app.get('/api/habits', (req, res) => {
  res.json(habits);
});

// Get a single habit
app.get('/api/habits/:id', (req, res) => {
  const habit = habits.find(h => h.id === parseInt(req.params.id));
  if (!habit) {
    return res.status(404).json({ error: 'Habit not found' });
  }
  res.json(habit);
});

// Create a new habit
app.post('/api/habits', (req, res) => {
  const { name, description, frequency } = req.body;
  
  if (!name) {
    return res.status(400).json({ error: 'Name is required' });
  }
  
  const newHabit = {
    id: nextId++,
    name,
    description: description || '',
    frequency: frequency || 'daily',
    completed: false,
    createdAt: new Date().toISOString()
  };
  
  habits.push(newHabit);
  res.status(201).json(newHabit);
});

// Update a habit
app.put('/api/habits/:id', (req, res) => {
  const habitIndex = habits.findIndex(h => h.id === parseInt(req.params.id));
  
  if (habitIndex === -1) {
    return res.status(404).json({ error: 'Habit not found' });
  }
  
  const { name, description, frequency, completed } = req.body;
  
  habits[habitIndex] = {
    ...habits[habitIndex],
    name: name !== undefined ? name : habits[habitIndex].name,
    description: description !== undefined ? description : habits[habitIndex].description,
    frequency: frequency !== undefined ? frequency : habits[habitIndex].frequency,
    completed: completed !== undefined ? completed : habits[habitIndex].completed
  };
  
  res.json(habits[habitIndex]);
});

// Delete a habit
app.delete('/api/habits/:id', (req, res) => {
  const habitIndex = habits.findIndex(h => h.id === parseInt(req.params.id));
  
  if (habitIndex === -1) {
    return res.status(404).json({ error: 'Habit not found' });
  }
  
  habits.splice(habitIndex, 1);
  res.status(204).send();
});

// Toggle habit completion
app.patch('/api/habits/:id/toggle', (req, res) => {
  const habit = habits.find(h => h.id === parseInt(req.params.id));
  
  if (!habit) {
    return res.status(404).json({ error: 'Habit not found' });
  }
  
  habit.completed = !habit.completed;
  res.json(habit);
});

// Health check
app.get('/health', (req, res) => {
  res.json({ status: 'ok', message: 'HAPO API is running' });
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
