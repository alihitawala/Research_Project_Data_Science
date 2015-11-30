
from nose.tools import *
import Independent_Study
import Independent_Study.Main as Main

def setup():
    print "SETUP!"

def test_product_json() :
    Main.brand_name_match('{"Condition":["New"],"Brand":["AT&T"],"Product Short Description":["AT&T 1856 Corded Phone"],"Actual Color":["White"],"Product Segment":["Electronics"],"Color":["White"],"Product Name":["AT&T 1856 Corded Phone"],"Product Type":["Corded Phones"],"Has Warranty":["Y"],"Category":["Corded Phones"],"Manufacturer":["AT&T"],"Product Long Description":["AT&T 1856 Corded Phone"],"GTIN":["00650530015977"],"Warranty Information":["1 year warranty"],"UPC":["650530015977"]}',
                          '{"Product Type":["Answering Machines & Caller ID"],"Manufacturer Part Number":["AT1856"],"Product Name":["Vtech Communications Inc AT1856 Speakerphone With Caller I.D. Corded - Speakerphone Answering System"],"Brand":["VTech"],"Manufacturer":["VTech"],"Product Long Description":["<br/>&#8226; Speakerphone operates during power failures no batteries needed<br/>&#8226; Receiver speakerphone and ringer volume control<br/>&#8226; 3 one-touch memory buttons 9 number speed dial with mute flash redial and chain dialing<br/>&#8226; Adjustable LCD contrast 50 name/number caller ID history visual message waiting and new call indicator with entry removal button and display dial<br/>&#8226; Answering system features 19 minutes of digital recording time remote access with toll saver call screening/intercept time/day stamp audible message alert message memory guard for power failures voice prompts and memo recording<br/>&#8226; Table/wall mountable<br/>&#8226; 7.56 width x 7.52 depth x 4.65 height<br/>&#8226; Weighs 1.5 pounds<br/>&#8226; In a gift box.<br/>&#8226; Size In=3/4"],"Item ID":["10242673"],"Product Segment":["Electronics"],"UPC":["650530015977"]}')

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"
    