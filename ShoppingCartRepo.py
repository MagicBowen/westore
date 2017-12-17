import json
from functools import reduce

class ShoppingCartRepo:
    def __init__(self, file):
        self.file = file
        self._load()

    def _load(self):
        with open(self.file, encoding='utf-8') as json_file:
            self.shoppingCarts = json.loads(json_file.read())['shopping_cart']

    def add(self, product):
        self._load()
        userId = product["userId"]
        del product["userId"]
        if userId not in self.shoppingCarts.keys():
            self.shoppingCarts[userId] = []

        ueserCart = self.shoppingCarts[userId]
        ueserCart.append(product)
        self._save()

    def delete(self, userId):
        self._load()
        del self.shoppingCarts[userId]
        self._save()

    def getById(self, userId):
        if userId not in self.shoppingCarts.keys():
            return []
        return self.shoppingCarts[userId]

    def getByCondition(self, condition):
        return list(filter(lambda order : self._isSatisfied(order, condition), self.orders))

    def _isSatisfied(self, order, condition):
        if not condition: return True
        return reduce(lambda acc, item: acc and item[1] == str(order[item[0]]), condition.items(), True)

    def _save(self):
        with open(self.file, 'w') as json_file:
            json_file.write(json.dumps({'shopping_cart' : self.shoppingCarts}, ensure_ascii=False, indent = 2))


def main():
    cartRepo = ShoppingCartRepo('./db/shopping_cart.json')
    product = {'userId': '284894567', 'charge': '5458元', 'color': 'black', 'product_id': 'product-61', 'amount': '1', 'size': 'L'}
    cartRepo.add(product)
    # cartRepo.delete('284894567')

if __name__ == '__main__':
    main()


        
        
        
