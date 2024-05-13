from fastapi import APIRouter, Request
from pydantic import BaseModel
from database.productservice import *

products_router = APIRouter(tags=['Управление продуктами'], prefix='/products')

@products_router.post('/api/add_product')
async def add_product(name, price, short_description, long_description,
                      additional_info, count, category, size, color):
    new_product = add_product_db(name=name, price=price, short_description=short_description,
                                 long_description=long_description, additional_info=additional_info,
                                 count=count, category=category, size=size, color=color, added_date=datetime.now())
    if new_product:
        return new_product
    return 'Ошибка'

@products_router.delete('/api/delete_product')
async def delete_product(product_id):
    del_product = delete_product_db(product_id)
    if del_product:
        return del_product
    return del_product

@products_router.put('/api/change_product')
async def change_product(product_id, info_to_change, new_info):
    change_product_info = change_product_db(product_id, info_to_change, new_info)
    if change_product_info:
        return change_product_info
    return change_product_info

@products_router.get('/api/get_all_products')
async def get_all_products():
    all_products = get_all_products_db()
    if all_products:
        return all_products
    return 'Ошибка'

@products_router.get('/api/get_exact_product')
async def get_exact_product(product_id):
    exact_product = get_exact_product_db(product_id)
    if exact_product:
        return exact_product
    return 'Ошибка'
