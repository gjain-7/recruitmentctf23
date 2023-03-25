import os
import dotenv
from db import connection_context
from db_commands import start_database
from flask import Flask, render_template, request, redirect, session

dotenv.load_dotenv(".env")
app = Flask(__name__)   
app.secret_key = os.urandom(24)

@app.route('/', methods=['GET'])
def login():
    return render_template('login.html', flag = os.environ['FLAG'])

@app.route('/', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']

    query ="SELECT * FROM users WHERE username='" + username + "' and password='" + password + "'"
    print(query)
    with connection_context() as cur:
        cur.execute(query)
        try:
            user = cur.fetchone()
            print(user)
        except:
            return render_template('login.html', error = "Better Luck Next Time!")

    if user:
        session['user_id'] = user[1]
        return redirect('/')
    else:
        return render_template('login.html', error = "Invalid credentials")
    
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect('/')

if __name__ == '__main__':
    start_database()
    app.run(port=5000, debug=True)

