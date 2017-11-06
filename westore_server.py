from flask import Flask, request, Response, send_file, abort, redirect, url_for, jsonify
from flask_restful import Api, Resource
from werkzeug import secure_filename
from ProductRepo import *
from OrderRepo import *
from PostRepo import *


app = Flask(__name__)
# app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
api = Api(app)


class ProductsAPI(Resource):
    def __init__(self):
        self.repo = ProductRepo('./db/products.json')

    def get(self):
        condition = request.args
        tags = condition.getlist('tags')
        if tags: return self.repo.getByTags(tags)
        return self.repo.getByCondition(condition)
        

class ProductAPI(Resource):
    def __init__(self):
        self.repo = ProductRepo('./db/products.json')

    def get(self, id):   
        product = self.repo.getById(id)
        return product if product is not None else abort(404)


class OrdersAPI(Resource):
    def __init__(self):
        self.products = ProductRepo('./db/products.json')
        self.repo = OrderRepo('./db/orders.json')

    def get(self):
        return self.repo.getByCondition(request.args)

    def post(self):
        order = request.get_json()
        try:
            # need transaction in formal
            self.purchase(order['products'])
            self.repo.add(order)
        except Exception as e:
            print('exception occurred when post order: {}'.format(e))
            return {'result' : 'failed'}, 409
        return {'result' : 'success'}, 200

    def purchase(self, products):
        for product in products:
            self.products.removeStock(product)
        

class OrderAPI(Resource):
    def __init__(self):
        self.repo = OrderRepo('./db/orders.json')
    
    def get(self, id):
        order = self.repo.getById(id)
        return order if order is not None else abort(404)

    def put(self, id):
        pass

    def delete(self, id):
        pass    


class PostsAPI(Resource):
    def __init__(self):
        self.repo = PostRepo('./db/posts.json')

    def get(self):
        return self.repo.getByCondition(request.args)


class PostAPI(Resource):
    def __init__(self):
        self.repo = PostRepo('./db/posts.json')
    
    def get(self, id):
        post = self.repo.getById(id)
        return post if post is not None else abort(404)


api.add_resource(ProductsAPI, '/westore/api/products', endpoint = 'products')
api.add_resource(ProductAPI, '/westore/api/products/<string:id>', endpoint = 'product')

api.add_resource(OrdersAPI, '/westore/api/orders', endpoint = 'orders')
api.add_resource(OrderAPI, '/westore/api/orders/<string:id>', endpoint = 'order')

api.add_resource(PostsAPI, '/westore/api/posts', endpoint = 'posts')
api.add_resource(PostAPI, '/westore/api/posts/<string:id>', endpoint = 'post')


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
    return send_file("./intramirror/{}/target/{}.jpg".format(product_id, image_id), mimetype='image/jpeg')

@app.route('/westore', methods=['GET'])
def index():
    return '''
    <!doctype html>
    <title>Westore</title>
    <h1>WeStore Demo for Da-Da!!!</h1>
    '''


if __name__ == '__main__':
    app.run(debug=True)
