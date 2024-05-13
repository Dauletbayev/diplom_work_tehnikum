from fastapi import APIRouter, Request
from pydantic import BaseModel
from database.userservice import *
import re

class UserRegistration(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    password: str
    address_line: str
    country: str
    city: str

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Za-z]{2,})+')

def mail_checker(email):
    if re.fullmatch(regex, email):
        return True
    return False

users_router = APIRouter(tags=['Управление пользователями'], prefix='/users')

@users_router.post('/api/register')
async def register_user(user_data: UserRegistration):
    mail_validation = mail_checker(user_data.email)
    if mail_validation:
        try:
            reg_user = register_user_db(**user_data.dict())
            return {'status': 1, 'message': reg_user}
        except Exception as e:
            return {'status': 0, 'message': str(e)}
    return {'status': 0, 'message': 'Invalid email or phone'}

@users_router.post('/api/user')
async def get_user(user_id: int):
    exact_user = profile_info_db(user_id)
    if exact_user:
        return exact_user
    return {'status': 0, 'message': 'Пользователь не найден'}

@users_router.post('api/login')
async def login_user(login: str, password: str):
    checking = check_user_password_db(login, password)
    if checking:
        return checking
    return checking

@users_router.put('/api/change_profile')
async def change_user_profile(user_id : int, changeable_info: str, new_info: str):
    data = change_user_data_db(user_id, changeable_info, new_info)
    if data:
        return data
    return data

@users_router.delete('/api/delete_user')
async def delete_user(user_id):
    try:
        del_user = delete_user_db(user_id)
        return del_user
    except:
        return del_user
