__author__ = 'aliHitawala'
import Constants as C
from Product import Product, Pair
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('Start reading database')


def getJsonToken(data, tag, pid=-1):
    token = ''
    try :
        token = unicodeToString(data[tag][0])
    except:
        #logger.error("No matching token found for product id  : " + pid + tag)
        pass
    return token

def parse_json_create_object(data, pid):
    brand = getJsonToken(data, C.json_brand_tag, pid=pid)
    p_type = getJsonToken(data, C.json_p_type_tag, pid=pid)
    material = getJsonToken(data, C.json_material_tag, pid=pid)
    product_segment = getJsonToken(data, C.json_product_segment_tag, pid=pid)
    product_name = getJsonToken(data, C.json_product_name_tag, pid=pid)
    product_type = getJsonToken(data, C.json_product_type_tag, pid=pid)
    manufacturer = getJsonToken(data, C.json_manufacturer_tag, pid=pid)
    product_length = getJsonToken(data, C.json_product_length_tag, pid=pid)
    gtin = getJsonToken(data, C.json_gtin_tag, pid=pid)
    upc = getJsonToken(data, C.json_upc_tag, pid=pid)
    size = getJsonToken(data, C.json_size_tag, pid=pid)
    actual_color = getJsonToken(data, C.json_actual_color_tag, pid=pid)
    warranty = getJsonToken(data, C.json_warranty_tag, pid=pid)
    country_of_origin = getJsonToken(data, C.json_country_of_origin_tag, pid=pid)
    description = getJsonToken(data, C.json_description_tag, pid=pid)
    features = getJsonToken(data, C.json_features_tag, pid=pid)
    color = getJsonToken(data, C.json_color_tag, pid=pid)
    mpn = getJsonToken(data, C.json_mpn_tag, pid=pid)
    category = getJsonToken(data, C.json_category_tag, pid=pid)
    product_width = getJsonToken(data, C.json_product_width_tag, pid=pid)
    long_description = getJsonToken(data, C.json_long_description_tag, pid=pid)
    height = getJsonToken(data, C.json_height_tag, pid=pid)
    warranty_info = getJsonToken(data, C.json_warranty_info_tag, pid=pid)
    item_id = getJsonToken(data, C.json_item_id_tag, pid=pid)
    composite_wood_code = getJsonToken(data, C.json_composite_wood_code_tag, pid=pid)
    screen_size = getJsonToken(data, C.json_screen_size_tag, pid=pid)
    gender = getJsonToken(data, C.json_gender_tag, pid=pid)
    multipack_indicator = getJsonToken(data, C.json_multipack_indicator_tag, pid=pid)
    has_mercury = getJsonToken(data, C.json_has_mercury_tag, pid=pid)
    battery_type = getJsonToken(data, C.json_battery_type_tag, pid=pid)
    cpsc_regulated_indicator = getJsonToken(data, C.json_cpsc_regulated_indicator_tag, pid=pid)
    average_customer_rating = getJsonToken(data, C.json_average_customer_rating_tag, pid=pid)
    release_date = getJsonToken(data, C.json_release_date_tag, pid=pid)
    assembly_required = getJsonToken(data, C.json_assembly_required_tag, pid=pid)
    fastener_type = getJsonToken(data, C.json_fastener_type_tag, pid=pid)

    keys = [unicodeToString(x) for x in data.keys()]
    not_in_constant = [x for x in keys if x not in C.all_json_keys]
    if len(not_in_constant) > 0:
        str_msg = "Keys missing in the structure for product id " + pid + " : " + str(not_in_constant)
        logger.warning(str_msg)
    return Product(product_id=pid,
                   brand=brand,
                   p_type=p_type,
                   material=material,
                   product_segment = product_segment,
                   product_name = product_name,
                   product_type = product_type,
                   manufacturer = manufacturer,
                   product_length = product_length,
                   gtin = gtin,
                   upc = upc,
                   size = size,
                   actual_color = actual_color,
                   warranty = warranty,
                   country_of_origin = country_of_origin,
                   description=description,
                   features=features,
                   color=color,
                   mpn=mpn,
                   category=category,
                   product_width=product_width,
                   long_description=long_description,
                   height=height,
                   warranty_info=warranty_info,
                   item_id=item_id,
                   composite_wood_code=composite_wood_code,
                   screen_size=screen_size,
                   gender=gender,
                   multipack_indicator=multipack_indicator,
                   has_mercury=has_mercury,
                   battery_type=battery_type,
                   cpsc_regulated_indicator=cpsc_regulated_indicator,
                   average_customer_rating=average_customer_rating,
                   release_date=release_date,
                   assembly_required=assembly_required,
                   fastener_type=fastener_type)


def get_product_object(product_id_v, json_v):
    pid = product_id_v
    try:
        data = json.loads(json_v)
        return parse_json_create_object(data, pid)
    except:
        logger.error("Parsing failed for JSON, for product id : " + pid)


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
        is_match = match_str == 'MATCH'
        product_v = get_product_object(product_id_v, json_v)
        product_w = get_product_object(product_id_w, json_w)
        a = Pair(pair_id, product_v, product_w, is_match)
        pair_list.append(a)
    return pair_list


def parse_file_get_pairs():
    all_pairs = [line.rstrip('\n') for line in open(C.all_pairs_file_name)]
    return parse_tokens(all_pairs)


def unicodeToString(unicode):
    if unicode is None:
        return unicode
    else:
        return unicode.encode('ascii','ignore')

parse_file_get_pairs()