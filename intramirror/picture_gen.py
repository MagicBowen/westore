import os
import sys

sys.path.append("../lib/qrcode")

import QrCode

def get_product_info(product_folder):
    return product_folder.split(os.path.sep)[-1]

def generate_pictures_for_product(product_folder):
    target_folder = os.path.join(product_folder, 'target')
    if not os.path.isdir(target_folder):
        os.makedirs(target_folder)

    product_info = get_product_info(product_folder)
    for src_file in os.listdir(product_folder):
        if not os.path.isdir(src_file):
            (_, extension) = os.path.splitext(src_file)
            if extension == '.jpg':
                target_file = os.path.join(target_folder, src_file)
                src_file = os.path.join(product_folder,src_file)
                print('generate jpg from {} to {} with id {}'.format(src_file, target_file, product_info))
                QrCode.generate(product_info, src_file, target_file)

def generate_pictures(input_folder):
    for path in os.listdir(input_folder):
        if os.path.isdir(path):
            generate_pictures_for_product(path)


if __name__ == '__main__':
    input_folder = '.'
    generate_pictures(input_folder)