from flask import Flask, request, render_template_string

app = Flask(__name__)

# Simple HTML with form - no separate files
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Test Form</title>
</head>
<body>
    <h1>Test Form</h1>

    {% if message %}
        <p style="color: green; font-weight: bold;">{{ message }}</p>
    {% endif %}

    <form action="/test_form" method="POST">
        <input type="text" name="test_input" placeholder="Type something" required>
        <button type="submit">Submit</button>
    </form>

    <h2>Submitted Data:</h2>
    <ul>
    {% for item in data %}
        <li>{{ item }}</li>
    {% endfor %}
    </ul>
</body>
</html>
'''

# Store data in memory (simple list)
submitted_data = []

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, data=submitted_data)

@app.route('/test_form', methods=['POST'])
def test_form():
    print("=== FORM SUBMITTED! ===")
    user_input = request.form['test_input']
    print(f"Received: {user_input}")

    submitted_data.append(user_input)
    print(f"Data list now has: {len(submitted_data)} items")

    return render_template_string(HTML_TEMPLATE,
                                data=submitted_data,
                                message=f"Added: {user_input}")

if __name__ == '__main__':
    app.run(debug=True)
