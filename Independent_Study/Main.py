__author__ = 'aliHitawala'
import BrandNameMatcher

def brand_name_match(json_str_a, json_str_b, dict_path=None) :
    return BrandNameMatcher.match_products(json_str_a, json_str_b, dict_path)