__author__ = 'aliHitawala'
import ProductObjectCreator
import sys


def show_tuple_pairs(p):
    all_pairs = ProductObjectCreator.parse_file_get_pairs()
    pair_id = p
    pair = [x for x in all_pairs if x.pair_id == pair_id]
    pair = pair[0]
    attrs_v = vars(pair.v)
    attrs_w = vars(pair.w)
    for x in attrs_v:
        print "Product 1 %-20s %s" % (x, attrs_v[x])
        print "Product 2 %-20s %s" % (x, attrs_w[x])

show_tuple_pairs('20659771-28501877#UnbeatableSale.com')
