# HAPO
Habit Tracker and Performance Enhancer

A full-stack web application for tracking habits and enhancing personal performance. Built with React (frontend) and Node.js/Express (backend).

## Features

- ✅ Create, read, update, and delete habits
- 🎯 Track habit completion status
- 📊 View all your habits in one place
- 🔄 Set habit frequency (daily, weekly, monthly)
- 💾 In-memory data storage for quick MVP

## Tech Stack

### Backend
- Node.js
- Express.js
- CORS enabled for frontend communication

### Frontend
- React 19
- Vite (build tool)
- Modern CSS styling

## Getting Started

### Prerequisites
- Node.js (v14 or higher)
- npm (v6 or higher)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/suba-commits/HAPO.git
cd HAPO
```

2. Install dependencies for both frontend and backend:
```bash
npm run install:all
```

Or install them separately:
```bash
# Install backend dependencies
npm run install:backend

# Install frontend dependencies
npm run install:frontend
```

### Building

To build both frontend and backend:
```bash
npm run build
```

To build separately:
```bash
# Build backend (no build step needed for Node.js)
npm run build:backend

# Build frontend (creates production build in frontend/dist)
npm run build:frontend
```

### Running the Application

You need to run both the backend server and the frontend development server:

#### Option 1: Using two terminal windows

**Terminal 1 - Backend Server:**
```bash
npm run start:backend
```
The backend API will start on `http://localhost:3001`

**Terminal 2 - Frontend Development Server:**
```bash
npm run start:frontend
```
The frontend will start on `http://localhost:5173`

#### Option 2: Using individual commands

```bash
# Start backend server
cd backend
npm start

# In another terminal, start frontend
cd frontend
npm run dev
```

### Testing the Application

1. Open your browser and navigate to `http://localhost:5173`
2. You should see the HAPO habit tracker interface
3. Try adding a new habit by clicking the "+ Add Habit" button
4. Toggle habit completion by checking/unchecking the checkboxes
5. Delete habits using the trash icon

## API Endpoints

The backend provides the following REST API endpoints:

- `GET /api/habits` - Get all habits
- `GET /api/habits/:id` - Get a specific habit
- `POST /api/habits` - Create a new habit
- `PUT /api/habits/:id` - Update a habit
- `DELETE /api/habits/:id` - Delete a habit
- `PATCH /api/habits/:id/toggle` - Toggle habit completion status
- `GET /health` - Health check endpoint

## Project Structure

```
HAPO/
├── backend/
│   ├── server.js          # Express server with API routes
│   ├── package.json       # Backend dependencies
│   └── node_modules/      # Backend dependencies (git-ignored)
├── frontend/
│   ├── src/
│   │   ├── App.jsx        # Main React component
│   │   ├── App.css        # Component styles
│   │   ├── index.css      # Global styles
│   │   └── main.jsx       # React entry point
│   ├── public/            # Static assets
│   ├── index.html         # HTML template
│   ├── package.json       # Frontend dependencies
│   ├── vite.config.js     # Vite configuration
│   └── node_modules/      # Frontend dependencies (git-ignored)
├── package.json           # Root package.json with build scripts
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## Development

### Backend Development
The backend uses plain Node.js with Express. Make changes to `backend/server.js` and restart the server to see changes.

### Frontend Development
The frontend uses Vite with Hot Module Replacement (HMR). Changes to React components will automatically reload in the browser.

## Future Enhancements

- Add database integration (MongoDB, PostgreSQL)
- User authentication and authorization
- Habit streaks and statistics
- Data visualization and charts
- Mobile responsive design improvements
- Progressive Web App (PWA) support
- Habit reminders and notifications

## License

ISC
