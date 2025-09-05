# database.py
import sqlite3
from datetime import datetime, date

# File where our database will be stored
DATABASE = 'habits.db'

def get_db_connection():
    """
    Connect to our SQLite database
    Think of this like opening a file, but for databases
    """
    conn = sqlite3.connect(DATABASE)
    # This makes results come back as dictionaries instead of tuples
    # So instead of ('Drink Water', 1) we get {'name': 'Drink Water', 'id': 1}
    conn.row_factory = sqlite3.Row
    return conn

def init_database():
    """
    Create our tables if they don't exist
    Like creating empty spreadsheets with column headers
    """
    conn = get_db_connection()

    # Create habits table - stores our habit names
    conn.execute('''
        CREATE TABLE IF NOT EXISTS habits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Create completions table - tracks when we complete habits
    conn.execute('''
        CREATE TABLE IF NOT EXISTS completions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            habit_id INTEGER,
            completion_date DATE,
            completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (habit_id) REFERENCES habits (id),
            UNIQUE(habit_id, completion_date)
        )
    ''')

    conn.commit()  # Save changes
    conn.close()   # Close connection

# ========== HABIT FUNCTIONS ==========

def add_habit(name):
    """
    Add a new habit to the database
    Returns True if successful, False if habit already exists
    """
    print(f"=== add_habit called with name: '{name}' ===")  # Debug
    try:
        conn = get_db_connection()
        print("Database connection established")  # Debug
        conn.execute('INSERT INTO habits (name) VALUES (?)', (name,))
        conn.commit()
        conn.close()
        print("Habit added successfully!")  # Debug
        return True
    except sqlite3.IntegrityError as e:
        print(f"IntegrityError: {e}")  # Debug
        # This happens if habit name already exists
        return False
    except Exception as e:
        print(f"Unexpected error in add_habit: {e}")  # Debug
        return False

def get_all_habits():
    """
    Get all habits with today's completion status
    Returns a list of dictionaries like:
    [{'id': 1, 'name': 'Drink Water', 'completed': True}, ...]
    """
    conn = get_db_connection()
    today = date.today()

    # Complex SQL query - gets habits and checks if completed today
    habits = conn.execute('''
        SELECT h.id, h.name, h.created_at,
               CASE WHEN c.completion_date IS NOT NULL THEN 1 ELSE 0 END as completed
        FROM habits h
        LEFT JOIN completions c ON h.id = c.habit_id AND c.completion_date = ?
        ORDER BY h.created_at
    ''', (today,)).fetchall()

    conn.close()

    # Convert to list of dictionaries for easier use
    return [dict(habit) for habit in habits]

def delete_habit(habit_id):
    """Delete a habit and all its completions"""
    conn = get_db_connection()
    # Delete completions first (because of foreign key)
    conn.execute('DELETE FROM completions WHERE habit_id = ?', (habit_id,))
    # Then delete the habit
    conn.execute('DELETE FROM habits WHERE id = ?', (habit_id,))
    conn.commit()
    conn.close()

# ========== COMPLETION FUNCTIONS ==========

def mark_habit_complete(habit_id, completion_date=None):
    """
    Mark a habit as completed for a specific date (default: today)
    Returns True if successful, False if already completed
    """
    if completion_date is None:
        completion_date = date.today()

    try:
        conn = get_db_connection()
        conn.execute('''
            INSERT INTO completions (habit_id, completion_date)
            VALUES (?, ?)
        ''', (habit_id, completion_date))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        # Already completed for this date
        return False

def mark_habit_incomplete(habit_id, completion_date=None):
    """
    Remove completion for a habit on a specific date (default: today)
    """
    if completion_date is None:
        completion_date = date.today()

    conn = get_db_connection()
    conn.execute('''
        DELETE FROM completions
        WHERE habit_id = ? AND completion_date = ?
    ''', (habit_id, completion_date))
    conn.commit()
    conn.close()

# ========== STATS FUNCTIONS ==========

def get_habit_stats():
    """
    Get overall stats for the dashboard
    Returns dictionary with total habits, completed today, etc.
    """
    conn = get_db_connection()
    today = date.today()

    # Total habits
    total_habits = conn.execute('SELECT COUNT(*) FROM habits').fetchone()[0]

    # Completed today
    completed_today = conn.execute('''
        SELECT COUNT(*) FROM completions WHERE completion_date = ?
    ''', (today,)).fetchone()[0]

    # Best streak (this is complex, we'll simplify for now)
    # For now, just return dummy data
    best_streak = 0

    conn.close()

    return {
        'total_habits': total_habits,
        'completed_today': completed_today,
        'best_streak': best_streak
    }

# ========== INITIALIZE ==========
# This runs when we import this file
if __name__ == '__main__':
    init_database()
    print("Database initialized!")
