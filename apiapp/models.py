from apiapp import db
from apiapp import ma

class Product(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name= db.Column(db.Stirng(100),unique=True)
    description = db.Column(db.Text)
    price = db.Column(db.Integer)
    qty =  db.Column(db.Integer)

    def __init__(self,,name,description,price,qty):
        self.name=name
        self.description= description
        self.price=price
        self.qty=qty

        
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id','name','description','price')

product_schema = ProductSchema(strict=True)
products_schema = ProductSchema(many=True,strict=True)