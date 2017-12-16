import os
import sys
import json
import random
import codecs


def modify_quantity(input_folder, number_ceil):
    for path in os.listdir(input_folder):
        if os.path.isdir(path):
            product = None
            with open(os.path.join(path, 'intro.json'), 'r', encoding='utf-8') as product_json:
                product = json.loads(product_json.read())
                for key in product['quantity'].keys():
                    product['quantity'][key] = random.randint(1, number_ceil)

            with open(os.path.join(path, 'intro.json'), 'w+', encoding='utf-8') as file:
                product_json = json.dumps(product, ensure_ascii=False, indent=2)
                print('modify quantity of product: {}'.format(path))
                file.write(product_json)


if __name__ == '__main__':
    input_folder = '.'
    number_ceil = 10
    modify_quantity(input_folder, number_ceil)