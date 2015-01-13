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
import mocking

import wtl.utils
import wtl.response
import wtl.control_prim
import wtl.script

XMLBASE = """<?xml version="1.0" ?>
<wells xmlns="none">%s</wells>"""

XML_ENCODING = '<?xml version="1.0" encoding="%s"?>\n<wells xmlns="http://www.witsml.org/schemas/131">%s</wells>'
XMLBODY = '\n\t\n<well uid="tuid123">\n\t\n <name>Test Well</name>\t<numAPI>testAPI</numAPI>\n\n</well>'
XML1 = XMLBASE %(XMLBODY)
XMLWITHPLUS = XMLBASE %('\n\t\n<well uid="tuid+123">\n\t\n <name>Test Well</name>\t<numAPI>testAPI</numAPI>\n\n</well>')

XML_LOG_1311 =  """<?xml version="1.0" encoding="UTF-8"?>
              <logs xmlns="http://www.witsml.org/schemas/131" version="1.3.1.1">
                <log uidWell='w1' uidWellbore='wb1' uid='l1'>
                  <indexCurve columnIndex="2">M2</indexCurve>
                  <logCurveInfo>
                    <mnemonic>M1</mnemonic>
                    <columnIndex>1</columnIndex>
                    <unit>m</unit>
                  </logCurveInfo>
                  <logCurveInfo>
                    <mnemonic>M2</mnemonic>
                    <columnIndex>2</columnIndex>
                    <unit>m</unit>
                  </logCurveInfo>
                  <logCurveInfo>
                    <mnemonic>M3</mnemonic>
                    <columnIndex>3</columnIndex>
                    <unit>m</unit>
                  </logCurveInfo>
                  <logCurveInfo>
                    <mnemonic>M4</mnemonic>
                      <columnIndex>4</columnIndex>
                      <unit>m</unit>
                  </logCurveInfo>
                  <logData>                        
                    <data>1,2,3.0,</data>
                    <data>2,0,3.1,10</data>
                    <data>3,4,3.2,20</data>
                    <data>4,0,3.3,</data>
                    <data>5,,3.4,30</data>
                  </logData>
                </log>
              </logs>"""
              
XML_LOG_1311_OUT_OF_ORDER =  """<?xml version="1.0" encoding="UTF-8"?>
                              <logs xmlns="http://www.witsml.org/schemas/131" version="1.3.1.1">
                                <log uidWell='w1' uidWellbore='wb1' uid='l1'>
                                  <indexCurve columnIndex="1">M4</indexCurve>
                                  <logCurveInfo>
                                    <mnemonic>M1</mnemonic>
                                    <columnIndex>2</columnIndex>
                                    <unit>m</unit>
                                  </logCurveInfo>
                                  <logCurveInfo>
                                    <mnemonic>M2</mnemonic>
                                    <columnIndex>3</columnIndex>
                                    <unit>ft</unit>
                                  </logCurveInfo>
                                  <logCurveInfo>
                                    <mnemonic>M3</mnemonic>
                                    <columnIndex>4</columnIndex>
                                    <unit>deg</unit>
                                  </logCurveInfo>
                                  <logCurveInfo>
                                    <mnemonic>M4</mnemonic>
                                      <columnIndex>1</columnIndex>
                                      <unit>C</unit>
                                  </logCurveInfo>
                                  <logData>                        
                                    <data>1,2,3.0,</data>
                                    <data>2,0,3.1,10</data>
                                    <data>3,4,3.2,20</data>
                                    <data>4,0,3.3,</data>
                                    <data>5,,3.4,30</data>
                                  </logData>
                                </log>
                              </logs>"""      
                              
XML_LOG_1311_NO_COLUMN_IDX =  """<?xml version="1.0" encoding="UTF-8"?>
                              <logs xmlns="http://www.witsml.org/schemas/131" version="1.3.1.1">
                                <log uidWell='w1' uidWellbore='wb1' uid='l1'>
                                  <indexCurve columnIndex="1">M4</indexCurve>
                                  <logCurveInfo>
                                    <mnemonic>M1</mnemonic>
                                    <unit>m</unit>
                                  </logCurveInfo>
                                  <logCurveInfo>
                                    <mnemonic>M2</mnemonic>
                                    <unit>ft</unit>
                                  </logCurveInfo>
                                  <logCurveInfo>
                                    <mnemonic>M3</mnemonic>
                                    <unit>deg</unit>
                                  </logCurveInfo>
                                  <logCurveInfo>
                                    <mnemonic>M4</mnemonic>
                                      <unit>C</unit>
                                  </logCurveInfo>
                                  <logData>                        
                                    <data>1,2,3.0,</data>
                                    <data>2,0,3.1,10</data>
                                    <data>3,4,3.2,20</data>
                                    <data>4,0,3.3,</data>
                                    <data>5,,3.4,30</data>
                                  </logData>
                                </log>
                              </logs>"""           
              
XML_LOG_1410 =  """<?xml version="1.0" encoding="UTF-8"?>
              <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                <log uidWell='w1' uidWellbore='wb1' uid='l1'>
                  <indexCurve>M1</indexCurve>
                  <logCurveInfo>
                    <mnemonic>M1</mnemonic>
                    <unit>m</unit>
                  </logCurveInfo>
                  <logCurveInfo>
                    <mnemonic>M2</mnemonic>
                    <unit>m</unit>
                  </logCurveInfo>
                  <logCurveInfo>
                    <mnemonic>M3</mnemonic>
                    <unit>m</unit>
                  </logCurveInfo>
                  <logCurveInfo>
                    <mnemonic>M4</mnemonic>
                    <unit>m</unit>
                  </logCurveInfo>
                  <logData>                        
                    <mnemonicList>M1,M2,M3,M4</mnemonicList>
                    <unitList>m,m,m,m</unitList>
                    <data>1,2,3.0,</data>
                    <data>2,0,3.1,10</data>
                    <data>3,4,3.2,20</data>
                    <data>4,0,3.3,</data>
                    <data>5,,3.4,30</data>
                  </logData>
                </log>
              </logs>"""
         
XML_1410_WITH_ARRAY_CURVE = """<?xml version="1.0" encoding="UTF-8"?>  
        <logs xmlns="http://www.witsml.org/schemas/1series" version="1.4.1.0">
            <log uidWell="W-12" uidWellbore="B-01" uid="f34a">
                <nameWell>6507/7-A-42</nameWell>
                <nameWellbore>A-42</nameWellbore>
                <name>L001</name>
                <indexType>measured depth</indexType>
                <startIndex uom="m">499</startIndex>
                <endIndex uom="m">509.01</endIndex>
                <stepIncrement uom="m">0</stepIncrement>
                <direction>increasing</direction>
                <indexCurve>Mdepth</indexCurve>
                <nullValue>-999.25</nullValue>
                <logCurveInfo uid="lci-1">
                    <mnemonic>Mdepth</mnemonic>
                    <classWitsml>measured depth of hole</classWitsml>
                    <unit>m</unit>
                    <mnemAlias>md</mnemAlias>
                    <nullValue>-999.25</nullValue>
                    <minIndex uom="m">499</minIndex>
                    <maxIndex uom="m">509.01</maxIndex>
                    <curveDescription>Measured depth</curveDescription>
                    <sensorOffset uom="m">0</sensorOffset>
                    <traceState>raw</traceState>
                    <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="lci-2">
                    <mnemonic>Vdepth</mnemonic>
                    <classWitsml>TVD of hole</classWitsml>
                    <unit>m</unit>
                    <mnemAlias>tvd</mnemAlias>
                    <nullValue>-999.25</nullValue>
                    <minIndex uom="m">499</minIndex>
                    <maxIndex uom="m">509.01</maxIndex>
                    <curveDescription>Vertical depth</curveDescription>
                    <sensorOffset uom="m">0</sensorOffset>
                    <traceState>raw</traceState>
                    <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="lci-3">
                    <mnemonic>Array</mnemonic>
                    <unit>ft</unit>
                    <mnemAlias>array</mnemAlias>
                    <nullValue>-999.25</nullValue>
                    <minIndex uom="m">500.01</minIndex>
                    <maxIndex uom="m">509.01</maxIndex>
                    <curveDescription>example of an array</curveDescription>
                    <sensorOffset uom="m">0</sensorOffset>
                    <traceState>raw</traceState>
                    <typeLogData>double</typeLogData>
                    <axisDefinition uid="axis1">
                        <order>1</order>
                        <count>3</count>
                        <doubleValues>1,2,3</doubleValues>
                    </axisDefinition>
                    <axisDefinition uid="axis2">
                        <order>2</order>
                        <count>2</count>
                        <doubleValues>1,2</doubleValues>
                    </axisDefinition>
                </logCurveInfo>
                <logCurveInfo uid="lci-4">
                    <mnemonic>Bit Dist</mnemonic>
                    <classWitsml>measured depth of DST bottom</classWitsml>
                    <unit>m</unit>
                    <mnemAlias>distBit</mnemAlias>
                    <nullValue>-999.25</nullValue>
                    <minIndex uom="m">499</minIndex>
                    <maxIndex uom="m">509.01</maxIndex>
                    <curveDescription>Distance drilled by bit</curveDescription>
                    <sensorOffset uom="m">0</sensorOffset>
                    <traceState>raw</traceState>
                    <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logData>
                    <mnemonicList>Mdepth,Vdepth,Array,Bit Dist</mnemonicList>
                    <unitList>m,m,ft,m</unitList>
                    <data>499.00,498.99,-999.25 -999.25 -999.25 -999.25 -999.25 -999.25,1.25</data>
                    <data>500.01,500.00,01 11 21 31 41 51,1.90</data>
                    <data>501.03,501.02,02 12 22 32 42 52,2.92</data>
                    <data>502.01,502.00,03 13 23 33 43 53,3.90</data>
                    <data>503.01,503.00,04 14 24 34 44 54,4.90</data>
                    <data>504.05,504.04,05 15 25 35 45 55,5.94</data>
                    <data>505.03,505.00,06 16 26 36 46 56,2.03</data>
                    <data>506.04,505.95,07 17 27 37 47 57,3.04</data>
                    <data>507.04,506.91,08 18 28 38 48 58,4.04</data>
                    <data>508.01,507.84,09 19 29 39 49 59,5.01</data>
                    <data>509.01,508.75,-999.25 30 -999.25 -999.25 -999.25 -999.25,6.01</data>
                </logData>
                <commonData>
                    <dTimCreation>2003-11-24T08:15:00.000Z</dTimCreation>
                    <dTimLastChange>2003-11-24T08:17:00.000Z</dTimLastChange>
                    <itemState>plan</itemState>
                    <comments>These are the comments associated with the log object.</comments>
                </commonData>                
              </log>
        </logs>        
        """   

XML_WELLBORE = """<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet href="./stylesheets/generic.xsl" type="text/xsl" media="screen"?>
<!--           Example of Wellbore data     -->
<wellbores 
    xmlns="http://www.witsml.org/schemas/1series" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
    xsi:schemaLocation="http://www.witsml.org/schemas/1series  ../xsd_schemas/obj_wellbore.xsd" 
    version="1.4.1.1">
<!-- 
These examples are only intended to demonstrate the type of data that can be exchanged.
They totally artificial and are not intended to demonstrate best practices. 
-->
    <documentInfo>
        <documentName>wellbore</documentName>
        <fileCreationInformation>
            <fileCreationDate>2001-10-31T08:15:00.000Z</fileCreationDate> 
            <fileCreator>John Smith</fileCreator>
        </fileCreationInformation>
    </documentInfo>
    <wellbore uidWell="W-12" uid="B-01">
        <nameWell>6507/7-A-42</nameWell>
        <name>A-42</name>
        <number>1234-0987</number>
        <suffixAPI>02</suffixAPI>
        <numGovt>Govt001</numGovt>
        <statusWellbore>active</statusWellbore>
        <purposeWellbore>exploration</purposeWellbore>
        <typeWellbore>initial</typeWellbore>
        <shape>horizontal</shape>
        <dTimKickoff>2001-03-15T13:20:00.000Z</dTimKickoff>
        <md uom="ft">0</md>
        <tvd uom="ft">0</tvd>
        <mdKickoff uom="ft">0</mdKickoff>
        <tvdKickoff uom="ft">0</tvdKickoff>
        <mdPlanned uom="ft">15800</mdPlanned>
        <tvdPlanned uom="ft">12567</tvdPlanned>
        <mdSubSeaPlanned uom="ft">12800</mdSubSeaPlanned>
        <tvdSubSeaPlanned uom="ft">9567</tvdSubSeaPlanned>
        <dayTarget uom="d">128</dayTarget>
        <commonData>
            <dTimCreation>2001-04-30T08:15:00.000Z</dTimCreation>
            <dTimLastChange>2001-05-31T08:15:00.000Z</dTimLastChange>
            <itemState>plan</itemState>
            <comments>These are the comments associated with the Wellbore data object.</comments>
        </commonData>
    </wellbore>
    <wellbore uidWell="W-12" uid="B-02">
        <nameWell>6507/7-A-42</nameWell>
        <name>A-43</name>
        <parentWellbore uidRef="B-01">A-42</parentWellbore>
        <number>Wellbore Number 2</number>
        <suffixAPI>03</suffixAPI>
        <numGovt>Govt Number 12345</numGovt>
        <statusWellbore>drilling</statusWellbore>
        <purposeWellbore>exploration</purposeWellbore>
        <typeWellbore>sidetrack</typeWellbore>
        <shape>horizontal</shape>
        <dTimKickoff>2001-04-14T09:25:00.000Z</dTimKickoff>
        <md uom="ft">10760</md>
        <tvd uom="ft">9230</tvd>
        <mdKickoff uom="ft">10760</mdKickoff>
        <tvdKickoff uom="ft">9230</tvdKickoff>
        <mdPlanned uom="ft">15800</mdPlanned>
        <tvdPlanned uom="ft">12567</tvdPlanned>
        <mdSubSeaPlanned uom="ft">12900</mdSubSeaPlanned>
        <tvdSubSeaPlanned uom="ft">9567</tvdSubSeaPlanned>
        <dayTarget uom="d">35</dayTarget>
        <commonData>
            <dTimCreation>2001-04-30T08:15:00.000Z</dTimCreation>
            <dTimLastChange>2001-05-31T08:15:00.000Z</dTimLastChange>
            <itemState>plan</itemState>
            <comments>These are the comments associated with the Wellbore data object.</comments>
        </commonData>
    </wellbore>
</wellbores>
"""        
#<statusWellbore>active2</statusWellbore> should be <statusWellbore>active</statusWellbore>
XML_WELLBORE_BAD = """<?xml version="1.0" encoding="UTF-8"?>
<wellbores 
    xmlns="http://www.witsml.org/schemas/1series" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
    xsi:schemaLocation="http://www.witsml.org/schemas/1series  ../xsd_schemas/obj_wellbore.xsd" 
    version="1.4.1.1">
    <wellbore uidWell="W-12" uid="B-01">
        <nameWell>6507/7-A-42</nameWell>
        <name>A-42</name>
        <statusWellbore>active2</statusWellbore>
        <commonData>
            <dTimCreation>2001-04-30T08:15:00.000Z</dTimCreation>
            <dTimLastChange>2001-05-31T08:15:00.000Z</dTimLastChange>
            <itemState>plan</itemState>
            <comments>These are the comments associated with the Wellbore data object.</comments>
        </commonData>
    </wellbore>
</wellbores>
"""
                           

class ResponseTest(unittest.TestCase, mocking.MockingTestMixin):
    def setUp(self):
        unittest.TestCase.setUp(self)
        mocking.MockingTestMixin.setUp(self)

        wtl.script.Script.init()

        self.stub(wtl.control_prim, "fail")

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        mocking.MockingTestMixin.tearDown(self)
    
    def test_ReturnValue_clear(self):
        x = wtl.response.ReturnValue()
        x.set('200')
        x.clear()
        self.assertTrue(x.value == None)
    
    def test_ReturnValue_clear(self):
        x = wtl.response.ReturnValue()
        x.set('200')
        x.clear()
        self.assertTrue(x.value == None)
    
    def test_ReturnValue_set_integer(self):
        x = wtl.response.ReturnValue()
        x.set(200)
        self.assertTrue(x.value == 200)
    
    def test_ReturnValue_set_string(self):
        x = wtl.response.ReturnValue()
        x.set('200')
        self.assertTrue(x.value == '200')
    
    def test_ReturnValue_get(self):
        x = wtl.response.ReturnValue()
        x.set(200)
        self.assertTrue(x.get() == 200)
    
    def test_ReturnValue_get_first_word(self):
        x = wtl.response.ReturnValue()
        x.get_first_word()
        self.assertTrue(wtl.control_prim.fail.called)
        x.set('200 abc')
        self.assertTrue(x.get_first_word() == '200')
        x.set('300')
        self.assertTrue(x.get_first_word() == '300')
        x.set('')
        x.get_first_word()
        self.assertTrue(wtl.control_prim.fail.called)
    
    def test_ReturnValue_check_value_is_set_valueNotSet(self):
        x = wtl.response.ReturnValue()
        x.check_value_is_set()
        self.assertTrue(wtl.control_prim.fail.called)
    
    def test_ReturnValue_check_value_is_set_valueSet(self):
        x = wtl.response.ReturnValue(1)
        x.check_value_is_set()
        self.assertFalse(wtl.control_prim.fail.called)
    
    def test_ReturnValue_check_value_noValue(self):
        x = wtl.response.ReturnValue()
        x.check_value(2)
        self.assertTrue(wtl.control_prim.fail.called)
    
    def test_ReturnValue_check_value_NoMatch(self):
        x = wtl.response.ReturnValue(12)
        x.check_value(3)
        self.assertTrue(wtl.control_prim.fail.called)
    
    def test_ReturnValue_check_value_match(self):
        x = wtl.response.ReturnValue(12)
        x.check_value(12)
        self.assertFalse(wtl.control_prim.fail.called)
    
    def test_ReturnValue_check_value_matchString(self):
        x = wtl.response.ReturnValue(15)
        x.check_value('15')
        self.assertFalse(wtl.control_prim.fail.called)
    
    def test_ReturnValue_check_value_matchVariable(self):
        x = wtl.response.ReturnValue(11)
        wtl.utils.set_variable_value('y','11')
        x.check_value('$y$')
        self.assertFalse(wtl.control_prim.fail.called)
    
    def test_ReturnValue_check_value_matchAnything(self):
        x = wtl.response.ReturnValue(18)
        x.check_value('.*', enable_regex=True)
        self.assertFalse(wtl.control_prim.fail.called)
    
    def test_ReturnValue_check_value_matchRegex(self):
        x = wtl.response.ReturnValue(167)
        x.check_value('.*6.*', enable_regex=True)
        self.assertFalse(wtl.control_prim.fail.called)
    
    def test_ReturnValue_check_string_noValue(self):
        x = wtl.response.ReturnValue()
        x.check_string('2')
        self.assertTrue(wtl.control_prim.fail.called)
    
    def test_ReturnValue_check_string_noMatch(self):
        x = wtl.response.ReturnValue('12')
        x.check_string('3', enable_regex=False)
        self.assertTrue(wtl.control_prim.fail.called)
    
    def test_ReturnValue_check_string_noMatch_regex(self):
        x = wtl.response.ReturnValue('1+2')
        x.check_string('1+2', enable_regex=True)
        self.assertTrue(wtl.control_prim.fail.called)

    def test_ReturnValue_check_string_match(self):
        x = wtl.response.ReturnValue('1+2')
        x.check_string('1+2', enable_regex=False)
        self.assertFalse(wtl.control_prim.fail.called)
    
    def test_ReturnValue_check_xml_string_noMatch_regex(self):
        x = wtl.response.ReturnValue('1+2')
        x.check_string('1+2', enable_regex=True)
        self.assertTrue(wtl.control_prim.fail.called)

    def test_ReturnValue_check_xml_string_match_regex(self):
        x = wtl.response.ReturnValue('1+2')
        x.check_string('1\+2', enable_regex=True)
        self.assertFalse(wtl.control_prim.fail.called)

    def test_ReturnValue_check_value_contains_noValue(self):
        x = wtl.response.ReturnValue()
        x.check_value_contains('1')
        self.assertTrue(wtl.control_prim.fail.called)

    def test_ReturnValue_check_value_contains_stringContainedAtStart(self):
        x = wtl.response.ReturnValue(-15)
        x.check_value_contains('-')
        self.assertFalse(wtl.control_prim.fail.called)
    
    def test_ReturnValue_check_value_contains_stringContainedAtEnd(self):
        x = wtl.response.ReturnValue('12345')
        x.check_value_contains('345')
        self.assertFalse(wtl.control_prim.fail.called)
    
    def test_ReturnValue_check_value_contains_stringContainedAtMiddle(self):
        x = wtl.response.ReturnValue('abcdefghijk')
        x.check_value_contains('de')
        self.assertFalse(wtl.control_prim.fail.called)
    
    def test_ReturnValue_check_value_contains_stringNotContained(self):
        x = wtl.response.ReturnValue('xyz')
        x.check_value_contains('yy')
        self.assertTrue(wtl.control_prim.fail.called)
    
    def test_ReturnValue_check_success_noValue(self):
        x = wtl.response.ReturnValue()
        x.check_success()
        self.assertTrue(wtl.control_prim.fail.called)
    
    def test_ReturnValue_check_success_successTrue(self):
        x = wtl.response.ReturnValue(2)
        x.check_success()
        self.assertFalse(wtl.control_prim.fail.called)
    
    def test_ReturnValue_check_success_successFalse(self):
        x = wtl.response.ReturnValue(-23)
        x.check_success()
        self.assertTrue(wtl.control_prim.fail.called)
    
    def test_ReturnValue_check_success_string(self):
        x = wtl.response.ReturnValue('abc')
        x.check_success()
        self.assertTrue(wtl.control_prim.fail.called)
    
    def test_ReturnValue_check_success_noValue(self):
        x = wtl.response.ReturnValue()
        x.check_failure()
        self.assertTrue(wtl.control_prim.fail.called)
    
    def test_ReturnValue_check_failure_failureTrue(self):
        x = wtl.response.ReturnValue(-1000)
        x.check_failure()
        self.assertFalse(wtl.control_prim.fail.called)
    
    def test_ReturnValue_check_failure_failureFalse(self):
        x = wtl.response.ReturnValue(1)
        x.check_failure()
        self.assertTrue(wtl.control_prim.fail.called)
    
    def test_ReturnValue_check_failure_string(self):
        x = wtl.response.ReturnValue('abc')
        x.check_failure()
        self.assertTrue(wtl.control_prim.fail.called)
    
    def test_XMLValue_get_log_data_NoData(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
              <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                <log uidWell='w1' uidWellbore='wb1' uid='l1'>
                  <indexCurve>M1</indexCurve>
                  <logData>
                    <mnemonicList>M1,M2,M3,M4</mnemonicList>
                    <unitList>m,m,ft,ft</unitList>
                  </logData>
                </log>
              </logs>""")
        self.assertTrue(len(x.log_data) == 0)
        self.assertTrue(x.get_mnemonics_list() == ['M1','M2','M3','M4'])
        self.assertTrue(x.get_units_list() == ['m','m','ft','ft'])
        self.assertTrue(x.get_index_curve_list() == [True,False,False,False])
        
    def test_XMLValue_get_log_data_1311(self):
        x = wtl.response.XMLValue(XML_LOG_1311)
        self.assertTrue(x.log_data == [
                                   ['1','2','3.0',''],
                                   ['2','0','3.1','10'],
                                   ['3','4','3.2','20'],
                                   ['4','0','3.3',''],
                                   ['5','','3.4','30']
                                  ])
        self.assertTrue(x.get_mnemonics_list() == ['M1','M2','M3','M4'])
        self.assertTrue(x.get_units_list() == ['m','m','m','m'])
        self.assertTrue(x.get_index_curve_list() == [False,True,False,False])
        
    def test_XMLValue_get_log_data_1311_out_of_order(self):
        x = wtl.response.XMLValue(XML_LOG_1311_OUT_OF_ORDER)
        self.assertTrue(x.log_data == [
                                   ['1','2','3.0',''],
                                   ['2','0','3.1','10'],
                                   ['3','4','3.2','20'],
                                   ['4','0','3.3',''],
                                   ['5','','3.4','30']
                                  ])
        
        self.assertTrue(x.get_mnemonics_list() == ['M4','M1','M2','M3'])
        self.assertTrue(x.get_units_list() == ['C','m','ft','deg'])
        self.assertTrue(x.get_index_curve_list() == [True,False,False,False])
        
    def test_XMLValue_get_log_data_1311_no_column_idx(self):
        x = wtl.response.XMLValue(XML_LOG_1311_NO_COLUMN_IDX)
        self.assertTrue(x.log_data == [
                                   ['1','2','3.0',''],
                                   ['2','0','3.1','10'],
                                   ['3','4','3.2','20'],
                                   ['4','0','3.3',''],
                                   ['5','','3.4','30']
                                  ])
        
        self.assertTrue(x.get_mnemonics_list() == ['','','',''])
        self.assertTrue(x.get_units_list() == ['','','',''])
        self.assertTrue(x.get_index_curve_list() ==  [True,False,False,False])    

    def test_XMLValue_get_log_data_1410(self):
        x = wtl.response.XMLValue(XML_LOG_1410)
        self.assertTrue(x.log_data == [
                                   ['1','2','3.0',''],
                                   ['2','0','3.1','10'],
                                   ['3','4','3.2','20'],
                                   ['4','0','3.3',''],
                                   ['5','','3.4','30']
                                  ])
        self.assertTrue(x.get_mnemonics_list() == ['M1','M2','M3','M4'])
        self.assertTrue(x.get_units_list() == ['m','m','m','m'])
        self.assertTrue(x.get_index_curve_list() == [True,False,False,False])


    def test_XMLValue_get_log_data_noLogCurveInfo(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
              <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                <log uidWell='w1' uidWellbore='wb1' uid='l1'>
                  <indexCurve>M1</indexCurve>
                  <logData>                        
                    <mnemonicList>M1,M2,M3,M4</mnemonicList>
                    <unitList>m,m,ft,ft</unitList>
                    <data>1.1,2.1,3.1,4.1</data>
                    <data>5,6,7,8</data>
                    <data>9,,,</data>>
                  </logData>
                </log>
              </logs>""")              
        self.assertTrue(x.log_data == [
                                   ['1.1','2.1','3.1','4.1'],
                                   ['5','6','7','8'],
                                   ['9','','','']
                                  ])
        self.assertTrue(x.get_mnemonics_list() == ['M1','M2','M3','M4'])
        self.assertTrue(x.get_units_list() == ['m','m','ft','ft'])
        self.assertTrue(x.get_index_curve_list() == [True,False,False,False])
    
    def test_XMLValue_get_log_data_noIndex(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
              <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                <log uidWell='w1' uidWellbore='wb1' uid='l1'>
                  <logData>                        
                    <mnemonicList>M1,M2,M3</mnemonicList>
                    <unitList>m,ft,ft</unitList>
                    <data>5,6,7</data>
                  </logData>
                </log>
              </logs>""")              
        self.assertTrue(x.log_data == [
                                   ['5','6','7']
                                  ])
        self.assertTrue(x.get_mnemonics_list() == ['M1','M2','M3'])
        self.assertTrue(x.get_units_list() == ['m','ft','ft'])
        self.assertTrue(x.get_index_curve_list() == [False,False,False])

    def test_XMLValue_get_log_data_noUnits(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
              <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                <log uidWell='w1' uidWellbore='wb1' uid='l1'>
                  <indexCurve>M1</indexCurve>
                  <logData>                        
                    <mnemonicList>M1,M2,M3</mnemonicList>
                    <data>5,6,7</data>
                  </logData>
                </log>
              </logs>""")              
        self.assertTrue(x.log_data == [
                                   ['5','6','7']
                                  ])
        self.assertTrue(x.get_mnemonics_list() == ['M1','M2','M3'])
        self.assertTrue(x.get_units_list() == [])
        self.assertTrue(x.get_index_curve_list() == [True,False,False])

    def test_XMLValue_clear(self):
        x = wtl.response.XMLValue(XML_LOG_1410)
        self.assertFalse(x.value == None)
        self.assertFalse(x.log_data == None)
        x.clear()
        self.assertTrue(x.value == None)
        self.assertTrue(x.log_data == None)
    
    def test_XMLValue__remove_encoding(self):
        x = wtl.response.XMLValue()
        s = x._remove_encoding("""<?xml version="1.0" encoding="UTF-8"?><wells xmlns="none"></wells>""")
        self.assertTrue(s == """<?xml version="1.0" ?><wells xmlns="none"></wells>""")
    
    def test_XMLValue__remove_encoding_multiLine(self):
        x = wtl.response.XMLValue()
        s = x._remove_encoding("""<?xml version="1.0" encoding="UTF-8"?>
        <wells xmlns="none">%s</wells>""")
        self.assertTrue(s == """<?xml version="1.0" ?>
        <wells xmlns="none">%s</wells>""")

    def test_XMLValue__remove_encoding_noEncoding(self):
        x = wtl.response.XMLValue()
        s = x._remove_encoding("""<wells xmlns="none"></wells>""")
        self.assertTrue(s == """<wells xmlns="none"></wells>""")
    
    def test_XMLValue_set_badXML(self):
        x = wtl.response.XMLValue(XML_LOG_1410)
        x.set("""<wells xmlns="none">""")
        self.assertTrue(x.value == None)
        self.assertTrue(x.log_data == None)
    
    def test_XMLValue_set_removeSpaces(self):
        x = wtl.response.XMLValue()
        x.set("""<?xml version="1.0" encoding="UTF-8"?>
                 <logs xmlns="none">                 <log>
                                     <logData>   <data>1,2,3</data>
                        
                        </logData></log>
                                                      </logs>""")
        self.assertTrue(x.value == """<logs><log><logData><data>1,2,3</data></logData></log></logs>""")


    def test_XMLValue_set_logData(self):
        x = wtl.response.XMLValue()
        x.set("""<?xml version="1.0" encoding="UTF-8"?>
                 <logs xmlns="none"><log><logData><data>1,2,3</data></logData></log></logs>""")
        self.assertTrue(x.value == """<logs><log><logData><data>1,2,3</data></logData></log></logs>""")
        self.assertFalse(x.log_data == None)
    
    def test_check_element_included_failIfDoesntExist(self):
        x = wtl.response.XMLValue(XML1)
        x.check_element_included('notexist')
        self.assertTrue(wtl.control_prim.fail.called)

    def test_check_element_included_successIfExists(self):
        x = wtl.response.XMLValue(XML1)
        x.check_element_included('well')
        self.assertFalse(wtl.control_prim.fail.called)

    def test_check_element_included_all_objects_success(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
              <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                <log uidWell='w1' uidWellbore='wb1' uid='l1'>
                  <name>log 1</name>
                </log>
                <log uidWell='w1' uidWellbore='wb1' uid='l2'>
                  <name>log 2</name>
                </log>
                <log uidWell='w1' uidWellbore='wb1' uid='l3'>
                  <name>log 3</name>
                </log>
              </logs>""")              
        x.check_element_included('name', check='all_objects')
        self.assertFalse(wtl.control_prim.fail.called)

    def test_check_element_included_all_objects_fail(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
              <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                <log uidWell='w1' uidWellbore='wb1' uid='l1'>
                  <name>log 1</name>
                </log>
                <log uidWell='w1' uidWellbore='wb1' uid='l2'>
                  <nameWell>log 2</nameWell>
                </log>
                <log uidWell='w1' uidWellbore='wb1' uid='l3'>
                  <name>log 3</name>
                </log>
              </logs>""")              
        x.check_element_included('name', check='all_objects')
        self.assertTrue(wtl.control_prim.fail.called)

    def test_check_element_not_included_successIfDoesntExist(self):
        x = wtl.response.XMLValue(XML1)
        x.check_element_not_included('notexist')
        self.assertFalse(wtl.control_prim.fail.called)

    def test_check_element_not_included_failIfExists(self):
        x = wtl.response.XMLValue(XML1)
        x.check_element_not_included('well')
        self.assertTrue(wtl.control_prim.fail.called)

    def test_check_element_value_failIfDoesntMatch(self):
        x = wtl.response.XMLValue(XML1)
        x.check_element_value('name', 'notexist')
        self.assertTrue(wtl.control_prim.fail.called)

    def test_check_element_value_successIfMatch(self):
        x = wtl.response.XMLValue(XML1)
        x.check_element_value('name', 'Test Well')
        self.assertFalse(wtl.control_prim.fail.called)

    def test_check_element_failIfDoesntMatch_regex(self):
        x = wtl.response.XMLValue(XML1)
        x.check_element_value('name', 'Tes.*dell', enable_regex=True)
        self.assertTrue(wtl.control_prim.fail.called)

    def test_check_element_value_successIfMatch_regex(self):
        x = wtl.response.XMLValue(XML1)
        x.check_element_value('name', 'Tes.*ell', enable_regex=True)
        self.assertFalse(wtl.control_prim.fail.called)

    def test_check_element_value_caseSensitive(self):
        x = wtl.response.XMLValue(XML1)
        x.check_element_value('name', 'test Well')
        self.assertTrue(wtl.control_prim.fail.called)

    def test_check_element_value_successIfMatch(self):
        x = wtl.response.XMLValue(XML1)
        x.check_element_value('name', 'Test Well')
        self.assertFalse(wtl.control_prim.fail.called)

    def test_check_element_value_contains_successIfContains(self):
        x = wtl.response.XMLValue(XML1)
        x.check_element_value_contains('name', 't W')
        self.assertFalse(wtl.control_prim.fail.called)

    def test_check_element_value_greaterthan_success(self):
        DOC = """<?xml version="1.0" encoding="%s"?>
                <wells xmlns="http://www.witsml.org/schemas/131">
                    <size>1.2</size>
                </wells>"""
        x = wtl.response.XMLValue(DOC)
        x.check_element_value_greaterthan('size', 1)
        self.assertFalse(wtl.control_prim.fail.called)
        x.check_element_value_greaterthan('size', 0.11)
        self.assertFalse(wtl.control_prim.fail.called)

    def test_check_element_value_greaterthan_failequal(self):
        DOC = """<?xml version="1.0" encoding="%s"?>
                <wells xmlns="http://www.witsml.org/schemas/131">
                    <size>1.2</size>
                </wells>"""
        x = wtl.response.XMLValue(DOC)
        x.check_element_value_greaterthan('size', 1.2)
        self.assertTrue(wtl.control_prim.fail.called)

    def test_check_element_value_greaterthan_faillessthan(self):
        DOC = """<?xml version="1.0" encoding="%s"?>
                <wells xmlns="http://www.witsml.org/schemas/131">
                    <size>1.2</size>
                </wells>"""
        x = wtl.response.XMLValue(DOC)
        x.check_element_value_greaterthan('size', 2)
        self.assertTrue(wtl.control_prim.fail.called)

    def test_check_element_value_lessthan_success(self):
        DOC = """<?xml version="1.0" encoding="%s"?>
                <wells xmlns="http://www.witsml.org/schemas/131">
                    <size>1.2</size>
                </wells>"""
        x = wtl.response.XMLValue(DOC)
        x.check_element_value_lessthan('size', 2)
        self.assertFalse(wtl.control_prim.fail.called)
        x.check_element_value_lessthan('size', 999.12)
        self.assertFalse(wtl.control_prim.fail.called)

    def test_check_element_value_lessthan_failequal(self):
        DOC = """<?xml version="1.0" encoding="%s"?>
                <wells xmlns="http://www.witsml.org/schemas/131">
                    <size>1.2</size>
                </wells>"""
        x = wtl.response.XMLValue(DOC)
        x.check_element_value_lessthan('size', 1.2)
        self.assertTrue(wtl.control_prim.fail.called)

    def test_check_element_value_greaterthan_faillessthan(self):
        DOC = """<?xml version="1.0" encoding="%s"?>
                <wells xmlns="http://www.witsml.org/schemas/131">
                    <size>1.2</size>
                </wells>"""
        x = wtl.response.XMLValue(DOC)
        x.check_element_value_lessthan('size', 0.52)
        self.assertTrue(wtl.control_prim.fail.called)

    def test_check_attribute_included_failIfDoesntExist(self):
        x = wtl.response.XMLValue(XML1)
        x.check_attribute_included('well', 'notexist')
        self.assertTrue(wtl.control_prim.fail.called)

    def test_check_attribute_included_successIfExists(self):
        x = wtl.response.XMLValue(XML1)
        x.check_attribute_included('well', 'uid')
        self.assertFalse(wtl.control_prim.fail.called)

    def test_check_attribute_not_included_successIfDoesntExist(self):
        x = wtl.response.XMLValue(XML1)
        x.check_attribute_not_included('well', 'notexist')
        self.assertFalse(wtl.control_prim.fail.called)

    def test_check_attribute_not_included_failIfExists(self):
        x = wtl.response.XMLValue(XML1)
        x.check_attribute_not_included('well', 'uid')
        self.assertTrue(wtl.control_prim.fail.called)
 
    def test_check_attribute_value_failIfDoesntMatch(self):
        x = wtl.response.XMLValue(XML1)
        x.check_attribute_value('well', 'uid', 'notexist')
        self.assertTrue(wtl.control_prim.fail.called)

    def test_check_attribute_value_successIfMatch(self):
        x = wtl.response.XMLValue(XML1)
        x.check_attribute_value('well', 'uid', 'tuid123')
        self.assertFalse(wtl.control_prim.fail.called)

    def test_check_attribute_value_failIfDoesntMatch_regex(self):
        x = wtl.response.XMLValue(XMLWITHPLUS)
        x.check_attribute_value('well', 'uid', 'tuid+123', enable_regex=True)
        self.assertTrue(wtl.control_prim.fail.called)

    def test_check_attribute_value_successIfMatch_regex(self):
        x = wtl.response.XMLValue(XMLWITHPLUS)
        x.check_attribute_value('well', 'uid', 't.id\+1.3', enable_regex=True)
        self.assertFalse(wtl.control_prim.fail.called)

    def test_check_attribute_value_all_objects_success(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
              <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                <log uidWell='w1' uidWellbore='wb1' uid='l1'>
                  <name>log 1</name>
                  <element uidWell='w1' uidWellbore='wb1' uid='l1'/>
                </log>
                <log uidWell='w1' uidWellbore='wb1' uid='l2'>
                  <name>log 2</name>
                  <element uidWell='w1' uidWellbore='wb1' uid='l2'/>
                </log>
                <log uidWell='w1' uidWellbore='wb1' uid='l3'>
                  <name>log 3</name>
                  <element uidWell='w1' uidWellbore='wb1' uid='l3'/>
                </log>
              </logs>""")              
        x.check_attribute_value('element', 'uidWellbore', 'wb1', check='all_objects')
        self.assertFalse(wtl.control_prim.fail.called)

    def test_check_attribute_value_all_objects_fail(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
              <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                <log uidWell='w1' uidWellbore='wb1' uid='l1'>
                  <name>log 1</name>
                  <element uidWell='w1' uidWellbore='wb1' uid='l1'/>
                </log>
                <log uidWell='w1' uidWellbore='wb1' uid='l2'>
                  <name>log 2</name>
                  <element uidWell='w1' uidWellbore='wb1' uid='l2'/>
                </log>
                <log uidWell='w1' uidWellbore='wb1'>
                  <name>log 3</name>
                  <element uidWell='w1' uidWellbore='wb1'/>
                </log>
              </logs>""")              
        x.check_attribute_value('element', 'uid', 'l1', check='all_objects')
        self.assertTrue(wtl.control_prim.fail.called)

    def test_check_attribute_value_is_contained_failIfDoesntContain(self):
        x = wtl.response.XMLValue(XML1)
        x.check_attribute_value_is_contained('well', 'uid', 'tuid12')
        self.assertTrue(wtl.control_prim.fail.called)

    def test_check_attribute_value_is_contained_successIfContains(self):
        x = wtl.response.XMLValue(XMLWITHPLUS)
        x.check_attribute_value_is_contained('well', 'uid', 'Ztuid+123Z')
        self.assertFalse(wtl.control_prim.fail.called)

    def test_check_number_of_objects_successIfCorrect(self):
        x = wtl.response.XMLValue(XML1)
        x.check_number_of_objects(1)
        self.assertFalse(wtl.control_prim.fail.called)

    def test_check_number_of_objects_successIfCorrectNoObjects(self):
        XML_DOC = """<?xml version="1.0" encoding="UTF-8"?>
                     <wells 
                         xmlns="http://www.witsml.org/schemas/1series" version="1.4.1.1">
                     </wells>"""
        x = wtl.response.XMLValue(XML_DOC)
        x.check_number_of_objects(0)
        self.assertFalse(wtl.control_prim.fail.called)

    def test_check_number_of_objects_successIfCorrectWithDocumentInfo(self):
        XML_DOC = """<?xml version="1.0" encoding="UTF-8"?>
                     <wells xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                       <documentInfo>
                         <documentName>well</documentName>
                         <fileCreationInformation>
                           <fileCreationDate>2001-10-31T08:15:00.000Z</fileCreationDate>
                           <fileCreator>John Smith</fileCreator>
                         </fileCreationInformation>
                       </documentInfo>
                       <well uid="tuid123">
                         <name>Test Well</name>
                        <numAPI>testAPI</numAPI>
                       </well>
                     </wells>"""
        x = wtl.response.XMLValue(XML_DOC)
        x.check_number_of_objects(1)
        self.assertFalse(wtl.control_prim.fail.called)

    def test_check_number_of_objects_successIfCorrectWithComments(self):
        XML_DOC = """<?xml version="1.0" encoding="UTF-8"?>
                     <wells 
                         xmlns="http://www.witsml.org/schemas/1series" version="1.4.1.1">
                         <!-- comment 1 -->
                         <!-- comment 2 -->
                         <well uid="w-12">
                             <name>6507/7-A-42</name>
                         </well>
                     </wells>"""
        x = wtl.response.XMLValue(XML_DOC)
        x.check_number_of_objects(1)
        self.assertFalse(wtl.control_prim.fail.called)
 
    def test_check_number_of_objects_failIfIncorrect(self):
        x = wtl.response.XMLValue(XML1)
        x.check_number_of_objects(2)
        self.assertTrue(wtl.control_prim.fail.called)

    def test_check_number_of_objects_failIfIncorrectWithDocumentInfo(self):
        XML_DOC = """<?xml version="1.0" encoding="UTF-8"?>
                     <wells xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                       <documentInfo>
                         <documentName>well</documentName>
                         <fileCreationInformation>
                           <fileCreationDate>2001-10-31T08:15:00.000Z</fileCreationDate>
                           <fileCreator>John Smith</fileCreator>
                         </fileCreationInformation>
                       </documentInfo>
                       <well uid="tuid123">
                         <name>Test Well</name>
                        <numAPI>testAPI</numAPI>
                       </well>
                     </wells>"""
        x = wtl.response.XMLValue(XML_DOC)
        x.check_number_of_objects(2)
        self.assertTrue(wtl.control_prim.fail.called)

    def test_check_number_of_objects_greaterthan_successIfCorrect(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
              <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                <log uidWell='w1' uidWellbore='wb1' uid='l1'/>
                <log uidWell='w1' uidWellbore='wb1' uid='l2'/>
                <log uidWell='w1' uidWellbore='wb1' uid='l3'/>
              </logs>""")
        x.check_number_of_objects_greaterthan(2)
        self.assertFalse(wtl.control_prim.fail.called)

    def test_check_number_of_objects_greaterthan_failIfIncorrect(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
              <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                <log uidWell='w1' uidWellbore='wb1' uid='l1'/>
                <log uidWell='w1' uidWellbore='wb1' uid='l2'/>
                <log uidWell='w1' uidWellbore='wb1' uid='l3'/>
              </logs>""")
        x.check_number_of_objects_greaterthan(3)
        self.assertTrue(wtl.control_prim.fail.called)

    def test_check_number_of_objects_lessthan_successIfCorrect(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
              <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                <log uidWell='w1' uidWellbore='wb1' uid='l1'/>
                <log uidWell='w1' uidWellbore='wb1' uid='l2'/>
                <log uidWell='w1' uidWellbore='wb1' uid='l3'/>
              </logs>""")
        x.check_number_of_objects_lessthan(4)
        self.assertFalse(wtl.control_prim.fail.called)

    def test_check_number_of_objects_lessthan_failIfIncorrect(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
              <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                <log uidWell='w1' uidWellbore='wb1' uid='l1'/>
                <log uidWell='w1' uidWellbore='wb1' uid='l2'/>
                <log uidWell='w1' uidWellbore='wb1' uid='l3'/>
              </logs>""")
        x.check_number_of_objects_lessthan(3)
        self.assertTrue(wtl.control_prim.fail.called)

    def test_XMLValue_set_encoding_shouldAcceptEncodingUTF8(self):
        # Test UTF-8
        x1 = XML_ENCODING %("UTF-8", XMLBODY)
        r = wtl.response.XMLValue()
        r.set(unicode(x1))
        r.set(x1)
        
    def test_XMLValue_set_encoding_shouldAcceptEncodingUTF16(self):
        # Test UTF-16
        x1 = XML_ENCODING %("UTF-16", XMLBODY)
        r = wtl.response.XMLValue()
        r.set(x1.encode("UTF-16"))
        
    def test_XMLValue_set_encoding_shouldAcceptEncodingNone(self):
        # Test no encoding
        x1 = XML1
        r = wtl.response.XMLValue()
        r.set(unicode(x1))
        r.set(x1)        

    def test_XMLValue_set_encoding_shouldAcceptEncodingInvalid(self):
        # Test invalid encoding
        x1 = XML_ENCODING %("abc", XMLBODY)
        r = wtl.response.XMLValue()
        r.set(unicode(x1))
        r.set(x1)        

    def test_XMLValue_get_attribute(self):
        # Test get attribute function
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
              <logs xmlns="http://www.witsml.org/schemas/131" version="1.3.1.1">
                  <log>
                    <element1/>
                    <element2 at1="123" at2=""/>
                    <element3/>
                    <mnemonic>M1</mnemonic>
                    <columnIndex>1</columnIndex>
                    <unit>m</unit>
                  </log>
              </logs>""")
        
        self.assertTrue(x.get_attribute('element2', 'at1') == '123')
        self.assertTrue(x.get_attribute('element2', 'at2') == '')
        self.assertTrue(x.get_attribute('element2', 'at3') == None)
        self.assertTrue(x.get_attribute('element4', 'at3') == None)

    def test_build_elements_list(self):
        # Test build_elements_list method
        x = wtl.response.XMLValue(XML_LOG_1410)
        elements = x.build_elements_list();
        self.assertTrue( elements == ['logs', 'logs[version]',
                                                 'log', 'log[uidWell]' , 'log[uidWellbore]', 'log[uid]',
                                                 'indexCurve', 
                                                 'logCurveInfo', 'mnemonic', 'unit',
                                                 'logCurveInfo', 'mnemonic', 'unit',
                                                 'logCurveInfo', 'mnemonic', 'unit',
                                                 'logCurveInfo', 'mnemonic', 'unit',
                                                 'logData', 'mnemonicList',   'unitList',
                                                 'data', 'data', 'data', 'data', 'data'] ) 

    def test_build_elements_list_just_plural(self):
        # Test build_elements_list method
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
                                     <logs xmlns="http://www.witsml.org/schemas/131" version="1.3.1.1"/>""")
        elements = x.build_elements_list();
        self.assertTrue( elements == ['logs', 'logs[version]'] ) 


    def test_build_attribute_and_child_elements_list(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
              <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                <log attrib1='a1' attrib2='a2' attrib3='a3'>
                  <element1>elem1</element1>
                  <element2>elem2</element2>
                  <element3>elem3</element3>
                </log>
                <log attrib4='a4'>
                  <element4 attrib5='a5'>
                      <element5 attrib7='a7'>elem5</element5>                      
                  </element4>
                </log>
                <log attrib6='a6'/>
                <log/>
                <log>
                  <element6>elem6</element6>
                  <element7>
                      <element8>elem8</element8>
                  </element7>    
                  <element7/>
                  <element6>elem6</element6>
                </log>
              </logs>""") 
        
        
        element = x.get_element("log")
        self.assertTrue(x.build_attribute_and_child_elements_list(None)== [])
        self.assertTrue(x.build_attribute_and_child_elements_list(element[0])== ['log[attrib1]' , 'log[attrib2]', 'log[attrib3]', 'element1', 'element2', 'element3' ])
        self.assertTrue(x.build_attribute_and_child_elements_list(element[1])== ['log[attrib4]', 'element4'])
        self.assertTrue(x.build_attribute_and_child_elements_list(element[2])== ['log[attrib6]'])
        self.assertTrue(x.build_attribute_and_child_elements_list(element[3])== [])
        self.assertTrue(x.build_attribute_and_child_elements_list(element[4])== ['element6','element7'])

    def test_check_element_attribute_and_children_list_matchExact(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
            <wellbores>
                <wellbore uidWell="W-12" uid="B-01">
                    <nameWell>6507/7-A-42</nameWell>
                    <name>A-41</name>
                </wellbore>
                <wellbore uidWell="W-12" uid="B-02">
                    <nameWell>6507/7-A-42</nameWell>
                    <name>A-42</name>
                </wellbore>
                <wellbore uidWell="W-13" uid="C-01">
                    <nameWell>6507/7-A-43</nameWell>
                    <name>B-41</name>
                </wellbore>
            </wellbores>""") 
        x.check_element_attribute_and_children_list('wellbore',['wellbore[uidWell]', 'wellbore[uid]', 'name', 'nameWell'],
                                                    match='exact')
        self.assertFalse(wtl.control_prim.fail.called)
        
    def test_check_element_attribute_and_children_list_matchExact_missingAttribute(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
            <wellbores>
                <wellbore uidWell="W-12" uid="B-01">
                    <nameWell>6507/7-A-42</nameWell>
                    <name>A-41</name>
                </wellbore>
                <wellbore uidWell="W-12">
                    <nameWell>6507/7-A-42</nameWell>
                    <name>A-42</name>
                </wellbore>
                <wellbore uidWell="W-13" uid="C-01">
                    <nameWell>6507/7-A-43</nameWell>
                    <name>B-41</name>
                </wellbore>
            </wellbores>""") 
        x.check_element_attribute_and_children_list('wellbore',['wellbore[uidWell]', 'wellbore[uid]', 'name', 'nameWell'],
                                                    match='exact')
        self.assertTrue(wtl.control_prim.fail.called)
        
    def test_check_element_attribute_and_children_list_matchExact_missingChild(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
            <wellbores>
                <wellbore uidWell="W-12" uid="B-01">
                    <nameWell>6507/7-A-42</nameWell>
                    <name>A-41</name>
                </wellbore>
                <wellbore uidWell="W-12" uid="B-02">
                    <nameWell>6507/7-A-42</nameWell>
                    <name>A-42</name>
                </wellbore>
                <wellbore uidWell="W-13" uid="C-01">
                    <name>B-41</name>
                </wellbore>
            </wellbores>""") 
        x.check_element_attribute_and_children_list('wellbore',['wellbore[uidWell]', 'wellbore[uid]', 'name', 'nameWell'],
                                                    match='exact')
        self.assertTrue(wtl.control_prim.fail.called)
        
    def test_check_element_attribute_and_children_list_matchExact_extraAttribute(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
            <wellbores>
                <wellbore uidWell="W-12" uid="B-01" extra="extra">
                    <nameWell>6507/7-A-42</nameWell>
                    <name>A-41</name>
                </wellbore>
                <wellbore uidWell="W-12" uid="B-02">
                    <nameWell>6507/7-A-42</nameWell>
                    <name>A-42</name>
                </wellbore>
                <wellbore uidWell="W-13" uid="C-01">
                    <nameWell>6507/7-A-43</nameWell>
                    <name>B-41</name>
                </wellbore>
            </wellbores>""")  
        x.check_element_attribute_and_children_list('wellbore',['wellbore[uidWell]', 'wellbore[uid]', 'name', 'nameWell'],
                                                    match='exact')
        self.assertTrue(wtl.control_prim.fail.called)
        
    def test_check_element_attribute_and_children_list_matchExact_extraChild(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
            <wellbores>
                <wellbore uidWell="W-12" uid="B-01">
                    <nameWell>6507/7-A-42</nameWell>
                    <name>A-41</name>
                </wellbore>
                <wellbore uidWell="W-12" uid="B-02">
                    <nameWell>6507/7-A-42</nameWell>
                    <extra/>
                    <name>A-42</name>
                </wellbore>
                <wellbore uidWell="W-13" uid="C-01">
                    <nameWell>6507/7-A-43</nameWell>
                    <name>B-41</name>
                </wellbore>
            </wellbores>""")  
        x.check_element_attribute_and_children_list('wellbore',['wellbore[uidWell]', 'wellbore[uid]', 'name', 'nameWell'],
                                                    match='exact')
        self.assertTrue(wtl.control_prim.fail.called)
        
    def test_check_element_attribute_and_children_list_matchExact_missing_element_in_List(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
            <wellbores>
                <wellbore uidWell="W-12" uid="B-01">
                    <nameWell>6507/7-A-42</nameWell>
                    <name>A-41</name>
                </wellbore>
                <wellbore uidWell="W-12" uid="B-02">
                    <nameWell>6507/7-A-42</nameWell>
                    <name>A-42</name>
                </wellbore>
                <wellbore uidWell="W-13" uid="C-01">
                    <nameWell>6507/7-A-43</nameWell>
                    <name>B-41</name>
                </wellbore>
            </wellbores>""") 
        x.check_element_attribute_and_children_list('wellbore',['wellbore[uidWell]', 'wellbore[uid]', 'nameWell'],
                                                    match='exact')
        self.assertTrue(wtl.control_prim.fail.called)        
        
    def test_check_element_attribute_and_children_list_matchExact_missing_attribute_in_List(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
            <wellbores>
                <wellbore uidWell="W-12" uid="B-01">
                    <nameWell>6507/7-A-42</nameWell>
                    <name>A-41</name>
                </wellbore>
                <wellbore uidWell="W-12" uid="B-02">
                    <nameWell>6507/7-A-42</nameWell>
                    <name>A-42</name>
                </wellbore>
                <wellbore uidWell="W-13" uid="C-01">
                    <nameWell>6507/7-A-43</nameWell>
                    <name>B-41</name>
                </wellbore>
            </wellbores>""") 
        x.check_element_attribute_and_children_list('wellbore',['wellbore[uidWell]', 'name', 'nameWell'],
                                                    match='exact')
        self.assertTrue(wtl.control_prim.fail.called)           
        
    def test_check_element_attribute_and_children_list_matchExact_subElement_well(self):        
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="utf-8"?>
                                   <wells xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                      <well uid="Energistics-well-0001">
                                         <name>Energistics Certification Well 1</name>
                                         <wellDatum uid="KB">
                                             <name>Kelly Bushing</name>
                                             <code>KB</code>
                                             <elevation uom="ft">78.5</elevation>
                                         </wellDatum>
                                         <wellCRS uid="proj1">
                                             <name>ED50 / UTM Zone 31N</name>
                                             <mapProjection>
                                                 <nameCRS namingSystem="epsg">ED50 / UTM Zone 31N</nameCRS>
                                                 <NADType>unknown</NADType>
                                             </mapProjection>
                                         </wellCRS>
                                         <wellCRS uid="geog1">
                                            <name>ED50</name>
                                            <geographic>
                                                <nameCRS namingSystem="epsg">ED50</nameCRS>
                                            </geographic>
                                         </wellCRS>
                                      </well>
                                   </wells>""")
        x.check_element_attribute_and_children_list('well/wellCRS/mapProjection',['nameCRS', 'NADType'],
                                                    match='exact')
        self.assertFalse(wtl.control_prim.fail.called)        

    def test_check_element_attribute_and_children_list_matchExact_subElement_trajectory(self):        
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
    <trajectorys xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
        <trajectory uidWell="Energistics-well-0001" uidWellbore="Energistics-w1-wellbore-0001" uid="Energistics-w1-wb1-trajectory-0001">
            <nameWell>Energistics Certification Well 1</nameWell>
            <nameWellbore>Energistics Certification Well 1 Wellbore 1</nameWellbore>
            <name>Energistics Certification Well 1 Wellbore 1 Trajectory 1</name>
            <trajectoryStation uid="1">
                <typeTrajStation>tie in point</typeTrajStation>
                <md uom="ft">0</md>
            </trajectoryStation>
            <trajectoryStation uid="2">
                <typeTrajStation>tie in point</typeTrajStation>
                <md uom="ft">0</md>
            </trajectoryStation>            
            <commonData>
                <itemState>plan</itemState>
                <comments>These are the comments associated with the trajectory data object.</comments>
            </commonData>
        </trajectory>
    </trajectorys>
    """)
        x.check_element_attribute_and_children_list('trajectory/trajectoryStation',['trajectoryStation[uid]', 'typeTrajStation', 'md'],
                                                    match='exact')
        self.assertFalse(wtl.control_prim.fail.called)                 
        
    def test_check_element_attribute_and_children_list_matchExact_subElement_extraElement_trajectory(self):        
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
    <trajectorys xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
        <trajectory uidWell="Energistics-well-0001" uidWellbore="Energistics-w1-wellbore-0001" uid="Energistics-w1-wb1-trajectory-0001">
            <nameWell>Energistics Certification Well 1</nameWell>
            <nameWellbore>Energistics Certification Well 1 Wellbore 1</nameWellbore>
            <name>Energistics Certification Well 1 Wellbore 1 Trajectory 1</name>
            <trajectoryStation uid="1">
                <typeTrajStation>tie in point</typeTrajStation>
                <md uom="ft">0</md>
            </trajectoryStation>
            <trajectoryStation uid="2">
                <typeTrajStation>tie in point</typeTrajStation>
                <md uom="ft">0</md>
                <extra/>
            </trajectoryStation>  
            <commonData>
                <itemState>plan</itemState>
                <comments>These are the comments associated with the trajectory data object.</comments>
            </commonData>
        </trajectory>
    </trajectorys>
    """)
        x.check_element_attribute_and_children_list('trajectory/trajectoryStation',['trajectoryStation[uid]', 'typeTrajStation', 'md'],
                                                    match='exact')
        self.assertTrue(wtl.control_prim.fail.called)         
        
    def test_check_element_attribute_and_children_list_matchAtleast(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
            <wellbores xmlns="http://www.witsml.org/schemas/1series" 
                       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
                       xsi:schemaLocation="http://www.witsml.org/schemas/1series  ../xsd_schemas/obj_wellbore.xsd" 
                       version="1.4.1.1">
                <wellbore uidWell="W-12" uid="B-01">
                    <nameWell>6507/7-A-42</nameWell>
                    <name>A-41</name>
                    <extra>blah</extra>
                </wellbore>
                <wellbore uidWell="W-12" uid="B-02" attrib="extra">
                    <nameWell>6507/7-A-42</nameWell>
                    <name>A-42</name>
                </wellbore>
                <wellbore uidWell="W-13" uid="C-01" attrib="extra">
                    <nameWell>6507/7-A-43</nameWell>
                <name>B-41</name>
                    <extra>blah</extra>
                </wellbore>
            </wellbores>""") 
        x.check_element_attribute_and_children_list('wellbore',['wellbore[uidWell]', 'wellbore[uid]', 'name', 'nameWell'],
                                                    match='at-least')
        self.assertFalse(wtl.control_prim.fail.called)

    def test_check_element_attribute_and_children_list_matchAtleast_missingAttribute(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
            <wellbores>
                <wellbore uidWell="W-12" uid="B-01">
                    <nameWell>6507/7-A-42</nameWell>
                    <name>A-41</name>
                    <extra>blah</extra>
                </wellbore>
                <wellbore uidWell="W-12" uid="B-02" attrib="extra">
                    <nameWell>6507/7-A-42</nameWell>
                    <name>A-42</name>
                </wellbore>
                <wellbore uid="C-01" attrib="extra">
                    <nameWell>6507/7-A-43</nameWell>
                <name>B-41</name>
                    <extra>blah</extra>
                </wellbore>
            </wellbores>""") 
        x.check_element_attribute_and_children_list('wellbore',['wellbore[uidWell]', 'wellbore[uid]', 'name', 'nameWell'],
                                                    match='at-least')
        self.assertTrue(wtl.control_prim.fail.called)

    def test_check_element_attribute_and_children_list_matchAtleast_missingChild(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
            <wellbores>
                <wellbore uidWell="W-12" uid="B-01">
                    <nameWell>6507/7-A-42</nameWell>
                    <extra>blah</extra>
                </wellbore>
                <wellbore uidWell="W-12" uid="B-02" attrib="extra">
                    <nameWell>6507/7-A-42</nameWell>
                    <name>A-42</name>
                </wellbore>
                <wellbore uidWell="W-13" uid="C-01" attrib="extra">
                    <nameWell>6507/7-A-43</nameWell>
                <name>B-41</name>
                    <extra>blah</extra>
                </wellbore>
            </wellbores>""") 
        x.check_element_attribute_and_children_list('wellbore',['wellbore[uidWell]', 'wellbore[uid]', 'name', 'nameWell'],
                                                    match='at-least')
        self.assertTrue(wtl.control_prim.fail.called)

    def test_check_element_attribute_and_children_list_matchAtMost(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
            <wellbores xmlns="http://www.witsml.org/schemas/1series" 
                       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
                       xsi:schemaLocation="http://www.witsml.org/schemas/1series  ../xsd_schemas/obj_wellbore.xsd" 
                       version="1.4.1.1">
                <wellbore uidWell="W-12">
                    <nameWell>6507/7-A-42</nameWell>
                    <name>A-41</name>
                </wellbore>
                <wellbore uidWell="W-12" uid="B-02">
                    <name>A-42</name>
                </wellbore>
                <wellbore/>
            </wellbores>""") 
        x.check_element_attribute_and_children_list('wellbore',['wellbore[uidWell]', 'wellbore[uid]', 'name', 'nameWell'],
                                                    match='at-most')
        self.assertFalse(wtl.control_prim.fail.called)

    def test_check_element_attribute_and_children_list_matchAtMost_extraAttribute(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
            <wellbores>
                <wellbore uidWell="W-12">
                    <nameWell>6507/7-A-42</nameWell>
                    <name>A-41</name>
                </wellbore>
                <wellbore/>
                <wellbore uidWell="W-12" uid="B-02" extra="extra">
                    <name>A-42</name>
                </wellbore>
            </wellbores>""") 
        x.check_element_attribute_and_children_list('wellbore',['wellbore[uidWell]', 'wellbore[uid]', 'name', 'nameWell'],
                                                    match='at-most')
        self.assertTrue(wtl.control_prim.fail.called)

    def test_check_element_attribute_and_children_list_matchAtMost_extraChild(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
            <wellbores>
                <wellbore uidWell="W-12">
                    <nameWell>6507/7-A-42</nameWell>
                    <name>A-41</name>
                </wellbore>
                <wellbore uidWell="W-12" uid="B-02">
                    <name>A-42</name>
                    <extra/>
                </wellbore>
                <wellbore/>
            </wellbores>""") 
        x.check_element_attribute_and_children_list('wellbore',['wellbore[uidWell]', 'wellbore[uid]', 'name', 'nameWell'],
                                                    match='at-most')
        self.assertTrue(wtl.control_prim.fail.called)

    def test_check_only_included(self):
        # Test build_elements_list method
        x = wtl.response.XMLValue(XML_LOG_1410)
        self.assertTrue( x.check_only_included( ['logs', 'logs[version]',
                                                 'log', 'log[uidWell]' , 'log[uidWellbore]', 'log[uid]',
                                                 'indexCurve', 
                                                 'logCurveInfo', 'mnemonic', 'unit',
                                                 'logCurveInfo', 'mnemonic', 'unit',
                                                 'logCurveInfo', 'mnemonic', 'unit',
                                                 'logCurveInfo', 'mnemonic', 'unit',
                                                 'logData', 'mnemonicList',   'unitList',
                                                 'data', 'data', 'data', 'data', 'data'] ) ) 
        self.assertFalse(wtl.control_prim.fail.called)

    def test_check_only_included_failure_underrun(self):
        # Test build_elements_list method (underrun list)
        x = wtl.response.XMLValue(XML_LOG_1410)
        x.check_only_included( ['logs', 'logs[version]',
                                                 'log', 'log[uidWell]' , 'log[uidWellbore]', 'log[uid]',
                                                 'indexCurve', 
                                                 'logCurveInfo', 'mnemonic', 'unit',
                                                 'logCurveInfo', 'mnemonic', 'unit',
                                                 'logCurveInfo', 'mnemonic', 'unit',
                                                 'logCurveInfo', 'mnemonic', 'unit',
                                                 'logData', 'mnemonicList',   'unitList',
                                                 'data', 'data', 'data', 'data'] )
        self.assertTrue(wtl.control_prim.fail.called)


    def test_check_only_included_bad_element(self):
        # Test build_elements_list method
        x = wtl.response.XMLValue(XML_LOG_1410)
        x.check_only_included( ['logs', 'logs[version]',
                                                 'leg', 'log[uidWell]' , 'log[uidWellbore]', 'log[uid]',
                                                 'indexCurve', 
                                                 'logCurveInfo', 'mnemonic', 'unit',
                                                 'logCurveInfo', 'mnemonic', 'unit',
                                                 'logCurveInfo', 'mnemonic', 'unit',
                                                 'logCurveInfo', 'mnemonic', 'unit',
                                                 'logData', 'mnemonicList',   'unitList',
                                                 'data', 'data', 'data', 'data', 'data'] )
        self.assertTrue(wtl.control_prim.fail.called)

    def test_check_only_included_bad_attribute(self):
        # Test build_elements_list method
        x = wtl.response.XMLValue(XML_LOG_1410)
        x.check_only_included( ['logs', 'logs[version]',
                                                 'log', 'log[uidWell]' , 'log[uidWellbore]', 'log[uido]',
                                                 'indexCurve', 
                                                 'logCurveInfo', 'mnemonic', 'unit',
                                                 'logCurveInfo', 'mnemonic', 'unit',
                                                 'logCurveInfo', 'mnemonic', 'unit',
                                                 'logCurveInfo', 'mnemonic', 'unit',
                                                 'logData', 'mnemonicList',   'unitList',
                                                 'data', 'data', 'data', 'data', 'data'] )
        self.assertTrue(wtl.control_prim.fail.called)

    def test_check_only_included_failure_overrun(self):
        # Test build_elements_list method (overrun list)
        x = wtl.response.XMLValue(XML_LOG_1410)
        x.check_only_included( ['logs', 'logs[version]',
                                                 'log', 'log[uidWell]' , 'log[uidWellbore]', 'log[uid]',
                                                 'indexCurve', 
                                                 'logCurveInfo', 'mnemonic', 'unit',
                                                 'logCurveInfo', 'mnemonic', 'unit',
                                                 'logCurveInfo', 'mnemonic', 'unit',
                                                 'logCurveInfo', 'mnemonic', 'unit',
                                                 'logData', 'mnemonicList',   'unitList',
                                                 'data', 'data', 'data', 'data', 'data', 'data'] ) 
        self.assertTrue(wtl.control_prim.fail.called)

    def test_check_only_included_failure_missing_element(self):
        # Test build_elements_list method (missing element)
        x = wtl.response.XMLValue(XML_LOG_1410)
        x.check_only_included(  ['logs', 'logs[version]',
                                                 'log[uidWell]' , 'log[uidWellbore]', 'log[uid]',
                                                 'indexCurve', 
                                                 'logCurveInfo', 'mnemonic', 'unit',
                                                 'logCurveInfo', 'mnemonic', 'unit',
                                                 'logCurveInfo', 'mnemonic', 'unit',
                                                 'logCurveInfo', 'mnemonic', 'unit',
                                                 'logData', 'mnemonicList',   'unitList',
                                                 'data', 'data', 'data', 'data', 'data']) 
        self.assertTrue(wtl.control_prim.fail.called)
 
    def test_check_only_included_failure_missing_attrib(self):
        # Test build_elements_list method (missing attribute)
        x = wtl.response.XMLValue(XML_LOG_1410)
        x.check_only_included( ['logs', 'logs[version]',
                                                 'log', 'log[uidWellbore]', 'log[uid]',
                                                 'indexCurve', 
                                                 'logCurveInfo', 'mnemonic', 'unit',
                                                 'logCurveInfo', 'mnemonic', 'unit',
                                                 'logCurveInfo', 'mnemonic', 'unit',
                                                 'logCurveInfo', 'mnemonic', 'unit',
                                                 'logData', 'mnemonicList',   'unitList',
                                                 'data', 'data', 'data', 'data', 'data'] ) 
        self.assertTrue(wtl.control_prim.fail.called)
                
    def test_check_valid_witsml_versions(self):
        x = wtl.response.XMLValue(XML_LOG_1410)
        self.assertFalse(x.check_valid_witsml_versions(""))
        self.assertFalse(x.check_valid_witsml_versions("1.2.1a"))
        
        self.assertTrue(x.check_valid_witsml_versions("1.2.0"))
        self.assertTrue(x.check_valid_witsml_versions("1.2.0,1.2.1"))
        self.assertTrue(x.check_valid_witsml_versions("1.2.0,1.3.1.0"))
        self.assertTrue(x.check_valid_witsml_versions("1.2.0,1.3.1.0,1.3.1.1"))
        self.assertTrue(x.check_valid_witsml_versions("1.2.0,1.3.1.0,1.3.1.1,1.4.1"))
        self.assertTrue(x.check_valid_witsml_versions("1.2.0,1.3.1.0,1.3.1.1,1.4.1.1"))
        self.assertTrue(x.check_valid_witsml_versions("1.2.0,1.3.1.0,1.3.1.1,1.4.1,1.4.1.1"))
                
        self.assertFalse(x.check_valid_witsml_versions("1.2.1,1.2.0"))
        self.assertFalse(x.check_valid_witsml_versions("1.3.1.0,1.2.0"))
        self.assertFalse(x.check_valid_witsml_versions("1.2.0,1.3.1.1,1.3.1.0"))
        self.assertFalse(x.check_valid_witsml_versions("1.2.0,1.3.1.0,1.4.1,1.3.1.1"))
        self.assertFalse(x.check_valid_witsml_versions("1.2.0,1.3.1.0,1.3.1.1,1.4.1.1,1.4.1"))
        self.assertFalse(x.check_valid_witsml_versions("1.2.0,1.3.1.0,1.3.1.1,1.4.2,1.4.1.1"))
        
        # check spacing fails
        self.assertFalse(x.check_valid_witsml_versions("1.2.0, 1.2.1"))
        self.assertFalse(x.check_valid_witsml_versions("1.2.0,1.3.1.0, 1.3.1.1"))
        self.assertFalse(x.check_valid_witsml_versions("1.2.0, 1.3.1.0 , 1.3.1.1, 1.4.1"))
        self.assertFalse(x.check_valid_witsml_versions("1.2.0,1.3.1.0,     1.3.1.1,1.4.1.1"))
        self.assertFalse(x.check_valid_witsml_versions("1.2.0,1.3.1.0,1.3.1.1,1.4.1,1.4.1.1 "))
        self.assertFalse(x.check_valid_witsml_versions("1.2.0, 1.3.1.0,\t1.3.1.1,1.4.1"))
            
    def test_check_xmlout_string_does_not_contain_basic_strings(self):
        x = wtl.response.XMLValue(XML_LOG_1410)
        
        x.check_string_does_not_contain("STRING_NOT_TO_BE_FOUND")
        self.assertFalse(wtl.control_prim.fail.called)

        x.check_string_does_not_contain(".*M1.*")
        self.assertFalse(wtl.control_prim.fail.called)
                    
        x.check_string_does_not_contain("M1")
        self.assertTrue(wtl.control_prim.fail.called)
        
    def test_check_xmlout_string_does_not_contain_string_variable(self):
        x = wtl.response.XMLValue(XML_LOG_1410)
        
        wtl.utils.set_variable_value('foundTestString', "M1")
        wtl.utils.set_variable_value('notFoundTestString', "STRING_NOT_TO_BE_FOUND")      
        
        x.check_string_does_not_contain("$notFoundTestString$")
        self.assertFalse(wtl.control_prim.fail.called)
        
        x.check_string_does_not_contain("$foundTestString$")
        self.assertTrue(wtl.control_prim.fail.called)

    def test_check_log_data_index_value(self):
        # Test log data index value properly populated
        x = wtl.response.XMLValue(XML_LOG_1410)
        x.check_log_data_index_value(0, 1, error_margin=1)
        x.check_log_data_index_value(1, '2')
        x.check_log_data_index_value(2, 3, error_margin=1)
        x.check_log_data_index_value(3, 4.1, error_margin=10)
        x.check_log_data_index_value(4, 4.9, error_margin=10)             
        self.assertFalse(wtl.control_prim.fail.called)

    def test_check_log_data_index_value_index_too_high(self):
        x = wtl.response.XMLValue(XML_LOG_1410)
        x.check_log_data_index_value(7, 3, error_margin=99)
        self.assertTrue(wtl.control_prim.fail.called)

    def test_check_log_data_index_value_no_float_value_received(self):
        XML_TIMELOG =  """<?xml version="1.0" encoding="UTF-8"?>
              <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.1">
                <log uidWell='w1' uidWellbore='wb1' uid='l1'>
                  <indexCurve>M1</indexCurve>
                  <logCurveInfo>
                    <mnemonic>M1</mnemonic>
                    <unit>datetime</unit>
                  </logCurveInfo>
                  <logCurveInfo>
                    <mnemonic>M2</mnemonic>
                    <unit>m</unit>
                  </logCurveInfo>
                  <logData>                        
                    <mnemonicList>M1,M2</mnemonicList>
                    <unitList>datetime,m</unitList>
                    <data>2003-11-24T08:15:00.000Z,2</data>
                    <data>2003-11-24T08:15:01.000Z,0</data>
                  </logData>
                </log>
              </logs>"""
        x = wtl.response.XMLValue(XML_TIMELOG)
        x.check_log_data_index_value(0, 3, error_margin=99)
        self.assertTrue(wtl.control_prim.fail.called)
  
    def test_check_log_data_data_value(self):
        # Test log data data value properly populated
        x = wtl.response.XMLValue(XML_LOG_1410)
        x.check_log_data_data_value(0,'M1', 1, error_margin=1)
        x.check_log_data_data_value(1,'M1', '2')
        x.check_log_data_data_value(2,'M1', 3, error_margin=1)
        x.check_log_data_data_value(3,'M1', 4.1, error_margin=10)
        x.check_log_data_data_value(4,'M1', 4.9, error_margin=10)             
        x.check_log_data_data_value(4,'M2', '')
        self.assertFalse(wtl.control_prim.fail.called)

    def test_check_log_data_data_value_index_too_high(self):
        x = wtl.response.XMLValue(XML_LOG_1410)
        x.check_log_data_data_value(7,'M1', 3, error_margin=99)
        self.assertTrue(wtl.control_prim.fail.called)

    def test_check_log_data_data_value_bad_mnemonic(self):
        x = wtl.response.XMLValue(XML_LOG_1410)
        x.check_log_data_data_value(0,'M7', 3, error_margin=99)
        self.assertTrue(wtl.control_prim.fail.called)

    def test_check_log_data_data_value_no_value_received(self):
        x = wtl.response.XMLValue(XML_LOG_1410)
        x.check_log_data_data_value(4,'M2', 3, error_margin=99)
        self.assertTrue(wtl.control_prim.fail.called)
  
    def test_check_log_data_all(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
              <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                <log uidWell='w1' uidWellbore='wb1' uid='l1'>
                  <indexCurve>M1</indexCurve>
                  <logData>                        
                    <mnemonicList>M1,M2,M3,M4</mnemonicList>
                    <unitList>m,m,ft,ft</unitList>
                    <data>1.1,2.1,3.1,4.1</data>
                    <data>5,6,7,8</data>
                    <data>9,10,11,12</data>
                  </logData>
                </log>
              </logs>""")  
        data = [(1.1,2.1,3.1,4.1),
                (5,6,7,8),
                (9,10,11,12)]
        x.check_log_data_all(data, ['M1','M2','M3','M4'], index_error_margin=1, error_margin=1)
        self.assertFalse(wtl.control_prim.fail.called)
   
    def test_check_log_data_all_different_order(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
              <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                <log uidWell='w1' uidWellbore='wb1' uid='l1'>
                  <indexCurve>M1</indexCurve>
                  <logData>                        
                    <mnemonicList>M1,M2,M3,M4</mnemonicList>
                    <unitList>m,m,ft,ft</unitList>
                    <data>1.1,2.1,3.1,4.1</data>
                    <data>5,6,7,8</data>
                    <data>9,10,11,12</data>
                  </logData>
                </log>
              </logs>""")  
        data = [(1.1,4.1,2.1,3.1),
                (5,8,6,7),
                (9,12,10,11)]
        x.check_log_data_all(data, ['M1','M4','M2','M3'], index_error_margin=1, error_margin=1)
        self.assertFalse(wtl.control_prim.fail.called)
   
    def test_check_log_data_all_bad_mnemonic_list(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
              <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                <log uidWell='w1' uidWellbore='wb1' uid='l1'>
                  <indexCurve>M1</indexCurve>
                  <logData>                        
                    <mnemonicList>M1,M2,M3,M4</mnemonicList>
                    <unitList>m,m,ft,ft</unitList>
                    <data>1.1,2.1,3.1,4.1</data>
                    <data>5,6,7,8</data>
                    <data>9,10,11,12</data>
                  </logData>
                </log>
              </logs>""")  
        data = [(1.1,2.1,3.1,4.1),
                (5,6,7,8),
                (9,10,11,12)]
        x.check_log_data_all(data, ['M1','M2','M3'], index_error_margin=1, error_margin=1)
        self.assertTrue(wtl.control_prim.fail.called)
   
    def test_check_log_data_all_bad_index(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
              <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                <log uidWell='w1' uidWellbore='wb1' uid='l1'>
                  <indexCurve>M1</indexCurve>
                  <logData>                        
                    <mnemonicList>M1,M2,M3,M4</mnemonicList>
                    <unitList>m,m,ft,ft</unitList>
                    <data>1.1,2.1,3.1,4.1</data>
                    <data>5,6,7,8</data>
                    <data>9,10,11,12</data>
                  </logData>
                </log>
              </logs>""")  
        data = [(1.1,2.1,3.1,4.1),
                (5,6,7,8),
                (9.95,10,11,12)]
        x.check_log_data_all(data, ['M1','M2','M3','M4'], index_error_margin=10, error_margin=1)
        self.assertTrue(wtl.control_prim.fail.called)

    def test_check_log_data_all_bad_value(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
              <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                <log uidWell='w1' uidWellbore='wb1' uid='l1'>
                  <indexCurve>M1</indexCurve>
                  <logData>                        
                    <mnemonicList>M1,M2,M3,M4</mnemonicList>
                    <unitList>m,m,ft,ft</unitList>
                    <data>1.1,2.1,3.1,4.1</data>
                    <data>5,6,7,8</data>
                    <data>9,10,11,12</data>
                  </logData>
                </log>
              </logs>""")  
        data = [(1.1,2.1,3.1,4.1),
                (5,6,7,8),
                (9,11.5,11,12)]
        x.check_log_data_all(data, ['M1','M2','M3','M4'], index_error_margin=1, error_margin=10)
        self.assertTrue(wtl.control_prim.fail.called)

    def test_check_log_data_all_bad_number_of_nodes(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
              <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                <log uidWell='w1' uidWellbore='wb1' uid='l1'>
                  <indexCurve>M1</indexCurve>
                  <logData>                        
                    <mnemonicList>M1,M2,M3,M4</mnemonicList>
                    <unitList>m,m,ft,ft</unitList>
                    <data>1.1,2.1,3.1,4.1</data>
                    <data>5,6,7,8</data>
                    <data>9,10,11,12</data>
                    <data>2,1,3.0,5</data>
                  </logData>
                </log>
              </logs>""")  
        data = [(1.1,2.1,3.1,4.1),
                (5,6,7,8),
                (9,10,11,12)]
        x.check_log_data_all(data, ['M1','M2','M3','M4'], index_error_margin=1, error_margin=10)
        self.assertTrue(wtl.control_prim.fail.called)

    def test_check_log_data_all_bad_number_of_points(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
              <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                <log uidWell='w1' uidWellbore='wb1' uid='l1'>
                  <indexCurve>M1</indexCurve>
                  <logData>                        
                    <mnemonicList>M1,M2,M3,M4,M5</mnemonicList>
                    <unitList>m,m,ft,ft,m</unitList>
                    <data>1.1,2.1,3.1,4.1,1</data>
                    <data>5,6,7,8,1</data>
                    <data>9,10,11,12,1</data>
                  </logData>
                </log>
              </logs>""")  
        data = [(1.1,2.1,3.1,4.1),
                (5,6,7,8),
                (9,10,11,12)]
        x.check_log_data_all(data, ['M1','M2','M3','M4','M5'], index_error_margin=1, error_margin=10)
        self.assertTrue(wtl.control_prim.fail.called)
        
    def test_check_log_data_bad_number_of_rows(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
              <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                <log uidWell='w1' uidWellbore='wb1' uid='l1'>
                  <indexCurve>M1</indexCurve>
                  <logData>                        
                    <mnemonicList>M1,M2,M3,M4</mnemonicList>
                    <unitList>m,m,ft,ft</unitList>
                    <data>1.1,2.1,3.1,4.1</data>
                    <data>5,6,7,8</data>
                    <data>9,10,11,12</data>
                  </logData>
                </log>
              </logs>""")  
        data = [(1.1,2.1,3.1,4.1),
                (5,6,7,8)]
        x.check_log_data_all(data, ['M1','M2','M3','M4'], index_error_margin=1, error_margin=1)
        self.assertTrue(wtl.control_prim.fail.called)


    def test_get_log_data_index_value(self):
        # Test log data index value properly populated
        x = wtl.response.XMLValue(XML_LOG_1410)
        self.assertTrue(x.get_log_data_index_value(0) == '1')
        self.assertTrue(x.get_log_data_index_value(1) == '2')
        self.assertTrue(x.get_log_data_index_value(2) == '3')
        self.assertTrue(x.get_log_data_index_value(3) == '4')
        self.assertTrue(x.get_log_data_index_value(4) == '5')

    def test_get_log_data_data_value(self):
        # Test log data data value properly populated
        x = wtl.response.XMLValue(XML_LOG_1410)
        self.assertTrue(x.get_log_data_data_value(0,'M1') == '1')
        self.assertTrue(x.get_log_data_data_value(1,'M1') == '2')
        self.assertTrue(x.get_log_data_data_value(2,'M1') == '3')
        self.assertTrue(x.get_log_data_data_value(3,'M1') == '4')
        self.assertTrue(x.get_log_data_data_value(4,'M1') == '5')
        
        self.assertTrue(x.get_log_data_data_value(0,'M2') == '2')
        self.assertTrue(x.get_log_data_data_value(1,'M2') == '0')
        self.assertTrue(x.get_log_data_data_value(2,'M2') == '4')
        self.assertTrue(x.get_log_data_data_value(3,'M2') == '0')
        self.assertTrue(x.get_log_data_data_value(4,'M2') == '')
        
        self.assertTrue(x.get_log_data_data_value(0,'M3') == '3.0')
        self.assertTrue(x.get_log_data_data_value(1,'M3') == '3.1')
        self.assertTrue(x.get_log_data_data_value(2,'M3') == '3.2')
        self.assertTrue(x.get_log_data_data_value(3,'M3') == '3.3')
        self.assertTrue(x.get_log_data_data_value(4,'M3') == '3.4')
        
        self.assertTrue(x.get_log_data_data_value(0,'M4') == '')
        self.assertTrue(x.get_log_data_data_value(1,'M4') == '10')
        self.assertTrue(x.get_log_data_data_value(2,'M4') == '20')
        self.assertTrue(x.get_log_data_data_value(3,'M4') == '')
        self.assertTrue(x.get_log_data_data_value(4,'M4') == '30')
  
    def test_get_log_data_data_value_array(self):
        # Test log data data value properly populated with an array curve
        x = wtl.response.XMLValue(XML_1410_WITH_ARRAY_CURVE)
        self.assertTrue(x.get_log_data_data_value(0,'Vdepth') == '498.99')
        self.assertTrue(x.get_log_data_data_value(1,'Vdepth') == '500.00')
        self.assertTrue(x.get_log_data_data_value(2,'Vdepth') == '501.02')
        self.assertTrue(x.get_log_data_data_value(10,'Vdepth') == '508.75')
        self.assertTrue(x.get_log_data_data_value(0,'Array') == '-999.25 -999.25 -999.25 -999.25 -999.25 -999.25')
        self.assertTrue(x.get_log_data_data_value(1,'Array') == "01 11 21 31 41 51")
        self.assertTrue(x.get_log_data_data_value(2,'Array') == "02 12 22 32 42 52")
        self.assertTrue(x.get_log_data_data_value(10,'Array') == "-999.25 30 -999.25 -999.25 -999.25 -999.25")   
        self.assertTrue(x.get_log_data_data_value(0,'Bit Dist') == '1.25')
        self.assertTrue(x.get_log_data_data_value(1,'Bit Dist') == '1.90')
        self.assertTrue(x.get_log_data_data_value(2,'Bit Dist') == '2.92')
        self.assertTrue(x.get_log_data_data_value(10,'Bit Dist') == '6.01') 
        self.assertTrue(x.get_log_curve_array_length('Vdepth') == 1)
        self.assertTrue(x.get_log_curve_array_length('Array') == 6)        
        self.assertTrue(x.get_log_curve_array_length('Bit Dist') == 1) 
        
    def test_get_log_data_number_of_nodes(self):
        # Test log data data value properly populated
        x = wtl.response.XMLValue(XML_LOG_1410)
        self.assertTrue(x.get_log_data_number_of_nodes() == 5)
        
    def test_get_log_data_number_of_nodes_no_units(self):    
        # Test with no units
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
              <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                <log uidWell='w1' uidWellbore='wb1' uid='l1'>
                  <indexCurve>M1</indexCurve>
                  <logData>                        
                    <mnemonicList>M1,M2,M3</mnemonicList>
                    <data>5,6,7</data>
                  </logData>
                </log>
              </logs>""")    
        self.assertTrue(x.get_log_data_number_of_nodes() == 1)
        
    def test_get_log_data_number_of_nodes_noLogCurveInfo(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
              <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                <log uidWell='w1' uidWellbore='wb1' uid='l1'>
                  <indexCurve>M1</indexCurve>
                  <logData>                        
                    <mnemonicList>M1,M2,M3,M4</mnemonicList>
                    <unitList>m,m,ft,ft</unitList>
                    <data>1.1,2.1,3.1,4.1</data>
                    <data>5,6,7,8</data>
                    <data>9,,,</data>>
                  </logData>
                </log>
              </logs>""")  
        self.assertTrue(x.get_log_data_number_of_nodes() == 3)
        
    def test_get_log_data_number_of_points(self):
        # Test log data data value properly populated
        x = wtl.response.XMLValue(XML_LOG_1410)
        self.assertTrue(x.get_log_data_number_of_points() == 20)
        
        x = wtl.response.XMLValue(XML_LOG_1311)
        self.assertTrue(x.get_log_data_number_of_points() == 20)
        
    def test_get_log_data_number_of_points_no_units(self):
        # Test log data data value properly populated
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
              <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                <log uidWell='w1' uidWellbore='wb1' uid='l1'>
                  <indexCurve>M1</indexCurve>
                  <logData>                        
                    <mnemonicList>M1,M2,M3</mnemonicList>
                    <data>5,6,7</data>
                  </logData>
                </log>
              </logs>""")  
        self.assertTrue(x.get_log_data_number_of_points() == 3)
        
    def test_get_log_data_number_of_nodes_noLogCurveInfo(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
              <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                <log uidWell='w1' uidWellbore='wb1' uid='l1'>
                  <indexCurve>M1</indexCurve>
                  <logData>                        
                    <mnemonicList>M1,M2,M3,M4</mnemonicList>
                    <unitList>m,m,ft,ft</unitList>
                    <data>1.1,2.1,3.1,4.1</data>
                    <data>5,6,7,8</data>
                    <data>9,,,</data>>
                  </logData>
                </log>
              </logs>""")  
        self.assertTrue(x.get_log_data_number_of_points() == 12)
        
    def test_get_log_data_number_of_points_no_data(self):
        # Test log data data value properly populated
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
              <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                <log uidWell='w1' uidWellbore='wb1' uid='l1'>
                  <indexCurve>M1</indexCurve>
                  <logData>                        
                    <mnemonicList>M1,M2,M3</mnemonicList>
                  </logData>
                </log>
              </logs>""")  
        self.assertTrue(x.get_log_data_number_of_points() == 0)
        
    def test_get_log_data_mnemonic_and_unit_list(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
              <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                <log uidWell='w1' uidWellbore='wb1' uid='l1'>
                  <indexCurve>M1</indexCurve>
                  <logData>                        
                    <mnemonicList>M1,M2,M3,M4</mnemonicList>
                    <unitList>m,m,ft,ft</unitList>
                    <data>1.1,2.1,3.1,4.1</data>
                    <data>5,6,7,8</data>
                    <data>9,,,</data>>
                  </logData>
                </log>
              </logs>""")  
        mnemonic_list = x.get_mnemonics_list()
        self.assertTrue(len(mnemonic_list) == 4)
        self.assertTrue(mnemonic_list[0] == "M1")
        self.assertTrue(mnemonic_list[1] == "M2")
        self.assertTrue(mnemonic_list[2] == "M3")
        self.assertTrue(mnemonic_list[3] == "M4")
        
        unit_list = x.get_units_list()
        self.assertTrue(len(unit_list) == 4)
        self.assertTrue(unit_list[0] == "m")
        self.assertTrue(unit_list[1] == "m")
        self.assertTrue(unit_list[2] == "ft")
        self.assertTrue(unit_list[3] == "ft")
        
        index_list = x.get_index_curve_list()
        self.assertTrue(len(index_list) == 4)
        self.assertTrue(index_list[0] == True)
        self.assertTrue(index_list[1] == False)
        self.assertTrue(index_list[2] == False)
        self.assertTrue(index_list[3] == False)
   
    def test_get_log_data_mnemonic_and_unit_list_no_log_data(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
              <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                <log uidWell='w1' uidWellbore='wb1' uid='l1'>
                  <logData>                        
                    <mnemonicList>M1,M2,M3,M4</mnemonicList>
                    <unitList>m,m,ft,ft</unitList>
                  </logData>
                </log>
              </logs>""")  
        
        mnemonic_list = x.get_mnemonics_list()
        self.assertTrue(len(mnemonic_list) == 4)
        self.assertTrue(mnemonic_list[0] == "M1")
        self.assertTrue(mnemonic_list[1] == "M2")
        self.assertTrue(mnemonic_list[2] == "M3")
        self.assertTrue(mnemonic_list[3] == "M4")
        
        unit_list = x.get_units_list()
        self.assertTrue(len(unit_list) == 4)
        self.assertTrue(unit_list[0] == "m")
        self.assertTrue(unit_list[1] == "m")
        self.assertTrue(unit_list[2] == "ft")
        self.assertTrue(unit_list[3] == "ft")
        
        index_list = x.get_index_curve_list()
        self.assertTrue(len(index_list) == 4)
        self.assertTrue(index_list[0] == False)
        self.assertTrue(index_list[1] == False)
        self.assertTrue(index_list[2] == False)
        self.assertTrue(index_list[3] == False)
        
    def test_get_log_data_mnemonic_and_unit_list_empty(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
              <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                <log uidWell='w1' uidWellbore='wb1' uid='l1'>
                  <indexCurve>M1</indexCurve>
                  <logData>                        
                    <data>1.1,2.1,3.1,4.1</data>
                    <data>5,6,7,8</data>
                    <data>9,,,</data>>
                  </logData>
                </log>
              </logs>""")  
        self.assertTrue(len(x.get_mnemonics_list()) == 0)
        self.assertTrue(len(x.get_units_list()) == 0)
        self.assertTrue(len(x.get_units_list()) == 0)
        
    def test_get_log_data_mnemonic_and_unit_list_one(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
              <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                <log uidWell='w1' uidWellbore='wb1' uid='l1'>
                  <indexCurve>M1</indexCurve>
                  <logData>                        
                    <mnemonicList>M1</mnemonicList>
                    <unitList>m</unitList>
                    <data>1.1</data>
                    <data>5</data>
                    <data>9</data>>
                  </logData>
                </log>
              </logs>""")  
        mnemonics_list = x.get_mnemonics_list()
        self.assertTrue(len(mnemonics_list) == 1)
        self.assertTrue(mnemonics_list[0] == "M1")
        
        units_list = x.get_units_list()
        self.assertTrue(len(units_list) == 1)
        self.assertTrue(units_list[0] == "m")
        
        index_list = x.get_index_curve_list()
        self.assertTrue(len(index_list) == 1)
        self.assertTrue(index_list[0] == True)
        
    def test_xpath_support(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
              <root xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                <elem1 uidWell='w1' uidWellbore='wb1' uid='l1'>
                  <elem2>Elem2</elem2>
                  <elem3 id="1">                        
                    <elem2>Elem2-1</elem2>
                    <elem2>Elem2-2</elem2>
                    <elem3/>
                    <elem2>Elem2-3</elem2>
                  </elem3>
                  <elem3 id="2">                        
                    <elem2>Elem2-4</elem2>
                  </elem3>
                  <elem4>                        
                    <elem2>Elem2-5</elem2>
                  </elem4>                        
                </elem1>
              </root>""")
        self.assertTrue(x.get_recurring_element_list('root') == [None])
        self.assertTrue(x.get_recurring_element_list('elem1') == [None])
        self.assertTrue(x.get_recurring_element_list('elem2') == ['Elem2', 'Elem2-1', 'Elem2-2', 'Elem2-3', 'Elem2-4', 'Elem2-5'])
        self.assertTrue(x.get_recurring_element_list('elem3') == [None, None, None])
        self.assertTrue(x.get_recurring_element_list('/root/elem1/elem2') == ['Elem2'])
        self.assertTrue(x.get_recurring_element_list('/root/elem1/elem3/elem2') == ['Elem2-1', 'Elem2-2', 'Elem2-3', 'Elem2-4'])
        self.assertTrue(x.get_recurring_element_list('/root/elem1/elem3/elem2[1]') == ['Elem2-1', 'Elem2-4'])
        self.assertTrue(x.get_recurring_element_list('/root/elem1/*/elem2') == ['Elem2-1', 'Elem2-2', 'Elem2-3', 'Elem2-4', 'Elem2-5'])
        self.assertTrue(x.get_recurring_element_list('/root/elem1/elem3/elem2[last()]') == ['Elem2-3', 'Elem2-4'])
        self.assertTrue(x.get_recurring_element_list('/root/elem1/elem3[@id="1"]/elem2[last()]') == ['Elem2-3'])
        self.assertTrue(x.get_recurring_element_list('/root/elem1/elem3[2]/elem2') == ['Elem2-4'])
        
    def test_object_index(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
              <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                <log uidWell='w1' uidWellbore='wb1' uid='L1'>
                  <name>log 1</name>
                  <element uidWell='w1' uidWellbore='wb1' uid='L1'/>
                </log>
                <log uidWell='w1' uidWellbore='wb1' uid='L2'>
                  <name>log 2</name>
                  <element uidWell='w1' uidWellbore='wb1' uid='L2'/>
                </log>
                <log uidWell='w1' uidWellbore='wb1' uid='L3'>
                  <name>log 3</name>
                  <element uidWell='w1' uidWellbore='wb1' uid='L3'/>
                </log>
              </logs>""")              
        self.assertTrue(x.get_element_text_value('name') == 'log 1')
        self.assertTrue(x.get_element_text_value('log/name') == 'log 1')
        self.assertTrue(x.get_element_text_value('logs/log/name') == 'log 1')
        self.assertTrue(x.get_element_text_value('name', _object_index=1) == 'log 1')
        self.assertTrue(x.get_element_text_value('name', _object_index=2) == 'log 2')
        self.assertTrue(x.get_element_text_value('log/name', _object_index=2) == 'log 2')
        self.assertTrue(x.get_element_text_value('logs/log/name', _object_index=2) == 'log 2')
        self.assertTrue(x.get_element_text_value('name', _object_index=3) == 'log 3')
        
        self.assertTrue(x.get_attribute('log', 'uid') == 'L1')
        self.assertTrue(x.get_attribute('logs/log', 'uid') == 'L1')
        self.assertTrue(x.get_attribute('log', 'uid', _object_index=1) == 'L1')
        self.assertTrue(x.get_attribute('logs/log', 'uid', _object_index=1) == 'L1')
        self.assertTrue(x.get_attribute('log', 'uid', _object_index=2) == 'L2')
        self.assertTrue(x.get_attribute('logs/log', 'uid', _object_index=2) == 'L2')
        self.assertTrue(x.get_attribute('log', 'uid', _object_index=3) == 'L3')
        self.assertTrue(x.get_attribute('logs/log', 'uid', _object_index=3) == 'L3')

    def test_get_element_text_value(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
              <root xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                <elem1 uidWell='w1' uidWellbore='wb1' uid='l1'>
                  <elem4>Elem4</elem4>
                  <elem3 id="1">                        
                    <elem4>Elem4-3-1</elem4>
                    <elem4>Elem4-3-2</elem4>
                    <elem4/>
                    <elem4>Elem4-3-3</elem4>
                  </elem3>
                  <elem5 id="2">                        
                    <elem6>Elem4-5-1</elem6>
                    <elem4>Elem4-5-2</elem4>
                  </elem5>
                </elem1>
              </root>""")
        self.assertTrue(x.get_element_text_value('/root/elem1/elem3/elem4') == 'Elem4-3-1')
        self.assertTrue(x.get_element_text_value('elem4') == 'Elem4')
        self.assertTrue(x.get_element_text_value('elem6') == 'Elem4-5-1')
        
    def test_get_log_data_mnemonic_and_unit_list_reentrant(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
              <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                <log uidWell='w1' uidWellbore='wb1' uid='l1'>
                  <indexCurve>M1</indexCurve>
                  <logData>                        
                    <data>1.1,2.1,3.1,4.1</data>
                    <data>5,6,7,8</data>
                    <data>9,,,</data>>
                  </logData>
                </log>
              </logs>""")  
        self.assertTrue(len(x.get_mnemonics_list()) == 0)
        self.assertTrue(len(x.get_units_list()) == 0)
        self.assertTrue(len(x.get_units_list()) == 0)
        
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
              <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                <log uidWell='w1' uidWellbore='wb1' uid='l1'>
                  <indexCurve>M1</indexCurve>
                  <logData>                        
                    <mnemonicList>M1</mnemonicList>
                    <unitList>m</unitList>
                    <data>1.1</data>
                    <data>5</data>
                    <data>9</data>>
                  </logData>
                </log>
              </logs>""")  
        mnemonics_list = x.get_mnemonics_list()
        self.assertTrue(len(mnemonics_list) == 1)
        self.assertTrue(mnemonics_list[0] == "M1")
        
        units_list = x.get_units_list()
        self.assertTrue(len(units_list) == 1)
        self.assertTrue(units_list[0] == "m")
        
        index_list = x.get_index_curve_list()
        self.assertTrue(len(index_list) == 1)
        self.assertTrue(index_list[0] == True)
        
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
              <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                <log uidWell='w1' uidWellbore='wb1' uid='l1'>
                  <indexCurve>M1</indexCurve>
                  <logData>                        
                    <mnemonicList>M1,M2,M3,M4</mnemonicList>
                    <unitList>m,m,ft,ft</unitList>
                    <data>1.1,2.1,3.1,4.1</data>
                    <data>5,6,7,8</data>
                    <data>9,,,</data>>
                  </logData>
                </log>
              </logs>""")  
        mnemonic_list = x.get_mnemonics_list()
        self.assertTrue(len(mnemonic_list) == 4)
        self.assertTrue(mnemonic_list[0] == "M1")
        self.assertTrue(mnemonic_list[1] == "M2")
        self.assertTrue(mnemonic_list[2] == "M3")
        self.assertTrue(mnemonic_list[3] == "M4")
        
        unit_list = x.get_units_list()
        self.assertTrue(len(unit_list) == 4)
        self.assertTrue(unit_list[0] == "m")
        self.assertTrue(unit_list[1] == "m")
        self.assertTrue(unit_list[2] == "ft")
        self.assertTrue(unit_list[3] == "ft")
        
        index_list = x.get_index_curve_list()
        self.assertTrue(len(index_list) == 4)
        self.assertTrue(index_list[0] == True)
        self.assertTrue(index_list[1] == False)
        self.assertTrue(index_list[2] == False)
        self.assertTrue(index_list[3] == False)
        
    def test_get_latest_dTimChange(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
              <changeLogs xmlns="http://www.witsml.org/schemas/1series" version="1.4.1.1">
                <changeLog uidWell="UUID-1" uidWellbore="B-01" uidObject="obj">
                  <nameWell>DemoWell2</nameWell>
                  <nameWellbore>Wellbore4</nameWellbore>
                  <nameObject>ChangeLogTest</nameObject>
                  <objectType>log</objectType>
                  <lastChangeType>update</lastChangeType>
                  <lastChangeInfo>Updated item</lastChangeInfo>
                  <commonData>
                    <dTimLastChange>2010-10-28T12:55:39.315Z</dTimLastChange>
                  </commonData>
                </changeLog>
            </changeLogs>""")
        self.assertTrue(x.get_latest_dTimChange() == None)

        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
              <changeLogs xmlns="http://www.witsml.org/schemas/1series" version="1.4.1.1">
                <changeLog uidWell="UUID-1" uidWellbore="B-01" uidObject="obj">
                  <nameWell>DemoWell2</nameWell>
                  <nameWellbore>Wellbore4</nameWellbore>
                  <nameObject>ChangeLogTest</nameObject>
                  <objectType>log</objectType>
                  <lastChangeType>update</lastChangeType>
                  <lastChangeInfo>Updated item</lastChangeInfo>
                  <changeHistory>
                    <dTimChange>2010-10-28T10:51:39Z</dTimChange>
                    <changeType>add</changeType>
                  </changeHistory>
                  <commonData>
                    <dTimLastChange>2010-10-28T12:55:39.315Z</dTimLastChange>
                  </commonData>
                </changeLog>
            </changeLogs>""")
        self.assertTrue(x.get_latest_dTimChange() == '2010-10-28T10:51:39Z')

        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>
              <changeLogs xmlns="http://www.witsml.org/schemas/1series" version="1.4.1.1">
                <changeLog uidWell="UUID-1" uidWellbore="B-01" uidObject="obj">
                  <nameWell>DemoWell2</nameWell>
                  <nameWellbore>Wellbore4</nameWellbore>
                  <nameObject>ChangeLogTest</nameObject>
                  <objectType>log</objectType>
                  <lastChangeType>update</lastChangeType>
                  <lastChangeInfo>Updated item</lastChangeInfo>
                  <changeHistory>
                    <dTimChange>2010-10-28T09:51:40-01:00</dTimChange>
                    <changeType>add</changeType>
                  </changeHistory>
                  <changeHistory>
                    <dTimChange>2010-10-28T10:51:41Z</dTimChange>
                    <changeType>update</changeType>
                  </changeHistory>
                  <changeHistory>
                    <dTimChange>2010-10-28T12:51:39+02:00</dTimChange>
                    <changeType>delete</changeType>
                  </changeHistory>
                  <commonData>
                    <dTimLastChange>2010-10-28T12:55:39.315Z</dTimLastChange>
                  </commonData>
                </changeLog>
            </changeLogs>""")
        self.assertTrue(x.get_latest_dTimChange() == '2010-10-28T10:51:41Z')
                
    def test_check_recurring_element_value(self):        
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>  
            <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                  <log uidWell='w1' uidWellbore='wb1' uid='l1'>
                    <logCurveInfo uid="1">
                      <mnemonic>DEPTH</mnemonic>
                    </logCurveInfo>
                    <logCurveInfo uid="2">
                      <mnemonic>GR</mnemonic>
                    </logCurveInfo>
                    <logCurveInfo uid="3">
                      <mnemonic>CALI</mnemonic>
                    </logCurveInfo>
                    <logCurveInfo uid="4">
                      <mnemonic>DR+HO</mnemonic>
                    </logCurveInfo>
                    <logCurveInfo uid="5">
                      <mnemonic>RHOB</mnemonic>
                    </logCurveInfo>
                  </log>
              </logs>""")  
        x.check_recurring_element_value('logs/log/logCurveInfo/mnemonic', ['DEPTH', 'CALI', 'GR', 'RHOB', 'DR+HO'])
        self.assertFalse(wtl.control_prim.fail.called)     
        x.check_recurring_element_value('logs/log/logCurveInfo/mnemonic', ['DEPTH', 'GR', 'CALI', 'RHOB'])
        self.assertTrue(wtl.control_prim.fail.called)            
        
    def test_check_recurring_element_value_regex(self):        
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>  
            <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                  <log uidWell='w1' uidWellbore='wb1' uid='l1'>
                    <logCurveInfo uid="1">
                      <mnemonic>DEPTH</mnemonic>
                    </logCurveInfo>
                    <logCurveInfo uid="2">
                      <mnemonic>GR</mnemonic>
                    </logCurveInfo>
                    <logCurveInfo uid="3">
                      <mnemonic>CALI</mnemonic>
                    </logCurveInfo>
                    <logCurveInfo uid="4">
                      <mnemonic>DR+HO</mnemonic>
                    </logCurveInfo>
                    <logCurveInfo uid="5">
                      <mnemonic>RHOB</mnemonic>
                    </logCurveInfo>
                  </log>
              </logs>""")  
        x.check_recurring_element_value('logs/log/logCurveInfo/mnemonic', ['D.*H', 'CA.I', 'GR', 'RHOB', 'DR\+HO'], enable_regex=True)
        self.assertFalse(wtl.control_prim.fail.called)     
        x.check_recurring_element_value('logs/log/logCurveInfo/mnemonic', ['DEPTH', 'CALI', 'GR', 'RHOB', 'DR+HO'], enable_regex=True)
        self.assertTrue(wtl.control_prim.fail.called)            

    def test_check_recurring_element_value_repeating_value(self):        
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>  
            <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                  <log uidWell='w1' uidWellbore='wb1' uid='l1'>
                    <logCurveInfo uid="1">
                      <mnemonic>DEPTH</mnemonic>
                    </logCurveInfo>
                    <logCurveInfo uid="2">
                      <mnemonic>DRHO</mnemonic>
                    </logCurveInfo>
                    <logCurveInfo uid="3">
                      <mnemonic>CALI</mnemonic>
                    </logCurveInfo>
                    <logCurveInfo uid="4">
                      <mnemonic>DRHO</mnemonic>
                    </logCurveInfo>
                    <logCurveInfo uid="5">
                      <mnemonic>RHOB</mnemonic>
                    </logCurveInfo>
                  </log>
              </logs>""")  
        x.check_recurring_element_value('logs/log/logCurveInfo/mnemonic', ['DRHO', 'DEPTH', 'CALI', 'RHOB', 'DRHO'])
        self.assertFalse(wtl.control_prim.fail.called)     
        x.check_recurring_element_value('logs/log/logCurveInfo/mnemonic', ['DEPTH', 'CALI', 'RHOB', 'DRHO'])
        self.assertTrue(wtl.control_prim.fail.called)            
        
    def test_check_recurring_element_value_contains(self):        
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>  
            <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                  <log uidWell='w1' uidWellbore='wb1' uid='l1'>
                    <logCurveInfo uid="1">
                      <mnemonic>DEPTH</mnemonic>
                    </logCurveInfo>
                    <logCurveInfo uid="2">
                      <mnemonic>GR</mnemonic>
                    </logCurveInfo>
                    <logCurveInfo uid="3">
                      <mnemonic>CALI</mnemonic>
                    </logCurveInfo>
                    <logCurveInfo uid="4">
                      <mnemonic>DR+HO</mnemonic>
                    </logCurveInfo>
                    <logCurveInfo uid="5">
                      <mnemonic>RHOB</mnemonic>
                    </logCurveInfo>
                  </log>
              </logs>""")  
        x.check_recurring_element_value_contains('logs/log/logCurveInfo/mnemonic', ['DEPTH', 'GR', 'CALI', 'RHOB', 'DR+HO'])
        self.assertFalse(wtl.control_prim.fail.called)     
        x.check_recurring_element_value_contains('logs/log/logCurveInfo/mnemonic', ['DEPTH', 'GR', 'CALI', 'RHOB'])
        self.assertFalse(wtl.control_prim.fail.called) 
        x.check_recurring_element_value_contains('logs/log/logCurveInfo/mnemonic', [])
        self.assertFalse(wtl.control_prim.fail.called)          
        x.check_recurring_element_value_contains('logs/log/logCurveInfo/mnemonic', ['DEPTH', 'GR', 'CALI', 'RHOB2'])
        self.assertTrue(wtl.control_prim.fail.called)
                      
    def test_check_recurring_element_value_contains_regex(self):        
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>  
            <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                  <log uidWell='w1' uidWellbore='wb1' uid='l1'>
                    <logCurveInfo uid="1">
                      <mnemonic>DEPTH</mnemonic>
                    </logCurveInfo>
                    <logCurveInfo uid="2">
                      <mnemonic>GR</mnemonic>
                    </logCurveInfo>
                    <logCurveInfo uid="3">
                      <mnemonic>CALI</mnemonic>
                    </logCurveInfo>
                    <logCurveInfo uid="4">
                      <mnemonic>DR+HO</mnemonic>
                    </logCurveInfo>
                    <logCurveInfo uid="5">
                      <mnemonic>RHOB</mnemonic>
                    </logCurveInfo>
                  </log>
              </logs>""")  
        x.check_recurring_element_value_contains('logs/log/logCurveInfo/mnemonic', ['DEPTH', 'GR', 'CALI', 'RHOB'], enable_regex=True)
        self.assertFalse(wtl.control_prim.fail.called) 
        x.check_recurring_element_value_contains('logs/log/logCurveInfo/mnemonic', ['D.*H', 'GR', 'C.LI', 'RHOB'], enable_regex=True)
        self.assertFalse(wtl.control_prim.fail.called) 
        x.check_recurring_element_value_contains('logs/log/logCurveInfo/mnemonic', [], enable_regex=True)
        self.assertFalse(wtl.control_prim.fail.called)          
        x.check_recurring_element_value_contains('logs/log/logCurveInfo/mnemonic', ['DEPTH', 'GR', 'CALI', 'DR+HO'], enable_regex=True)
        self.assertTrue(wtl.control_prim.fail.called)
                      
    def test_check_recurring_element_value_contains_repeating_value(self):        
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>  
            <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                  <log uidWell='w1' uidWellbore='wb1' uid='l1'>
                    <logCurveInfo uid="1">
                      <mnemonic>DEPTH</mnemonic>
                    </logCurveInfo>
                    <logCurveInfo uid="2">
                      <mnemonic>GR</mnemonic>
                    </logCurveInfo>
                    <logCurveInfo uid="3">
                      <mnemonic>CALI</mnemonic>
                    </logCurveInfo>
                    <logCurveInfo uid="4">
                      <mnemonic>DRHO</mnemonic>
                    </logCurveInfo>
                    <logCurveInfo uid="5">
                      <mnemonic>DRHO</mnemonic>
                    </logCurveInfo>
                  </log>
              </logs>""")  
        x.check_recurring_element_value_contains('logs/log/logCurveInfo/mnemonic', ['DRHO', 'DRHO'])
        self.assertFalse(wtl.control_prim.fail.called)     
        x.check_recurring_element_value_contains('logs/log/logCurveInfo/mnemonic', ['DRHO', 'DRHO', 'DRHO'])
        self.assertTrue(wtl.control_prim.fail.called)
        
    def test_get_recurring_element_list_via_key(self):
        x = wtl.response.XMLValue("""<?xml version="1.0" encoding="UTF-8"?>  
            <logs xmlns="http://www.witsml.org/schemas/131" version="1.4.1.0">
                  <log uidWell='w1' uidWellbore='wb1' uid='l1'>
                    <logCurveInfo uid="1a">
                      <mnemonic>DEPTH</mnemonic>
                      <minIndex uom="ft">1</minIndex>
                    </logCurveInfo>
                    <logCurveInfo uid="2b">
                      <mnemonic>GR</mnemonic>
                      <minIndex uom="ft">2</minIndex>
                    </logCurveInfo>
                    <logCurveInfo uid="3c">
                      <mnemonic>CALI</mnemonic>
                      <minIndex uom="ft">3</minIndex>
                    </logCurveInfo>
                    <logCurveInfo uid="4d">
                      <mnemonic>DRHO</mnemonic>
                      <minIndex uom="ft">4</minIndex>
                    </logCurveInfo>
                    <logCurveInfo uid="5e">
                      <mnemonic>RHOB</mnemonic>
                      <minIndex uom="ft">5</minIndex>
                    </logCurveInfo>
                  </log>
              </logs>""")
        list = x.get_recurring_element_list_via_key("logCurveInfo", ['DEPTH','GR','DRHO','CALI','RHOB'], 'mnemonic','minIndex')        
        self.assertTrue(list == ['1', '2', '4', '3', '5'])
        list = x.get_recurring_element_list_via_key("logCurveInfo", ['1a','2b','4d','3c','5e'], '@uid','minIndex')        
        self.assertTrue(list == ['1', '2', '4', '3', '5'])    
        list = x.get_recurring_element_list_via_key("logCurveInfo", ['DEPTH','BADMNEMONIC','DRHO','CALI','RHOB'], 'mnemonic','minIndex')        
        self.assertTrue(list == ['1', None, '4', '3', '5'])
        list = x.get_recurring_element_list_via_key("logCurveInfo", ['DEPTH','GR','DRHO','CALI','RHOB'], 'mnemonic','maxIndex')        
        self.assertTrue(list == [None, None, None, None, None])
        list = x.get_recurring_element_list_via_key("logCurveInfo", ['DEPTH','GR','DRHO','CALI','RHOB'], 'BADMNEMONIC','minIndex')        
        self.assertTrue(list == [None, None, None, None, None])    
        list = x.get_recurring_element_list_via_key("logCurveInfo", [], 'mnemonic','minIndex')        
        self.assertTrue(list == [])  
        list = x.get_recurring_element_list_via_key("BadlogCurveInfo", ['DEPTH','GR','DRHO','CALI','RHOB'], 'mnemonic','minIndex')        
        self.assertTrue(list == [None, None, None, None, None])                
        
    def test_check_valid_write_schema_1410_log(self):
        # tests that validation passes for 1.4.1.0 log object which complies with write schema
        x = wtl.response.XMLValue(XML_1410_WITH_ARRAY_CURVE)      
        self.assertTrue(x.check_valid_write_schema())
        
    def test_check_invalid_write_schema_1410_log(self):
        # tests that validation fails for 1.4.1.0 log object which does not comply with write schema (only read schema)
        x = wtl.response.XMLValue(XML_LOG_1410)  
        x.check_valid_write_schema()
        self.assertTrue(wtl.control_prim.fail.called)  
        
    def test_check_invalid_write_schema_1311_log(self):
        # tests that validation fails for 1.3.1.1 log object which does not comply with write schema
        x = wtl.response.XMLValue(XML_LOG_1311)  
        x.check_valid_write_schema()
        self.assertTrue(wtl.control_prim.fail.called)     
         
    def test_check_valid_write_schema_1411_wellbore(self):
        # tests that validation passes for 1.4.1.1 wellbore object which complies with write schema
        x = wtl.response.XMLValue(XML_WELLBORE)  
        self.assertTrue(x.check_valid_write_schema())
        
    def test_check_invalid_write_schema_1411_2_wellbore(self):
        # tests that validation fails for 1.4.1.1 wellbore object which does not comply with 1.3.1.1 wellbore write schema
        x = wtl.response.XMLValue(XML_WELLBORE)  
        x.check_valid_write_schema()
        self.assertFalse(wtl.control_prim.fail.called)     

    def test_check_invalid_write_schema_1411_bad_wellbore(self):
        # tests that validation fails for 1.4.1.1 wellbore object which does not comply with 1.3.1.1 wellbore write schema
        x = wtl.response.XMLValue(XML_WELLBORE_BAD)  
        x.check_valid_write_schema()
        self.assertTrue(wtl.control_prim.fail.called) 


        
if __name__ == '__main__':
    unittest.main()
