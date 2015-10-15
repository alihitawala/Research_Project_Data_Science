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
        return "N"
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
        pair_list[pair_id] = match
    count_matched_correct = 0.0
    count_matched_wrong = 0.0
    count_actual_Y_match = 0.0
    count_actual_Y_mismatch = 0.0
    count_on_which_no_prediction = 0.0
    count_total = 0.0
    for pair in all_pairs:
        pair_id = pair.pair_id
        result_actual = pair_list[pair_id]
        result_found = pair.brand_match
        count_total += 1
        if result_actual == result_found and result_actual != 'D':
            count_matched_correct += 1
            if result_actual == 'Y':
                count_actual_Y_match += 1
        elif result_found != 'D' and result_actual != 'D':
            count_matched_wrong += 1
            if result_actual == 'Y':
                count_actual_Y_mismatch += 1
            logger.warning("Brand name not matched correctly for pair id : " + pair.pair_id)
        if result_found == 'D':
            count_on_which_no_prediction += 1
    logger.info("Total brand name matched : " + str(count_matched_correct))
    precision = (count_matched_correct/(count_matched_wrong+count_matched_correct))*100
    recall = (count_actual_Y_match/ (count_actual_Y_match+count_actual_Y_mismatch)) * 100
    coverage = ((count_total-count_on_which_no_prediction)/ count_total) * 100
    logger.info("Recall :: " + str(recall))
    logger.info("Precision :: " + str(precision))
    logger.info("Coverage :: " + str(coverage))

def matcher():
    all_pairs = ProductObjectCreator.parse_file_get_pairs()
    count_matched = 0
    count_d_matched = 0
    count_total = 0
    for pair in all_pairs:
        is_match = match(pair)
        count_total += 1
        if is_match == 'Y':
            count_matched+=1
        if is_match == 'D':
            count_d_matched+=1
        pair.brand_match = is_match
    print "Matched : ", count_matched
    print "Don't know match : ", count_d_matched
    print "Total pair in consideration", count_total
    populate_results(all_pairs)
    get_precision(all_pairs)


def populate_results(all_pairs):
    result_file = open(C.results_file_name, 'w+')
    result_file.write('%-20s %20s %20s %20s %20s\n' % ("Pair_ID", "Product_1_Brand", "Product_2_Brand", "Matcher_Result", "Actual_result"))
    for pair in all_pairs:
        if pair.v is not None and pair.w is not None:
            result_file.write('%-20s %20s %20s %20s %20s\n' % (pair.pair_id, pair.v.brand, pair.w.brand, str(pair.brand_match), str(pair.is_match)))
    result_file.close()

matcher()