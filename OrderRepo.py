import json
from functools import reduce


class OrderRepo:
    def __init__(self, file):
        self.file = file
        with open(file, encoding='utf-8') as json_file:
            self.orders = json.loads(json_file.read())['orders']

    def add(self, order):
        order['id'] = 'order-' + str(len(self.orders) + 1)
        order["payed"] = False
        order["payedTime"] = ""
        order["postNo"] = None
        self.orders.append(order)
        self._save()
        
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
            