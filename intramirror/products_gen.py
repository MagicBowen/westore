import os
import sys
import json
import codecs

def get_product(path):
    print('deal product {}'.format(path))
    with open(os.path.join(path, 'intro.json'), 'r') as product_json:
        product = json.loads(product_json.read())
        product['id'] = path.split(os.path.sep)[-1]
        return product


def generate_products(products_folder):
    products = []
    for path in os.listdir(products_folder):
        if os.path.isdir(path):
            products.append(get_product(path))
    return products


def generate_json(input_folder, json_file):
    with open(json_file, 'w') as file:
        products = generate_products(input_folder)
        product_json = json.dumps({'products' : products}, ensure_ascii=False, indent=2)
        file.write(product_json)


if __name__ == '__main__':
    json_file = '../db/products.json'
    input_folder = '.'
    generate_json(input_folder, json_file)