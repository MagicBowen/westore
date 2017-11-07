from flask import url_for

def make_public_order(order):
    new_order = {}
    for field in order:
        if field == 'postNo':
            uri = url_for('posts', id=order['postNo'], _external=True) if order['postNo'] else None
            new_order['post'] = uri
        else:
            new_order[field] = order[field]
    return new_order

def make_public_product(product):
    new_pictures = []
    for picture in product['pictures']:
        new_picture = {}
        new_picture['tags'] = picture['tags']
        new_picture['uri'] = url_for('download_picture', productid = product['id'], pictureid = picture['name'], _external=True)
        new_pictures.append(new_picture)
    product['pictures'] = new_pictures
    return product


if __name__ == '__main__':
    pass