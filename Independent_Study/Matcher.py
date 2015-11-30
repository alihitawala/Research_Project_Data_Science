__author__ = 'aliHitawala'
import logging
import Constants as C
from BrandNameDictionary import BrandNameList
from Prediction import Prediction
import editdistance
import re

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

brand_list = BrandNameList()


def _if_either_product_not_defined(pair):
    return pair.v is None or pair.w is None


def _if_both_product_not_defined(pair):
    return pair.v is None and pair.w is None


def _if_no_brand_name_in_either_product(pair):
    return pair.v.brand is None or pair.w.brand is None \
           or pair.v.brand.strip() == '' or pair.w.brand.strip() == ''


def _is_exact_match(pair):
    if _if_no_brand_name_in_either_product(pair):
        return Prediction(0, 0)
    if pair.v.brand == pair.w.brand:
        return Prediction(1)
    return Prediction(0)


def _intersection_words(word1, word2):
    c1 = word1.split()
    c2 = word2.split()
    c3 = set(c1).intersection(set(c2))
    return list(c3)


def _is_part_match(pair):
    if _if_no_brand_name_in_either_product(pair):
        return Prediction(0, 0)
    p = _is_exact_match(pair)
    if p.prediction == 1:
        return p
    brand1 = pair.v.brand
    brand2 = pair.w.brand
    
    if brand1 not in brand_list.get_list() or brand2 not in brand_list.get_list():
        if _check_edit_distance_measure(brand1, brand2):
            return Prediction(1)
    intersects = _intersection_words(brand1, brand2)
    matching_extent = 0
    for intersected_word in intersects:
        #TODO can imporve for case Apple Corp America & Apple Corp
        if intersected_word in brand_list.get_list():
            matching_extent += int(brand_list.get_map()[intersected_word])
    m = C.threshold_dictionary_part_weighted_measure * 5
    threshold = C.threshold_dictionary_part_weighted_measure
    if matching_extent > m:
        return Prediction(1)
    elif matching_extent > threshold:
        return Prediction(1, 1.0 * (matching_extent-threshold)/(m-threshold))
    return Prediction(0, 1.0 * (threshold-matching_extent)/threshold)

def _check_edit_distance_measure(string1, string2):
    measure = editdistance.eval(string1, string2)
    return 1-(float(measure)/max(len(string1), len(string2))) >= C.threshold_edit_distance_measure


def _check_jaccard_measure(string1, string2):
    set1 = _get_token_length_n(string1, 2)
    set2 = _get_token_length_n(string2, 2)
    n = len(set1.intersection(set2))
    return (n / float(len(set1) + len(set2) - n)) > C.threshold_jaccard_measure


def _get_token_length_n(string, length):
    s = set()
    for i in range(len(string)-length+1):
        j = i+length
        s.add(string[i:j])
    return s


def _is_jaccard_match(pair):
    if _if_no_brand_name_in_either_product(pair):
        return Prediction(0)
    if _is_exact_match(pair).prediction == 1:
        return Prediction(1)
    if _check_jaccard_measure(pair.v.brand, pair.w.brand):
        return Prediction(1)
    return Prediction(0)


def _get_all_keywords(v):
    attrs = vars(v)
    result = set()
    for key in attrs:
        value = attrs[key]
        if type(value) is str and value.strip() != "":
            v_list = [x.lower().strip('.') for x in re.split(C.regex_to_tokenize_words_into_set, value)]
            if len(v_list) > 0:
                result |= set(v_list)
    return result


def _check_product_description_for_both_product(pair):
    key_words_v = _get_all_keywords(pair.v)
    key_words_w = _get_all_keywords(pair.w)
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
    threshold = C.threshold_brand_value
    m = threshold * 3
    if max_value >= m:
        return Prediction(1)
    if max_value >= threshold:
        logger.info("4.14 :: Brand predicted for pair id : " + pair.pair_id + " brand + " + max_probable_brand + ", good confidence :: " + str(max_value))
        return Prediction(1, 1.0 * (max_value-threshold)/(m-threshold))
    elif max_value > C.threshold_brand_value_lower_confidence:
        logger.info("4.14 :: Brand predicted for pair id : " + pair.pair_id + " brand + " + max_probable_brand + ", low confidence :: " + str(max_value))
        return Prediction(-1)
    return Prediction(0)


def _check_product_description_for_one_product(pair, product_to_check, brand):
    keywords_in_products = _get_all_keywords(product_to_check)
    tokens_in_brand = set(re.split(C.regex_to_tokenize_words_into_set, brand))
    new_set = tokens_in_brand.difference(keywords_in_products)
    if len(new_set) == 0:
        brand_weight = 1
        if product_to_check in brand_list.get_list():
            brand_weight = int(brand_list.get_map()[product_to_check])
        threshold = C.threshold_brand_value
        logger.info("4.23 :: Brand predicted for pair id : " + pair.pair_id + " brand + " + brand)
        if threshold <= brand_weight:
            return Prediction(1)
        else:
            return Prediction(1, 1.0 * brand_weight/threshold)
    return Prediction(0)

def check_product_descripton_given_unmatched_brand(pair):
    return _check_product_description_for_both_product(pair)


def _is_brand_match_on_description(pair):
    if _is_exact_match(pair).prediction == 1:
        return Prediction(1)
    if (pair.v.brand is None or pair.v.brand.strip() == '') \
            and (pair.w.brand is None or pair.w.brand.strip() == ''):
        result = _check_product_description_for_both_product(pair)
        if result.prediction == 1 or result.prediction == -1:
            logger.info("ALGO id : 4.1, pair matched " + pair.pair_id + " Prediction :: " + str(result.prediction) + " Extent :: " + str(result.confidence))
            return result
    elif pair.v.brand is None or pair.v.brand.strip() == '':
        result = _check_product_description_for_one_product(pair, pair.v, pair.w.brand)
        if result.prediction == 1 or result.prediction == -1:
            logger.info("ALGO id : 4.2, pair matched " + pair.pair_id + " Prediction :: " + str(result.prediction) + " Extent :: " + str(result.confidence))
            return result
    elif pair.w.brand is None or pair.w.brand.strip() == '':
        result = _check_product_description_for_one_product(pair, pair.w, pair.v.brand)
        if result.prediction == 1 or result.prediction == -1:
            logger.info("ALGO id : 4.3, pair matched " + pair.pair_id + " Prediction :: " + str(result.prediction) + " Extent :: " + str(result.confidence))
            return result
    else:
        result = check_product_descripton_given_unmatched_brand(pair)
        if result.prediction == 1 or result.prediction == -1:
            logger.info("ALGO id : 4.4, pair matched " + pair.pair_id + " Prediction :: " + str(result.prediction) + " Extent :: " + str(result.confidence))
            return result
    return Prediction(0)


def aggregate_matcher(pair, algorithm_pref=None, dict_path=None):
    if algorithm_pref is None:
        logger.error("Aggregate Matcher called without any algorithm")
        return None
    if _if_both_product_not_defined(pair):
        return Prediction(0)
    if _if_either_product_not_defined(pair):
        return Prediction(0)
    # reinitializing dict object if a new file name is provided
    if dict_path is not None:
        global brand_list
        brand_list = BrandNameList(dict_path)
    for algorithm in algorithm_pref:
        if algorithm == C.matcher_algo_exact_match:
            p = _is_exact_match(pair)
            if p.prediction == 1:
                logger.info("ALGO id : 1, pair matched " + pair.pair_id)
                return p
        elif algorithm == C.matcher_algo_part_match:
            p = _is_part_match(pair)
            if p.prediction == 1:
                logger.info("ALGO id : 2, pair matched " + pair.pair_id)
                return p
        elif algorithm == C.matcher_algo_jaccard_match:
            p = _is_jaccard_match(pair)
            if p == p.prediction == 1:
                logger.info("ALGO id : 3, pair matched " + pair.pair_id)
                return p
        elif algorithm == C.matcher_algo_information_extraction:
            return _is_brand_match_on_description(pair)
    return Prediction(0)