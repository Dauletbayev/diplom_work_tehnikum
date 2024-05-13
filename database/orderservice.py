from database.models import *
from database import get_db
from datetime import datetime

def make_order_db(user_id: int, product_name: str, product_count: int):
    db = next(get_db())
    try:
        product = db.query(Product).filter_by(name=product_name).first()
        if product:
            total_price = product.price * int(product_count)
            product.count -= int(product_count)
            db.commit()
            cart_product = Cart(
                user_id=user_id,
                product_name=product_name,
                product_count=product_count,
                total_price=total_price,
                added_date=datetime.now()
            )
            print(cart_product.user_id)
            db.add(cart_product)
            db.commit()
            return 'Заказ успешно оформлен'
        else:
            return 'Продукт не найден'
    except Exception as e:
        return f'Ошибка: {str(e)}'


def order_history_db(user_id: int):
    db = next(get_db())
    orders = db.query(Order).filter_by(user_id=user_id).all()
    return orders

def clear_order_history_db(user_id: int):
    db = next(get_db())
    db.query(Order).filter_by(user_id=user_id).delete()
    db.commit()
    return 'История заказов очищена'
