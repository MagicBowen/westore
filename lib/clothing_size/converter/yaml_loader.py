import yaml

class NotSupportedStandardError(Exception):
    def __init__(self, standard):
        self._standard = standard
    def __str__(self):
        return repr('not supported standard %s' %self._standard)

class NotSupportedSize(Exception):
    def __init__(self, standard, size):
        self._standard = standard
        self._size = size
    def __str__(self):
        return repr('size %s not defined in standard %s' %(self._size, self._standard))

class GenericSizeConverter:
    def __init__(self, dictionary):
        self._dictionary = dictionary
    
    def convert(self, from_standard, to_standard, from_size):
        for standard in self._dictionary:
            if from_standard in standard:
                from_list = standard[from_standard]
                print from_list
            if to_standard in standard:
                to_list = standard[to_standard]
                print to_list
        if from_list == None:
            raise NotSupportedStandardError(from_standard)
        if to_list == None:
            raise NotSupportedStandardError(to_standard)
        try:
            index = from_list.index(from_size)
        except KeyError:
            raise NotSupportedSize(from_size)
        return to_list[index]


WOMEN_KEY = 'women'
MEN_KEY = 'men'
STANDARDS_KEY = 'standards'
TOP_CLOTHING_KEY = 'top_clothing'
SHOES_KEY = 'shoes'


class SizeConverter:
    def __init__(self, file_name):
        self._dictionary = yaml.load(file(file_name))
        self._women_top_clothing = GenericSizeConverter(self._dictionary[WOMEN_KEY][TOP_CLOTHING_KEY][STANDARDS_KEY])
        self._men_shoes = GenericSizeConverter(self._dictionary[MEN_KEY][SHOES_KEY][STANDARDS_KEY])

    def convert_women_top_clothing_size(self, from_standard, to_standard, from_size):
        return self._women_top_clothing.convert(from_standard, to_standard, from_size)

    def convert_men_shoes_size(self, from_standard, to_standard, from_size):
        return self._men_shoes.convert(from_standard, to_standard, from_size)


def load_clothing_size(file_name):
    return yaml.load(file(file_name))


if __name__ == '__main__': 
    dictionary = load_clothing_size('../data/clothing_size.yml')
    converter = GenericSizeConverter(dictionary['women']['top_clothing']['standards'])
    print converter.convert('international', 'Italy', 'XS')

