from flask import Blueprint, request,jsonify
from .models import Product,product_schema,products_schema
from . import db

views = Blueprint('views', __name__)

#create
@views.route('/product',methods=['post'])
def add_product():
  name=request.json['name']
  description=request.json['description']
  price=request.json['price']
  

  new_product=Product(name, description, price)

  db.session.add(new_product)
  db.session.commit()

  return product_schema.jsonify(new_product)

#getting all products
@views.route('/getallproducts',methods=['GET'])
def get_products():
  all_products=Product.query.all()
  result=products_schema.dump(all_products)
  return jsonify(result)


#get a product
@views.route('/getproduct/<id>',methods=['GET'])
def get_product(id):
  product=Product.query.get(id)
  
  return product_schema.jsonify(product)

#update a product
@views.route('/update/<id>',methods=['PUT'])
def update_product(id):
  product=Product.query.get(id)

  name=request.json['name']
  description=request.json['description']
  price=request.json['price']
 

  product.name=name
  product.description=description
  product.price=price
 

  
  db.session.commit()

  return product_schema.jsonify(product)
  

#delete
@views.route('/delete/<id>',methods=['DELETE'])
def delete_product(id):
  product=Product.query.get(id)
  db.session.delete(product)
  db.session.commit()
  return product_schema.jsonify(product)