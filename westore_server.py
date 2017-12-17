from flask import Flask, request, Response, send_file, abort, redirect, url_for, jsonify, render_template
from flask_restful import Api, Resource
from flask_cors import CORS
from werkzeug import secure_filename
from ProductRepo import *
from OrderRepo import *
from PostRepo import *
from MakePublicEntity import *
from ShoppingCartRepo import ShoppingCartRepo


app = Flask(__name__)
CORS(app) 
# app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
api = Api(app)

PRODUCT_DB_FILE       = './db/products.json'
ORDERS_DB_FILE        = './db/orders.json'
SHOPPING_CART_DB_FILE = './db/shopping_cart.json'


class ProductsAPI(Resource):
    def __init__(self):
        self.repo = ProductRepo(PRODUCT_DB_FILE)

    def get(self):
        products = self.repo.getByCondition(request.args)
        return {'products' : list(map(lambda p : make_public_product(p), products))}


class ProductAPI(Resource):
    def __init__(self):
        self.repo = ProductRepo(PRODUCT_DB_FILE)

    def get(self, id):   
        products = self.repo.getById(id)
        if not products:
            abort(404)
        return make_public_product(products[0])


class OrdersAPI(Resource):
    def __init__(self):
        self.repo = OrderRepo(ORDERS_DB_FILE, SHOPPING_CART_DB_FILE)

    def get(self):
        orders = self.repo.getByCondition(request.args)
        return {'orders' : list(map(lambda order: make_public_order(order), orders))}

    def post(self):
        order = request.get_json()
        try:
            orderId = self.repo.add(order)
        except Exception as e:
            print('exception occurred when post order: {}'.format(e))
            return {'result' : 'failed'}, 409
        return {'result' : 'success', 'data': orderId }, 200

    def purchase(self, products):
        for product in products:
            self.products.removeStock(product)
        

class OrderAPI(Resource):
    def __init__(self):
        self.repo = OrderRepo(ORDERS_DB_FILE, SHOPPING_CART_DB_FILE)
    
    def get(self, id):
        orders = self.repo.getById(id)
        if not orders:
            abort(404)
        return make_public_order(orders[0])

    def put(self, id):
        pass

    def delete(self, id):
        pass    


class ShoppingCartsAPI(Resource):
    def __init__(self):
        self.repo = ShoppingCartRepo(SHOPPING_CART_DB_FILE)

    def get(self):
        pass

    def post(self):
        order = request.get_json()
        try:
            orderId = self.repo.add(order)
        except Exception as e:
            print('exception occurred when post order: {}'.format(e))
            return {'result' : 'failed'}, 409
        return {'result' : 'success'}, 200

class ShoppingCartAPI(Resource):
    def __init__(self):
        self.repo = ShoppingCartRepo(SHOPPING_CART_DB_FILE)
    
    def get(self, id):
        cart = self.repo.getById(id)
        if not cart:
            abort(404)
        return cart

    def put(self, id):
        pass

    def delete(self, id):
        pass    

class PostsAPI(Resource):
    def __init__(self):
        self.repo = PostRepo('./db/posts.json')

    def get(self):
        return {'posts' : self.repo.getByCondition(request.args)}


class PostAPI(Resource):
    def __init__(self):
        self.repo = PostRepo('./db/posts.json')
    
    def get(self, id):
        posts = self.repo.getById(id)
        if not posts:
            abort(404)
        return posts[0]


api.add_resource(ProductsAPI, '/westore/api/products', endpoint = 'products')
api.add_resource(ProductAPI, '/westore/api/products/<string:id>', endpoint = 'product')

api.add_resource(OrdersAPI, '/westore/api/orders', endpoint = 'orders')
api.add_resource(OrderAPI, '/westore/api/orders/<string:id>', endpoint = 'order')

api.add_resource(PostsAPI, '/westore/api/posts', endpoint = 'posts')
api.add_resource(PostAPI, '/westore/api/posts/<string:id>', endpoint = 'post')

api.add_resource(ShoppingCartsAPI, '/westore/api/shopping/cart', endpoint = 'shoppings')
api.add_resource(ShoppingCartAPI, '/westore/api/shopping/cart/<string:id>', endpoint = 'shopping')



import os
import QrCodeScan

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/westore/picture/upload', methods=['GET', 'POST'])
def upload_picture():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            id = QrCodeScan.scan(file_path)
            return jsonify({'id' : id})
    return '''
    <!doctype html>
    <title>Upload Picture</title>
    <h1>Upload product picture</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

@app.route('/westore/picture/download', methods=['GET'])
def download_picture():
    product_id = request.args.get('productid')
    image_id = request.args.get('pictureid')
    return send_file("./intramirror/{}/target/{}".format(product_id, image_id), mimetype='image/jpeg')

@app.route('/westore/picture/size/relation', methods=['GET'])
def query_size_relation():
    relation_Name = request.args.get('relationName')
    sex  = request.args.get('sex')
    size_type = request.args.get('size_type')
    return send_file("./sizeRelation/{}/{}/{}".format(sex, size_type, relation_Name), mimetype='image/jpeg')

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
