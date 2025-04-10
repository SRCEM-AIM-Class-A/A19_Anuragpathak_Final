from flask import Flask, request, render_template
import re
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    error = None
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')

        if not name or not re.match(r'^[A-Za-z\s]+$', name):
            error = "Name must only contain letters and spaces."
        elif not age or not age.isdigit():
            error = "Valid age is required."
        else:
            return f"<h2>Hello, {name}! You are {age} years old.</h2>"

    return render_template('form.html', error=error)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Important for Docker  # Changed port