# API

Server: http://39.106.47.238:8080/

## product

- query all products: `/westore/api/products`

```bash
curl -i http://39.106.47.238:8080/westore/api/products
```

- query specified product: `/westore/api/products/<productid>`

```bash
curl -i http://39.106.47.238:8080/westore/api/products/coat-0
```

- query products by condition: `/westore/api/products`

```bash
curl -i http://39.106.47.238:8080/westore/api/products?color=red
curl -i http://39.106.47.238:8080/westore/api/products?tags=female&tags=shoes
```

## picture

- get product picture: `/westore/picture/download`

```bash
curl -i http://39.106.47.238:8080/westore/picture/download?productid=shoes-3&pictureid=1
```

- upload procuct picture and get the QRCode: `/westore/picture/upload`
It's a simple HTML page, upload picture from page and will get the QRCode value in picture.


## order

- query all orders: `/westore/api/orders`
- query specified order: `/westore/api/orders/<orderid>`
- query orders by condition: `/westore/api/orders?<condition>`
- post a new order: `/westore/api/orders`

```bash
curl -i -X POST -H "Content-Type: application/json" -d '{"payer": "Robert", "products": [{"id": "1", "number": 1, "size": "XS"}, {"id": "2", "number": 1,"size": "S"}], "receiver": {"address": "XXX", "phone": "13991945678", "name": "Robert Wang"}, "totalPrice": 1968.4}' http://39.106.47.238:8080/westore/api/orders
```

## post
- query all posts: `/westore/api/posts`
- query specified post: `/westore/api/posts/<postid>`
- query orders by condition: `/westore/api/posts?<condition>`
