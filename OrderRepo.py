import json
from functools import reduce
from ShoppingCartRepo import ShoppingCartRepo


class OrderRepo:
    def __init__(self, ordersfile, shoppingCartFile):
        self.file = ordersfile
        self.shoppingCart = ShoppingCartRepo(shoppingCartFile)
        with open(ordersfile, encoding='utf-8') as json_file:
            self.orders = json.loads(json_file.read())['orders']

    def add(self, order):
        orderInfo = {}
        orderInfo['id'] = 'order-' + str(len(self.orders) + 1)
        orderInfo['payed'] = False
        orderInfo["payedTime"] = ""
        orderInfo["postNo"] = None
        orderInfo["recipients"] = order["recipients"]
        shoppingCart = self.shoppingCart.getById(order["userId"])
        if shoppingCart: 
            orderInfo["products"] = shoppingCart
            self.shoppingCart.delete(order["userId"])

        orderInfo["payment-way"] = order["payment-way"]
        self.orders.append(orderInfo)
        self._save()
        return orderInfo['id']
        
    def getAll(self):
        return self.orders

    def getById(self, id):
        return self.getByCondition({'id' : id})

    def getByCondition(self, condition):
        return list(filter(lambda order : self._isSatisfied(order, condition), self.orders))

    def _isSatisfied(self, order, condition):
        if not condition: return True
        return reduce(lambda acc, item: acc and item[1] == str(order[item[0]]), condition.items(), True)

    def _save(self):
        with open(self.file, 'w') as json_file:
            json_file.write(json.dumps({'orders' : self.orders}, ensure_ascii=False, indent = 2))


def main():
    orderRepo = OrderRepo('./db/orders.json', './db/shopping_cart.json')
    order = {'userId': '284894567', 'payment-way': '微信', 'recipients': {'address': '西安万科城雅居乐花园5号楼', 'name': '尉先生', 'phone': '18629022031'}}
    print(orderRepo.add(order))

if __name__ == '__main__':
    main()
            