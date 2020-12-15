from Wave_Hotel import app
from flask import render_template, request, redirect, url_for
from Wave_Hotel import app, login
from Wave_Hotel.models import *
from Wave_Hotel.admin import *
from flask_login import login_user
import hashlib
from Wave_Hotel import db
from Wave_Hotel import utils



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/rooms')
def show_rooms():
    kw = request.args.get("kw")
    cate_id = request.args.get("category_id")
    rooms = utils.read_rooms(cate_id=cate_id, kw=kw)

    return render_template('rooms.html', rooms= rooms)


@app.route("/rooms/<string:cate_id>")
def room_detail(cate_id):
    rooms = utils.get_price_by_cate_id(cate_id=cate_id)
    return render_template('room-details.html',
                           rooms=rooms)

@app.route("/bookingRoom")
def book_rooms():
    return render_template("book-rooms.html")
# @app.route("/login-admin", methods=["post", "get"])
# def login_admin():
#     return redirect("/admin")


@app.route('/login-admin', methods=["POST", "GET"])
def login_admin():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password", "")
        password = str(hashlib.md5(password.strip().encode("utf-8")).hexdigest())
        user = User.query.filter(User.username == username.strip(),
                                 User.password == password).first()

        if user:
            login_user(user=user)

    return redirect("/admin")


@login.user_loader
def user_load(user_id):
    return User.query.get(user_id)


@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/contact")
def contactWave():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=False)
