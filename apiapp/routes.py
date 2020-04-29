from apiapp import app,db,ma,jsonify,request
from apiapp.models import product,productSchema


product_schema = productSchema()
products_schema = productSchema(many=True)


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
def show_products():
    all = product.query.all()
    result = products_schema.dump(all)
    return products_schema.jsonify(result.data) 

@app.route("/product/<id>")
def show_product(id):
    result.data =  product.query.get(id)
    return product_schema.jsonify(result.data) 