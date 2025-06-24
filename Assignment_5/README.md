## Habit Tracker - README

### Overview

This project provides a simple yet powerful **Habit Tracker** in Python. It allows you to create, track, and manage daily habits, mark them as completed, calculate streaks, and persist your progress to disk using JSON files. The code is modular and extensible, making it suitable for both personal use and as a foundation for more advanced habit-tracking applications.

---

### Features

- **Create and Remove Habits:** Add new habits with descriptions and remove them when no longer needed.
- **Mark Habits as Done:** Record the completion of a habit for any date.
- **Streak Calculation:** Automatically calculate your current streak for each habit.
- **Persistence:** Save and load your habit data to/from a JSON file.
- **Reporting:** Get a summary of all habits and their current streaks.
- **Operator Overloading:** Combine two `HabitTracker` instances using the `+` operator.
- **Duck Typing Utility:** `summarize(obj)` prints a habit's name and streak if compatible.

---

### Usage

#### 1. Creating a HabitTracker

```python
from habits import HabitTracker

tracker = HabitTracker()
tracker.add_habit("Exercise", "30 minutes of physical activity")
tracker.add_habit("Read", "Read at least 10 pages of a book")
```

#### 2. Marking Habits as Done

```python
tracker.mark_done("Exercise")  # marks today as done
tracker.mark_done("Read", "2025-06-23")  # marks a specific date
```

#### 3. Viewing and Reporting

```python
for habit in tracker.list_habits():
    print(habit)

print(tracker.report())  # {'Exercise': 1, 'Read': 1}
```

#### 4. Saving and Loading

```python
tracker.save("my_habits.json")
tracker.load("my_habits.json")
```

#### 5. Combining Trackers

```python
tracker2 = HabitTracker()
tracker2.add_habit("Meditate", "10 minutes mindfulness")
combined = tracker + tracker2
```

#### 6. Using the Summarize Utility

```python
from habits import summarize
summarize(tracker.habits["Exercise"])
```

---

### Classes

#### `Habit`
- **Attributes:** `name`, `description`, (private) `__history`
- **Methods:**  
  - `mark_done(date)`: Mark habit as done on a date  
  - `streak()`: Return current streak  
  - `to_dict()`, `from_dict()`: For JSON serialization  
  - `__str__()`, `__repr__()`

#### `HabitTracker`
- **Attributes:** `habits` (dict of habits)
- **Methods:**  
  - `add_habit(name, desc)`, `remove_habit(name)`  
  - `mark_done(name, date=None)`  
  - `list_habits()`  
  - `report()`  
  - `save(filename)`, `load(filename)`  
  - `__add__(other)`: Merge two trackers

#### `PersistenceError`
- Custom exception for save/load errors

---

### Error Handling

- **PersistenceError:** Raised if saving or loading fails.
- **Graceful Handling:** If the JSON file is missing, a new tracker starts empty.

---

### Example

```python
tracker = HabitTracker()
tracker.add_habit("Drink Water", "Drink 8 glasses daily")
tracker.mark_done("Drink Water")
print(tracker.report())  # {'Drink Water': 1}
tracker.save("habits.json")
```

---

### Requirements

- Python 3.7+
- Standard library only (no external dependencies)

---

### Extending

- Add reminders, notifications, or GUI
- Integrate with calendar APIs
- Visualize streaks with charts

---

**Happy habit tracking!**  
Feel free to fork, modify, and contribute.
