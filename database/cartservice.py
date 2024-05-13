from database.models import Cart, Product
from database import get_db
from datetime import datetime

def add_to_cart_db(user_id: int, product_name: str, product_count: int, total_price: float):
    db = next(get_db())
    # Создаем запись в таблице корзины
    cart_item = Cart(
        user_id=user_id,
        product_name=product_name,
        product_count=product_count,
        total_price=total_price,
        added_date=datetime.now()
    )
    db.add(cart_item)
    db.commit()
    return 'Продукт успешно добавлен в корзину'

def delete_all_products_from_cart_db(user_id: int):
    db = next(get_db())
    cart_items = db.query(Cart).filter_by(Cart.user_id == user_id).all()
    for cart_item in cart_items:
        db.delete(cart_item)
    db.commit()
    return 'Корзина успешно очищена'

def delete_exact_product_from_cart_db(user_id: int, product_name: str):
    db = next(get_db())
    cart_item_to_delete = db.query(Cart).filter_by(user_id=user_id, product_name=product_name).first()
    if cart_item_to_delete:
        db.delete(cart_item_to_delete)
        db.commit()
        return 'Продукт успешно удален из корзины'
    else:
        return 'Продукт не найден в корзине'

def get_cart_db(user_id: int):
    db = next(get_db())
    cart_items = db.query(Cart).filter_by(user_id=user_id).all()
    return cart_items

def send_cart_to_admin_db():
    pass

