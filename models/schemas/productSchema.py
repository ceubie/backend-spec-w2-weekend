from . import ma
from marshmallow import fields

class ProductSchema(ma.Schema):
    id = fields.Integer(required=False)
    name = fields.String(required=True)
    brand = fields.String(required=True)
    category = fields.String(required=True)
    price = fields.String(required=True)

    class Meta:
        fields = ("id", "name", "brand", "category", "price")

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)