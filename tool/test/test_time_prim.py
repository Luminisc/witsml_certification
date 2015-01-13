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

sys.path.append("../src/wtl")

import unittest

import wtl.time_prim
import wtl.script

class UtilsTest(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        
        wtl.script.Script.init()
        wtl.script.Script.get_current_script().name = "123"
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_check_timestamp_equals(self):
        self.assertTrue(wtl.time_prim.check_timestamp_equals("2012-07-31T17:34:01Z", "2012-07-31T17:34:01Z"))
        self.assertTrue(wtl.time_prim.check_timestamp_equals("2012-07-31T20:00-07:00", "2012-08-01T03:00Z"))
        self.assertRaises(wtl.script.ScriptEvent,wtl.time_prim.check_timestamp_equals, "2012-07-31T17:34Z", "2012-07-31T17:35Z")
        self.assertRaises(Exception,wtl.time_prim.check_timestamp_equals, "2012-07-31T20:00-07:00", 21)
        
    def test_check_timestamp_lessthan(self):
        self.assertTrue(wtl.time_prim.check_timestamp_lessthan("2012-07-31T17:34Z", "2012-07-31T17:35Z"))
        self.assertRaises(wtl.script.ScriptEvent,wtl.time_prim.check_timestamp_lessthan, "2012-07-31T17:34:01Z", "2012-07-31T17:34:01Z")
        self.assertRaises(wtl.script.ScriptEvent,wtl.time_prim.check_timestamp_lessthan, "2012-07-31T17:35Z", "2012-07-31T17:34Z")
        self.assertRaises(wtl.script.ScriptEvent,wtl.time_prim.check_timestamp_lessthan, "2012-07-31T20:00-07:00", "2012-08-01T03:00Z")
        self.assertRaises(Exception,wtl.time_prim.check_timestamp_lessthan, "2012-07-31T17:34Z", 21)
        
    def test_check_timestamp_lessthan_equalto(self):
        self.assertTrue(wtl.time_prim.check_timestamp_lessthan_equalto("2012-07-31T17:34Z", "2012-07-31T17:35Z"))
        self.assertTrue(wtl.time_prim.check_timestamp_lessthan_equalto("2012-07-31T17:34:01Z", "2012-07-31T17:34:01Z"))
        self.assertTrue(wtl.time_prim.check_timestamp_lessthan_equalto("2012-07-31T20:00-07:00", "2012-08-01T03:00Z"))
        self.assertTrue(wtl.time_prim.check_timestamp_lessthan_equalto("2012-07-31T19:59:59-07:00", "2012-08-01T03:00Z"))
        self.assertRaises(wtl.script.ScriptEvent,wtl.time_prim.check_timestamp_lessthan_equalto, "2012-07-31T17:35Z", "2012-07-31T17:34Z")
        self.assertRaises(Exception, wtl.time_prim.check_timestamp_lessthan_equalto, 21, "2012-07-31T17:35Z")
        
    def test_check_timestamp_greaterthan(self):
        self.assertTrue(wtl.time_prim.check_timestamp_greaterthan("2012-07-31T17:35Z", "2012-07-31T17:34Z"))
        self.assertTrue(wtl.time_prim.check_timestamp_greaterthan("2012-08-01T03:00:01Z","2012-07-31T20:00-07:00"))  
        self.assertRaises(wtl.script.ScriptEvent,wtl.time_prim.check_timestamp_greaterthan, "2012-07-31T17:34Z", "2012-07-31T17:35Z")
        self.assertRaises(wtl.script.ScriptEvent,wtl.time_prim.check_timestamp_greaterthan, "2012-07-31T17:34:01Z", "2012-07-31T17:34:01Z")
        self.assertRaises(wtl.script.ScriptEvent,wtl.time_prim.check_timestamp_greaterthan, "2012-08-01T03:00Z","2012-07-31T20:00-07:00")
        self.assertRaises(Exception,wtl.time_prim.check_timestamp_greaterthan, 2,"2012-07-31T20:00-07:00")
        
    def test_check_timestamp_greaterthan_equalto(self):
        self.assertTrue(wtl.time_prim.check_timestamp_greaterthan_equalto("2012-07-31T17:34:01Z", "2012-07-31T17:34:01Z"))
        self.assertTrue(wtl.time_prim.check_timestamp_greaterthan_equalto("2012-07-31T17:35Z", "2012-07-31T17:34Z"))
        self.assertTrue(wtl.time_prim.check_timestamp_greaterthan_equalto("2012-07-31T20:00-07:00", "2012-08-01T03:00Z"))
        self.assertTrue(wtl.time_prim.check_timestamp_greaterthan_equalto("2012-08-01T03:00:01Z","2012-07-31T20:00-07:00"))
        self.assertRaises(wtl.script.ScriptEvent,wtl.time_prim.check_timestamp_greaterthan_equalto, "2012-07-31T17:34Z", "2012-07-31T17:35Z")
        self.assertRaises(wtl.script.ScriptEvent,wtl.time_prim.check_timestamp_greaterthan_equalto, "2012-07-31T19:59:59-07:00", "2012-08-01T03:00Z")  
        self.assertRaises(wtl.script.ScriptEvent,wtl.time_prim.check_timestamp_greaterthan_equalto, "2012-07-31T20:00-07:00", "")

    def test_add_seconds_to_timestamp(self):
        self.assertTrue(wtl.time_prim.add_seconds_to_timestamp("2012-07-31T20:00-07:00",0) == "2012-08-01T03:00:00Z")
        self.assertTrue(wtl.time_prim.add_seconds_to_timestamp("2012-07-31T20:00-07:00",5) == "2012-08-01T03:00:05Z")
        self.assertTrue(wtl.time_prim.add_seconds_to_timestamp("2012-08-01T03:00:00Z",0) == "2012-08-01T03:00:00Z")
        self.assertTrue(wtl.time_prim.add_seconds_to_timestamp("2012-08-01T03:00:00Z",5) == "2012-08-01T03:00:05Z")
        self.assertTrue(wtl.time_prim.add_seconds_to_timestamp("2012-08-01T03:00:00Z",60) == "2012-08-01T03:01:00Z")
        self.assertTrue(wtl.time_prim.add_seconds_to_timestamp("2012-08-01T03:00:00Z",3600) == "2012-08-01T04:00:00Z")
        self.assertTrue(wtl.time_prim.add_seconds_to_timestamp("2012-08-01T03:00:00Z",24*3600) == "2012-08-02T03:00:00Z")
        self.assertRaises(Exception, wtl.time_prim.add_seconds_to_timestamp, 27,24)
        
    def test_subtract_seconds_to_timestamp(self):
        self.assertTrue(wtl.time_prim.subtract_seconds_to_timestamp("2012-07-31T20:00-07:00",0) == "2012-08-01T03:00:00Z")
        self.assertTrue(wtl.time_prim.subtract_seconds_to_timestamp("2012-07-31T20:00-07:00",5) == "2012-08-01T02:59:55Z")
        self.assertTrue(wtl.time_prim.subtract_seconds_to_timestamp("2012-08-01T03:00:00Z",0) == "2012-08-01T03:00:00Z")
        self.assertTrue(wtl.time_prim.subtract_seconds_to_timestamp("2012-08-01T03:00:00Z",5) == "2012-08-01T02:59:55Z")
        self.assertTrue(wtl.time_prim.subtract_seconds_to_timestamp("2012-08-01T03:00:00Z",60) == "2012-08-01T02:59:00Z")
        self.assertTrue(wtl.time_prim.subtract_seconds_to_timestamp("2012-08-01T03:00:00Z",3600) == "2012-08-01T02:00:00Z")
        self.assertTrue(wtl.time_prim.subtract_seconds_to_timestamp("2012-08-01T03:00:00Z",24*3600) == "2012-07-31T03:00:00Z")
        self.assertRaises(Exception, wtl.time_prim.subtract_seconds_to_timestamp, 27,24)

    def test_get_current_datetime_string(self):
        iso_str = "2009-06-21T05:45:00-05:00"
        dt1 = wtl.time_prim.get_current_datetime_string()
        dt2 = wtl.time_prim.get_current_datetime_string()
        self.assertTrue(wtl.time_prim.check_timestamp_greaterthan_equalto(dt2, dt1))
        self.assertTrue(wtl.time_prim.check_timestamp_greaterthan(dt1, iso_str))

        
if __name__ == '__main__':
    unittest.main()
