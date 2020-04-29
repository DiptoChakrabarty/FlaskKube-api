from apiapp import app,db,ma
from apiapp.models import Product,ProductSchema




product_schema = ProductSchema(strict=True)
products_schema = ProductSchema(many=True,strict=True)