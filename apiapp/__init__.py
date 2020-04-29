from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app=Flask(__name__)
path= os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///"+os.path.join(path,"db.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db= SQLAlchemy(app)
db.init_app(app)
db.create_all()

ma= Marshmallow(app)


from apiapp import routes