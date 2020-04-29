from apiapp import db

class Product(db.Model):
    id = db.Column(db.Integer,primary_key=True)