#******************************************************************************
# Copyright (c) 2011 Pason Systems Corp.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
#******************************************************************************

import sys
import datetime
import pytz

sys.path.append("../src/wtl")

import unittest

import wtl.control_prim
import wtl.utils
import wtl.script

class UtilsTest(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        
        wtl.script.Script.init()
                    
    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_encode_compare_strings_different(self):    
        self.assertFalse(wtl.utils.compare_strings('123', '12'))
        self.assertFalse(wtl.utils.compare_strings('123', '1234'))
        self.assertFalse(wtl.utils.compare_strings('123', '321'))
        self.assertFalse(wtl.utils.compare_strings('123', 'a123'))
        self.assertFalse(wtl.utils.compare_strings('123', ''))
        self.assertFalse(wtl.utils.compare_strings('1.3', '1x3', enable_regex=False))
        self.assertFalse(wtl.utils.compare_strings('1.3', '13', enable_regex=True))
        self.assertFalse(wtl.utils.compare_strings('1*3', '1245', enable_regex=True))
        self.assertFalse(wtl.utils.compare_strings('123+4', '123+4', enable_regex=True))
        self.assertFalse(wtl.utils.compare_strings('123(4)', '123(4)', enable_regex=True))
        
    def test_encode_compare_strings_same(self):
        self.assertTrue(wtl.utils.compare_strings('123', '123'))
        self.assertTrue(wtl.utils.compare_strings('123', '123', enable_regex=True))
        self.assertTrue(wtl.utils.compare_strings('1.3', '1x3', enable_regex=True))
        self.assertTrue(wtl.utils.compare_strings('1.*3', '13', enable_regex=True))
        self.assertTrue(wtl.utils.compare_strings('1.*3', '1abcdf3', enable_regex=True))
        self.assertTrue(wtl.utils.compare_strings('.*', '', enable_regex=True))
        self.assertTrue(wtl.utils.compare_strings('.*', 'jdjuhgeununbdufg', enable_regex=True))
        self.assertTrue(wtl.utils.compare_strings('1*3', '111111111111113', enable_regex=True))
        self.assertTrue(wtl.utils.compare_strings('2013-02-21T17:23:46.2494363+11:00', '2013-02-21T17:23:46.2494363+11:00'))
        self.assertTrue(wtl.utils.compare_strings('123+4', '123+4'))
        self.assertTrue(wtl.utils.compare_strings('123(4)', '123(4)'))

    def test_encode_compare_strings30(self):
        self.assertTrue(wtl.utils.compare_strings('1&x&3', '1abcd3', enable_regex=True))
        self.assertTrue('abcd' == wtl.utils.get_variable_value('x'))

    def test_encode_compare_strings31(self):
        self.assertTrue(wtl.utils.compare_strings('&wwwww&1234&x&56789&y&0&zzz&', 'w1234x56789y0z', enable_regex=True))
        self.assertTrue('w' == wtl.utils.get_variable_value('wwwww'))
        self.assertTrue('x' == wtl.utils.get_variable_value('x'))
        self.assertTrue('y' == wtl.utils.get_variable_value('y'))
        self.assertTrue('z' == wtl.utils.get_variable_value('zzz'))

    def test_encode_compare_strings32(self):
        self.assertTrue(wtl.utils.compare_strings('&x&1.*2&y&', 'x1878787878787878782y', enable_regex=True))
        self.assertTrue('x' == wtl.utils.get_variable_value('x'))
        self.assertTrue('y' == wtl.utils.get_variable_value('y'))

    def test_encode_compare_strings33(self):
        self.assertTrue(wtl.utils.compare_strings('name&xx&xname123name&yy&xname','nameAAAxname123nameBBBxname', enable_regex=True))
        self.assertTrue('AAA' == wtl.utils.get_variable_value('xx'))
        self.assertTrue('BBB' == wtl.utils.get_variable_value('yy'))

    def test_process_string(self):
        #General 
        self.assertTrue(wtl.utils.process_string("") == "")
        self.assertTrue(wtl.utils.process_string("ab") == "ab")

        #Condition 
        self.assertTrue(wtl.utils.process_string("~^ab") == "^ab")
        self.assertTrue(wtl.utils.process_string("a~^b") == "a^b")
        self.assertTrue(wtl.utils.process_string("ab~^") == "ab^")
        self.assertTrue(wtl.utils.process_string("^ab") == "")
        self.assertTrue(wtl.utils.process_string("a^b") == "")
        self.assertTrue(wtl.utils.process_string("ab^") == "")
        self.assertTrue(wtl.utils.process_string("^^ab") == "")
        self.assertTrue(wtl.utils.process_string("a^^b") == "")
        self.assertTrue(wtl.utils.process_string("ab^^") == "")
        self.assertTrue(wtl.utils.process_string("^1==1?xxx:yyy^ab") == "xxxab")
        self.assertTrue(wtl.utils.process_string("a^1==1?xxx:yyy^b") == "axxxb")
        self.assertTrue(wtl.utils.process_string("ab^1==1?xxx:yyy^") == "abxxx")
        self.assertTrue(wtl.utils.process_string("^1==2?xxx:yyy^ab") == "yyyab")
        self.assertTrue(wtl.utils.process_string("a^1==2?xxx:yyy^b") == "ayyyb")
        self.assertTrue(wtl.utils.process_string("ab^1==2?xxx:yyy^") == "abyyy")
        wtl.utils.set_variable_value('a', '3')
        self.assertTrue(wtl.utils.process_string("ab^$a$==3?xxx:yyy^") == "abxxx")
        self.assertTrue(wtl.utils.process_string("ab^$a$==2?xxx:yyy^") == "abyyy")

        #Files
        self.assertTrue(wtl.utils.process_string("~#ab") == "#ab")
        self.assertTrue(wtl.utils.process_string("a~#b") == "a#b")
        self.assertTrue(wtl.utils.process_string("ab~#") == "ab#")
        self.assertTrue(wtl.utils.process_string("#ab") == "")
        self.assertTrue(wtl.utils.process_string("a#b") == "")
        self.assertTrue(wtl.utils.process_string("ab#") == "")
        self.assertTrue(wtl.utils.process_string("##ab") == "")
        self.assertTrue(wtl.utils.process_string("a##b") == "")
        self.assertTrue(wtl.utils.process_string("ab##") == "")
        f = open('witsmltempfile', 'w')
        f.write('0123456789\n0123456789')
        f.close()
        self.assertTrue(wtl.utils.process_string("#witsmltempfile#ab") == "0123456789\n0123456789ab")
        self.assertTrue(wtl.utils.process_string("a#witsmltempfile#b") == "a0123456789\n0123456789b")
        self.assertTrue(wtl.utils.process_string("ab#witsmltempfile#") == "ab0123456789\n0123456789")

        #Variables
        self.assertTrue(wtl.utils.process_string("~$ab") == "$ab")
        self.assertTrue(wtl.utils.process_string("a~$b") == "a$b")
        self.assertTrue(wtl.utils.process_string("ab~$") == "ab$")
        self.assertTrue(wtl.utils.process_string("$ab") == "")
        self.assertTrue(wtl.utils.process_string("a$b") == "")
        self.assertTrue(wtl.utils.process_string("ab$") == "")
        self.assertTrue(wtl.utils.process_string("$$ab") == "")
        self.assertTrue(wtl.utils.process_string("a$$b") == "")
        self.assertTrue(wtl.utils.process_string("ab$$") == "")
        wtl.utils.set_variable_value('var', '123')
        self.assertTrue(wtl.utils.process_string("$var$ab") == "123ab")
        self.assertTrue(wtl.utils.process_string("a$var$b") == "a123b")
        self.assertTrue(wtl.utils.process_string("ab$var$") == "ab123")
        wtl.utils.set_variable_value('var', '123')
        self.assertTrue(wtl.utils.process_string("$var$ab") == "123ab")
        self.assertTrue(wtl.utils.process_string("a$var$b") == "a123b")
        self.assertTrue(wtl.utils.process_string("ab$var$") == "ab123")

        #Combined
        f = open('witsmltempfile2', 'w')
        f.write('$var1$')
        f.close()
        wtl.utils.set_variable_value('var1', 123)
        wtl.utils.set_variable_value('var2', 456)
        self.assertTrue(wtl.utils.process_string("a^1==1?$var2$:#witsmltempfile2#^b") == "a456b")
        self.assertTrue(wtl.utils.process_string("a^1==2?$var2$:#witsmltempfile2#^b") == "a123b")

    def test_encode_options_in_bad_dictionary(self):
        x = wtl.utils.encode_options_in(23)
        self.assertTrue(x == '')

    def test_encode_options_in_empty_dictionary(self):
        x = wtl.utils.encode_options_in({})
        self.assertTrue(x == '')

    def test_encode_options_in_one_option(self):
        x = wtl.utils.encode_options_in({'returnElements':'id-only'})
        self.assertTrue(x == 'returnElements=id-only')

    def test_encode_options_in_two_options(self):
        x = wtl.utils.encode_options_in({'returnElements':'id-only','maxReturnNodes':'100'})
        self.assertTrue(x == 'maxReturnNodes=100;returnElements=id-only')
        
    def test_iso_to_utc_with_offset(self):
        iso_str = "2009-06-21T05:45:00-05:00"
        jun = datetime.datetime(2009,6,21,5,45,0)

        dt = wtl.utils.iso_to_utc(iso_str)
        self.assertEqual(dt, pytz.timezone("US/Central").localize(jun))
        self.assertEqual(dt.utcoffset(), datetime.timedelta(0))
        
    def test_iso_to_utc_with_Z(self):
        "Check that an ISO string with Z as its timezone parses"
        iso_str = "2009-12-21T17:47Z"
        dec = datetime.datetime(2009,12,21,17,47,0)
        
        dt = wtl.utils.iso_to_utc(iso_str)
        self.assertEqual(dt, pytz.utc.localize(dec))
        self.assertEqual(dt.utcoffset(), datetime.timedelta(0))

    def test_iso_to_utc_has_no_tz_info_should_pass_when_forced(self):
        "Check that an ISO string w/o timezone info parses when forced"
        iso_str = "2009-12-21T17:47"
        dec = datetime.datetime(2009,12,21,17,47,0)

        dt = wtl.utils.iso_to_utc(iso_str, interpretInTimezone=True)
        self.assertEqual(dt, pytz.utc.localize(dec))
        self.assertEqual(dt.utcoffset(), datetime.timedelta(0))
        
    def test_iso_to_utc_exceptions(self):
        # No tz and not forced
        self.assertRaises(Exception,wtl.utils.iso_to_utc,"2009-12-21T17:47")
        # Bad parameter passed
        self.assertRaises(Exception,wtl.utils.iso_to_utc,"25")
        self.assertRaises(Exception,wtl.utils.iso_to_utc,25)
        
    
    def test_iso_to_localized_calgary_without_dst(self):
        "Check that localization accounts for DST (or lack thereof)"
        cgy_dec = wtl.utils.iso_to_localized("2009-12-21T17:47:00", "Canada/Mountain", interpretInTimezone=True)

        self.assertEqual(cgy_dec.utcoffset(), datetime.timedelta(hours=-7))

    def test_iso_to_localized_australia_no_dst(self):
        "Check that localization works where there is no DST"
        aus_jun = wtl.utils.iso_to_localized("2009-06-21T05:45:00", "Australia/Brisbane", interpretInTimezone=True)
        self.assertEqual(aus_jun.utcoffset(), datetime.timedelta(hours=10))

        aus_dec = wtl.utils.iso_to_localized("2009-12-21T17:47:00", "Australia/Brisbane", interpretInTimezone=True)
        self.assertEqual(aus_dec.utcoffset(), datetime.timedelta(hours=10))

    def test_iso_to_localized_esceptions(self):
        "Native date fails - Ensure that the function will not accept timezone agnostic datetimes"
        dt = "2009-10-10T10:00:00"
        self.assertRaises(ValueError, wtl.utils.iso_to_localized, dt, "US/Central")
        # Bad parameter passed
        self.assertRaises(Exception, wtl.utils.iso_to_localized, 25, "Australia/Brisbane", interpretInTimezone=True)

    def test_iso_to_localized_naive_date_passes_when_forced(self):
        """
        Ensure that an ISO string w/o timezone info parses when forced and that
        empty timezone strings imply UTC
        """
        iso_str = "2009-12-21T17:47"
        dec = datetime.datetime(2009,12,21,17,47,0)
        
        dt = wtl.utils.iso_to_localized(iso_str, "", interpretInTimezone=True)
        self.assertEqual(dt, pytz.utc.localize(dec))
        self.assertEqual(dt.utcoffset(), datetime.timedelta(0))
        
    def test_datetime_to_iso_utc_preserve_timezone(self):      
        jun = datetime.datetime(2009,6,21,5,45,0)
        expected = "2009-06-21T05:45:00+00:00"

        "Check that a UTC datetime is printed with an offset of 0"
        iso_str = wtl.utils.datetime_to_iso(pytz.utc.localize(jun))
        self.assertEqual(iso_str, expected)

    def test_datetime_to_iso_utc_drop_timezone(self):
        dec = datetime.datetime(2009,12,21,17,47,0)
        expected = "2009-12-21T17:47:00Z"

        "Check that a UTC datetime is printed with the timezone identifier Z"
        iso_str = wtl.utils.datetime_to_iso(pytz.utc.localize(dec), False)
        self.assertEqual(iso_str, expected)

    def test_datetime_to_iso_localized_preserve_timezone(self):
        jun = datetime.datetime(2009,6,21,5,45,0)
        expected = "2009-06-21T05:45:00-05:00"

        "Check that a localized datetime is printed with its offset from UTC"
        iso_str = wtl.utils.datetime_to_iso(pytz.timezone("US/Central").localize(jun))
        self.assertEqual(iso_str, expected)

    def test_datetime_to_iso_localized_drop_timezone(self):
        dec = datetime.datetime(2009,12,21,17,47,0)
        expected = "2009-12-21T17:47:00Z"

        "Check that a localized datetime is converted to UTC"
        iso_str = wtl.utils.datetime_to_iso(pytz.timezone("US/Central").localize(dec), False)
        expected = "2009-12-21T23:47:00Z"
        self.assertEqual(iso_str, expected)

    def test_datetime_to_iso_naive_date_fails(self):
        "Check that the function will not accept timezone agnostic datetimes"
        dt = datetime.datetime.now()
        self.assertRaises(ValueError, wtl.utils.datetime_to_iso, dt)

if __name__ == '__main__':
    unittest.main()
