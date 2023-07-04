from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Połączenie z bazą danych
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Sprawdź, czy login i hasło nie są już zajęte
        cursor.execute('SELECT * FROM users WHERE username = ? OR email = ?', (username, email))
        existing_user = cursor.fetchone()

        if existing_user:
            error_message = 'Nazwa użytkownika lub adres email są już zajęte.'
            return render_template('register.html', error_message=error_message)

        # Dodaj użytkownika do bazy danych
        cursor.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, password))
        conn.commit()

        return redirect(url_for('index'))

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
