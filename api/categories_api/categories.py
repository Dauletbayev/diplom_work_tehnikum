from fastapi import APIRouter
from database.productservice import *

categories_router = APIRouter(tags=['Управление категориями'], prefix='/categories')

@categories_router.post('/api/add_category')
async def add_category(category_title):
    new_category = add_category_db(category_title)
    if new_category:
        return new_category
    return 'Ошибка при создании категории'

@categories_router.delete('/api/delete_category')
async def delete_category(category_id):
    try:
        del_category = delete_category_db(category_id)
        return del_category
    except:
        return 'Ошибка'

@categories_router.put('/api/change_category')
async def change_category(category_id, new_category_title):
    change = change_category_db(category_id, new_category_title)
    if change:
        return change
    return change

@categories_router.get('/api/get_all_category')
async def get_all_category():
    all_category = get_all_category_db()
    if all_category:
        return all_category
    return 'Ошибка'

@categories_router.get('/api/get_exact_category')
async def get_exact_category(category_id):
    exact_category = get_exact_category_db(category_id)
    if exact_category:
        return exact_category
    return 'Ошибка'
