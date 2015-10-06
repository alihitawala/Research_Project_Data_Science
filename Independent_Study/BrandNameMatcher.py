__author__ = 'aliHitawala'
import ProductObjectCreator
from BrandNameDictionary import BrandNameList
import Constants as C
from Product import Product


brand_list = BrandNameList()


def match(v, w):
    if v is None or w is None:
        return False
    brand_v = v.brand
    brand_w = w.brand
    if brand_v == brand_w:
        return True
    return False


def matcher():
    all_pairs = ProductObjectCreator.parse_file_get_pairs()
    for pair in all_pairs:
        is_match = match(pair.v, pair.w)
        if is_match:
            pair.brand_match = True
    result_file = open(C.results_file_name, 'w+')
    result_file.write('%-20s %20s %20s %20s %20s %20s %20s\n' % ("Pair_ID", "Product_1_ID", "Product_1_Brand", "Product_2_ID", "Product_2_Brand", "Matcher_Result", "Actual_result"))
    for pair in all_pairs:
        if pair.v is not None and pair.w is not None:
            result_file.write('%-20s %20s %20s %20s %20s %20s %20s\n' % (pair.pair_id, pair.v.product_id, pair.v.brand, pair.w.product_id, pair.w.brand, str(pair.brand_match), str(pair.is_match)))

matcher()