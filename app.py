from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Predefined riddle answers
answers = {
    'level1': 'Answer1',
    'level2': 'Answer2',
    'level3': 'Answer3'
}

@app.route('/')
def index():
    session.clear()  # Clear session for a fresh start
    return redirect(url_for('level1'))

# Level 1 Route
@app.route('/level1', methods=['GET', 'POST'])
def level1():
    if request.method == 'POST':
        answer = request.form.get('answer')
        if answer == answers['level1']:
            session['level1'] = True
            return redirect(url_for('level2'))
        else:
            return render_template('level1.html', error="Wrong answer, try again.")
    return render_template('level1.html')

# Level 2 Route
@app.route('/level2', methods=['GET', 'POST'])
def level2():
    if not session.get('level1'):
        return redirect(url_for('level1'))
    if request.method == 'POST':
        answer = request.form.get('answer')
        if answer == answers['level2']:
            session['level2'] = True
            return redirect(url_for('level3'))
        else:
            return render_template('level2.html', error="Wrong answer, try again.")
    return render_template('level2.html')

# Level 3 Route
@app.route('/level3', methods=['GET', 'POST'])
def level3():
    if not session.get('level2'):
        return redirect(url_for('level2'))
    if request.method == 'POST':
        answer = request.form.get('answer')
        if answer == answers['level3']:
            session['completed'] = True
            return redirect(url_for('success'))
        else:
            return render_template('level3.html', error="Wrong answer, try again.")
    return render_template('level3.html')

# Success Route (after solving all riddles)
@app.route('/success')
def success():
    if not session.get('completed'):
        return redirect(url_for('level1'))
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
