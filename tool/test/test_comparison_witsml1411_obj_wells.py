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

XML_WELL = """<?xml version="1.0" encoding="UTF-8"?>
<!--           Example of Well data         -->
<wells 
    xmlns="http://www.witsml.org/schemas/1series" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
    xsi:schemaLocation="http://www.witsml.org/schemas/1series  ../xsd_schemas/obj_well.xsd" 
    version="1.4.1.1">
<!-- 
These examples are only intended to demonstrate the type of data that can be exchanged.
They totally artificial and are not intended to demonstrate best practices. 
-->
    <documentInfo>
        <documentName>well</documentName>
        <fileCreationInformation>
            <fileCreationDate>2001-10-31T08:15:00.000Z</fileCreationDate> 
            <fileCreator>John Smith</fileCreator>
        </fileCreationInformation>
    </documentInfo>
    <well uid="w-12">
        <name>6507/7-A-42</name>
        <nameLegal>Company Legal Name</nameLegal>
        <numLicense>Company License Number</numLicense>
        <numGovt>Govt-Number</numGovt>
        <dTimLicense>2001-05-15T13:20:00.000Z</dTimLicense>
        <field>Big Field</field>
        <country>US</country>
        <state>TX</state>
        <county>Montgomery</county>
        <region>Region Name</region>
        <district>District Name</district>
        <block>Block Name</block>
        <timeZone>-06:00</timeZone>
        <operator>Operating Company</operator>
        <operatorDiv>Division Name</operatorDiv>
        <pcInterest uom="%">65</pcInterest>
        <numAPI>123-543-987AZ</numAPI>
        <statusWell>drilling</statusWell>
        <purposeWell>exploration</purposeWell>
        <dTimSpud>2001-05-31T08:15:00.000Z</dTimSpud>
        <dTimPa>2001-07-15T15:30:00.000Z</dTimPa>
        <wellheadElevation uom="ft">500</wellheadElevation>
        <wellDatum uid="KB">
            <name>Kelly Bushing</name>
            <code>KB</code>
            <elevation uom="ft" datum="SL">78.5</elevation>
        </wellDatum>
        <wellDatum uid="SL">
            <name>Sea Level</name>
            <code>SL</code>
            <datumName namingSystem="EPSG" code="5106">Caspian Sea</datumName>
        </wellDatum>
        <groundElevation uom="ft">250</groundElevation>
        <waterDepth uom="ft">520</waterDepth>
        <wellLocation uid="loc-1">
            <wellCRS uidRef="proj1">ED50 / UTM Zone 31N</wellCRS>
            <easting uom="m">425353.84</easting>
            <northing uom="m">6623785.69</northing>
            <description>Location of well surface point in projected system.</description>
        </wellLocation>
        <referencePoint uid="SRP1">
            <name>Slot Bay Centre</name>
            <type>Site Reference Point</type>
            <location uid="loc-1">
                <wellCRS uidRef="proj1">ED50 / UTM Zone 31N</wellCRS>
                <easting uom="m">425366.47</easting>
                <northing uom="m">6623781.95</northing>
            </location>
            <location uid="loc-2">
                <wellCRS uidRef="localWell1">WellOneWSP</wellCRS>
                <localX uom="m">12.63</localX>
                <localY uom="m">-3.74</localY>
                <description>Location of the Site Reference Point with respect to the well surface point</description>
            </location>
        </referencePoint>
        <referencePoint uid="WRP2">
            <name>Sea Bed</name>
            <type>Well Reference Point</type>
            <elevation uom="ft" datum="SL">-118.40</elevation>
            <measuredDepth uom="ft" datum="KB">173.09</measuredDepth>
            <location uid="loc-1">
                <wellCRS uidRef="proj1">ED50 / UTM Zone 31N</wellCRS>
                <easting uom="m">425353.84</easting>
                <northing uom="m">6623785.69</northing>
            </location>
            <location uid="loc-2">
                <wellCRS uidRef="geog1">ED50</wellCRS>
                <latitude uom="dega">59.743844</latitude>
                <longitude uom="dega">1.67198083</longitude>
            </location>
        </referencePoint>
        <wellCRS uid="geog1">
            <name>ED50</name>
                <geodeticCRS uidRef="4230">4230</geodeticCRS >
                <description>ED50 system with EPSG code 4230.</description>
        </wellCRS>
        <wellCRS uid="proj1">
            <name>ED50 / UTM Zone 31N</name>
            <mapProjectionCRS uidRef="23031">ED50 / UTM Zone 31N</mapProjectionCRS>
        </wellCRS>
        <wellCRS uid="localWell1">
            <name>WellOneWSP</name>
            <localCRS>
                <usesWellAsOrigin>true</usesWellAsOrigin>
                <yAxisAzimuth uom="dega" northDirection="grid north">0</yAxisAzimuth>
                <xRotationCounterClockwise>false</xRotationCounterClockwise>
            </localCRS>
        </wellCRS>
        <commonData>
            <dTimCreation>2001-04-30T08:15:00.000Z</dTimCreation>
            <dTimLastChange>2001-05-31T08:15:00.000Z</dTimLastChange>
            <itemState>plan</itemState>
            <comments>These are the comments associated with the Well data object.</comments>
            <defaultDatum uidRef="KB">Kelly Bushing</defaultDatum>
        </commonData>
    </well>
</wells>
"""


####################################################################
#
#xml well with modified uid removed comments 
#
#    <well uid="w-12">     ->        <well uid="">
#
#
XML_WELL_UID_MODIFIED_NO_COMMENTS = """<?xml version="1.0" encoding="UTF-8"?>
<wells 
    xmlns="http://www.witsml.org/schemas/1series" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
    xsi:schemaLocation="http://www.witsml.org/schemas/1series  ../xsd_schemas/obj_well.xsd" 
    version="1.4.1.1">

    <documentInfo>
        <documentName>well</documentName>
        <fileCreationInformation>
            <fileCreationDate>2001-10-31T08:15:00.000Z</fileCreationDate> 
            <fileCreator>John Smith</fileCreator>
        </fileCreationInformation>
    </documentInfo>
    <well uid="">
        <name>6507/7-A-42</name>
        <nameLegal>Company Legal Name</nameLegal>
        <numLicense>Company License Number</numLicense>
        <numGovt>Govt-Number</numGovt>
        <dTimLicense>2001-05-15T13:20:00.000Z</dTimLicense>
        <field>Big Field</field>
        <country>US</country>
        <state>TX</state>
        <county>Montgomery</county>
        <region>Region Name</region>
        <district>District Name</district>
        <block>Block Name</block>
        <timeZone>-06:00</timeZone>
        <operator>Operating Company</operator>
        <operatorDiv>Division Name</operatorDiv>
        <pcInterest uom="%">65</pcInterest>
        <numAPI>123-543-987AZ</numAPI>
        <statusWell>drilling</statusWell>
        <purposeWell>exploration</purposeWell>
        <dTimSpud>2001-05-31T08:15:00.000Z</dTimSpud>
        <dTimPa>2001-07-15T15:30:00.000Z</dTimPa>
        <wellheadElevation uom="ft">500</wellheadElevation>
        <wellDatum uid="KB">
            <name>Kelly Bushing</name>
            <code>KB</code>
            <elevation uom="ft" datum="SL">78.5</elevation>
        </wellDatum>
        <wellDatum uid="SL">
            <name>Sea Level</name>
            <code>SL</code>
            <datumName namingSystem="EPSG" code="5106">Caspian Sea</datumName>
        </wellDatum>
        <groundElevation uom="ft">250</groundElevation>
        <waterDepth uom="ft">520</waterDepth>
        <wellLocation uid="loc-1">
            <wellCRS uidRef="proj1">ED50 / UTM Zone 31N</wellCRS>
            <easting uom="m">425353.84</easting>
            <northing uom="m">6623785.69</northing>
            <description>Location of well surface point in projected system.</description>
        </wellLocation>
        <referencePoint uid="SRP1">
            <name>Slot Bay Centre</name>
            <type>Site Reference Point</type>
            <location uid="loc-1">
                <wellCRS uidRef="proj1">ED50 / UTM Zone 31N</wellCRS>
                <easting uom="m">425366.47</easting>
                <northing uom="m">6623781.95</northing>
            </location>
            <location uid="loc-2">
                <wellCRS uidRef="localWell1">WellOneWSP</wellCRS>
                <localX uom="m">12.63</localX>
                <localY uom="m">-3.74</localY>
                <description>Location of the Site Reference Point with respect to the well surface point</description>
            </location>
        </referencePoint>
        <referencePoint uid="WRP2">
            <name>Sea Bed</name>
            <type>Well Reference Point</type>
            <elevation uom="ft" datum="SL">-118.40</elevation>
            <measuredDepth uom="ft" datum="KB">173.09</measuredDepth>
            <location uid="loc-1">
                <wellCRS uidRef="proj1">ED50 / UTM Zone 31N</wellCRS>
                <easting uom="m">425353.84</easting>
                <northing uom="m">6623785.69</northing>
            </location>
            <location uid="loc-2">
                <wellCRS uidRef="geog1">ED50</wellCRS>
                <latitude uom="dega">59.743844</latitude>
                <longitude uom="dega">1.67198083</longitude>
            </location>
        </referencePoint>
        <wellCRS uid="geog1">
            <name>ED50</name>
                <geodeticCRS uidRef="4230">4230</geodeticCRS >
                <description>ED50 system with EPSG code 4230.</description>
        </wellCRS>
        <wellCRS uid="proj1">
            <name>ED50 / UTM Zone 31N</name>
            <mapProjectionCRS uidRef="23031">ED50 / UTM Zone 31N</mapProjectionCRS>
        </wellCRS>
        <wellCRS uid="localWell1">
            <name>WellOneWSP</name>
            <localCRS>
                <usesWellAsOrigin>true</usesWellAsOrigin>
                <yAxisAzimuth uom="dega" northDirection="grid north">0</yAxisAzimuth>
                <xRotationCounterClockwise>false</xRotationCounterClockwise>
            </localCRS>
        </wellCRS>
        <commonData>
            <dTimCreation>2001-04-30T08:15:00.000Z</dTimCreation>
            <dTimLastChange>2001-05-31T08:15:00.000Z</dTimLastChange>
            <itemState>plan</itemState>
            <comments>These are the comments associated with the Well data object.</comments>
            <defaultDatum uidRef="KB">Kelly Bushing</defaultDatum>
        </commonData>
    </well>
</wells>
"""

####################################################################
#
#xml well with modified well name 
#
#    <name>6507/7-A-42</name>     ->        <name>6507/7-A-43</name>
#
#

XML_WELL_TEXT_MODIFIED = """<?xml version="1.0" encoding="UTF-8"?>
<!--           Example of Well data         -->
<wells 
    xmlns="http://www.witsml.org/schemas/1series" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
    xsi:schemaLocation="http://www.witsml.org/schemas/1series  ../xsd_schemas/obj_well.xsd" 
    version="1.4.1.1">
<!-- 
These examples are only intended to demonstrate the type of data that can be exchanged.
They totally artificial and are not intended to demonstrate best practices. 
-->
    <documentInfo>
        <documentName>well</documentName>
        <fileCreationInformation>
            <fileCreationDate>2001-10-31T08:15:00.000Z</fileCreationDate> 
            <fileCreator>John Smith</fileCreator>
        </fileCreationInformation>
    </documentInfo>
    <well uid="w-12">
        <name>6507/7-A-43</name>
        <nameLegal>Company Legal Name</nameLegal>
        <numLicense>Company License Number</numLicense>
        <numGovt>Govt-Number</numGovt>
        <dTimLicense>2001-05-15T13:20:00.000Z</dTimLicense>
        <field>Big Field</field>
        <country>US</country>
        <state>TX</state>
        <county>Montgomery</county>
        <region>Region Name</region>
        <district>District Name</district>
        <block>Block Name</block>
        <timeZone>-06:00</timeZone>
        <operator>Operating Company</operator>
        <operatorDiv>Division Name</operatorDiv>
        <pcInterest uom="%">65</pcInterest>
        <numAPI>123-543-987AZ</numAPI>
        <statusWell>drilling</statusWell>
        <purposeWell>exploration</purposeWell>
        <dTimSpud>2001-05-31T08:15:00.000Z</dTimSpud>
        <dTimPa>2001-07-15T15:30:00.000Z</dTimPa>
        <wellheadElevation uom="ft">500</wellheadElevation>
        <wellDatum uid="KB">
            <name>Kelly Bushing</name>
            <code>KB</code>
            <elevation uom="ft" datum="SL">78.5</elevation>
        </wellDatum>
        <wellDatum uid="SL">
            <name>Sea Level</name>
            <code>SL</code>
            <datumName namingSystem="EPSG" code="5106">Caspian Sea</datumName>
        </wellDatum>
        <groundElevation uom="ft">250</groundElevation>
        <waterDepth uom="ft">520</waterDepth>
        <wellLocation uid="loc-1">
            <wellCRS uidRef="proj1">ED50 / UTM Zone 31N</wellCRS>
            <easting uom="m">425353.84</easting>
            <northing uom="m">6623785.69</northing>
            <description>Location of well surface point in projected system.</description>
        </wellLocation>
        <referencePoint uid="SRP1">
            <name>Slot Bay Centre</name>
            <type>Site Reference Point</type>
            <location uid="loc-1">
                <wellCRS uidRef="proj1">ED50 / UTM Zone 31N</wellCRS>
                <easting uom="m">425366.47</easting>
                <northing uom="m">6623781.95</northing>
            </location>
            <location uid="loc-2">
                <wellCRS uidRef="localWell1">WellOneWSP</wellCRS>
                <localX uom="m">12.63</localX>
                <localY uom="m">-3.74</localY>
                <description>Location of the Site Reference Point with respect to the well surface point</description>
            </location>
        </referencePoint>
        <referencePoint uid="WRP2">
            <name>Sea Bed</name>
            <type>Well Reference Point</type>
            <elevation uom="ft" datum="SL">-118.40</elevation>
            <measuredDepth uom="ft" datum="KB">173.09</measuredDepth>
            <location uid="loc-1">
                <wellCRS uidRef="proj1">ED50 / UTM Zone 31N</wellCRS>
                <easting uom="m">425353.84</easting>
                <northing uom="m">6623785.69</northing>
            </location>
            <location uid="loc-2">
                <wellCRS uidRef="geog1">ED50</wellCRS>
                <latitude uom="dega">59.743844</latitude>
                <longitude uom="dega">1.67198083</longitude>
            </location>
        </referencePoint>
        <wellCRS uid="geog1">
            <name>ED50</name>
                <geodeticCRS uidRef="4230">4230</geodeticCRS >
                <description>ED50 system with EPSG code 4230.</description>
        </wellCRS>
        <wellCRS uid="proj1">
            <name>ED50 / UTM Zone 31N</name>
            <mapProjectionCRS uidRef="23031">ED50 / UTM Zone 31N</mapProjectionCRS>
        </wellCRS>
        <wellCRS uid="localWell1">
            <name>WellOneWSP</name>
            <localCRS>
                <usesWellAsOrigin>true</usesWellAsOrigin>
                <yAxisAzimuth uom="dega" northDirection="grid north">0</yAxisAzimuth>
                <xRotationCounterClockwise>false</xRotationCounterClockwise>
            </localCRS>
        </wellCRS>
        <commonData>
            <dTimCreation>2001-04-30T08:15:00.000Z</dTimCreation>
            <dTimLastChange>2001-05-31T08:15:00.000Z</dTimLastChange>
            <itemState>plan</itemState>
            <comments>These are the comments associated with the Well data object.</comments>
            <defaultDatum uidRef="KB">Kelly Bushing</defaultDatum>
        </commonData>
    </well>
</wells>
"""

################################################
#
# Removed element <country>US</country>
#
#
XML_WELL_REMOVED_ELEMENT = """<?xml version="1.0" encoding="UTF-8"?>
<!--           Example of Well data         -->
<wells 
    xmlns="http://www.witsml.org/schemas/1series" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
    xsi:schemaLocation="http://www.witsml.org/schemas/1series  ../xsd_schemas/obj_well.xsd" 
    version="1.4.1.1">
<!-- 
These examples are only intended to demonstrate the type of data that can be exchanged.
They totally artificial and are not intended to demonstrate best practices. 
-->
    <documentInfo>
        <documentName>well</documentName>
        <fileCreationInformation>
            <fileCreationDate>2001-10-31T08:15:00.000Z</fileCreationDate> 
            <fileCreator>John Smith</fileCreator>
        </fileCreationInformation>
    </documentInfo>
    <well uid="w-12">
        <name>6507/7-A-42</name>
        <nameLegal>Company Legal Name</nameLegal>
        <numLicense>Company License Number</numLicense>
        <numGovt>Govt-Number</numGovt>
        <dTimLicense>2001-05-15T13:20:00.000Z</dTimLicense>
        <field>Big Field</field>
        
        <state>TX</state>
        <county>Montgomery</county>
        <region>Region Name</region>
        <district>District Name</district>
        <block>Block Name</block>
        <timeZone>-06:00</timeZone>
        <operator>Operating Company</operator>
        <operatorDiv>Division Name</operatorDiv>
        <pcInterest uom="%">65</pcInterest>
        <numAPI>123-543-987AZ</numAPI>
        <statusWell>drilling</statusWell>
        <purposeWell>exploration</purposeWell>
        <dTimSpud>2001-05-31T08:15:00.000Z</dTimSpud>
        <dTimPa>2001-07-15T15:30:00.000Z</dTimPa>
        <wellheadElevation uom="ft">500</wellheadElevation>
        <wellDatum uid="KB">
            <name>Kelly Bushing</name>
            <code>KB</code>
            <elevation uom="ft" datum="SL">78.5</elevation>
        </wellDatum>
        <wellDatum uid="SL">
            <name>Sea Level</name>
            <code>SL</code>
            <datumName namingSystem="EPSG" code="5106">Caspian Sea</datumName>
        </wellDatum>
        <groundElevation uom="ft">250</groundElevation>
        <waterDepth uom="ft">520</waterDepth>
        <wellLocation uid="loc-1">
            <wellCRS uidRef="proj1">ED50 / UTM Zone 31N</wellCRS>
            <easting uom="m">425353.84</easting>
            <northing uom="m">6623785.69</northing>
            <description>Location of well surface point in projected system.</description>
        </wellLocation>
        <referencePoint uid="SRP1">
            <name>Slot Bay Centre</name>
            <type>Site Reference Point</type>
            <location uid="loc-1">
                <wellCRS uidRef="proj1">ED50 / UTM Zone 31N</wellCRS>
                <easting uom="m">425366.47</easting>
                <northing uom="m">6623781.95</northing>
            </location>
            <location uid="loc-2">
                <wellCRS uidRef="localWell1">WellOneWSP</wellCRS>
                <localX uom="m">12.63</localX>
                <localY uom="m">-3.74</localY>
                <description>Location of the Site Reference Point with respect to the well surface point</description>
            </location>
        </referencePoint>
        <referencePoint uid="WRP2">
            <name>Sea Bed</name>
            <type>Well Reference Point</type>
            <elevation uom="ft" datum="SL">-118.40</elevation>
            <measuredDepth uom="ft" datum="KB">173.09</measuredDepth>
            <location uid="loc-1">
                <wellCRS uidRef="proj1">ED50 / UTM Zone 31N</wellCRS>
                <easting uom="m">425353.84</easting>
                <northing uom="m">6623785.69</northing>
            </location>
            <location uid="loc-2">
                <wellCRS uidRef="geog1">ED50</wellCRS>
                <latitude uom="dega">59.743844</latitude>
                <longitude uom="dega">1.67198083</longitude>
            </location>
        </referencePoint>
        <wellCRS uid="geog1">
            <name>ED50</name>
                <geodeticCRS uidRef="4230">4230</geodeticCRS >
                <description>ED50 system with EPSG code 4230.</description>
        </wellCRS>
        <wellCRS uid="proj1">
            <name>ED50 / UTM Zone 31N</name>
            <mapProjectionCRS uidRef="23031">ED50 / UTM Zone 31N</mapProjectionCRS>
        </wellCRS>
        <wellCRS uid="localWell1">
            <name>WellOneWSP</name>
            <localCRS>
                <usesWellAsOrigin>true</usesWellAsOrigin>
                <yAxisAzimuth uom="dega" northDirection="grid north">0</yAxisAzimuth>
                <xRotationCounterClockwise>false</xRotationCounterClockwise>
            </localCRS>
        </wellCRS>
        <commonData>
            <dTimCreation>2001-04-30T08:15:00.000Z</dTimCreation>
            <dTimLastChange>2001-05-31T08:15:00.000Z</dTimLastChange>
            <itemState>plan</itemState>
            <comments>These are the comments associated with the Well data object.</comments>
            <defaultDatum uidRef="KB">Kelly Bushing</defaultDatum>
        </commonData>
    </well>
</wells>
"""



################################################
#
# Removed attribute from namingSystem
#
#   <datumName namingSystem="EPSG" code="5106">Caspian Sea</datumName>
#
#
XML_WELL_REMOVED_ATTRIBUTE = """<?xml version="1.0" encoding="UTF-8"?>
<!--           Example of Well data         -->
<wells 
    xmlns="http://www.witsml.org/schemas/1series" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
    xsi:schemaLocation="http://www.witsml.org/schemas/1series  ../xsd_schemas/obj_well.xsd" 
    version="1.4.1.1">
<!-- 
These examples are only intended to demonstrate the type of data that can be exchanged.
They totally artificial and are not intended to demonstrate best practices. 
-->
    <documentInfo>
        <documentName>well</documentName>
        <fileCreationInformation>
            <fileCreationDate>2001-10-31T08:15:00.000Z</fileCreationDate> 
            <fileCreator>John Smith</fileCreator>
        </fileCreationInformation>
    </documentInfo>
    <well uid="w-12">
        <name>6507/7-A-42</name>
        <nameLegal>Company Legal Name</nameLegal>
        <numLicense>Company License Number</numLicense>
        <numGovt>Govt-Number</numGovt>
        <dTimLicense>2001-05-15T13:20:00.000Z</dTimLicense>
        <field>Big Field</field>
        <country>US</country>
        <state>TX</state>
        <county>Montgomery</county>
        <region>Region Name</region>
        <district>District Name</district>
        <block>Block Name</block>
        <timeZone>-06:00</timeZone>
        <operator>Operating Company</operator>
        <operatorDiv>Division Name</operatorDiv>
        <pcInterest uom="%">65</pcInterest>
        <numAPI>123-543-987AZ</numAPI>
        <statusWell>drilling</statusWell>
        <purposeWell>exploration</purposeWell>
        <dTimSpud>2001-05-31T08:15:00.000Z</dTimSpud>
        <dTimPa>2001-07-15T15:30:00.000Z</dTimPa>
        <wellheadElevation uom="ft">500</wellheadElevation>
        <wellDatum uid="KB">
            <name>Kelly Bushing</name>
            <code>KB</code>
            <elevation uom="ft" datum="SL">78.5</elevation>
        </wellDatum>
        <wellDatum uid="SL">
            <name>Sea Level</name>
            <code>SL</code>
            <datumName  code="5106">Caspian Sea</datumName>
        </wellDatum>
        <groundElevation uom="ft">250</groundElevation>
        <waterDepth uom="ft">520</waterDepth>
        <wellLocation uid="loc-1">
            <wellCRS uidRef="proj1">ED50 / UTM Zone 31N</wellCRS>
            <easting uom="m">425353.84</easting>
            <northing uom="m">6623785.69</northing>
            <description>Location of well surface point in projected system.</description>
        </wellLocation>
        <referencePoint uid="SRP1">
            <name>Slot Bay Centre</name>
            <type>Site Reference Point</type>
            <location uid="loc-1">
                <wellCRS uidRef="proj1">ED50 / UTM Zone 31N</wellCRS>
                <easting uom="m">425366.47</easting>
                <northing uom="m">6623781.95</northing>
            </location>
            <location uid="loc-2">
                <wellCRS uidRef="localWell1">WellOneWSP</wellCRS>
                <localX uom="m">12.63</localX>
                <localY uom="m">-3.74</localY>
                <description>Location of the Site Reference Point with respect to the well surface point</description>
            </location>
        </referencePoint>
        <referencePoint uid="WRP2">
            <name>Sea Bed</name>
            <type>Well Reference Point</type>
            <elevation uom="ft" datum="SL">-118.40</elevation>
            <measuredDepth uom="ft" datum="KB">173.09</measuredDepth>
            <location uid="loc-1">
                <wellCRS uidRef="proj1">ED50 / UTM Zone 31N</wellCRS>
                <easting uom="m">425353.84</easting>
                <northing uom="m">6623785.69</northing>
            </location>
            <location uid="loc-2">
                <wellCRS uidRef="geog1">ED50</wellCRS>
                <latitude uom="dega">59.743844</latitude>
                <longitude uom="dega">1.67198083</longitude>
            </location>
        </referencePoint>
        <wellCRS uid="geog1">
            <name>ED50</name>
                <geodeticCRS uidRef="4230">4230</geodeticCRS >
                <description>ED50 system with EPSG code 4230.</description>
        </wellCRS>
        <wellCRS uid="proj1">
            <name>ED50 / UTM Zone 31N</name>
            <mapProjectionCRS uidRef="23031">ED50 / UTM Zone 31N</mapProjectionCRS>
        </wellCRS>
        <wellCRS uid="localWell1">
            <name>WellOneWSP</name>
            <localCRS>
                <usesWellAsOrigin>true</usesWellAsOrigin>
                <yAxisAzimuth uom="dega" northDirection="grid north">0</yAxisAzimuth>
                <xRotationCounterClockwise>false</xRotationCounterClockwise>
            </localCRS>
        </wellCRS>
        <commonData>
            <dTimCreation>2001-04-30T08:15:00.000Z</dTimCreation>
            <dTimLastChange>2001-05-31T08:15:00.000Z</dTimLastChange>
            <itemState>plan</itemState>
            <comments>These are the comments associated with the Well data object.</comments>
            <defaultDatum uidRef="KB">Kelly Bushing</defaultDatum>
        </commonData>
    </well>
</wells>
"""



class Test(unittest.TestCase):


    def setUp(self):
        if not os.path.exists("reports"):
            os.makedirs("reports");



    def tearDown(self):
        pass


    def test_witsml_well_equal(self):
        result, report = witsml_obj_compare.witsml1411_compare_obj_wells( XML_WELL , XML_WELL_UID_MODIFIED_NO_COMMENTS )
        open("reports/repo_well_diff_uid.html","w").write(report);
        self.assertTrue( result );
    
    def test_witsml_well_text_modified(self):
        result, report = witsml_obj_compare.witsml1411_compare_obj_wells( XML_WELL , XML_WELL_TEXT_MODIFIED ) 
        open("reports/repo_well_diff_text.html","w").write(report);
        self.assertFalse( result );
        
    def test_witsml_well_removed_element(self):
        result, report = witsml_obj_compare.witsml1411_compare_obj_wells( XML_WELL , XML_WELL_REMOVED_ELEMENT ) 
        open("reports/repo_well_removed_element.html","w").write(report);
        self.assertFalse( result );
        
    def test_witsml_well_removed_attrib(self):
        result, report = witsml_obj_compare.witsml1411_compare_obj_wells( XML_WELL , XML_WELL_REMOVED_ATTRIBUTE ) 
        open("reports/repo_well_removed_attribute.html","w").write(report);
        self.assertFalse( result );
        
        
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()