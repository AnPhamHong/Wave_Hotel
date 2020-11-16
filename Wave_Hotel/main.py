from Wave_Hotel import app
from flask import render_template, request, redirect, url_for
from Wave_Hotel import app, login
from Wave_Hotel.models import *
from flask_login import login_user
import hashlib


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=["post", "get"])
def showLogin():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password", "")
        password = str(hashlib.md5(password.strip().encode("utf-8")).hexdigest())
        user = User.query.filter(User.username == username.strip(),
                                 User.password == password.first())
        if user:
            login_user(user=user)

    return render_template('login.html')


@login.user_loader
def user_load(user_id):
    return User.query.get(user_id)


if __name__ == "__main__":
    app.run(debug=True)