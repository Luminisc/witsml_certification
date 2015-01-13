
import sys

sys.path.append('../src/wtl')

import unittest
import mocking

import wtl.capability
import wtl.globals


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
        <schemaVersion>1.4.1.0</schemaVersion>
        <changeDetectionPeriod>200</changeDetectionPeriod>
        <growingTimeoutPeriod dataObject="log">60</growingTimeoutPeriod>
        <growingTimeoutPeriod dataObject="mudLog">30</growingTimeoutPeriod>
        <cascadedDelete>true</cascadedDelete>
        <compressionMethod>gzip</compressionMethod>
        <function name="WMLS_DeleteFromStore">
            <dataObject>attachment</dataObject>
            <dataObject>bhaRun</dataObject>
            <dataObject>cementJob</dataObject>
            <dataObject>convCore</dataObject>
            <dataObject>dtsInstalledSystem</dataObject>
            <dataObject>dtsMeasurement</dataObject>
            <dataObject>fluidsReport</dataObject>
            <dataObject>formationMarker</dataObject>
            <dataObject maxDataNodes="10000" maxDataPoints="20000">log</dataObject>
            <dataObject>message</dataObject>
            <dataObject maxDataPoints="30000">mudLog</dataObject>
            <dataObject>objectGroup</dataObject>
            <dataObject>opsReport</dataObject>
            <dataObject>realtime</dataObject>
            <dataObject>rig</dataObject>
            <dataObject>risk</dataObject>
            <dataObject>sidewallCore</dataObject>
            <dataObject>surveyProgram</dataObject>
            <dataObject>target</dataObject>
            <dataObject maxDataNodes="40000">trajectory</dataObject>
            <dataObject>tubular</dataObject>
            <dataObject>wbGeometry</dataObject>
            <dataObject>well</dataObject>
            <dataObject>wellbore</dataObject>
            <dataObject>wellLog</dataObject>
        </function>
        <function name="WMLS_GetFromStore"/>
        <function name="WMLS_AddToStore">
            <dataObject>attachment</dataObject>
        </function>
        <function name="WMLS_UpdateInStore">
            <dataObject>cementJob</dataObject>
            <dataObject>convCore</dataObject>
        </function>
        <function name="WMLS_GetVersion" />
        <function name="WMLS_GetBaseMsg" />
    </capServer>
</capServers>
"""


class ConfigTest(unittest.TestCase, mocking.MockingTestMixin):
    def setUp(self):
        unittest.TestCase.setUp(self)
        mocking.MockingTestMixin.setUp(self)

        wtl.globals.reset()       
    
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        mocking.MockingTestMixin.tearDown(self)
        
    def test_WITSMLStoreCapabilities_init(self):
        """ testing whether capabilities are parsed from xml """
        caps = wtl.capability.WITSMLStoreCapabilities("1.4.1.0", WITSML_STORE_CAP)
        self.assertTrue(wtl.globals.get_capability(wtl.capability.CAP_name) == "Store Name")
        self.assertTrue(wtl.globals.get_capability(wtl.capability.CAP_vendor) == "The Vendor")
        self.assertTrue(wtl.globals.get_capability(wtl.capability.CAP_version) == "The Version") 
        self.assertTrue(wtl.globals.get_capability(wtl.capability.CAP_changeDetectionPeriod) == 200)
        self.assertTrue(wtl.globals.get_growingTimeoutPeriod('log') == 60) 
        self.assertTrue(wtl.globals.get_growingTimeoutPeriod('mudLog') == 30) 
        self.assertTrue(wtl.globals.get_capability(wtl.capability.CAP_cascadedDelete) == True)
        self.assertTrue(wtl.globals.get_capability(wtl.capability.CAP_compressionMethod) == 'gzip')
        self.assertTrue(wtl.globals.is_function_object_supported('WMLS_DeleteFromStore' , 'attachment'))
        self.assertTrue(wtl.globals.is_function_object_supported('WMLS_DeleteFromStore' , 'bhaRun'))
        self.assertTrue(wtl.globals.is_function_object_supported('WMLS_DeleteFromStore' , 'cementJob'))
        self.assertTrue(wtl.globals.is_function_object_supported('WMLS_DeleteFromStore' , 'convCore'))
        self.assertTrue(wtl.globals.is_function_object_supported('WMLS_DeleteFromStore' , 'dtsInstalledSystem'))
        self.assertTrue(wtl.globals.is_function_object_supported('WMLS_DeleteFromStore' , 'dtsMeasurement'))
        self.assertTrue(wtl.globals.is_function_object_supported('WMLS_DeleteFromStore' , 'fluidsReport'))
        self.assertTrue(wtl.globals.is_function_object_supported('WMLS_DeleteFromStore' , 'formationMarker'))
        self.assertTrue(wtl.globals.is_function_object_supported('WMLS_DeleteFromStore' , 'log'))
        self.assertTrue(wtl.globals.is_function_object_supported('WMLS_DeleteFromStore' , 'message'))
        self.assertTrue(wtl.globals.is_function_object_supported('WMLS_DeleteFromStore' , 'mudLog'))
        self.assertTrue(wtl.globals.is_function_object_supported('WMLS_DeleteFromStore' , 'objectGroup'))
        self.assertTrue(wtl.globals.is_function_object_supported('WMLS_DeleteFromStore' , 'opsReport'))
        self.assertTrue(wtl.globals.is_function_object_supported('WMLS_DeleteFromStore' , 'realtime'))
        self.assertTrue(wtl.globals.is_function_object_supported('WMLS_DeleteFromStore' , 'rig'))
        self.assertTrue(wtl.globals.is_function_object_supported('WMLS_DeleteFromStore' , 'risk'))
        self.assertTrue(wtl.globals.is_function_object_supported('WMLS_DeleteFromStore' , 'sidewallCore'))
        self.assertTrue(wtl.globals.is_function_object_supported('WMLS_DeleteFromStore' , 'surveyProgram'))
        self.assertTrue(wtl.globals.is_function_object_supported('WMLS_DeleteFromStore' , 'target'))
        self.assertTrue(wtl.globals.is_function_object_supported('WMLS_DeleteFromStore' , 'trajectory'))
        self.assertTrue(wtl.globals.is_function_object_supported('WMLS_DeleteFromStore' , 'tubular'))
        self.assertTrue(wtl.globals.is_function_object_supported('WMLS_DeleteFromStore' , 'wbGeometry'))
        self.assertTrue(wtl.globals.is_function_object_supported('WMLS_DeleteFromStore' , 'well'))
        self.assertTrue(wtl.globals.is_function_object_supported('WMLS_DeleteFromStore' , 'wellbore'))
        self.assertTrue(wtl.globals.is_function_object_supported('WMLS_DeleteFromStore' , 'wellLog'))
        self.assertTrue(wtl.globals.is_function_object_supported('WMLS_AddToStore' , 'attachment'))
        self.assertTrue(wtl.globals.is_function_object_supported('WMLS_UpdateInStore' , 'cementJob'))
        self.assertTrue(wtl.globals.is_function_object_supported('WMLS_UpdateInStore' , 'convCore'))
        self.assertTrue(wtl.globals.get_maxDataNodes('WMLS_DeleteFromStore', 'log') == '10000')
        self.assertTrue(wtl.globals.get_maxDataPoints('WMLS_DeleteFromStore', 'log') == '20000')
        self.assertTrue(wtl.globals.get_maxDataPoints('WMLS_DeleteFromStore', 'mudLog') == '30000')
        self.assertTrue(wtl.globals.get_maxDataNodes('WMLS_DeleteFromStore', 'trajectory') == '40000')
        
    def test_WITSMLStoreCapabilities_init_bad_XML(self):
        """ testing whether capabilities are parsed from xml """
        caps = wtl.capability.WITSMLStoreCapabilities("1.4.1.0", """<capServer apiVers="1.4.1">
                                                                      <function name="WMLS_DeleteFromStore">
                                                                        <dataObject>attachment</dataObject>
                                                                      </function>""")
        self.assertFalse(wtl.globals.is_function_object_supported('WMLS_DeleteFromStore' , 'attachment'))

    def test_WITSMLStoreCapabilities_init_no_schema_match(self):
        """ testing whether capabilities are parsed from xml """
        caps = wtl.capability.WITSMLStoreCapabilities("1.4.1.1", WITSML_STORE_CAP)
        self.assertFalse(wtl.globals.is_function_object_supported('WMLS_DeleteFromStore' , 'attachment'))

    def test_WITSMLStoreCapabilities_init_empty(self):
        """ testing whether capabilities are parsed from xml """
        caps = wtl.capability.WITSMLStoreCapabilities("1.4.1.0", """<capServers xmlns="http://www.witsml.org/api/131" version="1.4.1">
                                                                  <capServer apiVers="1.4.1"/>
                                                             </capServers>""")
        self.assertTrue(wtl.globals.get_capability('name') == None)
        self.assertTrue(wtl.globals.get_capability('vendor') == None)
        self.assertTrue(wtl.globals.get_capability('version') == None) 
        self.assertTrue(wtl.globals.get_capability('changeDetectionPeriod') == None)
        self.assertTrue(wtl.globals.get_growingTimeoutPeriod('log') == None) 
        self.assertTrue(wtl.globals.get_growingTimeoutPeriod('mudLog') == None) 
        self.assertTrue(wtl.globals.get_capability('compressionMethod') == 'none')
        self.assertTrue(wtl.globals.get_capability('cascadedDelete') == False)
        self.assertFalse(wtl.globals.is_function_object_supported('WMLS_DeleteFromStore' , 'attachment'))
        self.assertTrue(wtl.globals.get_maxDataNodes('WMLS_DeleteFromStore', 'log') == None)

    def test_isSatisfyFollowingRequrements_Success(self):
        ''' testing whether capabilities are checked  (success case) '''
        caps = wtl.capability.WITSMLStoreCapabilities("1.4.1.0", WITSML_STORE_CAP);
        self.assertTrue(caps.isSatisfyFollowingRequrements('WMLS_DeleteFromStore:wellLog'))
        self.assertTrue(caps.isSatisfyFollowingRequrements('WMLS_DeleteFromStore:attachment'))
        self.assertTrue(caps.isSatisfyFollowingRequrements('WMLS_DeleteFromStore:attachment'))
        self.assertTrue(caps.isSatisfyFollowingRequrements('cascadedDelete=True'))
        self.assertTrue(caps.isSatisfyFollowingRequrements('changeDetectionPeriod=200'))
        self.assertTrue(caps.isSatisfyFollowingRequrements('compressionMethod=gzip'))
        self.assertTrue(caps.isSatisfyFollowingRequrements('WMLS_DeleteFromStore:log:maxDataPoints=20000'))

    def test_isSatisfyFollowingRequrements_Failure(self):
        ''' testing whether capabilities are checked  (fail case)'''
        caps = wtl.capability.WITSMLStoreCapabilities("1.4.1.0", WITSML_STORE_CAP);
        self.assertFalse(caps.isSatisfyFollowingRequrements('WMLS_GetFromStore:wellLog'))
        self.assertFalse(caps.isSatisfyFollowingRequrements('WMLS_DeleteFromStore:badobject'))
        self.assertFalse(caps.isSatisfyFollowingRequrements('cascadedDelete=False'))
        self.assertFalse(caps.isSatisfyFollowingRequrements('changeDetectionPeriod=100'))
        self.assertFalse(caps.isSatisfyFollowingRequrements('compressionMethod=none'))
        self.assertFalse(caps.isSatisfyFollowingRequrements('growingTimeoutPeriod=10'))
        self.assertFalse(caps.isSatisfyFollowingRequrements('WMLS_DeleteFromStore:log:maxDataPoints=10000'))
        self.assertFalse(caps.isSatisfyFollowingRequrements('WMLS_DeleteFromStore:mudLog:maxDataNodes=30000'))
        self.assertFalse(caps.isSatisfyFollowingRequrements('WMLS_DeleteFromStore:well:maxDataPoints=10000'))
        
    def test_isSatisfyFollowingRequrements_GreaterThan(self):
        ''' testing whether capabilities are checked  (> case)'''
        caps = wtl.capability.WITSMLStoreCapabilities("1.4.1.0", WITSML_STORE_CAP);
        self.assertTrue(caps.isSatisfyFollowingRequrements('changeDetectionPeriod>0'))
        self.assertTrue(caps.isSatisfyFollowingRequrements('changeDetectionPeriod>199'))
        self.assertFalse(caps.isSatisfyFollowingRequrements('changeDetectionPeriod>200'))
        self.assertFalse(caps.isSatisfyFollowingRequrements('changeDetectionPeriod>201'))
        
        self.assertTrue(caps.isSatisfyFollowingRequrements('WMLS_DeleteFromStore:log:maxDataPoints>0'))
        self.assertTrue(caps.isSatisfyFollowingRequrements('WMLS_DeleteFromStore:log:maxDataPoints>19999'))
        self.assertFalse(caps.isSatisfyFollowingRequrements('WMLS_DeleteFromStore:log:maxDataPoints>20000'))
        self.assertFalse(caps.isSatisfyFollowingRequrements('WMLS_DeleteFromStore:log:maxDataPoints>20001'))
        
    def test_isSatisfyFollowingRequrements_LessThan(self):
        ''' testing whether capabilities are checked  (< case)'''
        caps = wtl.capability.WITSMLStoreCapabilities("1.4.1.0", WITSML_STORE_CAP);
        self.assertFalse(caps.isSatisfyFollowingRequrements('changeDetectionPeriod<0'))
        self.assertFalse(caps.isSatisfyFollowingRequrements('changeDetectionPeriod<199'))
        self.assertFalse(caps.isSatisfyFollowingRequrements('changeDetectionPeriod<200'))
        self.assertTrue(caps.isSatisfyFollowingRequrements('changeDetectionPeriod<201'))
        
        self.assertFalse(caps.isSatisfyFollowingRequrements('WMLS_DeleteFromStore:log:maxDataPoints<0'))
        self.assertFalse(caps.isSatisfyFollowingRequrements('WMLS_DeleteFromStore:log:maxDataPoints<19999'))
        self.assertFalse(caps.isSatisfyFollowingRequrements('WMLS_DeleteFromStore:log:maxDataPoints<20000'))
        self.assertTrue(caps.isSatisfyFollowingRequrements('WMLS_DeleteFromStore:log:maxDataPoints<20001'))

if __name__ == '__main__':
    unittest.main()
