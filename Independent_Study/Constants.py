__author__ = 'aliHitawala'

brand_name_list_file_name = "files/brands.electronics-frank.txt"
brand_name_list_file_name_freq = "files/all_brand_dic.txt"
# all_pairs_file_name = "files/sample_elec_pairs.txt"
all_pairs_file_name = "files/elec_pairs_2K.txt"
results_file_name = "files/results.txt"
# brand_name_golden_data_file_name = "files/brand_name_match_golden_result"
brand_name_golden_data_file_name = "files/brand_name_match_golden_result_400"

matcher_algo_exact_match = "EXACT_MATCH"
matcher_algo_part_match = "PART_MATCH"
matcher_algo_jaccard_match = "JACCARD_MATCH"
matcher_algo_information_extraction = "INFORMATION_EXTRACTION"
threshold_edit_distance_measure = 0.9
threshold_dictionary_part_weighted_measure = 100
threshold_jaccard_measure = 0.9
threshold_brand_value = 1000
threshold_brand_value_lower_confidence = 200

regex_to_tokenize_words_into_set = ' |; |, |\*|\n|<|>|-|/|:|\''
json_brand_tag = "Brand"
json_p_type_tag = "Type"
json_material_tag = "Material"
json_product_segment_tag = "Product Segment"
json_product_name_tag = "Product Name"
json_product_type_tag = "Product Type"
json_manufacturer_tag = "Manufacturer"
json_product_length_tag = "Assembled Product Length"
json_gtin_tag = "GTIN"
json_platform_tag = "Video Game Platform"
json_upc_tag = "UPC"
json_size_tag = "Size"
json_warranty_tag = "Warranty Length"
json_country_of_origin_tag = "Country of Origin: Components"
json_description_tag = "Product Short Description"
json_actual_color_tag = "Actual Color"
json_features_tag = "Features"
json_color_tag = "Color"
json_mpn_tag = "Manufacturer Part Number"
json_category_tag = "Category"
json_product_width_tag = "Assembled Product Width"
json_long_description_tag = "Product Long Description"
json_height_tag = "Assembled Product Height"
json_warranty_info_tag = "Warranty Information"
json_item_id_tag = "Item ID"
json_screen_size_tag = "Screen Size"
json_gender_tag = "Gender"
json_multipack_indicator_tag = "Multipack Indicator"
json_composite_wood_code_tag = "Composite Wood Code"
json_has_mercury_tag = "Has Mercury"
json_battery_type_tag = "Battery Type"
json_cpsc_regulated_indicator_tag = "CPSC-Regulated Indicator"
json_average_customer_rating_tag = "Average Customer Rating"
json_release_date_tag = "Release Date"
json_assembly_required_tag = "Assembly Required"
json_fastener_type_tag = "Fastener Type"
all_json_keys = [
    json_brand_tag,
    json_p_type_tag,
    json_material_tag,
    json_product_segment_tag,
    json_product_name_tag,
    json_product_type_tag,
    json_manufacturer_tag,
    json_product_length_tag,
    json_gtin_tag,
    json_platform_tag,
    json_upc_tag,
    json_size_tag,
    json_warranty_tag,
    json_country_of_origin_tag,
    json_description_tag,
    json_actual_color_tag,
    json_features_tag,
    json_color_tag,
    json_mpn_tag,
    json_category_tag,
    json_product_width_tag,
    json_long_description_tag,
    json_height_tag,
    json_warranty_info_tag,
    json_item_id_tag,
    json_composite_wood_code_tag,
    json_screen_size_tag,
    json_gender_tag,
    json_multipack_indicator_tag,
    json_has_mercury_tag,
    json_battery_type_tag,
    json_cpsc_regulated_indicator_tag,
    json_average_customer_rating_tag,
    json_release_date_tag,
    json_assembly_required_tag,
    json_fastener_type_tag
]
