# 🎯 HAPO - Habit Tracker and Performance Enhancer

**HAPO** is an interactive daily habit tracking application that helps you build good habits and eliminate bad ones. Track your progress, earn points, build streaks, and get motivated with a fun and rewarding experience!

## ✨ Features

### 📊 Habit Management
- **Add Habits**: Track both good habits (to build) and bad habits (to eliminate)
- **Categorization**: Separate good habits (reading, exercise) from bad habits (smoking, excessive screen time)
- **Custom Goals**: Set personal goals for each habit
- **Flexible Tracking**: Daily or weekly habit tracking

### 🎮 Gamification & Rewards
- **Points System**: Earn points for every habit completion
- **Streak Tracking**: Build consecutive day streaks for each habit
- **Bonus Points**: Get streak bonuses - the longer your streak, the more points you earn
- **Motivational Messages**: Receive encouraging messages at milestone achievements
- **Performance Stats**: Track your best streaks and overall progress

### 📈 Progress Tracking
- **Daily Checklist**: See all habits you need to complete today
- **Statistics Dashboard**: View total points, streaks, and completion rates
- **Historical Data**: All your habit data is saved locally in JSON format
- **Best Performance**: Track your best performing habits

### 🎨 Interactive & Fun
- **Colorful Emojis**: Visual indicators for different habit types and status
- **Real-time Feedback**: Immediate feedback on habit logging
- **User-friendly CLI**: Easy-to-use command-line interface
- **Guidance**: Get tips and motivation based on your progress

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher
- No external dependencies required!

### Installation

1. Clone the repository:
```bash
git clone https://github.com/suba-commits/HAPO.git
cd HAPO
```

2. Run the app:
```bash
python3 hapo.py
```

That's it! No installation needed - just run the script.

## 📖 Usage Guide

### Starting HAPO
```bash
python3 hapo.py
```

You'll see the welcome banner and a command prompt:
```
🎯 HAPO>
```

### Available Commands

#### `add` - Add a New Habit
Add a habit you want to track. You'll be prompted for:
- Habit name (e.g., "Reading", "Exercise")
- Type: Good habit (to build) or Bad habit (to eliminate)
- Your goal (e.g., "Read 30 minutes daily")
- Frequency (daily or weekly)

**Example:**
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

#### `list` - View All Habits
Display all your tracked habits with their statistics:
- Current streaks
- Best streaks
- Total completions
- Points earned

```
🎯 HAPO> list
```

#### `log` - Log Habit Completion
Mark a habit as completed (or avoided for bad habits) for today:

```
🎯 HAPO> log
Select a habit to log:
  1. ✅ Reading
  2. ✅ Exercise
  3. 🚫 Smoking
Choice: 1
✅ Did you complete 'Reading' today? (y/n): y
🎉 Great job! 'Reading' logged for today!
   Streak: 5 days 🔥
   Points earned: +20 ⭐
```

#### `today` - View Today's Checklist
See which habits you need to complete today:

```
🎯 HAPO> today
📅 TODAY'S HABITS - Monday, February 08, 2026
  ✓ DONE Reading
  ⬜ PENDING Exercise
  ⬜ PENDING Meditation
Progress: 1 completed, 2 pending
```

#### `stats` - View Your Statistics
Display your overall performance and achievements:

```
🎯 HAPO> stats
📈 YOUR PERFORMANCE STATS
⭐ Total Points: 450
🔥 Combined Streak: 15 days
🏆 Best Combined Streak: 20 days
📋 Total Habits: 5
✓ Total Completions: 45
🌟 Best Performing Habit: Reading
   Streak: 10 days 🔥
📅 Today's Progress: 3/5 habits logged
```

#### `delete` - Remove a Habit
Delete a habit you no longer want to track:

```
🎯 HAPO> delete
🗑️  Enter habit name to delete: Old Habit
```

#### `help` - Show Help
Display all available commands and examples.

#### `exit` or `quit` - Exit the App
Close the application.

## 🎯 Example Use Cases

### Building Good Habits
Track habits that help you grow:
- 📚 **Reading**: Read 30 minutes daily
- 🏃 **Exercise**: Work out 5 times per week
- ✍️ **Writing**: Write 500 words daily
- 🧘 **Meditation**: Meditate 10 minutes daily
- 💧 **Hydration**: Drink 8 glasses of water daily
- 🌅 **Early Rising**: Wake up at 6 AM

### Eliminating Bad Habits
Track habits you want to eliminate:
- 🚬 **Smoking**: Quit smoking
- 📱 **Screen Time**: Reduce phone usage
- 🍔 **Junk Food**: Avoid junk food
- 🎮 **Gaming**: Limit gaming to 1 hour daily
- 😴 **Late Sleeping**: Stop staying up past midnight

## 🏆 Points & Rewards System

### How Points Work
- **Base Points**: 10 points per completion
- **Streak Bonus**: 2 points × current streak
- **Example**: With a 5-day streak, you earn 10 + (2 × 5) = 20 points

### Motivational Milestones
- **Day 1**: "Great start! The first step is always the hardest."
- **Day 7**: "One week strong! You're building momentum! 🚀"
- **Day 30**: "30 days! You're forming a real habit now! 🎯"
- **Day 100**: "100 DAYS! You're a LEGEND! 🏆👑"
- **Every 10 days**: Special encouragement messages

## 💾 Data Storage

All your habit data is stored locally in `hapo_data.json` in the same directory as the app. This file contains:
- All your habits and their details
- Daily completion logs
- Statistics and streaks
- Total points

The data persists between sessions, so you never lose your progress!

## 🎨 Features Explained

### Good Habits (Building) ✅
When you add a habit as "good", HAPO helps you:
- Build consistency through daily tracking
- Earn points for every completion
- Build streaks to create lasting habits
- Get motivated to continue

### Bad Habits (Eliminating) 🚫
When you add a habit as "bad", HAPO helps you:
- Track days you successfully avoid the habit
- Break the habit through accountability
- Build "avoidance streaks"
- Stay motivated to quit

### Interactive & Rewarding 🎮
HAPO makes habit tracking fun by:
- Using colorful emojis for visual feedback
- Awarding points and tracking streaks
- Providing motivational messages
- Showing your progress and achievements
- Making it easy to stay consistent

## 🛠️ Technical Details

- **Language**: Python 3.6+
- **Dependencies**: None (uses standard library only)
- **Storage**: JSON file (hapo_data.json)
- **Platform**: Cross-platform (Windows, macOS, Linux)

## 📝 Tips for Success

1. **Start Small**: Begin with 2-3 habits, then add more as you build consistency
2. **Be Specific**: Set clear, measurable goals (e.g., "Read 30 minutes" vs "Read more")
3. **Daily Review**: Check your `today` view each morning to plan your day
4. **Celebrate Wins**: Check your `stats` regularly to see your progress
5. **Don't Break the Chain**: Focus on maintaining streaks for motivation
6. **Be Honest**: Log honestly - it's about personal growth, not perfection

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📄 License

This project is open source and available for personal use.

## 🎯 Start Your Journey Today!

```bash
python3 hapo.py
```

Build better habits. Eliminate bad ones. Track your progress. 🚀

---

Made with ❤️ for building better lives through better habits.
