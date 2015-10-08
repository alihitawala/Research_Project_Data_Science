__author__ = 'aliHitawala'
import ProductObjectCreator
from BrandNameDictionary import BrandNameList
import Constants as C
import logging
import Matcher

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('Started the brand name matcher..')

brand_list = BrandNameList()


def match(pair):
    if pair.v is None or pair.w is None:
        logger.warning("Atleast one of the product is not parsed correctly in pair " + pair.pair_id)
        return False
    result = Matcher.aggregate_matcher(pair,
        algorithm_pref=[C.matcher_algo_exact_match, C.matcher_algo_part_match,
                        C.matcher_algo_jaccard_match, C.matcher_algo_information_extraction])
    return result


def get_precision(all_pairs):
    lines = [line.rstrip('\n') for line in open(C.brand_name_golden_data_file_name)]
    pair_list = {}
    for line in lines:
        tokens = [x.strip() for x in line.split('?')]
        pair_id = tokens.pop(0)
        match = tokens.pop(0)
        is_match = match == 'Y'
        pair_list[pair_id] = is_match
    count_matched_correct = 0.0
    count_matched_wrong = 0.0
    for pair in all_pairs:
        pair_id = pair.pair_id
        result_actual = pair_list[pair_id]
        result_found = pair.brand_match
        if result_actual == result_found:
            count_matched_correct+=1
        else:
            count_matched_wrong+=1
            logger.warning("Brand name not matched correctly for pair id : " + pair.pair_id)
    percent = (count_matched_correct/(count_matched_wrong+count_matched_correct))*100
    print percent

def matcher():
    all_pairs = ProductObjectCreator.parse_file_get_pairs()
    count_matched = 0;
    for pair in all_pairs:
        is_match = match(pair)
        if is_match:
            pair.brand_match = True
            count_matched+=1
    print "Matched : ", count_matched
    populate_results(all_pairs)
    get_precision(all_pairs)


def populate_results(all_pairs):
    result_file = open(C.results_file_name, 'w+')
    result_file.write('%-20s %20s %20s %20s %20s %20s %20s\n' % ("Pair_ID", "Product_1_ID", "Product_1_Brand", "Product_2_ID", "Product_2_Brand", "Matcher_Result", "Actual_result"))
    for pair in all_pairs:
        if pair.v is not None and pair.w is not None:
            result_file.write('%-20s %20s %20s %20s %20s %20s %20s\n' % (pair.pair_id, pair.v.product_id, pair.v.brand, pair.w.product_id, pair.w.brand, str(pair.brand_match), str(pair.is_match)))
    result_file.close()

matcher()