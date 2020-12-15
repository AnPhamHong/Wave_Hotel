from Wave_Hotel.models import *
def read_rooms(kw=None,
                  cate_id=None, id=None,  name=None, image=None, priceRoom=None, conditionRoom=None):
    rooms = Room.query
    idR = str(id)
    cateID = str(cate_id)
    img = str(image)
    nameR = str(name)
    price = str(priceRoom)


    if cate_id:
        rooms = rooms.filter(Room.categoryRoom_id == cateID, rooms)

    if id:
        rooms = rooms.filter(Room.id == idR, rooms)

    if name:
        rooms = rooms.filter(Room.name == nameR, rooms)

    if image:
        rooms = rooms.filter(Room.image == img, rooms)

    if kw:
        rooms = rooms.filter(Room.name.contains(kw))

    if priceRoom:
        rooms = filter(lambda tt: tt.CategoryRoom.price == price, rooms)

    if conditionRoom:
        rooms = filter(lambda tt: tt.conditionRoom.value == conditionRoom, rooms)

    return rooms.all()
"""
def read_rooms(name=None, conditionRoom=None, categoryRoom_id=None, priceRoom=None):
    rooms = Room.query.all()
    cateRoom = str(categoryRoom_id)
    price = str(priceRoom)

    if name:
        rooms = filter(lambda tt: tt.name == name, rooms)
    if categoryRoom_id:
        rooms = list(filter(lambda tt: tt.CategoryRoom.name == cateRoom, rooms))
    if priceRoom:
        rooms = filter(lambda tt: tt.CategoryRoom.price == price, rooms)
    if conditionRoom:
        rooms = filter(lambda tt: tt.conditionRoom.value == conditionRoom, rooms)

    return rooms
"""





def read_categoryRoom(cateRoom_id):
    cateRoom = CategoryRoom.query
    cateRoom = cateRoom.filter(Room.categoryRoom_id == cateRoom_id)
    return cateRoom.all()


def get_price_by_cate_id(cate_id):
    return Room.query.get(cate_id)



def utilDetail(id=None, nameKH=None,
               CMND=None, phone=None, checkInTime=None,
               checkOutTime=None, numberGuests = None,
               GuestNN=None,
               roomID=None, typeGuest_id=None, surcharge_id=None):
    roomDe = RoomDetails.query.all()
    rooID = str(roomID)
    surchargeDe = str(surcharge_id)
    guestDe = str(typeGuest_id)

    if id:
        roomDe = filter(lambda tt: tt.RoomDetails.id == id, roomDe)

    if nameKH:
        roomDe = filter(lambda tt: tt.RoomDetails.nameKH == nameKH, roomDe)

    if CMND:
        roomDe = filter(lambda tt: tt.RoomDetails.CMND == CMND, roomDe)

    if phone:
        roomDe = filter(lambda tt: tt.RoomDetails.phone == phone, roomDe)

    if checkInTime:
        roomDe = filter(lambda tt: tt.RoomDetails.checkInTime == checkInTime, roomDe)

    if checkOutTime:
        roomDe = filter(lambda tt: tt.RoomDetails.checkOutTime == checkOutTime, roomDe)

    if numberGuests:
        roomDe = filter(lambda tt: tt.RoomDetails.numberGuests == numberGuests, roomDe)

    if GuestNN:
        roomDe = filter(lambda  tt: tt.RoomDetails.GuestNN == GuestNN, roomDe)

    if roomID:
        roomDe = list(filter(lambda tt: tt.Room.name == rooID, roomDe))

    if typeGuest_id:
        roomDe = list(filter(lambda  tt: tt.CategoryGuests.name == guestDe, roomDe))

    if surcharge_id:
        roomDe = list(filter(lambda tt: tt.Surcharge.id == surchargeDe, roomDe))

    return roomDe


