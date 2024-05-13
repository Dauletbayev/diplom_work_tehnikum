from fastapi import FastAPI

from database import Base, engine
from api.users_api.users import users_router
from api.products_api.products import products_router
from api.categories_api.categories import categories_router
from api.carts_api.carts import carts_router
from api.wishlists_api.wishlists import wishlists_router
from api.orders_api.orders import orders_router

Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/admin', title='MultiShop')

app.include_router(users_router)
app.include_router(categories_router)
app.include_router(products_router)
app.include_router(carts_router)
app.include_router(wishlists_router)
app.include_router(orders_router)
