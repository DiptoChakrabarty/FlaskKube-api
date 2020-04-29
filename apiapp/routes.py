from apiapp import app,db,ma,jsonify,request
from apiapp.models import product,productSchema


product_schema = productSchema()
products_schema = productSchema(many=True)


@app.route("/product",methods=["POST"])
def add_product():
    name= request.json["name"]
    description= request.json["description"]
    price= request.json["price"]
    qty= request.json["qty"]

    new = product(name,description,price,qty)

    db.session.add(new)
    db.session.commit()

    return product_schema.jsonify(new)