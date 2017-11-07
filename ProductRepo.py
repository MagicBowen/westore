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
        return list(filter(lambda p : p['id'] == id, self.products))

    def getByCondition(self, condition):
        productInTags = self.getByTags(condition.getlist('tags'))
        productInProperties = self.getByProperties(condition)
        result = []
        for p1 in productInProperties:
            for p2 in productInTags:
                if p1['id'] == p2['id']:
                    result.append(p1)
        return result

    def getByProperties(self, properties):
        if not properties: return self.products
        return list(filter(lambda p : self._isSatisfied(p, properties), self.products))

    def getByTags(self, tags):
        if not tags: return self.products
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
        for item in condition.items():
            if item[0] == 'tags': continue
            if item[1] != product[item[0]]: return False
        return True

    def _save(self):
        with open(self.file, 'w') as json_file:
            json_file.write(json.dumps({'products' : self.products}, ensure_ascii=False, indent = 2))            
            

if __name__ == '__main__':
    pass