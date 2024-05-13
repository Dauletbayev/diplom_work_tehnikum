from database.models import Category, CategoryPhoto, Product, ProductPhoto, Wishlist
from database import get_db
from datetime import datetime

def add_category_db(category_title: str):
    db = next(get_db())
    new_category = Category(category_title=category_title, category_date=datetime.now())
    db.add(new_category)
    db.commit()
    return {'status': 1, 'message': 'Категория успешно добавлена'}

def delete_category_db(category_id: int):
    db = next(get_db())
    category_to_delete = db.query(Category).filter_by(id=category_id).first()
    if category_to_delete:
        db.delete(category_to_delete)
        db.commit()
        return {'status': 1, 'message': 'Категория успешно удалена'}
    return {'status': 0, 'message': 'Ошибка при удалении'}

def change_category_db(category_id: int, new_category_title: str):
    db = next(get_db())
    category_to_change = db.query(Category).filter_by(id=category_id).first()
    if category_to_change:
        category_to_change.category_title = new_category_title
        category_to_change.category_date = datetime.now()
        db.commit()
        return {'status': 1, 'message': 'Категория успешно изменена'}
    return {'status': 0, 'message': 'Ошибка при удалении'}

def get_all_category_db():
    db = next(get_db())
    all_categories = db.query(Category).all()
    return all_categories

def get_exact_category_db(category_id: int):
    db = next(get_db())
    exact_category = db.query(Category).filter_by(id=category_id).first()
    return exact_category

def add_product_db(name: str, price: float, short_description: str, long_description: str,
                   additional_info: str, count: int, category: str, size: str, color: str, added_date=datetime.now()):
    db = next(get_db())
    new_product = Product(name=name, price=price, short_description=short_description,
                          long_description=long_description, additional_info=additional_info, count=count,
                          category=category, size=size, color=color, added_date=datetime.now())
    db.add(new_product)
    db.commit()
    return {'status': 1, 'message': 'Продукт успешно добавлен'}

def delete_product_db(product_id: int):
    db = next(get_db())
    product_to_delete = db.query(Product).filter_by(id=product_id).first()
    if product_to_delete:
        db.delete(product_to_delete)
        db.commit()
        return {'status': 1, 'message': 'Продукт успешно удалена'}
    return {'status': 0, 'message': 'Ошибка при удалении продукта'}

def change_product_db(product_id: int, info_to_change: str, new_info: str):
    db = next(get_db())
    product_to_change = db.query(Product).filter_by(id=product_id).first()
    if product_to_change:
        if info_to_change == 'name':
            product_to_change.name = new_info
            return 'Имя успешно изменена'
        elif info_to_change == 'price':
            product_to_change.price = new_info
            return 'Цена успешно изменена'
        elif info_to_change == 'short_description':
            product_to_change.short_description = new_info
            return 'Короткое описани успешно изменена'
        elif info_to_change == 'long_description':
            product_to_change.long_description = new_info
            return 'Длинное описание успешно изменена'
        elif info_to_change == 'additional_info':
            product_to_change.additional_info = new_info
            return 'Дополнительная информация успешно изменена'
        elif info_to_change == 'count':
            product_to_change.count = new_info
            return 'Количество продукта успешно обновлена'
        elif info_to_change == 'category':
            product_to_change.category = new_info
            return 'Категория успешно изменена'
        elif info_to_change == 'size':
            product_to_change.size = new_info
            return 'Размер успешно изменена'
        elif info_to_change == 'color':
            product_to_change.color = new_info
            return 'Цвет продукта успешно обновлена'
        return 'Ошибка при изменении продукта'
    return 'Продукт не найден'

def get_all_products_db():
    db = next(get_db())
    all_products = db.query(Product).all()
    return all_products

def get_exact_product_db(product_id: int):
    db = next(get_db())
    exact_product = db.query(Product).filter_by(id=product_id).first()
    return exact_product

def search_product_db():
    pass

def add_to_wishlist_db(user_id: int, product_name: str):
    db = next(get_db())
    product = db.query(Product).filter_by(name=product_name).first()
    if product:
        wishlist_item = Wishlist(
            user_id=user_id,
            product_name=product_name,
            product_price=product.price,
            add_date=datetime.now()
        )
        db.add(wishlist_item)
        db.commit()
        return 'Продукт успешно добавлен в "Wishlist"'
    else:
        return 'Продукт не найден в базе данных'


def delete_from_wishlist_db(wishlist_item_id: int):
    db = next(get_db())
    wishlist_item = db.query(Wishlist).filter_by(id=wishlist_item_id).first()
    if wishlist_item:
        db.delete(wishlist_item)
        db.commit()
        return 'Продукт успешно удален'
    return 'Ошибка при удалении'

def clear_wishlist_db(user_id: int):
    db = next(get_db())
    db.query(Wishlist).filter_by(user_id=user_id).delete()
    db.commit()
    return 'Вишлист успешно очищен'

def get_wishlist_db(user_id: int):
    db = next(get_db())
    wishlist_items = db.query(Wishlist).filter_by(user_id=user_id).all()
    return wishlist_items

