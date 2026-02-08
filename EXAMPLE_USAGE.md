# HAPO - Example Usage Session

This file demonstrates a typical usage session with HAPO.

## Starting HAPO

```bash
$ python3 hapo.py
```

## Output:

```
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║   🎯 HAPO - Habit Tracker & Performance Enhancer 🎯       ║
║                                                           ║
║   Build good habits. Eliminate bad ones. Track progress. ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
    
💡 Type 'help' for available commands

🎯 HAPO>
```

## Example Session

### 1. Adding a Good Habit (Reading)

```
🎯 HAPO> add

============================================================
➕ ADD NEW HABIT
============================================================

📝 Habit name (e.g., 'Reading', 'Exercise'): Reading

🏷️  Is this a GOOD habit or BAD habit?
   1. Good habit (to build, e.g., reading, exercise)
   2. Bad habit (to eliminate, e.g., smoking, excessive screen time)

Choice (1/2): 1

🎯 Your goal (e.g., 'Read 30 minutes daily'): Read 30 minutes every day

📅 Habit frequency:
   1. Daily
   2. Weekly

Choice (1/2): 1
✅ Habit 'Reading' added successfully!
   Goal: Read 30 minutes every day
   Type: daily
```

### 2. Adding Another Good Habit (Exercise)

```
🎯 HAPO> add

============================================================
➕ ADD NEW HABIT
============================================================

📝 Habit name (e.g., 'Reading', 'Exercise'): Exercise

🏷️  Is this a GOOD habit or BAD habit?
   1. Good habit (to build, e.g., reading, exercise)
   2. Bad habit (to eliminate, e.g., smoking, excessive screen time)

Choice (1/2): 1

🎯 Your goal (e.g., 'Read 30 minutes daily'): Work out 45 minutes daily

📅 Habit frequency:
   1. Daily
   2. Weekly

Choice (1/2): 1
✅ Habit 'Exercise' added successfully!
   Goal: Work out 45 minutes daily
   Type: daily
```

### 3. Adding a Bad Habit to Eliminate (Smoking)

```
🎯 HAPO> add

============================================================
➕ ADD NEW HABIT
============================================================

📝 Habit name (e.g., 'Reading', 'Exercise'): Smoking

🏷️  Is this a GOOD habit or BAD habit?
   1. Good habit (to build, e.g., reading, exercise)
   2. Bad habit (to eliminate, e.g., smoking, excessive screen time)

Choice (1/2): 2

🎯 Your goal (e.g., 'Quit smoking', 'Reduce screen time'): Quit smoking completely

📅 Habit frequency:
   1. Daily
   2. Weekly

Choice (1/2): 1
🚫 Habit 'Smoking' added successfully!
   Goal: Quit smoking completely
   Type: daily
```

### 4. Viewing All Habits

```
🎯 HAPO> list

============================================================
📊 YOUR HABITS
============================================================

✅ GOOD HABITS (Building):
------------------------------------------------------------

  📌 Reading
     Goal: Read 30 minutes every day
     💤 Current Streak: 0 days
     🏆 Best Streak: 0 days
     ✓ Completions: 0
     ⭐ Points: 0

  📌 Exercise
     Goal: Work out 45 minutes daily
     💤 Current Streak: 0 days
     🏆 Best Streak: 0 days
     ✓ Completions: 0
     ⭐ Points: 0

🚫 BAD HABITS (Eliminating):
------------------------------------------------------------

  📌 Smoking
     Goal: Quit smoking completely
     💤 Current Streak: 0 days
     🏆 Best Streak: 0 days
     ✓ Completions: 0
     ⭐ Points: 0
============================================================
```

### 5. Checking Today's Checklist

```
🎯 HAPO> today

============================================================
📅 TODAY'S HABITS - Sunday, February 08, 2026
============================================================

  ⬜ PENDING Reading
     Goal: Read 30 minutes every day

  ⬜ PENDING Exercise
     Goal: Work out 45 minutes daily

  ⬜ PENDING Smoking
     Goal: Quit smoking completely

------------------------------------------------------------
Progress: 0 completed, 3 pending
============================================================
```

### 6. Logging a Habit Completion

```
🎯 HAPO> log

============================================================
✓ LOG HABIT COMPLETION
============================================================

Select a habit to log:
  1. ✅ Reading
  2. ✅ Exercise
  3. 🚫 Smoking

Choice (number): 1

✅ Did you complete 'Reading' today?
   (y/n): y
🎉 Great job! 'Reading' logged for today!
   Streak: 1 days 🔥
   Points earned: +12 ⭐
   💬 Great start! The first step is always the hardest.
```

### 7. Logging Another Habit

```
🎯 HAPO> log

============================================================
✓ LOG HABIT COMPLETION
============================================================

Select a habit to log:
  1. ✅ Reading
  2. ✅ Exercise
  3. 🚫 Smoking

Choice (number): 3

🚫 Did you avoid 'Smoking' today?
   (y/n): y
💪 Great job! 'Smoking' logged for today!
   Streak: 1 days 🔥
   Points earned: +12 ⭐
   💬 Great start! The first step is always the hardest.
```

### 8. Viewing Statistics

```
🎯 HAPO> stats

============================================================
📈 YOUR PERFORMANCE STATS
============================================================

⭐ Total Points: 24
🔥 Combined Streak: 2 days
🏆 Best Combined Streak: 2 days
📋 Total Habits: 3
✓ Total Completions: 2

🌟 Best Performing Habit: Reading
   Streak: 1 days 🔥

📅 Today's Progress: 2/3 habits logged
============================================================
```

### 9. Checking Updated Today's View

```
🎯 HAPO> today

============================================================
📅 TODAY'S HABITS - Sunday, February 08, 2026
============================================================

  ✓ DONE Reading
     Goal: Read 30 minutes every day

  ⬜ PENDING Exercise
     Goal: Work out 45 minutes daily

  ✓ DONE Smoking
     Goal: Quit smoking completely

------------------------------------------------------------
Progress: 2 completed, 1 pending
============================================================
```

### 10. Getting Help

```
🎯 HAPO> help

📖 HAPO COMMANDS:

  add         Add a new habit to track
  list        List all habits
  log         Log a habit completion for today
  today       Show today's habit checklist
  stats       Show your performance statistics
  delete      Delete a habit
  help        Show this help message
  exit        Exit the app

💡 EXAMPLES:

  > add
    Follow prompts to add a new habit
  
  > list
    View all your habits
  
  > log
    Log a habit completion for today
  
  > today
    See what habits you need to complete today
  
  > stats
    View your overall progress and statistics

🎮 MAKE IT FUN:
  - Earn points for every completion
  - Build streaks for consistency
  - Get motivational messages
  - Track your best performances
```

### 11. Exiting the App

```
🎯 HAPO> exit

👋 Keep building those habits! See you tomorrow! 🌟
```

## Key Features Demonstrated

1. ✅ **Habit Management** - Add, view, and track habits
2. 🎯 **Goal Setting** - Set personal goals for each habit
3. 📊 **Progress Tracking** - Monitor completions and streaks
4. ⭐ **Points System** - Earn points with streak bonuses
5. 🔥 **Streak Building** - Build consecutive day streaks
6. 💬 **Motivational Messages** - Get encouragement at milestones
7. 📅 **Daily Checklist** - See what needs to be done today
8. 📈 **Statistics** - View overall performance metrics
9. 🎨 **Visual Feedback** - Emojis and colors for better UX
10. 💾 **Data Persistence** - All data saved automatically

## Motivational Milestones

As you continue using HAPO, you'll receive special messages at:
- **Day 1**: "Great start! The first step is always the hardest."
- **Day 7**: "One week strong! You're building momentum! 🚀"
- **Day 30**: "30 days! You're forming a real habit now! 🎯"
- **Day 100**: "100 DAYS! You're a LEGEND! 🏆👑"
- **Every 10 days**: Encouragement messages

## Tips for Best Results

1. **Be consistent** - Log habits daily
2. **Start small** - Begin with 2-3 habits
3. **Be honest** - Accurate tracking leads to real progress
4. **Review daily** - Check your `today` view each morning
5. **Celebrate wins** - Check `stats` to see your progress
6. **Don't give up** - If you break a streak, start again!

Happy habit building! 🎯🚀
