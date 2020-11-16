from sqlalchemy import Column, String, Enum, Integer
from Wave_Hotel import db
from enum import Enum as UserEnum
from flask_login import UserMixin


class SaleBase(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    def __str__(self):
        return self.name


class UserRole(UserEnum):
    USER = 1
    ADMIN = 2


class User(SaleBase, UserMixin):
    __tablename__ = 'userNhanVien'

    username = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    user_role = Column(Enum(UserRole), default=UserRole.USER)


if __name__ == '__main__':
    db.create_all()
