from flask import Flask
from flask import request

app = Flask(__name__)
@app .route('/')
@app.route('/')
def index():
    resp = make_response(render_template('home.html'))
    resp.set_cookie('username', 'the username')
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0')



