__author__ = 'aliHitawala'
import logging
import Constants as C
from BrandNameDictionary import BrandNameList
import editdistance
import distance
import re

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

brand_list = BrandNameList()


def if_either_product_not_defined(pair):
    return pair.v is None or pair.w is None


def if_both_product_not_defined(pair):
    return pair.v is None and pair.w is None


def if_no_brand_name_in_either_product(pair):
    return pair.v.brand is None or pair.w.brand is None


def is_exact_match(pair):
    if if_no_brand_name_in_either_product(pair):
        return False
    if pair.v.brand == pair.w.brand:
        return True
    return False


def intersection_words(word1, word2):
    c1 = word1.split()
    c2 = word2.split()
    c3 = set(c1).intersection(set(c2))
    return list(c3)


def is_part_match(pair):
    if if_no_brand_name_in_either_product(pair):
        return False
    if is_exact_match(pair):
        return True
    brand1 = pair.v.brand
    brand2 = pair.w.brand
    
    if brand1 not in brand_list.get_list() or brand2 not in brand_list.get_list():
        if check_edit_distance_measure(brand1, brand2):
            return True
    intersects = intersection_words(brand1, brand2)
    matching_extent = 0
    for intersected_word in intersects:
        #TODO can imporve for case Apple Corp America & Apple Corp
        if intersected_word in brand_list.get_list():
            matching_extent += int(brand_list.get_map()[intersected_word])
    return matching_extent > C.threshold_dictionary_part_weighted_measure
    

def check_edit_distance_measure(string1, string2):
    measure = editdistance.eval(string1, string2)
    return 1-(measure/max(len(string1), len(string2))) >= C.threshold_edit_distance_measure


def check_jaccard_measure(string1, string2):
    return distance.jaccard(string1, string2) == C.threshold_jaccard_measure


def is_jaccard_match(pair):
    if if_no_brand_name_in_either_product(pair):
        return False
    if is_exact_match(pair):
        return True
    return check_jaccard_measure(pair.v.brand, pair.w.brand)


def get_all_keywords(v):
    attrs = vars(v)
    result = set()
    for key in attrs:
        value = attrs[key]
        if type(value) is str and value.strip() != "":
            v_list = [x.strip('.') for x in re.split(C.regex_to_tokenize_words_into_set, value)]
            if len(v_list) > 0:
                result |= set(v_list)
    return result


def check_product_description_for_both_product(pair):
    key_words_v = get_all_keywords(pair.v)
    key_words_w = get_all_keywords(pair.w)
    intersect_words = key_words_v.intersection(key_words_w)
    map_brands = brand_list.get_map()
    max_value = 0
    max_probable_brand = ''
    for brand in brand_list.get_list():
        new_set = set(re.split(C.regex_to_tokenize_words_into_set, brand)).difference(intersect_words)
        if len(new_set) == 0 and brand in map_brands:
            brand_value = int(map_brands[brand])
            if brand_value > max_value:
                max_probable_brand = brand
                max_value = brand_value
    if max_value > C.threshold_brand_value:
        logger.info("Brand predicted for pair id : " + pair.pair_id + " brand + " + max_probable_brand)
        return True
    return False


def check_product_description_for_one_product(product_to_check, brand):
    keywords_in_products = get_all_keywords(product_to_check)
    tokens_in_brand = set(re.split(C.regex_to_tokenize_words_into_set, brand))
    new_set = tokens_in_brand.difference(keywords_in_products)
    if len(new_set) == 0:
        return True
    return False


def check_product_descripton_given_unmatched_brand(pair):
    return check_product_description_for_both_product(pair)


def is_brand_match_on_description(pair):
    if is_exact_match(pair):
        return True
    if pair.v.brand is None and pair.w.brand is None:
        if check_product_description_for_both_product(pair):
            logger.info("ALGO id : 4.1, pair matched " + pair.pair_id)
    elif pair.v.brand is None:
        if check_product_description_for_one_product(pair.v, pair.w.brand):
            logger.info("ALGO id : 4.2, pair matched " + pair.pair_id)
    elif pair.w.brand is None:
        if check_product_description_for_one_product(pair.w, pair.v.brand):
            logger.info("ALGO id : 4.3, pair matched " + pair.pair_id)
    elif check_product_descripton_given_unmatched_brand(pair):
        logger.info("ALGO id : 4.4, pair matched " + pair.pair_id)
        return True
    return False


def aggregate_matcher(pair, algorithm_pref = None):
    if algorithm_pref is None:
        logger.error("Aggregate Matcher called without any algorithm")
        return
    if if_both_product_not_defined(pair):
        return True
    if if_either_product_not_defined(pair):
        return False
    for algorithm in algorithm_pref:
        if algorithm == C.matcher_algo_exact_match and is_exact_match(pair):
            logger.info("ALGO id : 1, pair matched " + pair.pair_id)
            return True
        elif algorithm == C.matcher_algo_part_match and is_part_match(pair):
            logger.info("ALGO id : 2, pair matched " + pair.pair_id)
            return True
        elif algorithm == C.matcher_algo_jaccard_match and is_jaccard_match(pair):
            logger.info("ALGO id : 3, pair matched " + pair.pair_id)
            return True
        elif algorithm == C.matcher_algo_information_extraction and is_brand_match_on_description(pair):
            return True
    return False