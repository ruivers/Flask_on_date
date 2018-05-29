from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET'])
def signin_form():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def signin():
    user     = request.form['username']
    password = request.form['password']
    if user == 'admin' and  password == 'password':
        return render_template('index.html', request.form['username'])
    return render_template('error.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')