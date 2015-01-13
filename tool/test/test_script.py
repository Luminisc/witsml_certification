
import sys

sys.path.append('../src/wtl')

import unittest
import mocking

import wtl.script
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
            <dataObject maxDataPoints="3">mudLog</dataObject>
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
        <function name="WMLS_GetFromStore">
            <dataObject>log</dataObject>
        </function>
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

class ScriptTest(unittest.TestCase, mocking.MockingTestMixin):
    def setUp(self):
        unittest.TestCase.setUp(self)
        mocking.MockingTestMixin.setUp(self)

        wtl.globals.reset()       
    
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        mocking.MockingTestMixin.tearDown(self)
        
    def test_areMinimumRequirementsMet_functions(self):
        
        # setup globals for script test
        caps = wtl.capability.WITSMLStoreCapabilities("1.4.1.0", WITSML_STORE_CAP)
        wtl.globals.set(wtl.globals.GBL_SERVER_SCHEMA_VERSIONS, "1.4.1.0")
        wtl.globals.set(wtl.globals.GBL_SERVER_CAPABILITIES, wtl.capability.WITSMLStoreCapabilities("1.4.1.0", WITSML_STORE_CAP))
        wtl.script.Script.init()
        wtl.utils.set_variable_value('server_schema_version', "1.4.1.0")
        script = wtl.script.Script.get_current_script()
        
        script.set_info("To Test Blah", 
                        "Reference to Something", 
                        "Reference Text Here",
                        [], 
                        ["WMLS_GetFromStore:log",
                         "WMLS_AddToStore:attachment",
                         "WMLS_UpdateInStore:convCore",
                         "WMLS_DeleteFromStore:trajectory",
                         "WMLS_DeleteFromStore:objectGroup",
                         ],
                        ["1.4.1.0"])
        self.assertTrue(script.areMinimumRequirementsMet())
        
        script.set_info("To Test Blah", 
                        "Reference to Something", 
                        "Reference Text Here",
                        [], 
                        [
                         "WMLS_DeleteFromStore:trajectory:maxDataNodes>0"
                         ],
                        ["1.4.1.0"])
        self.assertTrue(script.areMinimumRequirementsMet())
        
        script.set_info("To Test Blah", 
                        "Reference to Something", 
                        "Reference Text Here",
                        [], 
                        [
                         "WMLS_DeleteFromStore:trajectory:maxDataNodes=40000"
                         ],
                        ["1.4.1.0"])
        self.assertTrue(script.areMinimumRequirementsMet())
        
        script.set_info("To Test Blah", 
                        "Reference to Something", 
                        "Reference Text Here",
                        [], 
                        [
                         "WMLS_DeleteFromStore:trajectory:maxDataNodes<40001"
                         "WMLS_DeleteFromStore:trajectory:maxDataPoints<0"
                         ],
                        ["1.4.1.0"])
        self.assertFalse(script.areMinimumRequirementsMet())
        
        script.set_info("To Test Blah", 
                        "Reference to Something", 
                        "Reference Text Here",
                        [], 
                        [
                         "WMLS_DeleteFromStore:trajectory:maxDataNodes<40001"
                         ],
                        ["1.4.1.0"])
        self.assertTrue(script.areMinimumRequirementsMet())
        
        script.set_info("To Test Blah", 
                        "Reference to Something", 
                        "Reference Text Here",
                        [], 
                        [
                         "WMLS_DeleteFromStore:trajectory:maxDataNodes>40000"
                         ],
                        ["1.4.1.0"])
        self.assertFalse(script.areMinimumRequirementsMet())
        
        script.set_info("To Test Blah", 
                        "Reference to Something", 
                        "Reference Text Here",
                        [], 
                        [
                         "WMLS_DeleteFromStore:trajectory:maxDataNodes>0"
                         "WMLS_DeleteFromStore:trajectory:maxDataPoints<20000"
                         ],
                        ["1.4.1.0"])
        self.assertFalse(script.areMinimumRequirementsMet())
        
        script.set_info("To Test Blah", 
                        "Reference to Something", 
                        "Reference Text Here",
                        [], 
                        [
                         "WMLS_DeleteFromStore:trajectory:maxDataNodes>0"
                         "WMLS_DeleteFromStore:trajectory:maxDataPoints>20000"
                         ],
                        ["1.4.1.0"])
        self.assertFalse(script.areMinimumRequirementsMet())
        
    def test_areMinimumRequirementsMet_values(self):
        
        # setup globals for script test
        caps = wtl.capability.WITSMLStoreCapabilities("1.4.1.0", WITSML_STORE_CAP)
        wtl.globals.set(wtl.globals.GBL_SERVER_SCHEMA_VERSIONS, "1.4.1.0")
        wtl.globals.set(wtl.globals.GBL_SERVER_CAPABILITIES, wtl.capability.WITSMLStoreCapabilities("1.4.1.0", WITSML_STORE_CAP))
        wtl.script.Script.init()
        wtl.utils.set_variable_value('server_schema_version', "1.4.1.0")
        script = wtl.script.Script.get_current_script()
        
        script.set_info("To Test Blah", 
                        "Reference to Something", 
                        "Reference Text Here",
                        [], 
                        ["changeDetectionPeriod=200",
                         "cascadedDelete=True",
                         "compressionMethod=gzip"
                         ],
                        ["1.4.1.0"])
        self.assertTrue(script.areMinimumRequirementsMet())
        
        script.set_info("To Test Blah", 
                        "Reference to Something", 
                        "Reference Text Here",
                        [], 
                        ["changeDetectionPeriod>200",
                         "cascadedDelete=True",
                         "compressionMethod=gzip"
                         ],
                        ["1.4.1.0"])
        self.assertFalse(script.areMinimumRequirementsMet())
        
        script.set_info("To Test Blah", 
                        "Reference to Something", 
                        "Reference Text Here",
                        [], 
                        ["changeDetectionPeriod=200",
                         "cascadedDelete=False",
                         "compressionMethod=gzip"
                         ],
                        ["1.4.1.0"])
        self.assertFalse(script.areMinimumRequirementsMet())
        
        script.set_info("To Test Blah", 
                        "Reference to Something", 
                        "Reference Text Here",
                        [], 
                        ["changeDetectionPeriod=200",
                         "cascadedDelete=True",
                         "compressionMethod=None"
                         ],
                        ["1.4.1.0"])
        self.assertFalse(script.areMinimumRequirementsMet())
                
        
    def test_areMinimumRequirementsMet_UnspecifiedValueWithComparison(self):
        
        # setup globals for script test
        caps = wtl.capability.WITSMLStoreCapabilities("1.4.1.0", WITSML_STORE_CAP)
        wtl.globals.set(wtl.globals.GBL_SERVER_SCHEMA_VERSIONS, "1.4.1.0")
        wtl.globals.set(wtl.globals.GBL_SERVER_CAPABILITIES, wtl.capability.WITSMLStoreCapabilities("1.4.1.0", WITSML_STORE_CAP))
        wtl.script.Script.init()
        wtl.utils.set_variable_value('server_schema_version', "1.4.1.0")
        script = wtl.script.Script.get_current_script()
        
        # test comparison against non-existent maxDataPoints
        script.set_info("To Test Blah", 
                        "Reference to Something", 
                        "Reference Text Here",
                        [], 
                        ["WMLS_DeleteFromStore:mudLog:maxDataPoints>0"],
                        ["1.4.1.0"])
        self.assertTrue(script.areMinimumRequirementsMet())
        
        script.set_info("To Test Blah", 
                        "Reference to Something", 
                        "Reference Text Here",
                        [], 
                        ["WMLS_DeleteFromStore:mudLog:maxDataPoints<0"],
                        ["1.4.1.0"])
        self.assertFalse(script.areMinimumRequirementsMet())
                
        script.set_info("To Test Blah", 
                        "Reference to Something", 
                        "Reference Text Here",
                        [], 
                        ["WMLS_DeleteFromStore:mudLog:maxDataPoints=0"],
                        ["1.4.1.0"])
        self.assertFalse(script.areMinimumRequirementsMet())
        
         # test extra equals
        script.set_info("To Test Blah", 
                        "Reference to Something", 
                        "Reference Text Here",
                        [], 
                        ["WMLS_DeleteFromStore:mudLog:maxDataPoints=0=12"],
                        ["1.4.1.0"])
        self.assertFalse(script.areMinimumRequirementsMet())
        
        script.set_info("To Test Blah", 
                        "Reference to Something", 
                        "Reference Text Here",
                        [], 
                        ["WMLS_DeleteFromStore:mudLog:maxDataPoints>12"],
                        ["1.4.1.0"])
        self.assertFalse(script.areMinimumRequirementsMet())
        
        script.set_info("To Test Blah", 
                        "Reference to Something", 
                        "Reference Text Here",
                        [], 
                        ["WMLS_DeleteFromStore:mudLog:maxDataPoints<12"],
                        ["1.4.1.0"])
        self.assertTrue(script.areMinimumRequirementsMet())
        
        
        
    def test_areMinimumRequirementsMet_UnspecifiedValueWithComparison(self):
        
        # setup globals for script test
        caps = wtl.capability.WITSMLStoreCapabilities("1.4.1.0", WITSML_STORE_CAP)
        wtl.globals.set(wtl.globals.GBL_SERVER_SCHEMA_VERSIONS, "1.4.1.0")
        wtl.globals.set(wtl.globals.GBL_SERVER_CAPABILITIES, wtl.capability.WITSMLStoreCapabilities("1.4.1.0", WITSML_STORE_CAP))
        wtl.script.Script.init()
        wtl.utils.set_variable_value('server_schema_version', "1.4.1.0")
        script = wtl.script.Script.get_current_script()
        
        # test with non-existent setting and comparison
        script.set_info("To Test Blah", 
                        "Reference to Something", 
                        "Reference Text Here",
                        [], 
                        ["growingTimeout>10"],
                        ["1.4.1.0"])
        self.assertTrue(script.areMinimumRequirementsMet())
        
        script.set_info("To Test Blah", 
                        "Reference to Something", 
                        "Reference Text Here",
                        [], 
                        ["growingTimeout<10"],
                        ["1.4.1.0"])
        self.assertFalse(script.areMinimumRequirementsMet())
        
        script.set_info("To Test Blah", 
                        "Reference to Something", 
                        "Reference Text Here",
                        [], 
                        ["growingTimeout=10"],
                        ["1.4.1.0"])
        self.assertFalse(script.areMinimumRequirementsMet())
        
        
    def test_areMinimumRequirementsMet_GlobalVariables(self):
        
        # setup globals for script test
        caps = wtl.capability.WITSMLStoreCapabilities("1.4.1.0", WITSML_STORE_CAP)
        wtl.globals.set(wtl.globals.GBL_SERVER_SCHEMA_VERSIONS, "1.4.1.0")
        wtl.globals.set(wtl.globals.GBL_SERVER_CAPABILITIES, wtl.capability.WITSMLStoreCapabilities("1.4.1.0", WITSML_STORE_CAP))
        wtl.script.Script.init()
        wtl.utils.set_variable_value('server_schema_version', "1.4.1.0")
        script = wtl.script.Script.get_current_script()
        
        wtl.globals.set('server_supports_numAPI', True)
        wtl.globals.set('server_supports_numGovt', False)
        script.set_info("To Test Blah", 
                        "Reference to Something", 
                        "Reference Text Here",
                        [], 
                        ["server_supports_numAPI"],
                        ["1.4.1.0"])
        self.assertTrue(script.areMinimumRequirementsMet())
        
        script.set_info("To Test Blah", 
                        "Reference to Something", 
                        "Reference Text Here",
                        [], 
                        ["server_supports_numGovt"],
                        ["1.4.1.0"])
        self.assertFalse(script.areMinimumRequirementsMet())

        
        
if __name__ == '__main__':
    unittest.main()
