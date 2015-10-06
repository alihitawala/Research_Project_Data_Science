__author__ = 'aliHitawala'


class Pair(object):
    def __init__(self, pair_id, v, w, is_match):
        self.pair_id = pair_id
        self.v = v
        self.w = w
        self.is_match = is_match
        self.brand_match = False

    def get_first_product(self):
        return self.v

    def get_second_product(self):
        return self.w

    def get_product(self, num):
        if num == 1:
            return self.v
        else:
            return self.w


class Product(object):
    def __init__(self,
                 product_id='',
                 brand='',
                 p_type='',
                 material='',
                 product_segment='',
                 product_name='',
                 product_type='',
                 manufacturer='',
                 product_length='',
                 gtin='',
                 platform='',
                 upc='',
                 size='',
                 actual_color='',
                 warranty='',
                 country_of_origin='',
                 description='',
                 features='',
                 color='',
                 mpn='',
                 category='',
                 product_width='',
                 long_description='',
                 height='',
                 warranty_info='',
                 item_id='',
                 composite_wood_code='',
                 screen_size='',
                 gender='',
                 multipack_indicator='',
                 has_mercury='',
                 battery_type='',
                 cpsc_regulated_indicator='',
                 average_customer_rating='',
                 release_date='',
                 assembly_required='',
                 fastener_type=''
                 ):
        self.product_id = product_id
        self.brand = brand
        self.p_type = p_type
        self.material = material
        self.product_segment = product_segment
        self.product_name = product_name
        self.product_type = product_type
        self.manufacturer = manufacturer
        self.product_length = product_length
        self.gtin = gtin
        self.platform = platform
        self.upc = upc
        self.size = size
        self.actual_color = actual_color
        self.warranty = warranty
        self.country_of_origin = country_of_origin
        self.description = description
        self.features = features
        self.color = color
        self.mpn = mpn
        self.category = category
        self.product_width = product_width
        self.long_description = long_description
        self.height = height
        self.warranty_info = warranty_info
        self.item_id = item_id,
        self.composite_wood_code = composite_wood_code
        self.screen_size=screen_size
        self.gender = gender
        self.multipack_indicator = multipack_indicator
        self.has_mercury = has_mercury
        self.battery_type = battery_type
        self.cpsc_regulated_indicator = cpsc_regulated_indicator
        self.average_customer_rating = average_customer_rating
        self.release_date = release_date
        self.assembly_required = assembly_required
        self.fastener_type = fastener_type