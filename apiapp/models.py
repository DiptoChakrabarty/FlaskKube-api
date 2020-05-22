from apiapp import db
from apiapp import ma

class product(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String(100),unique=True)
    description = db.Column(db.Text)
    price = db.Column(db.Integer)
    qty =  db.Column(db.Integer)

    def __init__(self,name,description,price,qty):
        self.name=name
        self.description= description
        self.price=price
        self.qty=qty

class users(db.Model):
    __tablename__= "users"
    id= db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(25),unique=True)
    password = db.Column(db.String(25))

    def __init__(self,username,password):
        self.username = username
        self.password = password
        
class productSchema(ma.Schema):
    class Meta:
        fields = ('id','name','description','price','qty')
