import json
from functools import reduce


class ProductRepo:
    def __init__(self, file):
        self.file = file
        with open(file) as json_file:
            self.products = json.loads(json_file.read())['products']
    
    def getAll(self):
        return self.products

    def getById(self, id):
        return self.getByCondition({'id' : id})

    def getByCondition(self, condition):
        return list(filter(lambda p : self._isSatisfied(p, condition), self.products))

    def getByTags(self, tags):
        return list(filter(lambda p: set(p['tags']) >= set(tags) , self.products))

    def removeStock(self, sell):
        for product in self.products:
            if product['id'] == sell['id']:
                quantity = product['quantity'][sell['size']]
                if quantity >= sell['number']:
                    product['quantity'][sell['size']] = quantity - sell['number']
                else:
                    raise Exception("Product {} of size ({}:{}) is not enough".format(product['id'],sell['size'],quantity))
        self._save()
                    

    def _isSatisfied(self, product, condition):
        if not condition: return True
        return reduce(lambda acc, item: acc and item[1] == str(product[item[0]]), condition.items(), True)

    def _save(self):
        with open(self.file, 'w') as json_file:
            json_file.write(json.dumps({'products' : self.products}, ensure_ascii=False, indent = 2))            
            

if __name__ == '__main__':
    pass