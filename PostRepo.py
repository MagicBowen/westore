import json
from functools import reduce


class PostRepo:
    def __init__(self, file):
        self.file = file
        with open(file, encoding='utf-8') as json_file:
            self.posts = json.loads(json_file.read())['posts']
    
    def getAll(self):
        return self.posts

    def getById(self, id):
        return self.getByCondition({'id' : id})

    def getByCondition(self, condition):
        return list(filter(lambda p : self._isSatisfied(p, condition), self.posts))

    def _isSatisfied(self, product, condition):
        if not condition: return True
        return reduce(lambda acc, item: acc and item[1] == str(product[item[0]]), condition.items(), True)

    def _save(self):
        with open(self.file, 'w') as json_file:
            json_file.write(json.dumps({'posts' : self.posts}, ensure_ascii=False, indent = 2))  