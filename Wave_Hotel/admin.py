from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
from markupsafe import Markup
from wtforms import validators
from flask_login import current_user, logout_user
from urllib import request

from Wave_Hotel import admin, db, utils
from flask import redirect, request, session
from datetime import date, datetime
from Wave_Hotel.models import *
import hashlib

class AuthenticatedView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

class UserView(AuthenticatedView):
    column_display_pk = True
    can_view_details = True
    column_labels = dict(id="Mã người dùng", nameNV="Tên người dùng",
                         username ="Tên đăng nhập", password="Mật khẩu",
                               user_role="Vai trò người dùng", post="Chức vụ",
                         phone="SĐT", join_date="Ngày gia nhập", sex="Giới tính")
    form_columns = ("nameNV", "username", "password", "user_role", "post", "phone", "join_date", "sex")
    def on_model_change(self, form, User, is_created=False):
        User.password = hashlib.md5(User.password.encode('utf-8')).hexdigest()

    form_widget_args = {
        'password':{
            'type':'password'
        }
    }

    def is_accessible(self):
        return current_user.is_authenticated and (current_user.user_role == UserRole.ADMIN)

class CategoryOfRoomView(ModelView):
   column_display_pk = True
   can_view_details = True
   column_labels = dict(id="Mã loại phòng", name="Tên loại phòng",
                        price="Giá tiền", maxPerson="Số khách tối đa",
                        description="Mô tả chi tiết")

   form_columns = ("name", "price", "maxPerson", "description")
   form_excluded_columns = ['rooms']
   def is_accessible(self):
       return current_user.is_authenticated and (current_user.user_role == UserRole.ADMIN)

class RoomView(ModelView):
    column_display_pk = True
    can_view_details = True
    column_labels = dict(id="Mã phòng", name="Tên phòng",
                         conditionRoom="Tình trạng phòng",
                         image ="Hình ảnh phòng",
                         categoryRoom_id ="Loại phòng")

    form_columns = ("name", "conditionRoom", "image", "categoryRoom_id")
    form_excluded_columns = ['roomDetails']

    def _room_condition_formatter(view, context, model, name):
        if model.conditionRoom:
            condition = model.conditionRoom.PHONGTRONG
            return condition
        else:
            return None

    def is_accessible(self):
        return current_user.is_authenticated and (current_user.user_role == UserRole.ADMIN)



class SurchargeView(ModelView):
    column_display_pk = True
    can_view_details = True
    column_list = ['surcharge_amount', 'surcharge_rate']
    column_labels = { 'surcharge_amount': 'Số lượng người phụ thu',
                      'surcharge_rate': 'Tỷ lệ phụ thu'
    }
    form_excluded_columns = ['roomDetails']

    def is_accessible(self):
        return current_user.is_authenticated and (current_user.user_role == UserRole.ADMIN)


class CategoryGuestView(ModelView):
    column_display_pk = True
    can_view_details = True
    form_columns = ('name', 'coefficient', 'note')
    column_labels = {"id": "Mã loại khách",
                     "name": "Loại khách",
                     "coefficient": "Hệ số loại khách",
                     "note": "Ghi chú"}
    form_excluded_columns = ['roomDetails_id']
    def is_accessible(self):
        return current_user.is_authenticated and (current_user.user_role == UserRole.ADMIN)


class RoomDetailView(ModelView):
    column_display_pk = True
    can_view_details = True
    column_labels = {
        "id": "Mã phiếu thuê",
        "nameKH": "Tên KH",
        "CMND": "CMND",
        "phone": "Số điện thoại",
        "checkInTime": "Ngày Check-in",
        "checkOutTime": "Ngày Check-out",
        "numberGuests": "Số lượng khách",
        "GuestNN": "Số khách nước ngoại",
        "roomID": "Phòng",
        "surchange_id" : "Sô phụ thu",
        "typeGuest_id" : "Loại khách"
    }

    form_columns = ('id','nameKH','CMND','phone','checkInTime','checkOutTime','numberGuests',
                    'GuestNN','Room','Surcharge','CategoryGuests')
    form_excluded_columns = ['bill']

    def on_model_change(self, form, RoomDetails, is_created):
        room = Room.query.get(form.Room.data.id)
        if form.Room.data.conditionRoom == conditionRoom.PHONGCOKHACH:
            raise validators.ValidationError("Phòng Đã Đặt")
        else:
            room.conditionRoom = conditionRoom.PHONGCOKHACH
            db.session.add(room)
            db.session.commit()

    def is_accessible(self):
        return current_user.is_authenticated and (current_user.user_role == UserRole.ADMIN or UserRole.USER)

class BillView(ModelView):
    column_display_pk = True
    can_view_details = True
    can_export = True
    column_labels = {"id": "Mã hóa đơn",
                     "datePay": "Ngày thanh toán",
                     "totalDay": "Tổng cộng ngày",
                     "priceDay": "Giá/ 1 đêm",
                     "totalCost": "Thành tiền",
                     "roomdetailsID": "Mã phiếu thuê",
                     "employeeID": "Nhân viên"
                     }
    form_columns = ('id','datePay', 'totalDay', 'priceDay', 'totalCost', 'RoomDetails', 'User')
    form_excluded_columns = ['totalDay', 'priceDay', 'totalCost']

    def on_model_change(self, form, Bill, is_created):
        room = Room.query.get(form.RoomDetails.data.roomID)
        if form.RoomDetails.data.Room.conditionRoom == conditionRoom.isOccupied:
            room.conditionRoom = conditionRoom.isVacant
            db.session.add(room)
            db.session.commit()

    def is_accessible(self):
        return current_user.is_authenticated and (current_user.user_role == UserRole.ADMIN)

        # if (datetime.now() - form.RoomDetails.date.checkInTime).days == 0:
        #     payment = (datetime.now().hour - form.RoomDetails.data.checkInTime.hour)
        # else:
        #     payment = (datetime.now() - form.RoomDetails.data.checkInTime).days * 24
        #     price =



class ChangeRuleView(ModelView):
    column_display_pk = True
    column_display_pk = True
    can_create = True
    can_set_page_size = True
    can_view_details = True
    column_labels = { "id" : "Mã quy định",
                      "name_change": "Quy định",
                      "contents": "Nội dung",
                      "user_id" : "Người cập nhật"}

    def is_accessible(self):
        return current_user.is_authenticated and (current_user.user_role == UserRole.ADMIN)



class AboutUsView(BaseView):
    @expose("/")
    def index(self):
        return self.render("admin/aboutus.html")

    def is_accessible(self):
        return current_user.is_authenticated

class LogoutView(BaseView):
    @expose("/")
    def index(self):
        logout_user()

        return redirect("/admin")

    def is_accessible(self):
        return current_user.is_authenticated

class RoomViewUser(BaseView):
    @expose("/")
    def index(self):
        r_id = request.args.get("id")
        r_name= request.args.get("name")
        r_conditionRoom = request.args.get("conditionRoom")
        r_image = request.args.get("image")
        r_categoryRoom = request.args.get("categoryRoom_id")
        return self.render("admin/roomView.html",
                           rooms = utils.read_rooms(id=r_id, name=r_name, conditionRoom=r_conditionRoom,
                                                    image=r_image, cate_id=r_categoryRoom))


"""
class Rooms(BaseView):
    @expose("/")
    def index(self):
        return self.render("admin/rooms.html")

    def is_accessible(self):
        return current_user.is_authenticated

class Services(BaseView):
    @expose("/")
    def index(self):
        return self.render("admin/services.html")

    def is_accessible(self):
        return current_user.is_authenticated


class Searchs(BaseView):
    @expose("/")
    def index(self):
        return self.render("#")

    def is_accessible(self):
        return current_user.is_authenticated


class Bills(BaseView):
    @expose("/")
    def index(self):
        return self.render("#")

    def is_accessible(self):
        return current_user.is_authenticated


class Reports(BaseView):
    @expose("/")
    def index(self):
        return self.render("#")

    def is_accessible(self):
        return current_user.is_authenticated



"""


admin.add_view(CategoryOfRoomView(CategoryRoom,db.session,name="Loại Phòng"))
admin.add_view(RoomView(Room, db.session, name="Phòng"))
admin.add_view(CategoryGuestView(CategoryGuests, db.session, name="Loại Khách"))
admin.add_view(SurchargeView(Surcharge, db.session, name="Phụ Thu"))
admin.add_view(RoomDetailView(RoomDetails, db.session, name="Phiếu Thuê"))
admin.add_view(BillView(Bill, db.session, name="Hóa Đơn"))
admin.add_view(UserView(User, db.session, name="Nhân Viên"))
admin.add_view(ChangeRuleView(ChangeTheRules, db.session, name="Thay Đổi Quy Định"))
admin.add_view(RoomViewUser(name="Xem Phòng"))
admin.add_view(AboutUsView(name="Liên Hệ"))
admin.add_view(LogoutView(name="Đăng Xuất"))