__author__ = 'aliHitawala'
import Constants


class BrandNameList(object):
    """
    collects all the element from a file and put it into a python object.
    """
    _no_brand_name = 2

    def __init__(self, path_to_file=Constants.brand_name_list_file_name_freq):
        lines = [line.rstrip('\n') for line in open(path_to_file)]
        self._list = []
        self._map = {}
        for line in lines:
            words = line.split()
            length = len(words)
            brand_name = ''
            for i in range(length-1):
                brand_name += ' ' + words[i]
            brand_name = brand_name.lower().strip()
            freq = words[-1]
            self._map[brand_name] = freq
            self._list.append(brand_name)
        if '' in self._map:
            self._map.pop('')

    def get_list(self):
        return self._list

    def get_map(self):
        return self._map