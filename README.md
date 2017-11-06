# README

## usage

```
nohup python3 westore_server.py &
```

## API

Host: http://ip:port/

Test on aliyun with `47.96.14.42:80`

### product

- query all products: `/westore/api/products`

```bash
curl -i http://ip:port/westore/api/products
```

- query specified product: `/westore/api/products/<productid>`

```bash
curl -i http://ip:port/westore/api/products/coat-0
```

- query products by condition: `/westore/api/products`

```bash
curl -i http://ip:port/westore/api/products?color=red
curl -i http://ip:port/westore/api/products?tags=female&tags=shoes
```

### picture

- get product picture: `/westore/picture/download`

```bash
curl -i http://ip:port/westore/picture/download?productid=shoes-3&pictureid=1
```

- upload procuct picture and get the QRCode: `/westore/picture/upload`
It's a simple HTML page, upload picture from page and will get the QRCode value in picture.


### order

- query all orders: `/westore/api/orders`
- query specified order: `/westore/api/orders/<orderid>`
- query orders by condition: `/westore/api/orders?<condition>`
- post a new order: `/westore/api/orders`

```bash
curl -i -X POST -H "Content-Type: application/json" -d '{"payer": "Robert", "products": [{"id": "1", "number": 1, "size": "XS"}, {"id": "2", "number": 1,"size": "S"}], "receiver": {"address": "XXX", "phone": "13991945678", "name": "Robert Wang"}, "totalPrice": 1968.4}' http://ip:port/westore/api/orders
```

### post
- query all posts: `/westore/api/posts`
- query specified post: `/westore/api/posts/<postid>`
- query orders by condition: `/westore/api/posts?<condition>`
