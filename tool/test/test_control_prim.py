# Copyright (c) 2012 Energistics

import sys
import time

sys.path.append('../src/wtl')

import unittest
import mocking

import wtl.control_prim
import wtl.capability
import wtl.globals

INTERVAL_TEST_TOLERANCE = 0.25

WITSML_STORE_CAP = """<capServers xmlns="http://www.witsml.org/api/131" version="1.4.1">
    <capServer apiVers="1.4.1">
        <contact>
            <name>The Store Name</name>
            <email>Support@TheStore.TheCom</email>
            <phone />
        </contact>
        <description>Store Description</description>
        <name>Store Name</name>
        <vendor>The Vendor</vendor>
        <version>The Version</version>
        <schemaVersion>1.4.1.1</schemaVersion>
        <changeDetectionPeriod>2</changeDetectionPeriod>
        <growingTimeoutPeriod dataObject="log">1</growingTimeoutPeriod>
        <growingTimeoutPeriod dataObject="mudLog">3</growingTimeoutPeriod>
        <changeDetectionPeriod>200</changeDetectionPeriod>
        <cascadedDelete>true</cascadedDelete>
        <compressionMethod>gzip</compressionMethod>
        <function name="WMLS_GetFromStore">
            <dataObject>well</dataObject>
        </function>
        <function name="WMLS_GetBaseMsg" />
    </capServer>
</capServers>
"""

def test_interval(start, end, expected):
    if (((end - start) > (expected - INTERVAL_TEST_TOLERANCE)) and ((end - start) < (expected + INTERVAL_TEST_TOLERANCE))):
        return True
    return False

class ConfigTest(unittest.TestCase, mocking.MockingTestMixin):
    def setUp(self):
        unittest.TestCase.setUp(self)
        mocking.MockingTestMixin.setUp(self)

        wtl.globals.reset()       
        wtl.capability.WITSMLStoreCapabilities("1.4.1.1", WITSML_STORE_CAP)
    
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        mocking.MockingTestMixin.tearDown(self)
        
    def test_pause_zero(self):
        """ testing pausing the script for a few seconds """
        start = time.time() 
        wtl.control_prim.pause(0)
        end = time.time()
        self.assertTrue(test_interval(start, end, 0))        

    def test_pause_non_zero(self):
        """ testing pausing the script for a few seconds """
        start = time.time() 
        wtl.control_prim.pause(2)
        end = time.time()
        self.assertTrue(test_interval(start, end, 2))        
 
    def test_pause_changeDetectionPeriod(self):
        """ testing pausing the script for a few seconds """
        
        start = time.time() 
        wtl.control_prim.pause_changeDetectionPeriod()
        end = time.time()
        self.assertTrue(test_interval(start, end, 2))        
 
    def test_pause_growingTimeoutPeriod(self):
        """ testing pausing the script for a few seconds """
        
        start = time.time() 
        wtl.control_prim.pause_growingTimeoutPeriod('log')
        end = time.time()
        self.assertTrue(test_interval(start, end, 1))        

        start = time.time() 
        wtl.control_prim.pause_growingTimeoutPeriod('well')
        end = time.time()
        self.assertTrue(test_interval(start, end, 0))        

        start = time.time() 
        wtl.control_prim.pause_growingTimeoutPeriod('mudLog')
        end = time.time()
        self.assertTrue(test_interval(start, end, 3))        
 
if __name__ == '__main__':
    unittest.main()
