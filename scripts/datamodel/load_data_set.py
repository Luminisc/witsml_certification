#! /usr/bin/env python
from wtl.witsml import *
import wtl.globals
import create_large_objects

test(
     purpose = "Load certification data set",
     reference =  "",
     reference_text = "",
    )

##########################################################################
# This script lads the certification data set to the server to be tested #
##########################################################################

# server_w1_uid
WMLS_GetFromStore(WMLTYPEIN_WELL, """<?xml version="1.0" encoding="UTF-8"?>
                                     <wells xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                       <well uid='Energistics-well-0001'/>                         
                                     </wells>
                                  """)  
check_ReturnValue_Success()

if (get_XMLout_NumberOfObjects_Int() == 1):
    WMLS_DeleteFromStore(WMLTYPEIN_WELL, """<?xml version="1.0" encoding="utf-8"?>
                                         <wells xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                           <well uid="Energistics-well-0001"/>
                                         </wells>
                                         """, OptionsIn={"cascadedDelete":"true"})  
    check_ReturnValue_Success()

WMLS_AddToStore(WMLTYPEIN_WELL, """<?xml version="1.0" encoding="utf-8"?>
                                   <wells xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                      <well uid="Energistics-well-0001">
                                         <name>Energistics Certification Well 1</name>
                                         <numGovt>Energistics-numGovt-11111</numGovt>
                                         <dTimLicense>2001-05-15T13:20:00Z</dTimLicense>
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
                                         <numAPI>Energistics-numAPI-11111</numAPI>
                                         <statusWell>drilling</statusWell>
                                         <purposeWell>exploration</purposeWell>
                                         <dTimSpud>2001-05-31T08:15:00Z</dTimSpud>
                                         <dTimPa>2001-07-15T15:30:00Z</dTimPa>
                                      </well>
                                   </wells>""")  
check_ReturnValue_Success()
partial_success("Added server_w1_uid successfully")

# server_w1_wb1_uid
WMLS_AddToStore(WMLTYPEIN_WELLBORE, """<?xml version="1.0" encoding="utf-8"?>
                                   <wellbores xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                      <wellbore uidWell="Energistics-well-0001" uid="Energistics-w1-wellbore-0001">
                                         <nameWell>Energistics Certification Well 1</nameWell>
                                         <name>Energistics Certification Wellbore 1</name>
                                      </wellbore>
                                   </wellbores>""")  
check_ReturnValue_Success()
partial_success("Added server_w1_wb1_uid successfully")

# server_w1_wb1_log1_uid - depth log
WMLS_AddToStore(WMLTYPEIN_LOG, """<?xml version="1.0" encoding="utf-8"?>
                                   <logs xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                      <log uidWell="Energistics-well-0001" uidWellbore="Energistics-w1-wellbore-0001" uid="Energistics-w1-wb1-log-0001">
                                         <nameWell>Energistics Certification Well 1</nameWell>
                                         <nameWellbore>Energistics Certification Well 1 Wellbore 1</nameWellbore>
                                         <name>Energistics Certification Well 1 Wellbore 1 Log 1</name>
                                         <indexType>measured depth</indexType>
                                         <startIndex uom="m">0</startIndex>
                                         <endIndex uom="m">4</endIndex>
                                         <direction>increasing</direction>
                                         <indexCurve>BDEP</indexCurve>
                                         <logCurveInfo uid='BDEP'>
                                           <mnemonic>BDEP</mnemonic>
                                           <unit>m</unit>
                                           <typeLogData>int</typeLogData>
                                         </logCurveInfo>
                                         <logCurveInfo uid='CURVE1'>
                                           <mnemonic>CURVE1</mnemonic>
                                           <unit>m/h</unit>
                                           <typeLogData>int</typeLogData>
                                         </logCurveInfo>
                                         <logCurveInfo uid='CURVE2'>
                                           <mnemonic>CURVE2</mnemonic>
                                           <unit>m/h</unit>
                                           <typeLogData>int</typeLogData>
                                         </logCurveInfo>
                                         <logCurveInfo uid='CURVE3'>
                                           <mnemonic>CURVE3</mnemonic>
                                           <unit>m/h</unit>
                                           <typeLogData>int</typeLogData>
                                         </logCurveInfo>
                                         <logData>
                                           <mnemonicList>BDEP,CURVE1,CURVE2,CURVE3</mnemonicList>
                                           <unitList>m, m/h, m/h, m/h</unitList>
                                           <data>0,0,0,0</data>
                                           <data>1,1,1,1</data>
                                           <data>2,2,2,2</data>
                                           <data>3,3,3,3</data>
                                           <data>4,4,4,4</data>
                                         </logData>
                                      </log>
                                   </logs>""")  
check_ReturnValue_Success()
partial_success("Added server_w1_wb1_log1_uid successfully")

# make server_w1_wb1_log1_uid growing
#todo

# server_w1_wb1_log2_uid - time log
WMLS_AddToStore(WMLTYPEIN_LOG, """<?xml version="1.0" encoding="utf-8"?>
                                   <logs xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                      <log uidWell="Energistics-well-0001" uidWellbore="Energistics-w1-wellbore-0001" uid="Energistics-w1-wb1-log-0002">
                                         <nameWell>Energistics Certification Well 1</nameWell>
                                         <nameWellbore>Energistics Certification Well 1 Wellbore 1</nameWellbore>
                                         <name>Energistics Certification Well 1 Wellbore 1 Log 2</name>
                                         <indexType>date time</indexType>
                                         <startDateTimeIndex>2012-07-26T15:17:20Z</startDateTimeIndex>
                                         <endDateTimeIndex>2012-07-26T15:17:50Z</endDateTimeIndex>
                                         <direction>increasing</direction>
                                         <indexCurve>TIME</indexCurve>
                                         <logCurveInfo uid='TIME'>
                                           <mnemonic>TIME</mnemonic>
                                           <unit>unitless</unit>
                                           <typeLogData>date time</typeLogData>
                                         </logCurveInfo>
                                         <logCurveInfo uid='ROP'>
                                           <mnemonic>ROP</mnemonic>
                                           <unit>m/h</unit>
                                           <typeLogData>int</typeLogData>
                                         </logCurveInfo>
                                         <logData>
                                           <mnemonicList>TIME,ROP</mnemonicList>
                                           <unitList>unitless,m/h</unitList>
                                           <data>2012-07-26T15:17:20Z,0</data>
                                           <data>2012-07-26T15:17:30Z,1</data>
                                           <data>2012-07-26T15:17:40Z,2</data>
                                           <data>2012-07-26T15:17:50Z,3</data>
                                         </logData>
                                      </log>
                                   </logs>""")  
check_ReturnValue_Success()
partial_success("Added server_w1_wb1_log2_uid successfully")

# server_w1_wb1_traj1_uid
WMLS_AddToStore(WMLTYPEIN_TRAJECTORY, """<?xml version="1.0" encoding="UTF-8"?>
<trajectorys xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
    <trajectory uidWell="Energistics-well-0001" uidWellbore="Energistics-w1-wellbore-0001" uid="Energistics-w1-wb1-trajectory-0001">
        <nameWell>Energistics Certification Well 1</nameWell>
        <nameWellbore>Energistics Certification Well 1 Wellbore 1</nameWellbore>
        <name>Energistics Certification Well 1 Wellbore 1 Trajectory 1</name>
        <dTimTrajStart>2001-10-31T08:15:00.000Z</dTimTrajStart>
        <dTimTrajEnd>2001-11-03T16:30:00.000Z</dTimTrajEnd>
        <mdMn uom="ft">0</mdMn>
        <mdMx uom="ft">14089.3</mdMx>
        <serviceCompany>Anadrill</serviceCompany>
        <magDeclUsed uom="dega">-4.038</magDeclUsed>
        <gridCorUsed uom="dega">0.99961</gridCorUsed>
        <aziVertSect uom="dega">82.700</aziVertSect>
        <dispNsVertSectOrig uom="ft">0</dispNsVertSectOrig>
        <dispEwVertSectOrig uom="ft">0</dispEwVertSectOrig>
        <definitive>true</definitive>
        <memory>true</memory>
        <finalTraj>true</finalTraj>
        <aziRef>grid north</aziRef>
        <trajectoryStation uid="34ht5">
            <dTimStn>2001-10-21T08:15:00.000Z</dTimStn>
            <typeTrajStation>tie in point</typeTrajStation>
            <md uom="ft">0</md>
            <tvd uom="ft">0</tvd>
            <incl uom="dega">0</incl>
            <azi uom="dega">47.3</azi>
            <mtf uom="dega">47.3</mtf>
            <gtf uom="dega">0</gtf>
            <dispNs uom="ft">0</dispNs>
            <dispEw uom="ft">0</dispEw>
            <vertSect uom="ft">0</vertSect>
            <dls uom="dega/ft">0</dls>
            <rateTurn uom="dega/ft">0</rateTurn>
            <rateBuild uom="dega/ft">0</rateBuild>
            <mdDelta uom="ft">0</mdDelta>
            <tvdDelta uom="ft">0</tvdDelta>
            <modelToolError>good gyro</modelToolError>
            <gravTotalUncert uom="m/s2">0</gravTotalUncert>
            <dipAngleUncert uom="dega">0</dipAngleUncert>
            <magTotalUncert uom="nT">0</magTotalUncert>
            <gravAccelCorUsed>false</gravAccelCorUsed>
            <magXAxialCorUsed>false</magXAxialCorUsed>
            <sagCorUsed>false</sagCorUsed>
            <magDrlstrCorUsed>false</magDrlstrCorUsed>
            <statusTrajStation>position</statusTrajStation>
            <rawData>
                <gravAxialRaw uom="ft/s2">0.116</gravAxialRaw>
                <gravTran1Raw uom="ft/s2">-0.168</gravTran1Raw>
                <gravTran2Raw uom="ft/s2">-1654</gravTran2Raw>
                <magAxialRaw uom="nT">22.77</magAxialRaw>
                <magTran1Raw uom="nT">22.5</magTran1Raw>
                <magTran2Raw uom="nT">27.05</magTran2Raw>
            </rawData>
            <corUsed>
                <gravAxialAccelCor uom="ft/s2">0.11</gravAxialAccelCor>
                <gravTran1AccelCor uom="ft/s2">0.14</gravTran1AccelCor>
                <gravTran2AccelCor uom="ft/s2">0.13</gravTran2AccelCor>
                <magAxialDrlstrCor uom="nT">0.17</magAxialDrlstrCor>
                <magTran1DrlstrCor uom="nT">0.16</magTran1DrlstrCor>
                <magTran2DrlstrCor uom="nT">0.24</magTran2DrlstrCor>
                <sagIncCor uom="dega">0</sagIncCor>
                <sagAziCor uom="dega">0</sagAziCor>
                <stnMagDeclUsed uom="dega">-4.038</stnMagDeclUsed>
                <stnGridCorUsed uom="dega">-0.4917</stnGridCorUsed>
                <dirSensorOffset uom="ft">48.3</dirSensorOffset>
            </corUsed>
            <valid>
                <magTotalFieldCalc uom="nT">51.19</magTotalFieldCalc>
                <magDipAngleCalc uom="dega">41.5</magDipAngleCalc>
                <gravTotalFieldCalc uom="ft/s2">0.999</gravTotalFieldCalc>
            </valid>
            <matrixCov>
                <varianceNN uom="ft2">0.005236</varianceNN>
                <varianceNE uom="ft2">0.005236</varianceNE>
                <varianceNVert uom="ft2">2.356194</varianceNVert>
                <varianceEE uom="ft2">0.005236</varianceEE>
                <varianceEVert uom="ft2">0.005236</varianceEVert>
                <varianceVertVert uom="ft2">0.785398</varianceVertVert>
                <biasN uom="ft">0</biasN>
                <biasE uom="ft">0</biasE>
                <biasVert uom="ft">0</biasVert>
            </matrixCov>
            <location uid="loc-1">
                <wellCRS uidRef="geog1">ED50</wellCRS>
                <latitude uom="dega">59.755300</latitude>
                <longitude uom="dega">1.71347417</longitude>
            </location>
            <location uid="loc-2">
                <wellCRS uidRef="proj1">ED50 / UTM Zone 31N</wellCRS>
                <easting uom="m">427710.69</easting>
                <northing uom="m">6625015.54</northing>
            </location>
        </trajectoryStation>
        <commonData>
            <itemState>plan</itemState>
            <comments>These are the comments associated with the trajectory data object.</comments>
        </commonData>
    </trajectory>
</trajectorys>
""")


partial_success("Added server_w1_wb1_traj1_uid successfully")

# server_w1_wb1_traj2_uid
WMLS_AddToStore(WMLTYPEIN_TRAJECTORY, """<?xml version="1.0" encoding="UTF-8"?>
<trajectorys xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
    <trajectory uidWell="Energistics-well-0001" uidWellbore="Energistics-w1-wellbore-0001" uid="Energistics-w1-wb1-trajectory-0002">
        <nameWell>Energistics Certification Well 1</nameWell>
        <nameWellbore>Energistics Certification Well 1 Wellbore 1</nameWellbore>
        <name>Energistics Certification Well 1 Wellbore 1 Trajectory 2</name>
        <dTimTrajStart>2001-10-31T08:15:00.000Z</dTimTrajStart>
        <dTimTrajEnd>2001-11-03T16:30:00.000Z</dTimTrajEnd>
        <mdMn uom="ft">0</mdMn>
        <mdMx uom="ft">14089.3</mdMx>
        <serviceCompany>Anadrill</serviceCompany>
        <magDeclUsed uom="dega">-4.038</magDeclUsed>
        <gridCorUsed uom="dega">0.99961</gridCorUsed>
        <aziVertSect uom="dega">82.700</aziVertSect>
        <dispNsVertSectOrig uom="ft">0</dispNsVertSectOrig>
        <dispEwVertSectOrig uom="ft">0</dispEwVertSectOrig>
        <definitive>true</definitive>
        <memory>true</memory>
        <finalTraj>true</finalTraj>
        <aziRef>grid north</aziRef>
        <trajectoryStation uid="34ht5">
            <dTimStn>2001-10-21T08:15:00.000Z</dTimStn>
            <typeTrajStation>tie in point</typeTrajStation>
            <md uom="ft">0</md>
            <tvd uom="ft">0</tvd>
            <incl uom="dega">0</incl>
            <azi uom="dega">47.3</azi>
            <mtf uom="dega">47.3</mtf>
            <gtf uom="dega">0</gtf>
            <dispNs uom="ft">0</dispNs>
            <dispEw uom="ft">0</dispEw>
            <vertSect uom="ft">0</vertSect>
            <dls uom="dega/ft">0</dls>
            <rateTurn uom="dega/ft">0</rateTurn>
            <rateBuild uom="dega/ft">0</rateBuild>
            <mdDelta uom="ft">0</mdDelta>
            <tvdDelta uom="ft">0</tvdDelta>
            <modelToolError>good gyro</modelToolError>
            <gravTotalUncert uom="m/s2">0</gravTotalUncert>
            <dipAngleUncert uom="dega">0</dipAngleUncert>
            <magTotalUncert uom="nT">0</magTotalUncert>
            <gravAccelCorUsed>false</gravAccelCorUsed>
            <magXAxialCorUsed>false</magXAxialCorUsed>
            <sagCorUsed>false</sagCorUsed>
            <magDrlstrCorUsed>false</magDrlstrCorUsed>
            <statusTrajStation>position</statusTrajStation>
            <rawData>
                <gravAxialRaw uom="ft/s2">0.116</gravAxialRaw>
                <gravTran1Raw uom="ft/s2">-0.168</gravTran1Raw>
                <gravTran2Raw uom="ft/s2">-1654</gravTran2Raw>
                <magAxialRaw uom="nT">22.77</magAxialRaw>
                <magTran1Raw uom="nT">22.5</magTran1Raw>
                <magTran2Raw uom="nT">27.05</magTran2Raw>
            </rawData>
            <corUsed>
                <gravAxialAccelCor uom="ft/s2">0.11</gravAxialAccelCor>
                <gravTran1AccelCor uom="ft/s2">0.14</gravTran1AccelCor>
                <gravTran2AccelCor uom="ft/s2">0.13</gravTran2AccelCor>
                <magAxialDrlstrCor uom="nT">0.17</magAxialDrlstrCor>
                <magTran1DrlstrCor uom="nT">0.16</magTran1DrlstrCor>
                <magTran2DrlstrCor uom="nT">0.24</magTran2DrlstrCor>
                <sagIncCor uom="dega">0</sagIncCor>
                <sagAziCor uom="dega">0</sagAziCor>
                <stnMagDeclUsed uom="dega">-4.038</stnMagDeclUsed>
                <stnGridCorUsed uom="dega">-0.4917</stnGridCorUsed>
                <dirSensorOffset uom="ft">48.3</dirSensorOffset>
            </corUsed>
            <valid>
                <magTotalFieldCalc uom="nT">51.19</magTotalFieldCalc>
                <magDipAngleCalc uom="dega">41.5</magDipAngleCalc>
                <gravTotalFieldCalc uom="ft/s2">0.999</gravTotalFieldCalc>
            </valid>
            <matrixCov>
                <varianceNN uom="ft2">0.005236</varianceNN>
                <varianceNE uom="ft2">0.005236</varianceNE>
                <varianceNVert uom="ft2">2.356194</varianceNVert>
                <varianceEE uom="ft2">0.005236</varianceEE>
                <varianceEVert uom="ft2">0.005236</varianceEVert>
                <varianceVertVert uom="ft2">0.785398</varianceVertVert>
                <biasN uom="ft">0</biasN>
                <biasE uom="ft">0</biasE>
                <biasVert uom="ft">0</biasVert>
            </matrixCov>
            <location uid="loc-1">
                <wellCRS uidRef="geog1">ED50</wellCRS>
                <latitude uom="dega">59.755300</latitude>
                <longitude uom="dega">1.71347417</longitude>
            </location>
            <location uid="loc-2">
                <wellCRS uidRef="proj1">ED50 / UTM Zone 31N</wellCRS>
                <easting uom="m">427710.69</easting>
                <northing uom="m">6625015.54</northing>
            </location>
        </trajectoryStation>
        <commonData>
            <itemState>plan</itemState>
            <comments>These are the comments associated with the trajectory data object.</comments>
        </commonData>
    </trajectory>
</trajectorys>
""")

partial_success("Added server_w1_wb1_traj2_uid successfully")

# server_w1_wb2_uid
WMLS_AddToStore(WMLTYPEIN_WELLBORE, """<?xml version="1.0" encoding="utf-8"?>
                                   <wellbores xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                      <wellbore uidWell="Energistics-well-0001" uid="Energistics-w1-wellbore-0002">
                                         <nameWell>Energistics Certification Well 1</nameWell>
                                         <name>Energistics Certification Wellbore 2</name>
                                      </wellbore>
                                   </wellbores>""")  
check_ReturnValue_Success()
partial_success("Added server_w1_wb2_uid successfully")

# server_w2_uid
WMLS_GetFromStore(WMLTYPEIN_WELL, """<?xml version="1.0" encoding="UTF-8"?>
                                     <wells xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                       <well uid='Energistics-well-0002'/>                         
                                     </wells>
                                  """)  
check_ReturnValue_Success()

if (get_XMLout_NumberOfObjects_Int() == 1):
    WMLS_DeleteFromStore(WMLTYPEIN_WELL, """<?xml version="1.0" encoding="utf-8"?>
                                         <wells xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                           <well uid="Energistics-well-0002"/>
                                         </wells>
                                         """,OptionsIn={"cascadedDelete":"true"})  
    check_ReturnValue_Success()

WMLS_AddToStore(WMLTYPEIN_WELL, """<?xml version="1.0" encoding="utf-8"?>
                                   <wells xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                      <well uid="Energistics-well-0002">
                                         <name>Energistics Certification Well 2</name>
                                         <numGovt>Energistics-numGovt-22222</numGovt>
                                         <dTimLicense>2001-05-15T13:20:00Z</dTimLicense>
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
                                         <numAPI>Energistics-numAPI-22222</numAPI>
                                         <statusWell>drilling</statusWell>
                                         <purposeWell>exploration</purposeWell>
                                         <dTimSpud>2001-05-31T08:15:00Z</dTimSpud>
                                         <dTimPa>2001-07-15T15:30:00Z</dTimPa>
                                      </well>
                                   </wells>""")  
check_ReturnValue_Success()
partial_success("Added server_w2_uid successfully")

# server_w2_wb1_uid
WMLS_AddToStore(WMLTYPEIN_WELLBORE, """<?xml version="1.0" encoding="utf-8"?>
                                   <wellbores xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                      <wellbore uidWell="Energistics-well-0002" uid="Energistics-w2-wellbore-0001">
                                         <nameWell>Energistics Certification Well 2</nameWell>
                                         <name>Energistics Certification Wellbore 2</name>
                                      </wellbore>
                                   </wellbores>""")  
check_ReturnValue_Success()
partial_success("Added server_w1_wb1_uid successfully")

# server_w2_wb1_log1_uid - depth log
WMLS_AddToStore(WMLTYPEIN_LOG, """<?xml version="1.0" encoding="utf-8"?>
                                   <logs xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                      <log uidWell="Energistics-well-0002" uidWellbore="Energistics-w2-wellbore-0001" uid="Energistics-w2-wb1-log-0001">
                                         <nameWell>Energistics Certification Well 2</nameWell>
                                         <nameWellbore>Energistics Certification Well 2 Wellbore 1</nameWellbore>
                                         <name>Energistics Certification Well 2 Wellbore 1 Log 1</name>
                                         <indexType>measured depth</indexType>
                                         <startIndex uom="m">0</startIndex>
                                         <endIndex uom="m">4</endIndex>
                                         <direction>increasing</direction>
                                         <indexCurve>BDEP</indexCurve>
                                         <logCurveInfo uid='BDEP'>
                                           <mnemonic>BDEP</mnemonic>
                                           <unit>m</unit>
                                           <typeLogData>int</typeLogData>
                                         </logCurveInfo>
                                         <logCurveInfo uid='CURVE1'>
                                           <mnemonic>CURVE1</mnemonic>
                                           <unit>m/h</unit>
                                           <typeLogData>int</typeLogData>
                                         </logCurveInfo>
                                         <logCurveInfo uid='CURVE2'>
                                           <mnemonic>CURVE2</mnemonic>
                                           <unit>m/h</unit>
                                           <typeLogData>int</typeLogData>
                                         </logCurveInfo>
                                         <logCurveInfo uid='CURVE3'>
                                           <mnemonic>CURVE3</mnemonic>
                                           <unit>m/h</unit>
                                           <typeLogData>int</typeLogData>
                                         </logCurveInfo>
                                         <logData>
                                           <mnemonicList>BDEP,CURVE1,CURVE2,CURVE3</mnemonicList>
                                           <unitList>m, m/h, m/h, m/h</unitList>
                                           <data>0,0,0,0</data>
                                           <data>1,1,1,1</data>
                                           <data>2,2,2,2</data>
                                           <data>3,3,3,3</data>
                                           <data>4,4,4,4</data>
                                         </logData>
                                      </log>
                                   </logs>""")  
check_ReturnValue_Success()
partial_success("Added server_w2_wb1_log1_uid successfully")


##########
# well 3
##########

# server_w3_uid
WMLS_GetFromStore(WMLTYPEIN_WELL, """<?xml version="1.0" encoding="UTF-8"?>
                                     <wells xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                       <well uid='Energistics-well-0003'/>                         
                                     </wells>
                                  """)  
check_ReturnValue_Success()

if (get_XMLout_NumberOfObjects_Int() == 1):
    WMLS_DeleteFromStore(WMLTYPEIN_WELL, """<?xml version="1.0" encoding="utf-8"?>
                                         <wells xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                           <well uid="Energistics-well-0003"/>
                                         </wells>
                                         """,OptionsIn={"cascadedDelete":"true"})  
    check_ReturnValue_Success()

WMLS_AddToStore(WMLTYPEIN_WELL, """<?xml version="1.0" encoding="utf-8"?>
                                   <wells xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                      <well uid="Energistics-well-0003">
                                         <name>Energistics Certification Well 3</name>
                                         <numGovt>Energistics-numGovt-22222</numGovt>
                                         <dTimLicense>2001-05-15T13:20:00Z</dTimLicense>
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
                                         <numAPI>Energistics-numAPI-22222</numAPI>
                                         <statusWell>drilling</statusWell>
                                         <purposeWell>exploration</purposeWell>
                                         <dTimSpud>2001-05-31T08:15:00Z</dTimSpud>
                                         <dTimPa>2001-07-15T15:30:00Z</dTimPa>
                                      </well>
                                   </wells>""")  
check_ReturnValue_Success()
partial_success("Added server_w3_uid successfully")

# server_w3_wb1_uid
WMLS_AddToStore(WMLTYPEIN_WELLBORE, """<?xml version="1.0" encoding="utf-8"?>
                                   <wellbores xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                      <wellbore uidWell="Energistics-well-0003" uid="Energistics-w3-wellbore-0001">
                                         <nameWell>Energistics Certification Well 3</nameWell>
                                         <name>Energistics Certification Well 3 Wellbore 1</name>
                                      </wellbore>
                                   </wellbores>""")  
check_ReturnValue_Success()
partial_success("Added server_w3_wb1_uid successfully")

# server_w3_wb1_mudlog1_uid
if (wtl.globals.is_function_object_supported('WMLS_AddToStore' , WMLTYPEIN_MUDLOG) == True):
    WMLS_AddToStore(WMLTYPEIN_MUDLOG, """<?xml version="1.0" encoding="utf-8"?>
                                    <mudLogs xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                        <mudLog uidWell="Energistics-well-0003" uidWellbore="Energistics-w3-wellbore-0001" uid="Energistics-w3-wb1-mudlog-0001">
                                            <nameWell>Energistics Certification Well 3</nameWell>
                                            <nameWellbore>Energistics Certification Well 3 Wellbore 1</nameWellbore>
                                            <name>Energistics Certifications Well 3 Mudlog 1</name>
                                        </mudLog>
                                    </mudLogs>""")  
    partial_success("Added server_w3_wb1_mudlog1_uid successfully")
    check_ReturnValue_Success()


# cleanup for Test 21
log('Cleanup Test 21')
WMLS_DeleteFromStore(WMLTYPEIN_WELL, """<?xml version="1.0" encoding="utf-8"?>
                                     <wells xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                       <well uid="certification-Test-21"/>
                                     </wells>
                                     """ )

##############################
# build large logs for well 3
##############################


#obtain maxDataNodes and maxDataPoints
server_maxDataNodes = {}
server_maxDataNodes['WMLS_AddToStore'] = int(wtl.globals.get_maxDataNodes('WMLS_AddToStore', 'log'))
server_maxDataNodes['WMLS_GetFromStore'] = int(wtl.globals.get_maxDataNodes('WMLS_GetFromStore', 'log'))
server_maxDataNodes['WMLS_UpdateInStore'] = int(wtl.globals.get_maxDataNodes('WMLS_UpdateInStore', 'log'))

server_maxDataPoints = {}
server_maxDataPoints['WMLS_AddToStore'] = int(wtl.globals.get_maxDataPoints('WMLS_AddToStore', 'log'))
server_maxDataPoints['WMLS_GetFromStore'] = int(wtl.globals.get_maxDataPoints('WMLS_GetFromStore', 'log'))
server_maxDataPoints['WMLS_UpdateInStore'] = int(wtl.globals.get_maxDataPoints('WMLS_UpdateInStore', 'log'))

create_large_objects.create_log_maxDataNodes("Energistics-well-0003",
         "Energistics-w3-wellbore-0001",
         "Energistics-w3-wb1-log-0001",
         "Energistics Certification Well 3",
         "Energistics Certification Well 3 Wellbore 1",
         "Energistics Certification Well 3 Wellbore 1 Log 1",
         "measured depth",
         server_maxDataNodes)
partial_success("Added server_w3_wb1_log1_uid successfully")    

create_large_objects.create_log_maxDataNodes("Energistics-well-0003",
         "Energistics-w3-wellbore-0001",
         "Energistics-w3-wb1-log-0003",
         "Energistics Certification Well 3",
         "Energistics Certification Well 3 Wellbore 1",
         "Energistics Certification Well 3 Wellbore 1 Log 3",
         "date time",
         server_maxDataNodes)
partial_success("Added server_w3_wb1_log3_uid successfully")    

create_large_objects.create_log_maxDataPoints("Energistics-well-0003",
         "Energistics-w3-wellbore-0001",
         "Energistics-w3-wb1-log-0002",
         "Energistics Certification Well 3",
         "Energistics Certification Well 3 Wellbore 1",
         "Energistics Certification Well 3 Wellbore 1 Log 2",
         "measured depth",
         server_maxDataPoints)
partial_success("Added server_w3_wb1_log2_uid successfully")    

create_large_objects.create_log_maxDataPoints("Energistics-well-0003",
         "Energistics-w3-wellbore-0001",
         "Energistics-w3-wb1-log-0004",
         "Energistics Certification Well 3",
         "Energistics Certification Well 3 Wellbore 1",
         "Energistics Certification Well 3 Wellbore 1 Log 4",
         "date time",
         server_maxDataPoints)
partial_success("Added server_w3_wb1_log4_uid successfully")   

# wait for the above changes to be detected by the server.
pause_for_changeDetectionPeriod()

success()
