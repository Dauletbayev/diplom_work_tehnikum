from database.models import User
from database import get_db
from datetime import datetime

def register_user_db(first_name: str, last_name: str, email: str, phone_number: str, password: str, address_line: str,
                     country: str, city: str):
    db = next(get_db())
    checker = check_user_db(phone_number, email)
    if checker == True:
        new_user = User(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number,
                        password=password, address_line=address_line, country=country,
                        city=city, reg_day=datetime.now())
        db.add(new_user)
        db.commit()
        return new_user.id
    return checker

def check_user_db(phone_number: str, email: str):
    db = next(get_db())
    checker_phone = db.query(User).filter_by(phone_number=phone_number).first()
    checker_email = db.query(User).filter_by(email=email).first()
    if checker_phone:
        return 'Номер телефона занят'
    elif checker_email:
        return 'почта занята'
    return True

def check_user_password_db(login: str, password: str):
    db = next(get_db())
    user_by_phone = db.query(User).filter_by(phone_number=login).first()
    user_by_email = db.query(User).filter_by(email=login).first()
    if user_by_phone:
        if user_by_phone.password == password:
            return user_by_phone.id
    elif user_by_email:
        if user_by_email.password == password:
            return user_by_email.id
    return 'Неправильный пароль'

def profile_info_db(user_id: int):
    db = next(get_db())
    user_info = db.query(User).filter_by(id=user_id).first()
    if user_info:
        return user_info
    return False

def change_user_data_db(user_id: int, changeable_info: str, new_info: str):
    db = next(get_db())
    user = db.query(User).filter_by(id=user_id).first()
    if user:
        try:
            if changeable_info == 'first_name':
                user.first_name = new_info
                db.commit()
                return 'Имя успешно обновлена'
            elif changeable_info == 'last_name':
                user.last_name = new_info
                db.commit()
                return 'Фамилия успешно обновлена'
            elif changeable_info == 'email':
                user.email = new_info
                db.commit()
                return 'Почта успешно обновлена'
            elif changeable_info == 'phone_number':
                user.phone_number = new_info
                db.commit()
                return 'Номер телефона успешно обновлен'
            elif changeable_info == 'password':
                user.password = new_info
                db.commit()
                return 'Пароль успешно обновлен'
            elif changeable_info == 'country':
                user.country = new_info
                db.commit()
                return 'Страна успешно обновлена'
            elif changeable_info == 'address_line':
                user.address_line = new_info
                db.commit()
                return 'Адрес успешно обновлен'
            elif changeable_info == 'city':
                user.city = new_info
                db.commit()
                return 'Город успешно обновлен'
            db.commit()
        except:
            return False
    return False

def delete_user_db(user_id: int):
    db = next(get_db())
    user = db.query(User).filter_by(id=user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return {'status': 1, 'message': 'Юзер успешно удален'}
    else:
        return {'status': 0, 'message': 'Ошибка'}
