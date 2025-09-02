# app.py
from flask import Flask, render_template

# Create the Flask app
app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    """Home page - shows welcome message"""
    return render_template('index.html')

# Route for habits page
@app.route('/habits')
def habits():
    """Habits page - will show all habits"""
    # For now, just some dummy data to test
    dummy_habits = [
        {'name': 'Drink Water', 'completed': True},
        {'name': 'Exercise', 'completed': False},
        {'name': 'Read Book', 'completed': True}
    ]
    return render_template('habits.html', habits=dummy_habits)

# Only run the app if this file is executed directly
if __name__ == '__main__':
    # Debug=True means the server restarts when you change code
    app.run(debug=True)
