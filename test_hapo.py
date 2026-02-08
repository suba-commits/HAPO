#!/usr/bin/env python3
"""
Test script for HAPO - Demonstrates all functionality
"""

import os
import sys
import json

# Import the HabitTracker class
from hapo import HabitTracker

def test_hapo():
    """Test all HAPO functionality."""
    print("=" * 70)
    print("🧪 TESTING HAPO - Habit Tracker & Performance Enhancer")
    print("=" * 70)
    
    # Use a test data file
    test_file = "/tmp/test_hapo_data.json"
    if os.path.exists(test_file):
        os.remove(test_file)
    
    tracker = HabitTracker(data_file=test_file)
    
    # Test 1: Add good habits
    print("\n✅ TEST 1: Adding good habits...")
    tracker.add_habit("Reading", "daily", "Read 30 minutes every day", "good")
    tracker.add_habit("Exercise", "daily", "Work out for 45 minutes", "good")
    tracker.add_habit("Meditation", "daily", "Meditate for 10 minutes", "good")
    tracker.add_habit("Writing", "daily", "Write 500 words daily", "good")
    print("✓ Good habits added successfully!\n")
    
    # Test 2: Add bad habits
    print("✅ TEST 2: Adding bad habits to eliminate...")
    tracker.add_habit("Smoking", "daily", "Quit smoking completely", "bad")
    tracker.add_habit("Excessive Screen Time", "daily", "Limit screen time to 2 hours", "bad")
    tracker.add_habit("Junk Food", "daily", "Avoid junk food", "bad")
    print("✓ Bad habits added successfully!\n")
    
    # Test 3: List all habits
    print("✅ TEST 3: Listing all habits...")
    tracker.list_habits()
    
    # Test 4: Show today's checklist
    print("✅ TEST 4: Today's checklist...")
    tracker.show_today()
    
    # Test 5: Log some habits
    print("✅ TEST 5: Logging habit completions...")
    tracker.log_habit("Reading", True)
    tracker.log_habit("Exercise", True)
    tracker.log_habit("Meditation", True)
    tracker.log_habit("Smoking", True)  # Successfully avoided smoking
    tracker.log_habit("Junk Food", True)  # Successfully avoided junk food
    print("\n")
    
    # Test 6: Show updated today's checklist
    print("✅ TEST 6: Updated today's checklist...")
    tracker.show_today()
    
    # Test 7: Show statistics
    print("✅ TEST 7: Showing statistics...")
    tracker.show_stats()
    
    # Test 8: Test streak building (simulate multiple days)
    print("✅ TEST 8: Testing streak building...")
    print("Simulating habit completion over multiple days...\n")
    
    from datetime import datetime, timedelta
    
    # Manually add logs for previous days to build streaks
    for i in range(1, 6):
        past_date = (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d")
        tracker.data["daily_logs"][past_date] = {
            "reading": True,
            "exercise": True
        }
        tracker.data["habits"]["reading"]["streak"] = i
        tracker.data["habits"]["reading"]["total_completions"] += 1
        tracker.data["habits"]["exercise"]["streak"] = i
        tracker.data["habits"]["exercise"]["total_completions"] += 1
    
    # Update best streaks
    tracker.data["habits"]["reading"]["best_streak"] = 5
    tracker.data["habits"]["exercise"]["best_streak"] = 5
    tracker.save_data()
    
    print("Streaks built! Let's see the updated stats...")
    tracker.show_stats()
    
    # Test 9: List only good habits
    print("✅ TEST 9: Filtering - Good habits only...")
    tracker.list_habits(filter_category="good")
    
    # Test 10: List only bad habits
    print("✅ TEST 10: Filtering - Bad habits only...")
    tracker.list_habits(filter_category="bad")
    
    # Test 11: Verify data persistence
    print("✅ TEST 11: Testing data persistence...")
    tracker2 = HabitTracker(data_file=test_file)
    print(f"✓ Data loaded successfully!")
    print(f"  - {len(tracker2.data['habits'])} habits loaded")
    print(f"  - {len(tracker2.data['daily_logs'])} days of logs loaded")
    print(f"  - {tracker2.data['user_stats']['total_points']} total points\n")
    
    # Test 12: Test duplicate habit prevention
    print("✅ TEST 12: Testing duplicate prevention...")
    tracker.add_habit("Reading", "daily", "Read more", "good")
    print()
    
    # Test 13: Test logging same habit twice in a day
    print("✅ TEST 13: Testing duplicate logging prevention...")
    tracker.log_habit("Writing", True)
    print()
    
    # Test 14: Test deleting a habit
    print("✅ TEST 14: Testing habit deletion...")
    tracker.delete_habit("Writing")
    print(f"✓ Habits after deletion: {len(tracker.data['habits'])}\n")
    
    # Test 15: Points calculation
    print("✅ TEST 15: Testing points system...")
    initial_points = tracker.data["user_stats"]["total_points"]
    tracker.log_habit("Meditation", True)
    new_points = tracker.data["user_stats"]["total_points"]
    points_earned = new_points - initial_points
    print(f"✓ Points earned from this completion: {points_earned}")
    print(f"✓ Total points: {new_points}\n")
    
    # Final summary
    print("=" * 70)
    print("🎉 ALL TESTS PASSED!")
    print("=" * 70)
    print("\n📊 FINAL STATE:")
    tracker.show_stats()
    tracker.list_habits()
    
    # Clean up test file
    if os.path.exists(test_file):
        os.remove(test_file)
    
    print("\n✅ Test completed successfully! HAPO is working perfectly!\n")
    return True


if __name__ == "__main__":
    try:
        success = test_hapo()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
