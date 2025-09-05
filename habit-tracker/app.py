# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime, date

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-later'

DATABASE = 'habits.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_database():
    conn = get_db_connection()

    conn.execute('''
        CREATE TABLE IF NOT EXISTS habits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

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

    conn.commit()
    conn.close()
    print("Database initialized!")

def get_all_habits():
    conn = get_db_connection()
    today = date.today()

    habits = conn.execute('''
        SELECT h.id, h.name, h.created_at,
               CASE WHEN c.completion_date IS NOT NULL THEN 1 ELSE 0 END as completed
        FROM habits h
        LEFT JOIN completions c ON h.id = c.habit_id AND c.completion_date = ?
        ORDER BY h.created_at
    ''', (today,)).fetchall()

    conn.close()
    return [dict(habit) for habit in habits]

def add_habit(name):
    try:
        conn = get_db_connection()
        conn.execute('INSERT INTO habits (name) VALUES (?)', (name,))
        conn.commit()
        conn.close()
        print(f"Successfully added habit: {name}")
        return True
    except sqlite3.IntegrityError:
        print(f"Habit already exists: {name}")
        return False
    except Exception as e:
        print(f"Error adding habit: {e}")
        return False

def get_habit_stats():
    conn = get_db_connection()
    today = date.today()

    total_habits = conn.execute('SELECT COUNT(*) FROM habits').fetchone()[0]
    completed_today = conn.execute('''
        SELECT COUNT(*) FROM completions WHERE completion_date = ?
    ''', (today,)).fetchone()[0]

    conn.close()

    return {
        'total_habits': total_habits,
        'completed_today': completed_today,
        'best_streak': 0
    }

def mark_habit_complete(habit_id):
    try:
        conn = get_db_connection()
        today = date.today()
        conn.execute('''
            INSERT INTO completions (habit_id, completion_date)
            VALUES (?, ?)
        ''', (habit_id, today))
        conn.commit()
        conn.close()
        print(f"Marked habit {habit_id} as complete")
        return True
    except sqlite3.IntegrityError:
        print(f"Habit {habit_id} already completed today")
        return False

def mark_habit_incomplete(habit_id):
    conn = get_db_connection()
    today = date.today()
    conn.execute('''
        DELETE FROM completions
        WHERE habit_id = ? AND completion_date = ?
    ''', (habit_id, today))
    conn.commit()
    conn.close()
    print(f"Marked habit {habit_id} as incomplete")

# Initialize database when app starts
init_database()

@app.route('/')
def index():
    stats = get_habit_stats()
    print(f"Stats: {stats}")
    return render_template('index.html', stats=stats)

@app.route('/habits')
def habits():
    habits_list = get_all_habits()
    print(f"Found {len(habits_list)} habits")
    return render_template('habits.html', habits=habits_list)

@app.route('/add_habit', methods=['POST'])
def add_new_habit():
    print("=== ADD HABIT ROUTE CALLED ===")
    habit_name = request.form['habit_name'].strip()
    print(f"Received habit name: '{habit_name}'")

    if not habit_name:
        flash('Please enter a habit name!', 'error')
        return redirect(url_for('habits'))

    if add_habit(habit_name):
        flash(f'Added habit: {habit_name}', 'success')
    else:
        flash('This habit already exists!', 'error')

    return redirect(url_for('habits'))

@app.route('/toggle_habit/<int:habit_id>')
def toggle_habit(habit_id):
    print(f"=== TOGGLE HABIT {habit_id} ===")
    habits_list = get_all_habits_with_streaks()  # Updated function call

    current_habit = None
    for habit in habits_list:
        if habit['id'] == habit_id:
            current_habit = habit
            break

    if current_habit is None:
        flash('Habit not found!', 'error')
        return redirect(url_for('habits'))

    if current_habit['completed']:
        mark_habit_incomplete(habit_id)
        flash(f'Marked "{current_habit["name"]}" as incomplete', 'info')
    else:
        mark_habit_complete(habit_id)
        flash(f'Great job! Completed "{current_habit["name"]}"', 'success')

    return redirect(url_for('habits'))

if __name__ == '__main__':
    app.run(debug=True)
