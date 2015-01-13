'''
Created on Mar 20, 2013

@organization: PetroDAQ Inc
@author: Denys Metelskyy
@contact: 2121 Golden Rd, Suite 1-A. The Woodlands, TX 77381. denys.metelskyy@petrodaq.com  
'''

import sys;
import os;

sys.path.append("../src/wcmp");

import unittest
import witsml_obj_compare;
import shutil;

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


####################################################################
#
#xml wellbore with modified uid removed comments different order
#
#    <well uid="w-12">     ->        <well uid="">
#
#
XML_WELLBORE_UID_MODIFIED_NO_COMMENTS = """<?xml version="1.0" encoding="UTF-8"?>
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
    
    
    
    <wellbore uidWell="W-12xxx" uid="xxxx">
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

</wellbores>
"""

####################################################################
#
#xml wellbore with modified state 
#
#    <numGovt>Govt001</numGovt>     ->        <numGovt>Govt0021</numGovt>
#
#

XML_WELLBORE_TEXT_MODIFIED = """<?xml version="1.0" encoding="UTF-8"?>
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
    <wellbore uidWell="XXX" uid="XXX">
        <nameWell>6507/7-A-42</nameWell>
        <name>A-42</name>
        <number>1234-0987</number>
        <suffixAPI>02</suffixAPI>
        <numGovt>Govt0021</numGovt>
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

################################################
#
# Removed element commonData
#
#
XML_WELLBORE_REMOVED_ELEMENT = """<?xml version="1.0" encoding="UTF-8"?>
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

    </wellbore>
</wellbores>
"""





class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_witsml_wellbore_equal(self):
        result, report = witsml_obj_compare.witsml1411_compare_obj_wellbores( XML_WELLBORE , XML_WELLBORE_UID_MODIFIED_NO_COMMENTS )
  
        f = open("reports/wellbore/repo_wellbore_diff_uid.html","w") ; 
        f.write(report);
        if result:
            f.write("<br/> == Everything went allrite - The XML Is equal as expected == <br/>");
        else:
            f.write("<br/> == FAIL! - The XML is different == <br/>");
            open("reports/wellbore/repo_wellbore_diff_uid.html.a.xml","w").write(XML_WELLBORE); 
            open("reports/wellbore/repo_wellbore_diff_uid.html.b.xml","w").write(XML_WELLBORE_UID_MODIFIED_NO_COMMENTS); 
        f.close();
        
        
        #open("reports/wellbore/repo_wellbore_diff_uid.html","w").write(report);
        self.assertTrue( result );
    
    def test_witsml_wellbore_text_modified(self):
        result, report = witsml_obj_compare.witsml1411_compare_obj_wellbores( XML_WELLBORE , XML_WELLBORE_TEXT_MODIFIED ) 
        f = open("reports/wellbore/repo_wellbore_diff_text.html","w") ; 
        f.write(report);
        if not result:
            f.write("<br/> == Everything went allrite - The XML Is Different as expected == <br/>");
        else:
            f.write("<br/> == FAIL! - The XML is NOT different == <br/>");
            open("reports/wellbore/repo_wellbore_diff_text.html.a.xml","w").write(XML_WELLBORE); 
            open("reports/wellbore/repo_wellbore_diff_text.html.b.xml","w").write(XML_WELLBORE_TEXT_MODIFIED); 
        f.close();
        
        #open("reports/wellbore/repo_wellbore_diff_text.html","w").write(report);
        self.assertFalse( result );
        
    def test_witsml_wellbore_removed_element(self):
        result, report = witsml_obj_compare.witsml1411_compare_obj_wellbores( XML_WELLBORE , XML_WELLBORE_REMOVED_ELEMENT, True ) 
        print ">>>>>>>>>>"
        print report;
        print "---"
        result, report = witsml_obj_compare.witsml1411_compare_obj_wellbores( XML_WELLBORE , XML_WELLBORE_REMOVED_ELEMENT ) 
        f = open("reports/wellbore/repo_wellbore_removed_element.html","w") ; 
        f.write(report);
        if not result:
            f.write("<br/> == Everything went allrite - The XML Is Different as expected == <br/>");
        else:
            f.write("<br/> == FAIL! - The XML is NOT different == <br/>");
            open("reports/wellbore/repo_wellbore_removed_element.html.a.xml","w").write(XML_WELLBORE); 
            open("reports/wellbore/repo_wellbore_removed_element.html.b.xml","w").write(XML_WELLBORE_REMOVED_ELEMENT); 
        f.close();
        self.assertFalse( result );
        
    
        
        
        
        


if __name__ == "__main__":

    try:
        if os.path.exists("reports/wellbore/"):
            shutil.rmtree('reports/wellbore/');
        os.makedirs("reports/wellbore/");
    except:
        pass;
    
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()