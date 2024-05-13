from fastapi import APIRouter
from database.productservice import *
from datetime import datetime

wishlists_router = APIRouter(tags=['Управление вишлист'], prefix='/wishlists')


@wishlists_router.post('/api/add_to_wishlist')
async def add_to_wishlist(user_id, product_name):
    new_wishlist = add_to_wishlist_db(user_id, product_name)
    if new_wishlist:
        return new_wishlist
    return 'Ошибка'

@wishlists_router.delete('/api/delete_from_wishlist')
async def delete_from_wishlist(wishlist_item_id):
    try:
        del_item = delete_from_wishlist_db(wishlist_item_id)
        return del_item
    except:
        return del_item

@wishlists_router.delete('/api/clear_wishlist')
async def clear_wishlist(user_id):
    try:
        del_wishlist = clear_wishlist_db(user_id)
        return del_wishlist
    except:
        return "Ошибка"

@wishlists_router.get('/api/get_wishlist')
async def get_wishlist(user_id):
    try:
        return get_wishlist_db(user_id)
    except:
        return 'Ошибка'


