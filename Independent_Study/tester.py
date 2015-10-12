__author__ = 'aliHitawala'
from BrandNameDictionary import BrandNameList
import distance
import re
import Constants as C

def main():
    brand_list = BrandNameList()
    print brand_list.get_list()

class animal(object):
    def __init__(self):
        self.legs = 0
        self.name = "a"


def parse_tokens(all_pairs):
    pair_list = []
    for pair in all_pairs:
        tokens = [x.strip() for x in pair.split('?')]
        pair_id = tokens.pop(0)
        product_id_v = tokens.pop(0)
        json_v = tokens.pop(0)
        product_id_w = tokens.pop(0)
        json_w = tokens.pop(0)
        match_str = tokens.pop(0)
        if match_str == 'MATCH':
            string = pair_id.strip()+'?Y'
            print string
        else:
            string = pair_id.strip()+'?'
            print string
    return pair_list

def parse_file_get_pairs():
    all_pairs = [line.rstrip('\n') for line in open(C.all_pairs_file_name)]
    return parse_tokens(all_pairs)

if __name__ == '__main__':
    # main()
    # c1 = "T Motors".split()
    # c2 = "Tesla".split()
    # c3 = set(c1).intersection(set(c2))
    # print list(c3)
    # parse_file_get_pairs()
    # text = "Feb-2010"
    # print re.search(r'([A-Za-z]{3})(-)(.+\d)', text).group(1)
    # text = "S1234"
    # print re.search(r'(S)(.+\d)', text).group(2)
    string = "alihuss"
    length = 2
    s = set()
    for i in range(len(string)-length+1):
        j = i+length
        s.add(string[i:j])
    for i in range(len(s)):
        print s.pop()

