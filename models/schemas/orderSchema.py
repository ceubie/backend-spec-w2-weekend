from . import ma
from marshmallow import fields

class OrderSchema(ma.Schema):
    id = fields.Integer(required=False)
    date = fields.Date(required=False) 
    customer_id = fields.Integer(required=True)
    products = fields.Nested("ProductSchema", many=True)

    class Meta:
        fields = ('id', 'date', 'customer_id', 'product_ids', 'products') 

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)