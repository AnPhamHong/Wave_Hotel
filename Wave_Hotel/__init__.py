from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import LoginManager
#khi import mot goi, file init se duoc thu thi va dinh nghia
#cac chuc nang ma mot goi cho phep cac ung dung khac co the su dung

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:An1851010010@localhost/wavehoteldb?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app=app)
admin = Admin(app=app, name="", template_mode="bootstrap4")

login = LoginManager(app=app)


