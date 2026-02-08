import { useState, useEffect } from 'react'
import './App.css'

const API_URL = 'http://localhost:3001/api';

function App() {
  const [habits, setHabits] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [newHabit, setNewHabit] = useState({
    name: '',
    description: '',
    frequency: 'daily'
  });
  const [showForm, setShowForm] = useState(false);

  // Fetch habits from API
  useEffect(() => {
    fetchHabits();
  }, []);

  const fetchHabits = async () => {
    try {
      setLoading(true);
      const response = await fetch(`${API_URL}/habits`);
      if (!response.ok) {
        throw new Error('Failed to fetch habits');
      }
      const data = await response.json();
      setHabits(data);
      setError(null);
    } catch (err) {
      setError('Unable to connect to backend. Make sure the server is running on port 3001.');
      console.error('Error fetching habits:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleAddHabit = async (e) => {
    e.preventDefault();
    if (!newHabit.name.trim()) return;

    try {
      const response = await fetch(`${API_URL}/habits`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(newHabit),
      });

      if (!response.ok) {
        throw new Error('Failed to add habit');
      }

      const addedHabit = await response.json();
      setHabits([...habits, addedHabit]);
      setNewHabit({ name: '', description: '', frequency: 'daily' });
      setShowForm(false);
    } catch (err) {
      setError('Failed to add habit');
      console.error('Error adding habit:', err);
    }
  };

  const handleToggleComplete = async (id) => {
    try {
      const response = await fetch(`${API_URL}/habits/${id}/toggle`, {
        method: 'PATCH',
      });

      if (!response.ok) {
        throw new Error('Failed to toggle habit');
      }

      const updatedHabit = await response.json();
      setHabits(habits.map(h => h.id === id ? updatedHabit : h));
    } catch (err) {
      setError('Failed to update habit');
      console.error('Error toggling habit:', err);
    }
  };

  const handleDeleteHabit = async (id) => {
    if (!window.confirm('Are you sure you want to delete this habit?')) {
      return;
    }

    try {
      const response = await fetch(`${API_URL}/habits/${id}`, {
        method: 'DELETE',
      });

      if (!response.ok) {
        throw new Error('Failed to delete habit');
      }

      setHabits(habits.filter(h => h.id !== id));
    } catch (err) {
      setError('Failed to delete habit');
      console.error('Error deleting habit:', err);
    }
  };

  if (loading) {
    return <div className="loading">Loading habits...</div>;
  }

  return (
    <div className="app">
      <header className="app-header">
        <h1>🎯 HAPO</h1>
        <p className="subtitle">Habit Tracker & Performance Enhancer</p>
      </header>

      {error && (
        <div className="error-message">
          {error}
        </div>
      )}

      <main className="main-content">
        <div className="habits-header">
          <h2>Your Habits</h2>
          <button 
            className="btn btn-primary" 
            onClick={() => setShowForm(!showForm)}
          >
            {showForm ? 'Cancel' : '+ Add Habit'}
          </button>
        </div>

        {showForm && (
          <form className="habit-form" onSubmit={handleAddHabit}>
            <div className="form-group">
              <label htmlFor="name">Habit Name *</label>
              <input
                type="text"
                id="name"
                value={newHabit.name}
                onChange={(e) => setNewHabit({ ...newHabit, name: e.target.value })}
                placeholder="e.g., Morning Exercise"
                required
              />
            </div>
            <div className="form-group">
              <label htmlFor="description">Description</label>
              <input
                type="text"
                id="description"
                value={newHabit.description}
                onChange={(e) => setNewHabit({ ...newHabit, description: e.target.value })}
                placeholder="Optional description"
              />
            </div>
            <div className="form-group">
              <label htmlFor="frequency">Frequency</label>
              <select
                id="frequency"
                value={newHabit.frequency}
                onChange={(e) => setNewHabit({ ...newHabit, frequency: e.target.value })}
              >
                <option value="daily">Daily</option>
                <option value="weekly">Weekly</option>
                <option value="monthly">Monthly</option>
              </select>
            </div>
            <button type="submit" className="btn btn-primary">Add Habit</button>
          </form>
        )}

        {habits.length === 0 ? (
          <div className="empty-state">
            <p>No habits yet. Start by adding your first habit!</p>
          </div>
        ) : (
          <div className="habits-list">
            {habits.map(habit => (
              <div 
                key={habit.id} 
                className={`habit-card ${habit.completed ? 'completed' : ''}`}
              >
                <div className="habit-content">
                  <div className="habit-checkbox">
                    <input
                      type="checkbox"
                      checked={habit.completed}
                      onChange={() => handleToggleComplete(habit.id)}
                      id={`habit-${habit.id}`}
                    />
                    <label htmlFor={`habit-${habit.id}`}></label>
                  </div>
                  <div className="habit-info">
                    <h3>{habit.name}</h3>
                    {habit.description && <p>{habit.description}</p>}
                    <span className="frequency-badge">{habit.frequency}</span>
                  </div>
                </div>
                <button
                  className="btn btn-delete"
                  onClick={() => handleDeleteHabit(habit.id)}
                  title="Delete habit"
                >
                  🗑️
                </button>
              </div>
            ))}
          </div>
        )}
      </main>

      <footer className="app-footer">
        <p>Track your habits, enhance your performance 💪</p>
      </footer>
    </div>
  )
}

export default App
