from fastapi import APIRouter
from database.cartservice import *

carts_router = APIRouter(tags=['Управление корзиной'], prefix='/carts')

@carts_router.post('/api/add_to_cart')
async def add_to_cart(user_id, product_name, product_count):
    new_cart = add_to_cart_db(user_id=user_id, product_name=product_name,
                              product_count=product_count)
    if new_cart:
        return new_cart
    return 'Ошибка'

@carts_router.delete('/api/delete_cart')
async def delete_cart(user_id):
    try:
        del_cart = delete_all_products_from_cart_db(user_id)
        return del_cart
    except:
        return 'Ошибка при удалении'

@carts_router.delete('/api/delete_exact_pr')
async def delete_exact_pr(user_id, product_name):
    try:
        del_pr = delete_exact_product_from_cart_db(user_id, product_name)
        return del_pr
    except:
        return del_pr

@carts_router.get('/api/get_cart')
async def get_cart(user_id):
    user_cart_items = get_cart_db(user_id)
    if not user_cart_items:
        return 'Корзина пуста'
    return 'Ошибка'

