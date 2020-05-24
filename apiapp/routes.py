from apiapp import app,db,ma,jsonify,request
from apiapp.models import product,productSchema,users
import bcrypt ,datetime
from flask_jwt import JWT,jwt_required
from apiapp.security import authenticate,identity
from datetime import timedelta


jwt = JWT(app, authenticate, identity)
product_schema = productSchema()
products_schema = productSchema(many=True)
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=6000)

db.create_all()

### Routes
@app.route("/productadd",methods=["POST"])
def add_product():
    name= request.json["name"]
    description= request.json["description"]
    price= request.json["price"]
    qty= request.json["qty"]

    new = product(name,description,price,qty)

    db.session.add(new)
    db.session.commit()

    return product_schema.jsonify(new)

@app.route("/products",methods=["GET"])
@jwt_required()
def show_products():
    all = product.query.all()
    result = products_schema.dump(all)
    return products_schema.jsonify(result) 

@app.route("/product/<id>")
def show_product(id):
    result =  product.query.get(id)
    return product_schema.jsonify(result) 

@app.route("/product/<id>",methods=["PUT"])
def update(id):
    result =  product.query.get(id)

    name= request.json["name"]
    description= request.json["description"]
    price= request.json["price"]
    qty= request.json["qty"]

    result.name = name
    result.description =description
    result.price = price
    result.qty= qty

    db.session.commit()
    return product_schema.jsonify(result)

@app.route("/product/<id>",methods=["DELETE"])
def delete_item(id):
    result =  product.query.get(id)
    db.session.delete(result)
    db.session.commit()

    return "Removed"

#### Users

@app.route("/users",methods=["POST"])
def create_user():
    data = request.get_json()
    
    hashed = bcrypt.hashpw(data["password"].encode('utf-8'),bcrypt.gensalt())
    new_user = users(username=data["username"],password=hashed )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "msg": "User Added",
        "status": 200
    })

@app.route("/usersdel/<id>",methods=["DELETE"])
def remove_user(id):
    user = users.query.get(id)
    db.session.delete(user)
    db.session.commit()

    return "User Removed "




