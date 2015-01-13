
import sys

sys.path.append('../src/wtl')

import unittest
import mocking

import wtl.globals


class ConfigTest(unittest.TestCase, mocking.MockingTestMixin):
    def setUp(self):
        unittest.TestCase.setUp(self)
        mocking.MockingTestMixin.setUp(self)

        wtl.globals.reset()
    
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        mocking.MockingTestMixin.tearDown(self)
        
    def test_globals_reset(self):
        wtl.globals.reset()
        self.assertTrue(wtl.globals.variables[wtl.globals.GBL_SERVER_SCHEMA_VERSIONS] == [])
        self.assertTrue(wtl.globals.variables[wtl.globals.GBL_SERVER_CAPABILITIES] == None)
        self.assertTrue(wtl.globals.variables[wtl.globals.CAP_PREFIX + 'cascadedDelete'] ==False)
        self.assertTrue(wtl.globals.variables[wtl.globals.CAP_PREFIX + 'compressionMethod'] =='none')

    def test_globals_set_get(self):
        wtl.globals.set('abc', '123')
        self.assertTrue(wtl.globals.variables['abc'] =='123')
        self.assertTrue(wtl.globals.get('abc') =='123')

        wtl.globals.set('def', None)
        self.assertTrue(wtl.globals.variables['def'] == None)
        self.assertTrue(wtl.globals.get('def') == None)

        wtl.globals.set('ghi', 1.2)
        self.assertTrue(wtl.globals.variables['ghi'] == 1.2)
        self.assertTrue(wtl.globals.get('ghi') == 1.2)
        
        self.assertTrue(wtl.globals.get('jkl') == None)

    def test_globals_set_get_capability(self):
        wtl.globals.set_capability('abc', '123')
        self.assertTrue(wtl.globals.variables[wtl.globals.CAP_PREFIX + 'abc'] =='123')
        self.assertTrue(wtl.globals.get_capability('abc') =='123')

        wtl.globals.set_capability('def', None)
        self.assertTrue(wtl.globals.variables[wtl.globals.CAP_PREFIX + 'def'] == None)
        self.assertTrue(wtl.globals.get_capability('def') == None)

        wtl.globals.set_capability('ghi',1.2)
        self.assertTrue(wtl.globals.variables[wtl.globals.CAP_PREFIX + 'ghi'] == 1.2)
        self.assertTrue(wtl.globals.get_capability('ghi') == 1.2)

    def test_globals_set_is_function_object_supported(self):
        wtl.globals.set_function_object_supported('fun', 'obj')
        self.assertTrue(wtl.globals.variables[wtl.globals.CAP_PREFIX + 'fun:obj'] == True)
        self.assertTrue(wtl.globals.is_function_object_supported('fun', 'obj') == True)
        self.assertTrue(wtl.globals.is_function_object_supported('fun2', 'obj') == False)
        self.assertTrue(wtl.globals.is_function_object_supported('fun', 'obj2') == False)
    
    def test_globals_set_get_max_data_nodes(self):
        wtl.globals.set_maxDataNodes('fun', 'obj', 123)
        self.assertTrue(wtl.globals.variables[wtl.globals.CAP_PREFIX + 'fun:obj:maxDataNodes'] ==123)
        self.assertTrue(wtl.globals.get_maxDataNodes('fun', 'obj') == 123)
        self.assertTrue(wtl.globals.get_maxDataNodes('fun2', 'obj') == None)
        self.assertTrue(wtl.globals.get_maxDataNodes('fun', 'obj2') == None)

    def test_globals_set_get_max_data_points(self):
        wtl.globals.set_maxDataPoints('fun', 'obj', 123)
        self.assertTrue(wtl.globals.variables[wtl.globals.CAP_PREFIX + 'fun:obj:maxDataPoints'] ==123)
        self.assertTrue(wtl.globals.get_maxDataPoints('fun', 'obj') == 123)
        self.assertTrue(wtl.globals.get_maxDataPoints('fun2', 'obj') == None)
        self.assertTrue(wtl.globals.get_maxDataPoints('fun', 'obj2') == None)

    def test_globals_set_get_growingTimeoutPeriod(self):
        wtl.globals.set_growingTimeoutPeriod('obj', 123)
        self.assertTrue(wtl.globals.variables[wtl.globals.CAP_PREFIX + 'obj-growingTimeoutPeriod'] ==123)
        self.assertTrue(wtl.globals.get_growingTimeoutPeriod('obj') == 123)
        self.assertTrue(wtl.globals.get_growingTimeoutPeriod('obj2') == None)


if __name__ == '__main__':
    unittest.main()
