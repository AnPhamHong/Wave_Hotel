from sqlalchemy import Column, String, Enum, Integer, ForeignKey, Float, Text, Date
from Wave_Hotel import db, admin
from enum import Enum as UserEnum
from flask_login import UserMixin, current_user
from flask_admin import BaseView, expose
from flask_login import logout_user
from flask import redirect
from sqlalchemy.orm import relationship
from flask_admin.contrib.sqla import ModelView




class SaleBase(db.Model):
    __abstract__ = True

    def get_id(self):
        return self.id

class UserRole(UserEnum):
    USER = 1
    ADMIN = 2


class conditionRoom(UserEnum): #Tinh trang phong hien tai
    PHONGTRONG = 'PHÒNG TRỐNG'
    PHONGCOKHACH = 'PHÒNG CÓ KHÁCH'


class guestRole(UserEnum):
    NOIDIA = 'ND',
    NUOCNGOAI = 'NN'


class sexual(UserEnum):
    Nam = 1,
    Nu = 2


class CategoryRoom(SaleBase): #Loai Phong
    __tablename__ = "categoryrooms"

    id = Column(String(5), primary_key=True) #Ma loai phong
    name = Column(String(45), nullable=False) #Ten loai phong
    price = Column(Float, default=0) #Gia cua tung loai phong
    maxPerson = Column(Integer, default=0) #So nguoi toi da cua phong
    description = Column(String(255), nullable=True)
    rooms = relationship('Room', backref='CategoryRoom', lazy=True)

    def __str__(self):
        return self.name



class Room(SaleBase): #Phong
    __tablename__ = "rooms"

    id = Column(String(5), primary_key=True) #Ma Phong
    name = Column(String(45), nullable=False)
    conditionRoom = Column(Enum(conditionRoom), default=conditionRoom.PHONGTRONG) #Tinh trang phong hien tai
    image = Column(String(255)) #Hinh anh phong
    roomDetails = relationship('RoomDetails', backref='Room', lazy=True)
    categoryRoom_id = Column(String(5),
                    ForeignKey(CategoryRoom.id), nullable=False)

    def __str__(self):
        return self.name


class CategoryGuests(SaleBase): #Loai Khach
    __tablename__ = "categoryguests"

    id = Column(String(5), primary_key=True)
    name = Column(Enum(guestRole), default=guestRole.NOIDIA) #Ten loai khach
    coefficient = Column(Float, nullable=False) #he so'
    note = Column(String(50), nullable=False)
    roomDetails_id = relationship('RoomDetails', backref='CategoryGuests', lazy=True)









class Surcharge(SaleBase): #Bang phu thu
    __tablename__ = "surcharge"
    id = Column(Integer, primary_key=True, autoincrement=True)
    surcharge_rate = Column(Float, nullable=False)  #Ti Le Phu Thu: Khach thu 3 nhan 0,25, khach nuoc ngoai nhan 1,5
    surcharge_amount = Column(Integer, nullable=False)  #So luong nguoi phu thu
    roomDetails = relationship('RoomDetails', backref="Surcharge", lazy=True)

    def __str__(self):
       return "Khách hàng thứ " + self.surcharge_amount.__str__() + " ~  " + self.surcharge_rate.__str__() + " %" + " của Wave"


class RoomDetails(SaleBase): #Phieu Thue Phong
    __tablename__ = "roomdetails"

    id = Column(String(10), primary_key=True)
    nameKH = Column(String(100), nullable=False)
    CMND = Column(String(20), primary_key=True)
    phone = Column(String(11), nullable=False)
    checkInTime = Column(Date,primary_key=True, nullable=False)
    checkOutTime = Column(Date, nullable=False)
    numberGuests = Column(Integer, nullable=False)
    GuestNN = Column(Integer, default=0)
    roomID = Column(String(5), ForeignKey(Room.id), nullable=False)
    surcharge_id = Column(Integer, ForeignKey(Surcharge.id), nullable=False)
    typeGuest_id = Column(String(5), ForeignKey(CategoryGuests.id), nullable=False)
    bill = relationship('Bill', backref='RoomDetails', lazy=True)


class User(SaleBase, UserMixin): #Nhan Vien
    __tablename__ = 'userNhanVien'

    id = Column(Integer,primary_key=True, autoincrement=True )
    username = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    user_role = Column(Enum(UserRole), default=UserRole.USER) #Phan quyen quan tri
    nameNV = Column(String(100), nullable=False)
    post = Column(String(30), nullable=False)
    phone = Column(String(11))
    join_date = Column(Date, nullable=False)
    sex = Column(Enum(sexual), nullable=False)
    bill = relationship('Bill', backref='User', lazy=True)

    def __str__(self):
        return self.nameNV

class Bill(SaleBase): #Hoa Don
    __tablename__ = "bill"

    id = Column(String(10), primary_key=True)
    datePay = Column(Date, nullable=False) #ngay thanh toan
    totalDay = Column(Integer, nullable=False) #tong so ngay thanh toan
    priceDay = Column(Float, nullable=False) #gia moi ngay
    totalCost = Column(Float, nullable=False) #Thanh Tien
    roomdetailsID = Column(String(10), ForeignKey(RoomDetails.id), nullable=False)
    employeeID = Column(Integer, ForeignKey(User.id), nullable=False)


class ChangeTheRules(SaleBase): #Thay Doi Quy Dinh
    __tablename__ = "change_the_rules"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name_change = Column(String(50), nullable=False)
    contents = Column(String(300), nullable=False)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)




if __name__ == '__main__':
    db.create_all()
