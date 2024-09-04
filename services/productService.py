from database import db
from models.product import Product
from sqlalchemy import select, update

def save(product_data):

    new_product = Product(name=product_data['name'], brand=product_data['brand'], category=product_data['category'], price=product_data['price'])
    db.session.add(new_product)
    db.session.commit()

    db.session.refresh(new_product)
    return new_product

def find_all():

    query = select(Product)
    all_products = db.session.execute(query).scalars().all()

    return all_products


# def find_one():

#     query = select(Product)
#     product = db.session.execute(query).scalar()

#     return product

# def update():

#     query = update(Product)



