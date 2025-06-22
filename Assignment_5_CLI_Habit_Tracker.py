# habits.py
import json
from datetime import datetime

class PersistenceError(Exception):
    """Raised when saving/loading habits fails."""
    pass

class Habit:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.__history = []

    def mark_done(self, date: str):
        if date not in self.__history:
            self.__history.append(date)
            self.__history.sort()

    def streak(self) -> int:
        dates = sorted([datetime.strptime(d, "%Y-%m-%d") for d in self.__history])
        streak = 0
        for i in range(len(dates) - 1, -1, -1):
            if i == len(dates) - 1:
                diff = (datetime.today() - dates[i]).days
            else:
                diff = (dates[i + 1] - dates[i]).days
            if diff == 1 or (i == len(dates) - 1 and diff == 0):
                streak += 1
            else:
                break
        return streak

    def __str__(self):
        return f"{self.name}: {self.description} — Done on {len(self.__history)} days"

    def __repr__(self):
        return f"Habit(name={self.name!r}, description={self.description!r})"

    def to_dict(self):
        return {'name': self.name, 'description': self.description, 'history': self.__history}

    @staticmethod
    def from_dict(data):
        h = Habit(data['name'], data['description'])
        h.__history = data['history']
        return h

class HabitTracker:
    DATE_FORMAT = "%Y-%m-%d"

    def __init__(self):
        self.habits = {}

    def add_habit(self, name: str, desc: str):
        self.habits[name] = Habit(name, desc)

    def remove_habit(self, name: str):
        self.habits.pop(name, None)

    def mark_done(self, name: str, date: str = None):
        if not date:
            date = datetime.today().strftime(self.DATE_FORMAT)
        self.habits[name].mark_done(date)

    def list_habits(self):
        return list(self.habits.values())

    def report(self):
        return {name: habit.streak() for name, habit in self.habits.items()}

    def save(self, filename: str):
        try:
            with open(filename, 'w') as f:
                json.dump({name: habit.to_dict() for name, habit in self.habits.items()}, f)
        except OSError as e:
            raise PersistenceError("Failed to save habits") from e

    def load(self, filename: str):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.habits = {name: Habit.from_dict(info) for name, info in data.items()}
        except FileNotFoundError:
            self.habits = {}
        except json.JSONDecodeError:
            raise PersistenceError("Invalid JSON in habits file")

    def __add__(self, other):
        new_tracker = HabitTracker()
        new_tracker.habits = {**self.habits, **other.habits}
        return new_tracker

# Optional duck typing utility
def summarize(obj):
    try:
        print(f"{obj.name}: Current streak is {obj.streak()} days")
    except AttributeError:
        print("Object missing required attributes.")
