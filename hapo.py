#!/usr/bin/env python3
"""
HAPO - Habit Tracker and Performance Enhancer
A daily habit tracking app that helps users build good habits and eliminate bad ones.
"""

import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import sys


class HabitTracker:
    """Main class for tracking habits and user progress."""
    
    def __init__(self, data_file: str = "hapo_data.json"):
        self.data_file = data_file
        self.data = self.load_data()
    
    def load_data(self) -> Dict:
        """Load habit data from JSON file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return self._get_default_data()
        return self._get_default_data()
    
    def _get_default_data(self) -> Dict:
        """Get default data structure."""
        return {
            "habits": {},
            "daily_logs": {},
            "user_stats": {
                "total_points": 0,
                "current_streak": 0,
                "best_streak": 0
            }
        }
    
    def save_data(self) -> None:
        """Save habit data to JSON file."""
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def add_habit(self, name: str, habit_type: str, goal: str, 
                  category: str = "good") -> None:
        """
        Add a new habit to track.
        
        Args:
            name: Name of the habit
            habit_type: Type (daily, weekly)
            goal: User's goal for this habit
            category: 'good' for building habits, 'bad' for eliminating habits
        """
        habit_id = name.lower().replace(" ", "_")
        
        if habit_id in self.data["habits"]:
            print(f"❌ Habit '{name}' already exists!")
            return
        
        self.data["habits"][habit_id] = {
            "name": name,
            "type": habit_type,
            "goal": goal,
            "category": category,
            "created_date": datetime.now().strftime("%Y-%m-%d"),
            "streak": 0,
            "best_streak": 0,
            "total_completions": 0,
            "points": 0
        }
        self.save_data()
        
        emoji = "✅" if category == "good" else "🚫"
        print(f"{emoji} Habit '{name}' added successfully!")
        print(f"   Goal: {goal}")
        print(f"   Type: {habit_type}")
    
    def list_habits(self, filter_category: Optional[str] = None) -> None:
        """List all habits or filter by category."""
        habits = self.data["habits"]
        
        if not habits:
            print("📋 No habits tracked yet. Add your first habit!")
            return
        
        print("\n" + "="*60)
        print("📊 YOUR HABITS")
        print("="*60)
        
        good_habits = []
        bad_habits = []
        
        for habit_id, habit in habits.items():
            if filter_category and habit["category"] != filter_category:
                continue
            
            if habit["category"] == "good":
                good_habits.append((habit_id, habit))
            else:
                bad_habits.append((habit_id, habit))
        
        if not filter_category or filter_category == "good":
            if good_habits:
                print("\n✅ GOOD HABITS (Building):")
                print("-" * 60)
                for habit_id, habit in good_habits:
                    self._print_habit_details(habit_id, habit)
        
        if not filter_category or filter_category == "bad":
            if bad_habits:
                print("\n🚫 BAD HABITS (Eliminating):")
                print("-" * 60)
                for habit_id, habit in bad_habits:
                    self._print_habit_details(habit_id, habit)
        
        print("="*60 + "\n")
    
    def _print_habit_details(self, habit_id: str, habit: Dict) -> None:
        """Print formatted habit details."""
        streak_emoji = "🔥" if habit["streak"] > 0 else "💤"
        print(f"\n  📌 {habit['name']}")
        print(f"     Goal: {habit['goal']}")
        print(f"     {streak_emoji} Current Streak: {habit['streak']} days")
        print(f"     🏆 Best Streak: {habit['best_streak']} days")
        print(f"     ✓ Completions: {habit['total_completions']}")
        print(f"     ⭐ Points: {habit['points']}")
    
    def log_habit(self, habit_name: str, completed: bool = True) -> None:
        """
        Log a habit completion for today.
        
        Args:
            habit_name: Name of the habit
            completed: True if completed, False if failed (for bad habits)
        """
        habit_id = habit_name.lower().replace(" ", "_")
        
        if habit_id not in self.data["habits"]:
            print(f"❌ Habit '{habit_name}' not found. Add it first!")
            return
        
        today = datetime.now().strftime("%Y-%m-%d")
        habit = self.data["habits"][habit_id]
        
        # Initialize today's log if needed
        if today not in self.data["daily_logs"]:
            self.data["daily_logs"][today] = {}
        
        # Check if already logged today
        if habit_id in self.data["daily_logs"][today]:
            print(f"⚠️  Already logged '{habit['name']}' today!")
            return
        
        # Log the habit
        self.data["daily_logs"][today][habit_id] = completed
        
        # Update habit statistics
        if completed:
            habit["total_completions"] += 1
            habit["streak"] += 1
            
            if habit["streak"] > habit["best_streak"]:
                habit["best_streak"] = habit["streak"]
            
            # Award points
            points_earned = self._calculate_points(habit)
            habit["points"] += points_earned
            self.data["user_stats"]["total_points"] += points_earned
            
            # Update streaks
            self._update_user_streaks()
            
            emoji = "🎉" if habit["category"] == "good" else "💪"
            print(f"{emoji} Great job! '{habit['name']}' logged for today!")
            print(f"   Streak: {habit['streak']} days 🔥")
            print(f"   Points earned: +{points_earned} ⭐")
            
            # Show motivational message
            self._show_motivation(habit)
        else:
            habit["streak"] = 0
            print(f"😔 Streak broken for '{habit['name']}'. Don't give up!")
            print(f"   Remember: {habit['goal']}")
        
        self.save_data()
    
    def _calculate_points(self, habit: Dict) -> int:
        """Calculate points based on streak and habit importance."""
        base_points = 10
        streak_bonus = habit["streak"] * 2
        return base_points + streak_bonus
    
    def _update_user_streaks(self) -> None:
        """Update overall user streaks."""
        total_streak = sum(h["streak"] for h in self.data["habits"].values())
        self.data["user_stats"]["current_streak"] = total_streak
        
        if total_streak > self.data["user_stats"]["best_streak"]:
            self.data["user_stats"]["best_streak"] = total_streak
    
    def _show_motivation(self, habit: Dict) -> None:
        """Show motivational messages based on progress."""
        streak = habit["streak"]
        
        if streak == 1:
            print("   💬 Great start! The first step is always the hardest.")
        elif streak == 7:
            print("   💬 One week strong! You're building momentum! 🚀")
        elif streak == 30:
            print("   💬 30 days! You're forming a real habit now! 🎯")
        elif streak == 100:
            print("   💬 100 DAYS! You're a LEGEND! 🏆👑")
        elif streak % 10 == 0:
            print(f"   💬 {streak} days and counting! Keep it up! 💪")
    
    def show_stats(self) -> None:
        """Display user statistics and progress."""
        stats = self.data["user_stats"]
        habits = self.data["habits"]
        
        print("\n" + "="*60)
        print("📈 YOUR PERFORMANCE STATS")
        print("="*60)
        
        print(f"\n⭐ Total Points: {stats['total_points']}")
        print(f"🔥 Combined Streak: {stats['current_streak']} days")
        print(f"🏆 Best Combined Streak: {stats['best_streak']} days")
        print(f"📋 Total Habits: {len(habits)}")
        
        if habits:
            total_completions = sum(h["total_completions"] for h in habits.values())
            print(f"✓ Total Completions: {total_completions}")
            
            # Find best performing habit
            best_habit = max(habits.values(), key=lambda h: h["streak"])
            if best_habit["streak"] > 0:
                print(f"\n🌟 Best Performing Habit: {best_habit['name']}")
                print(f"   Streak: {best_habit['streak']} days 🔥")
        
        # Show today's progress
        today = datetime.now().strftime("%Y-%m-%d")
        if today in self.data["daily_logs"]:
            completed_today = len(self.data["daily_logs"][today])
            print(f"\n📅 Today's Progress: {completed_today}/{len(habits)} habits logged")
        else:
            print(f"\n📅 Today's Progress: 0/{len(habits)} habits logged")
        
        print("="*60 + "\n")
    
    def show_today(self) -> None:
        """Show today's habit checklist."""
        today = datetime.now().strftime("%Y-%m-%d")
        habits = self.data["habits"]
        
        if not habits:
            print("📋 No habits to track yet. Add some habits first!")
            return
        
        print("\n" + "="*60)
        print(f"📅 TODAY'S HABITS - {datetime.now().strftime('%A, %B %d, %Y')}")
        print("="*60)
        
        today_logs = self.data["daily_logs"].get(today, {})
        
        for habit_id, habit in habits.items():
            if habit_id in today_logs:
                status = "✓ DONE" if today_logs[habit_id] else "✗ FAILED"
                print(f"\n  {status} {habit['name']}")
            else:
                print(f"\n  ⬜ PENDING {habit['name']}")
            print(f"     Goal: {habit['goal']}")
        
        completed = sum(1 for h in today_logs.values() if h)
        pending = len(habits) - len(today_logs)
        
        print("\n" + "-"*60)
        print(f"Progress: {completed} completed, {pending} pending")
        print("="*60 + "\n")
    
    def delete_habit(self, habit_name: str) -> None:
        """Delete a habit from tracking."""
        habit_id = habit_name.lower().replace(" ", "_")
        
        if habit_id not in self.data["habits"]:
            print(f"❌ Habit '{habit_name}' not found!")
            return
        
        habit = self.data["habits"][habit_id]
        del self.data["habits"][habit_id]
        
        # Clean up logs
        for date in self.data["daily_logs"]:
            if habit_id in self.data["daily_logs"][date]:
                del self.data["daily_logs"][date][habit_id]
        
        self.save_data()
        print(f"🗑️  Habit '{habit['name']}' deleted.")


def print_banner():
    """Print app banner."""
    banner = """
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║   🎯 HAPO - Habit Tracker & Performance Enhancer 🎯       ║
║                                                           ║
║   Build good habits. Eliminate bad ones. Track progress. ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
    """
    print(banner)


def print_help():
    """Print help information."""
    help_text = """
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
    """
    print(help_text)


def interactive_add_habit(tracker: HabitTracker) -> None:
    """Interactive prompt to add a habit."""
    print("\n" + "="*60)
    print("➕ ADD NEW HABIT")
    print("="*60)
    
    name = input("\n📝 Habit name (e.g., 'Reading', 'Exercise'): ").strip()
    if not name:
        print("❌ Habit name cannot be empty!")
        return
    
    print("\n🏷️  Is this a GOOD habit or BAD habit?")
    print("   1. Good habit (to build, e.g., reading, exercise)")
    print("   2. Bad habit (to eliminate, e.g., smoking, excessive screen time)")
    
    category_choice = input("\nChoice (1/2): ").strip()
    category = "good" if category_choice == "1" else "bad"
    
    if category == "good":
        goal = input("\n🎯 Your goal (e.g., 'Read 30 minutes daily'): ").strip()
    else:
        goal = input("\n🎯 Your goal (e.g., 'Quit smoking', 'Reduce screen time'): ").strip()
    
    print("\n📅 Habit frequency:")
    print("   1. Daily")
    print("   2. Weekly")
    
    freq_choice = input("\nChoice (1/2): ").strip()
    habit_type = "daily" if freq_choice == "1" else "weekly"
    
    tracker.add_habit(name, habit_type, goal, category)


def interactive_log_habit(tracker: HabitTracker) -> None:
    """Interactive prompt to log a habit."""
    habits = tracker.data["habits"]
    
    if not habits:
        print("❌ No habits to log. Add some habits first!")
        return
    
    print("\n" + "="*60)
    print("✓ LOG HABIT COMPLETION")
    print("="*60)
    
    print("\nSelect a habit to log:")
    habit_list = list(habits.items())
    
    for i, (habit_id, habit) in enumerate(habit_list, 1):
        emoji = "✅" if habit["category"] == "good" else "🚫"
        print(f"  {i}. {emoji} {habit['name']}")
    
    try:
        choice = int(input("\nChoice (number): ").strip())
        if 1 <= choice <= len(habit_list):
            habit_id, habit = habit_list[choice - 1]
            
            if habit["category"] == "good":
                print(f"\n✅ Did you complete '{habit['name']}' today?")
            else:
                print(f"\n🚫 Did you avoid '{habit['name']}' today?")
            
            confirm = input("   (y/n): ").strip().lower()
            completed = confirm == 'y'
            
            tracker.log_habit(habit['name'], completed)
        else:
            print("❌ Invalid choice!")
    except ValueError:
        print("❌ Invalid input!")


def main():
    """Main application loop."""
    tracker = HabitTracker()
    print_banner()
    print("💡 Type 'help' for available commands\n")
    
    while True:
        try:
            command = input("🎯 HAPO> ").strip().lower()
            
            if not command:
                continue
            
            if command in ['exit', 'quit', 'q']:
                print("\n👋 Keep building those habits! See you tomorrow! 🌟\n")
                break
            
            elif command == 'help':
                print_help()
            
            elif command == 'add':
                interactive_add_habit(tracker)
            
            elif command == 'list':
                tracker.list_habits()
            
            elif command == 'log':
                interactive_log_habit(tracker)
            
            elif command == 'today':
                tracker.show_today()
            
            elif command == 'stats':
                tracker.show_stats()
            
            elif command == 'delete':
                tracker.list_habits()
                name = input("\n🗑️  Enter habit name to delete: ").strip()
                if name:
                    tracker.delete_habit(name)
            
            else:
                print(f"❌ Unknown command: '{command}'. Type 'help' for available commands.")
        
        except KeyboardInterrupt:
            print("\n\n👋 Keep building those habits! See you tomorrow! 🌟\n")
            break
        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
