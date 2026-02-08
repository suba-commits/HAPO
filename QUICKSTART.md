# HAPO Quick Start Guide

## Installation & First Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/suba-commits/HAPO.git
   cd HAPO
   ```

2. **Run HAPO:**
   ```bash
   python3 hapo.py
   ```

3. **Run Tests:**
   ```bash
   python3 test_hapo.py
   ```

## Quick Tutorial (5 minutes)

### Step 1: Add Your First Habit
```
🎯 HAPO> add
📝 Habit name: Reading
🏷️  Is this a GOOD habit or BAD habit?
   1. Good habit
   2. Bad habit
Choice: 1
🎯 Your goal: Read 30 minutes every day
📅 Habit frequency:
   1. Daily
   2. Weekly
Choice: 1
✅ Habit 'Reading' added successfully!
```

### Step 2: View Your Habits
```
🎯 HAPO> list
```

### Step 3: Check Today's Tasks
```
🎯 HAPO> today
```

### Step 4: Log a Habit Completion
```
🎯 HAPO> log
Select a habit to log:
  1. ✅ Reading
Choice: 1
✅ Did you complete 'Reading' today? (y/n): y
🎉 Great job! 'Reading' logged for today!
   Streak: 1 days 🔥
   Points earned: +12 ⭐
```

### Step 5: Check Your Progress
```
🎯 HAPO> stats
```

## Common Commands Cheat Sheet

| Command | Description |
|---------|-------------|
| `add` | Add a new habit |
| `list` | View all habits |
| `log` | Log a habit completion |
| `today` | View today's checklist |
| `stats` | View your statistics |
| `delete` | Remove a habit |
| `help` | Show help |
| `exit` | Quit the app |

## Example Habits

### Good Habits to Build ✅
- Reading (30 minutes daily)
- Exercise (45 minutes daily)
- Meditation (10 minutes daily)
- Writing (500 words daily)
- Learning (1 hour daily)
- Hydration (8 glasses daily)
- Early Rising (wake up at 6 AM)

### Bad Habits to Eliminate 🚫
- Smoking
- Excessive Screen Time
- Junk Food
- Late Night Snacking
- Procrastination
- Oversleeping
- Gaming (excessive)

## Tips for Success

1. **Start with 2-3 habits** - Don't overwhelm yourself
2. **Be consistent** - Log every day to build streaks
3. **Set realistic goals** - Make them achievable
4. **Check daily** - Review your `today` view each morning
5. **Celebrate wins** - Check `stats` regularly to see progress

## Data Storage

All your data is saved in `hapo_data.json` in the same directory. Your progress persists between sessions!

## Getting Help

Type `help` in the app for detailed command information.

Happy habit building! 🎯
