from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app=Flask(__name__)
path= os.path.abspath(os.path.dirname(__file__))
db= SQLAlchemy(app)
#app.config["SQLALCHEMY_DATABASE_URI"]= 'mysql+pymysql://root:dipto@db:3306/product'
app.config["SECRET_KEY"]="kubernetes"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()


ma= Marshmallow(app)


from apiapp import routes