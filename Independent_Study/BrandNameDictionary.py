__author__ = 'aliHitawala'
import Constants


class BrandNameList(object):
    """
    collects all the element from a file and put it into a python object.
    """
    _no_brand_name = 2

    def __init__(self):
        self._list = [line.rstrip('\n') for line in open(Constants.brand_name_list_file_name)]
        self._list = self._list[self._no_brand_name:]

    def get_list(self):
        return self._list
