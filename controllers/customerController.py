from flask import request, jsonify
from models.schemas.customerSchema import customer_schema, customers_schema
from services import customerService
from marshmallow import ValidationError
from cache import cache


def save(): #name the controller the same as the service it recruites

    try:
        customer_data = customer_schema.load(request.json)
    
    except ValidationError as e:
        return jsonify(e.messages), 400 
    
    customer = customerService.save(customer_data)
    return customer_schema.jsonify(customer), 201 


@cache.cached(timeout=120)
def find_all():
    all_customers = customerService.find_all()

    return customers_schema.jsonify(all_customers), 200 