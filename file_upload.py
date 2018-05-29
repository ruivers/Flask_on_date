from flask import Flask
from flask import request
from flask import render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method =='GET':
        return  render_template('upload.html')
    else:
        f = request.files['the_file']
        f.save('static/uploads/' + secure_filename(f.filename))


if __name__ == '__main__':
    app.run(host='0.0.0.0')