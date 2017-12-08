import os
import sys
import shutil


def get_product_id(product_folder):
    return product_folder.split(os.path.sep)[-1]

def collect_pictures_for_product(product_folder, out_folder):
    if not os.path.isdir(out_folder):
        os.makedirs(out_folder)

    product_id = get_product_id(product_folder)
    picture_folder = os.path.join(product_folder, 'target')
    for src_file in os.listdir(picture_folder):
        if not os.path.isdir(src_file):
            (_, extension) = os.path.splitext(src_file)
            if extension == '.jpg':
                new_name = product_id + '-' + src_file
                target_path = os.path.join(out_folder, new_name)
                src_path = os.path.join(picture_folder, src_file)
                shutil.copy (src_path, target_path)
                print('copy {} to {}'.format(src_path, target_path))

def collect_pictures(input_folder, out_folder):
    for path in os.listdir(input_folder):
        if os.path.isdir(path):
            collect_pictures_for_product(path, out_folder)


if __name__ == '__main__':
    input_folder = '.'
    out_folder = './pictures'
    collect_pictures(input_folder, out_folder)