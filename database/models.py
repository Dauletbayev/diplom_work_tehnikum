from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, Date, Float
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, autoincrement=True, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    phone_number = Column(String, unique=True)
    password = Column(String)
    address_line = Column(String)
    country = Column(String)
    city = Column(String)
    reg_day = Column(DateTime)

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, autoincrement=True, primary_key=True)
    category_title = Column(String)
    category_date = Column(DateTime)

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    price = Column(Float)
    short_description = Column(String)
    long_description = Column(String)
    additional_info = Column(String)
    count = Column(Integer)
    category = Column(Integer, ForeignKey('categories.id'))
    size = Column(String)
    color = Column(String)
    added_date = Column(DateTime)

    category_fk = relationship(Category, lazy='subquery')

class ProductPhoto(Base):
    __tablename__ = 'product_photos'
    id = Column(Integer, autoincrement=True, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    photo_path = Column(String)
    photo_date = Column(DateTime)

    product_fk = relationship(Product, lazy='subquery')

class CategoryPhoto(Base):
    __tablename__ = 'category_photos'
    id = Column(Integer, autoincrement=True, primary_key=True)
    category_id = Column(Integer, ForeignKey('categories.id'))
    photo_path = Column(String)
    photo_date = Column(DateTime)

    category_fk = relationship(Category, lazy='subquery')

class Cart(Base):
    __tablename__ = 'carts'
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_name = Column(String)
    product_count = Column(Integer)
    total_price = Column(Float)
    added_date = Column(DateTime)

    user_fk = relationship(User, lazy='subquery')

class Wishlist(Base):
    __tablename__ = 'wishlists'
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_name = Column(String)
    product_price = Column(Float)
    add_date = Column(DateTime)

    user_fk = relationship(User, lazy='subquery')

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_name = Column(String)
    product_price = Column(Float)
    order_date = Column(DateTime)

    user_fk = relationship(User, lazy='subquery')
