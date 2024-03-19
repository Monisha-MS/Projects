from . import db,ma
class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(100))
    price = db.Column(db.Float)
 
 
    def __init__(self, name, description, price):
        self.name=name
        self.description=description
        self.price=price

#product schema
class ProductSchema(ma.Schema):
  class Meta:
    fields = ('id','name','description','price')

#init schema
product_schema=ProductSchema()
products_schema = ProductSchema(many=True)