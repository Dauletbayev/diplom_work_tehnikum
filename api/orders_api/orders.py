from fastapi import APIRouter
from database.orderservice import *

orders_router = APIRouter(tags=['Управление заказами'], prefix='/orders')

@orders_router.post('/api/make_order')
async def make_order(user_id, product_name, product_count):
    new_order = make_order_db(user_id, product_name, product_count)
    if new_order:
        return new_order
    return new_order

@orders_router.delete('/api/clear_order_history')
async def clear_order_history(user_id):
    try:
        clear_order_history_db(user_id)
    except:
        return 'Ошибка'

@orders_router.get('/api/order_history')
async def order_history(user_id):
    try:
        return order_history_db(user_id)
    except:
        return 'Ошибка'




