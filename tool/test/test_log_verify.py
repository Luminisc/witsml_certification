#******************************************************************************
# Copyright (c) 2012 Energistics
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
import wtl.log_verify
import wtl.store_prim
            
XML_ELAPSE_TIME_LOG_1410_OK = """
<logs xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" version="1.4.1.0">
  <log uidWell="T1cwMzAuSE9VX19fX19fRkxPVU5ERVJfX19fX19fX19fX18xOF9fX18=" uidWellbore="T1cwMzAuSE9VX19fX19fRkxPVU5ERVJfX19fX19fX19fX18xOF9fX18=" uid="VU5LTk9XTl9fX19fX19fX19fX19fX19fX19fX19fMV9fX19fMDAwMTFfX18=">
    <nameWell>LASTimeBasedCurves</nameWell>
    <nameWellbore>LASTimeBasedCurves</nameWellbore>
    <name>UNKNOWN</name>
    <objectGrowing>false</objectGrowing>
    <serviceCompany>UNKNOWN</serviceCompany>
    <runNumber>1</runNumber>
    <pass>0001</pass>
    <creationDate>2008-09-19T17:21:10-05:00</creationDate>
    <indexType>elapsed time</indexType>
    <startIndex uom="ms">820.2</startIndex>
    <endIndex uom="ms">3280.8</endIndex>
    <stepIncrement uom="ms">0</stepIncrement>
    <direction>increasing</direction>
    <indexCurve>ETIM</indexCurve>
    <logCurveInfo uid="ZXRpbV9fX19fX19fX19fX19fX19fX19fXw==">
      <mnemonic>ETIM</mnemonic>
      <classWitsml>elapse time</classWitsml>
      <unit>ms</unit>
      <mnemAlias>ETIM</mnemAlias>
      <minIndex uom="ms">820.2</minIndex>
      <maxIndex uom="ms">3280.8</maxIndex>
      <curveDescription>Elapse time</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="QlNfX19fX19fX19fX19fX19fX19fX19fXw==">
      <mnemonic>BS</mnemonic>
      <unit>in</unit>
      <mnemAlias>BS</mnemAlias>
      <nullValue>-999.25</nullValue>
      <minIndex uom="ms">820.200012207031</minIndex>
      <maxIndex uom="ms">3280.8</maxIndex>
      <curveDescription>BIT SIZE ApiCode=00 000 000 000</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="Q1NfX19fX19fX19fX19fX19fX19fX19fXw==">
      <mnemonic>CS</mnemonic>
      <mnemAlias/>
      <nullValue>-999.25</nullValue>
      <minIndex uom="ms">820.200012207031</minIndex>
      <maxIndex uom="ms">3280.8</maxIndex>
      <curveDescription>CABLE SPEED ApiCode=00 000 000 000</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="R1JfX19fX19fX19fX19fX19fX19fX19fXw==">
      <mnemonic>GR</mnemonic>
      <unit>gAPI</unit>
      <mnemAlias>GRD</mnemAlias>
      <nullValue>-999.25</nullValue>
      <minIndex uom="ms">820.200012207031</minIndex>
      <maxIndex uom="ms">3280.8</maxIndex>
      <curveDescription>NATURAL GAMMA RAY ApiCode=00 000 000 000</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="VEVOU19fX19fX19fX19fX19fX19fX19fXw==">
      <mnemonic>TENS</mnemonic>
      <unit>tonfUS</unit>
      <mnemAlias/>
      <nullValue>-999.25</nullValue>
      <minIndex uom="ms">820.200012207031</minIndex>
      <maxIndex uom="ms">3280.8</maxIndex>
      <curveDescription>CABLE TENSION ApiCode=00 000 000 000</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logData>
      <mnemonicList>ETIM,BS,CS,GR,TENS</mnemonicList>
      <unitList>ms,in,,gAPI,tonfUS</unitList>
      <data>820.2,7.875,0,42.3077,-0.9069109</data>
      <data>1640.4,7.875,0,33.3333,-0.9069109</data>
      <data>2460.6,7.875,0,38.4615,-0.9069109</data>
      <data>3280.8,7.875,0,25,-0.9069109</data>
    </logData>
    <commonData>
      <dTimCreation>2008-09-19T17:21:10-05:00</dTimCreation>
      <dTimLastChange>2009-08-26T17:12:32-05:00</dTimLastChange>
      <defaultDatum uidRef="18_KB">Kelly Bushing</defaultDatum>
    </commonData>
  </log>
</logs>
"""            
            
XML_LOG_1410_OK =  """<logs xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" version="1.4.1.0">
  <log uidWell="wellUid" uidWellbore="wellboreUid" uid="uid">
    <nameWell>DS Demo</nameWell>
    <nameWellbore>DS Demo</nameWellbore>
    <name>Downhole_Depth</name>
    <serviceCompany>Halliburton</serviceCompany>
    <indexType>measured depth</indexType>
    <startIndex uom="ft">1627</startIndex>
    <endIndex uom="ft">1634</endIndex>
    <stepIncrement uom="ft">1.00</stepIncrement>
    <direction>increasing</direction>
    <indexCurve>DEP</indexCurve>
    <logCurveInfo uid="DEP">
      <mnemonic namingSystem="DEP">DEP</mnemonic>
      <classWitsml>measured depth of hole</classWitsml>
      <unit>ft</unit>
      <mnemAlias namingSystem="Depth">Depth</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1634</maxIndex>
      <curveDescription>Depth</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="EWXT">
      <mnemonic namingSystem="EWXT">EWXT</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>min</unit>
      <mnemAlias namingSystem="EWXT">EWXT</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1634</maxIndex>
      <curveDescription>EWXT</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="R39P">
      <mnemonic namingSystem="R39P">R39P</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>ohm.m</unit>
      <mnemAlias namingSystem="R39P">R39P</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1634</maxIndex>
      <curveDescription>R39P</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="R15P">
      <mnemonic namingSystem="R15P">R15P</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>ohm.m</unit>
      <mnemAlias namingSystem="EWR Phase Res">EWR Phase Res</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1634</maxIndex>
      <curveDescription>EWR Phase Res</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="C39P">
      <mnemonic namingSystem="C39P">C39P</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>mmho/m</unit>
      <mnemAlias namingSystem="C39P">C39P</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1634</maxIndex>
      <curveDescription>C39P</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="DTEMP">
      <mnemonic namingSystem="DTEMP">DTEMP</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>degF</unit>
      <mnemAlias namingSystem="DTEMP">DTEMP</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1634</maxIndex>
      <curveDescription>DTEMP</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="DGRC">
      <mnemonic namingSystem="DGRC">DGRC</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>gAPI</unit>
      <mnemAlias namingSystem="DGRC">DGRC</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1634</maxIndex>
      <curveDescription>DGRC</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logData>
      <mnemonicList>DEP,EWXT,R39P,R15P,C39P,DTEMP,DGRC</mnemonicList>
      <unitList>ft,min,ohm.m,ohm.m,mmho/m,degF,gAPI</unitList>
      <data>1627,0,10,20,30,40,50</data>
      <data>1628,1,11,21,31,41,51</data>
      <data>1629,2,12,22,32,42,52</data>
      <data>1630,3,13,23,33,43,53</data>
      <data>1631,4,14,24,34,44,54</data>
      <data>1632,5,15,25,35,45,55</data>
      <data>1633,6,16,26,36,46,56</data>
      <data>1634,7,17,27,37,47,57</data>
    </logData>
    <commonData>
      <dTimLastChange>2012-10-04T13:21:46-05:00</dTimLastChange>
      <defaultDatum uidRef="DF">Derrick Floor</defaultDatum>
    </commonData>
  </log>
</logs>"""
                      

XML_LOG_HEADER_1410_OK =  """<logs xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" version="1.4.1.0">
  <log uidWell="wellUid" uidWellbore="wellboreUid" uid="uid">
    <nameWell>DS Demo</nameWell>
    <nameWellbore>DS Demo</nameWellbore>
    <name>Downhole_Depth</name>
    <serviceCompany>Halliburton</serviceCompany>
    <indexType>measured depth</indexType>
    <startIndex uom="ft">1627</startIndex>
    <endIndex uom="ft">1640</endIndex>
    <stepIncrement uom="ft">0</stepIncrement>
    <direction>increasing</direction>
    <indexCurve>DEP</indexCurve>
    <logCurveInfo uid="DEP">
      <mnemonic namingSystem="DEP">DEP</mnemonic>
      <classWitsml>measured depth of hole</classWitsml>
      <unit>ft</unit>
      <mnemAlias namingSystem="Depth">Depth</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1640</maxIndex>
      <curveDescription>Depth</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="EWXT">
      <mnemonic namingSystem="EWXT">EWXT</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>min</unit>
      <mnemAlias namingSystem="EWXT">EWXT</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1640</maxIndex>
      <curveDescription>EWXT</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="R39P">
      <mnemonic namingSystem="R39P">R39P</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>ohm.m</unit>
      <mnemAlias namingSystem="R39P">R39P</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1640</maxIndex>
      <curveDescription>R39P</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="R15P">
      <mnemonic namingSystem="R15P">R15P</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>ohm.m</unit>
      <mnemAlias namingSystem="EWR Phase Res">EWR Phase Res</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1640</maxIndex>
      <curveDescription>EWR Phase Res</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="C39P">
      <mnemonic namingSystem="C39P">C39P</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>mmho/m</unit>
      <mnemAlias namingSystem="C39P">C39P</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1640</maxIndex>
      <curveDescription>C39P</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="DTEMP">
      <mnemonic namingSystem="DTEMP">DTEMP</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>degF</unit>
      <mnemAlias namingSystem="DTEMP">DTEMP</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1640</maxIndex>
      <curveDescription>DTEMP</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="DGRC">
      <mnemonic namingSystem="DGRC">DGRC</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>gAPI</unit>
      <mnemAlias namingSystem="DGRC">DGRC</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1640</maxIndex>
      <curveDescription>DGRC</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <commonData>
      <dTimLastChange>2012-10-04T13:21:46-05:00</dTimLastChange>
      <defaultDatum uidRef="DF">Derrick Floor</defaultDatum>
    </commonData>
  </log>
</logs>"""

XML_LOG_1410_TIME_OK = """
<logs xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" version="1.4.1.0" xmlns="http://www.witsml.org/schemas/1series">
  <log uidWell="a872cd21-97ca-4cfd-8e17-d37fdf0760fe" uidWellbore="2e474c7d-fc7f-4e61-abbf-950f6afa38ca" uid="d2VsbEViYXNlZFpnbG9iYWxfcGR0WlRN">
    <nameWell>Realtime-Sim01</nameWell>
    <nameWellbore>Realtime-Sim01</nameWellbore>
    <name>Global_PDT_Time</name>
    <objectGrowing>false</objectGrowing>
    <serviceCompany>Halliburton</serviceCompany>
    <indexType>date time</indexType>
    <stepIncrement uom="Euc">0</stepIncrement>
    <startDateTimeIndex>2012-08-26T21:24:07-05:00</startDateTimeIndex>
    <endDateTimeIndex>2012-08-26T21:24:43-05:00</endDateTimeIndex>
    <direction>increasing</direction>
    <indexCurve>DateTime</indexCurve>
    <logCurveInfo uid="DateTime">
      <mnemonic namingSystem="DateTime">DateTime</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>s</unit>
      <mnemAlias namingSystem="Time &amp; Date">Time &amp; Date</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:43-05:00</maxDateTimeIndex>
      <curveDescription>Time &amp; Date</curveDescription>
      <typeLogData>date time</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="HDTVD">
      <mnemonic namingSystem="HDTVD">HDTVD</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>ft</unit>
      <mnemAlias namingSystem="Hole Depth TVD">Hole Depth TVD</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:43-05:00</maxDateTimeIndex>
      <curveDescription>Hole Depth TVD</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="HDEP">
      <mnemonic namingSystem="HDEP">HDEP</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>ft</unit>
      <mnemAlias namingSystem="Hole Depth">Hole Depth</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:43-05:00</maxDateTimeIndex>
      <curveDescription>Hole Depth</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="RSPD">
      <mnemonic namingSystem="RSPD">RSPD</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>ft/min</unit>
      <mnemAlias namingSystem="Running Speed">Running Speed</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:12-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:43-05:00</maxDateTimeIndex>
      <curveDescription>Running Speed</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="OBS">
      <mnemonic namingSystem="OBS">OBS</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>Unitless</unit>
      <mnemAlias namingSystem="On Btm Status">On Btm Status</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:12-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:43-05:00</maxDateTimeIndex>
      <curveDescription>On Btm Status</curveDescription>
      <typeLogData>string</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="BPOS">
      <mnemonic namingSystem="BPOS">BPOS</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>ft</unit>
      <mnemAlias namingSystem="Block Position">Block Position</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:43-05:00</maxDateTimeIndex>
      <curveDescription>Block Position</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="TVD">
      <mnemonic namingSystem="TVD">TVD</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>ft</unit>
      <mnemAlias namingSystem="TVD">TVD</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:43-05:00</maxDateTimeIndex>
      <curveDescription>TVD</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="DEPTH">
      <mnemonic namingSystem="DEPTH">DEPTH</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>ft</unit>
      <mnemAlias namingSystem="Depth">Depth</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:43-05:00</maxDateTimeIndex>
      <curveDescription>Depth</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="ISLS">
      <mnemonic namingSystem="ISLS">ISLS</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>Unitless</unit>
      <mnemAlias namingSystem="In Slips Status">In Slips Status</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:43-05:00</maxDateTimeIndex>
      <curveDescription>In Slips Status</curveDescription>
      <typeLogData>long</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="TDA">
      <mnemonic namingSystem="TDA">TDA</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>Unitless</unit>
      <mnemAlias namingSystem="T/D Activity">T/D Activity</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:43-05:00</maxDateTimeIndex>
      <curveDescription>T/D Activity</curveDescription>
      <typeLogData>string</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="ROPI">
      <mnemonic namingSystem="ROPI">ROPI</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>ft/h</unit>
      <mnemAlias namingSystem="ROP Inst">ROP Inst</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:38-05:00</maxDateTimeIndex>
      <curveDescription>ROP Inst</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logData>
      <mnemonicList>DateTime,HDTVD,HDEP,RSPD,OBS,BPOS,TVD,DEPTH,ISLS,TDA,ROPI</mnemonicList>
      <unitList>s,ft,ft,ft/min,Unitless,ft,ft,ft,Unitless,Unitless,ft/h</unitList>
      <data>2012-08-26T21:24:07-05:00,32.9999694824219,110,,,0,28.069995880127,105.069999694824,0,Trip In,60.0000038146973,</data>
      <data>2012-08-26T21:24:08-05:00,,,,,,,,,,60.0000038146973,</data>
      <data>2012-08-26T21:24:09-05:00,,,,,,,,,,,10.0084500014782</data>
      <data>2012-08-26T21:24:12-05:00,33.0337677001953,110.033798217773,58.7431983947754,On,39.9662017822266,33.0337715148926,110.033799999952,0,Drilling,,</data>
      <data>2012-08-26T21:24:17-05:00,33.0760192871094,110.076049804688,0.5,On,39.9239501953125,33.0760192871094,110.076050001383,0,Drilling,,</data>
      <data>2012-08-26T21:24:22-05:00,33.1182708740234,110.118301391602,0.5,On,39.8816986083984,33.1182708740234,110.118300000827,0,Drilling,,</data>
      <data>2012-08-26T21:24:27-05:00,33.1605224609375,110.160552978516,0.5,On,39.8394508361816,33.1605186462402,110.16055000027,0,Drilling,,</data>
      <data>2012-08-26T21:24:32-05:00,33.202766418457,110.202796936035,0.5,On,39.7971992492676,33.2027702331543,110.202800001701,0,Drilling,,</data>
      <data>2012-08-26T21:24:38-05:00,33.2450180053711,110.245048522949,0.5,On,39.7549514770508,33.2450180053711,110.245050001144,0,Drilling,60.0000038146973,</data>
      <data>2012-08-26T21:24:43-05:00,33.2872657775879,110.287300109863,0.5,On,39.7126998901367,33.2872657775879,110.287300000588,0,Drilling,,</data>
    </logData>
    <commonData>
      <dTimLastChange>2012-11-07T14:54:46-06:00</dTimLastChange>
      <defaultDatum uidRef="KB">Kelly Bushing</defaultDatum>
    </commonData>
  </log>
</logs>"""

XML_LOG_1410_ARRAY_OK =  """
<logs xmlns="http://www.witsml.org/schemas/1series" version="1.4.1.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.witsml.org/schemas/1series ..\Users\hbl4152\Downloads\witsml\witsml.1.4.1.RTM\data\witsml_v1.4.1_data\generated_write_schemas\obj_log.xsd">
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
            <maxIndex uom="m">508.01</maxIndex>
            <curveDescription>example of an array</curveDescription>
            <sensorOffset uom="m">0</sensorOffset>
            <traceState>raw</traceState>
            <typeLogData>double</typeLogData>
            <axisDefinition uid="axis1">
                <order>2</order>
                <count>3</count>
                <name>axis1</name>
                <propertyType>length</propertyType>
                <uom>ft</uom>                
                <doubleValues>1 2 3</doubleValues>
            </axisDefinition>
            <axisDefinition uid="axis2">
                <order>1</order>
                <count>2</count>
                <name>axis2</name>
                <propertyType>length</propertyType>
                <uom>ft</uom>
                <doubleValues>1 2</doubleValues>
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
            <data>509.01,508.75,,6.01</data>
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

XML_LOG_1410_UP_LOG_OK = """
<logs version="1.4.1.1" xmlns="http://www.witsml.org/schemas/1series">
  <log uidWell=" Test_Well" uidWellbore="MW_Up_Test_Wb" uid="L-10-50_Test">
    <nameWell> Test_Well</nameWell>
    <nameWellbore>MW Update Test Wellbore</nameWellbore>
    <name>Log 10 50</name>
    <objectGrowing>false</objectGrowing>
    <indexType>measured depth</indexType>
    <startIndex uom="ft">1000</startIndex>
    <endIndex uom="ft">972.3</endIndex>
    <direction>decreasing</direction>
    <indexCurve>Depth</indexCurve>
    <logCurveInfo>
      <mnemonic>Depth</mnemonic>
      <unit>ft</unit>
      <nullValue>-999.25</nullValue>
      <minIndex uom="ft">972.3</minIndex>
      <maxIndex uom="ft">1000</maxIndex>
      <curveDescription>measured depth index</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo>
      <mnemonic>ChannelA</mnemonic>
      <unit>psi</unit>
      <minIndex uom="ft">972.3</minIndex>
      <maxIndex uom="ft">998.3</maxIndex>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo>
      <mnemonic>ChannelB</mnemonic>
      <unit>klbf</unit>
      <minIndex uom="ft">973.3</minIndex>
      <maxIndex uom="ft">1000</maxIndex>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logData>
      <mnemonicList>Depth,ChannelA,ChannelB</mnemonicList>
      <unitList>ft,psi,klbf</unitList>
      <data>1000,,2</data>
      <data>999.3,,7</data>
      <data>998.3,11,12</data>
      <data>997.3,16,17</data>
      <data>996.3,21,22</data>
      <data>995.3,26,27</data>
      <data>994.3,31,32</data>
      <data>993.3,36,37</data>
      <data>992.3,41,42</data>
      <data>991.3,46,47</data>
      <data>990.3,51,52</data>
      <data>989.3,56,57</data>
      <data>988.3,61,62</data>
      <data>987.3,66,67</data>
      <data>986.3,71,72</data>
      <data>985.3,76,77</data>
      <data>984.3,81,82</data>
      <data>983.3,86,87</data>
      <data>982.3,91,92</data>
      <data>981.3,96,97</data>
      <data>980.3,101,102</data>
      <data>979.3,106,107</data>
      <data>978.3,111,112</data>
      <data>977.3,116,117</data>
      <data>976.3,121,122</data>
      <data>975.3,126,127</data>
      <data>974.3,131,132</data>
      <data>973.3,136,137</data>
      <data>972.3,141,</data>
    </logData>
  </log>
</logs>
"""

XML_LOG_HEADER_1410_TIME_OK =  """
<logs xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" version="1.4.1.0" xmlns="http://www.witsml.org/schemas/1series">
    <log uidWell="a872cd21-97ca-4cfd-8e17-d37fdf0760fe" uidWellbore="2e474c7d-fc7f-4e61-abbf-950f6afa38ca" uid="d2VsbEViYXNlZFpnbG9iYWxfcGR0WlRN">
        <nameWell>Realtime-Sim01</nameWell>
        <nameWellbore>Realtime-Sim01</nameWellbore>
        <name>Global_PDT_Time</name>
        <objectGrowing>false</objectGrowing>
        <serviceCompany>Halliburton</serviceCompany>
        <indexType>date time</indexType>
        <stepIncrement uom="Euc">0</stepIncrement>
        <startDateTimeIndex>2012-08-26T21:24:07-05:00</startDateTimeIndex>
        <endDateTimeIndex>2012-11-07T14:54:46-06:00</endDateTimeIndex>
        <direction>increasing</direction>
        <indexCurve>DateTime</indexCurve>
        <logCurveInfo uid="DateTime">
            <mnemonic namingSystem="DateTime">DateTime</mnemonic>
            <classWitsml>unknown</classWitsml>
            <unit>s</unit>
            <mnemAlias namingSystem="Time &amp; Date">Time &amp; Date</mnemAlias>
            <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
            <maxDateTimeIndex>2012-11-07T14:54:46-06:00</maxDateTimeIndex>
            <curveDescription>Time &amp; Date</curveDescription>
            <typeLogData>date time</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="HDTVD">
            <mnemonic namingSystem="HDTVD">HDTVD</mnemonic>
            <classWitsml>unknown</classWitsml>
            <unit>ft</unit>
            <mnemAlias namingSystem="Hole Depth TVD">Hole Depth TVD</mnemAlias>
            <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
            <maxDateTimeIndex>2012-11-07T14:54:46-06:00</maxDateTimeIndex>
            <curveDescription>Hole Depth TVD</curveDescription>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="HDEP">
            <mnemonic namingSystem="HDEP">HDEP</mnemonic>
            <classWitsml>unknown</classWitsml>
            <unit>ft</unit>
            <mnemAlias namingSystem="Hole Depth">Hole Depth</mnemAlias>
            <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
            <maxDateTimeIndex>2012-11-07T14:54:46-06:00</maxDateTimeIndex>
            <curveDescription>Hole Depth</curveDescription>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="RSPD">
            <mnemonic namingSystem="RSPD">RSPD</mnemonic>
            <classWitsml>unknown</classWitsml>
            <unit>ft/min</unit>
            <mnemAlias namingSystem="Running Speed">Running Speed</mnemAlias>
            <minDateTimeIndex>2012-08-26T21:24:12-05:00</minDateTimeIndex>
            <maxDateTimeIndex>2012-11-07T14:54:46-06:00</maxDateTimeIndex>
            <curveDescription>Running Speed</curveDescription>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="OBS">
            <mnemonic namingSystem="OBS">OBS</mnemonic>
            <classWitsml>unknown</classWitsml>
            <unit>Unitless</unit>
            <mnemAlias namingSystem="On Btm Status">On Btm Status</mnemAlias>
            <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
            <maxDateTimeIndex>2012-11-07T14:54:46-06:00</maxDateTimeIndex>
            <curveDescription>On Btm Status</curveDescription>
            <typeLogData>string</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="BPOS">
            <mnemonic namingSystem="BPOS">BPOS</mnemonic>
            <classWitsml>unknown</classWitsml>
            <unit>ft</unit>
            <mnemAlias namingSystem="Block Position">Block Position</mnemAlias>
            <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
            <maxDateTimeIndex>2012-11-07T14:54:46-06:00</maxDateTimeIndex>
            <curveDescription>Block Position</curveDescription>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="TVD">
            <mnemonic namingSystem="TVD">TVD</mnemonic>
            <classWitsml>unknown</classWitsml>
            <unit>ft</unit>
            <mnemAlias namingSystem="TVD">TVD</mnemAlias>
            <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
            <maxDateTimeIndex>2012-11-07T14:54:46-06:00</maxDateTimeIndex>
            <curveDescription>TVD</curveDescription>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="DEPTH">
            <mnemonic namingSystem="DEPTH">DEPTH</mnemonic>
            <classWitsml>unknown</classWitsml>
            <unit>ft</unit>
            <mnemAlias namingSystem="Depth">Depth</mnemAlias>
            <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
            <maxDateTimeIndex>2012-11-07T14:54:46-06:00</maxDateTimeIndex>
            <curveDescription>Depth</curveDescription>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="ISLS">
            <mnemonic namingSystem="ISLS">ISLS</mnemonic>
            <classWitsml>unknown</classWitsml>
            <unit>Unitless</unit>
            <mnemAlias namingSystem="In Slips Status">In Slips Status</mnemAlias>
            <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
            <maxDateTimeIndex>2012-11-07T14:54:46-06:00</maxDateTimeIndex>
            <curveDescription>In Slips Status</curveDescription>
            <typeLogData>long</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="TDA">
            <mnemonic namingSystem="TDA">TDA</mnemonic>
            <classWitsml>unknown</classWitsml>
            <unit>Unitless</unit>
            <mnemAlias namingSystem="T/D Activity">T/D Activity</mnemAlias>
            <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
            <maxDateTimeIndex>2012-11-07T14:54:46-06:00</maxDateTimeIndex>
            <curveDescription>T/D Activity</curveDescription>
            <typeLogData>string</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="ROPA">
            <mnemonic namingSystem="ROPA">ROPA</mnemonic>
            <classWitsml>unknown</classWitsml>
            <unit>ft/h</unit>
            <mnemAlias namingSystem="ROPA">ROPA</mnemAlias>
            <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
            <maxDateTimeIndex>2012-11-07T14:54:25-06:00</maxDateTimeIndex>
            <curveDescription>ROP Avg</curveDescription>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="ROPI">
            <mnemonic namingSystem="ROPI">ROPI</mnemonic>
            <classWitsml>unknown</classWitsml>
            <unit>ft/h</unit>
            <mnemAlias namingSystem="ROP Inst">ROP Inst</mnemAlias>
            <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
            <maxDateTimeIndex>2012-11-07T14:54:25-06:00</maxDateTimeIndex>
            <curveDescription>ROP Inst</curveDescription>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="DEP">
            <mnemonic namingSystem="DEP">DEP</mnemonic>
            <classWitsml>unknown</classWitsml>
            <unit>ft</unit>
            <mnemAlias namingSystem="Depth">Depth</mnemAlias>
            <minDateTimeIndex>2012-08-26T21:24:09-05:00</minDateTimeIndex>
            <maxDateTimeIndex>2012-11-07T14:54:44-06:00</maxDateTimeIndex>
            <curveDescription>Depth</curveDescription>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
    </log>
</logs>"""


XML_LOG_REQUESTLATEST_VALUE_1411_DEPTH_OK =  """
<logs version="1.4.1.1" xmlns="http://www.witsml.org/schemas/1series">
    <log uidWell="a872cd21-97ca-4cfd-8e17-d37fdf0760fe" uidWellbore="2e474c7d-fc7f-4e61-abbf-950f6afa38ca" uid="6f2d65ae-a7b9-4f7a-b477-002ff81ec3cc">
        <nameWell>Realtime-Sim01</nameWell>
        <nameWellbore>Realtime-Sim01</nameWellbore>
        <name>Global_PDT_Depth</name>
        <objectGrowing>false</objectGrowing>
        <serviceCompany>Halliburton</serviceCompany>
        <indexType>measured depth</indexType>
        <startIndex uom="ft">1</startIndex>
        <endIndex uom="ft">3</endIndex>
        <stepIncrement uom="ft">1</stepIncrement>
        <direction>increasing</direction>
        <indexCurve>DEP</indexCurve>
        <logCurveInfo uid="DEP">
            <mnemonic namingSystem="DEP">DEP</mnemonic>
            <classWitsml>measured depth of hole</classWitsml>
            <unit>ft</unit>
            <mnemAlias namingSystem="Depth">Depth</mnemAlias>
            <minIndex uom="ft">1</minIndex>
            <maxIndex uom="ft">3</maxIndex>
            <curveDescription>Depth</curveDescription>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="CURVE1">
            <mnemonic namingSystem="CURVE1">CURVE1</mnemonic>
            <classWitsml>unknown</classWitsml>
            <unit>ft/h</unit>
            <mnemAlias namingSystem="CURVE1">CURVE1</mnemAlias>
            <minIndex uom="ft">1</minIndex>
            <maxIndex uom="ft">1</maxIndex>
            <curveDescription>CURVE1</curveDescription>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="CURVE2">
            <mnemonic namingSystem="CURVE2">CURVE2</mnemonic>
            <classWitsml>unknown</classWitsml>
            <unit>ft/h</unit>
            <mnemAlias namingSystem="CURVE2">CURVE2</mnemAlias>
            <minIndex uom="ft">2</minIndex>
            <maxIndex uom="ft">2</maxIndex>
            <curveDescription>CURVE2</curveDescription>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="CURVE3">
            <mnemonic namingSystem="CURVE3">CURVE3</mnemonic>
            <classWitsml>unknown</classWitsml>
            <unit>ft/h</unit>
            <mnemAlias namingSystem="CURVE3">CURVE3</mnemAlias>
            <minIndex uom="ft">3</minIndex>
            <maxIndex uom="ft">3</maxIndex>
            <curveDescription>CURVE3</curveDescription>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logData>
            <mnemonicList>DEP,CURVE1,CURVE2,CURVE3</mnemonicList>
            <unitList>ft,ft/h,ft/h,ft/h</unitList>
            <data>1,10,,</data>
            <data>2,,100,</data>
            <data>3,,,1000</data>
        </logData>
        <commonData>
            <dTimLastChange>2012-11-07T16:54:46-06:00</dTimLastChange>
            <defaultDatum uidRef="KB">Kelly Bushing</defaultDatum>
        </commonData>
    </log>
</logs> 
"""

class LogVerifyest(unittest.TestCase, mocking.MockingTestMixin):
    
    logVerify = None
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        mocking.MockingTestMixin.setUp(self)

        wtl.script.Script.init()

        self.stub(wtl.control_prim, "fail")
        
        self.logVerify = wtl.store_prim.WITSMLServer.log_verify_object

        self.logVerify.setupFlag = False

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        mocking.MockingTestMixin.tearDown(self)
    
    def test_datum_defined(self):
        wtl.store_prim.WITSMLServer.xml_out.set("""
        <logs xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" version="1.4.1.0">
            <log uidWell="wellUid" uidWellbore="wellboreUid" uid="uid">
              <nameWell>DS Demo</nameWell>
              <nameWellbore>DS Demo</nameWellbore>
              <name>Downhole_Depth</name>
              <serviceCompany>Halliburton</serviceCompany>
              <indexType>measured depth</indexType>
              <startIndex uom="ft">1640</startIndex>
              <endIndex uom="ft">1640</endIndex>
              <stepIncrement uom="ft">0</stepIncrement>
              <direction>increasing</direction>   
              <indexCurve>DEP</indexCurve>
              <logCurveInfo uid="DEP">
                <mnemonic namingSystem="DEP">DEP</mnemonic>
                <classWitsml>measured depth of hole</classWitsml>
                <unit>ft</unit>
                <mnemAlias namingSystem="Depth">Depth</mnemAlias>
                <minIndex uom="ft">1627</minIndex>
                <maxIndex uom="ft">1640</maxIndex>
                <curveDescription>Depth</curveDescription>
                <typeLogData>double</typeLogData>
              </logCurveInfo>
              <logCurveInfo uid="EWXT">
                <mnemonic namingSystem="EWXT">EWXT</mnemonic>
                <classWitsml>unknown</classWitsml>
                <unit>min</unit>
                <mnemAlias namingSystem="EWXT">EWXT</mnemAlias>
                <minIndex uom="ft">1627</minIndex>
                <maxIndex uom="ft">1640</maxIndex>
                <curveDescription>EWXT</curveDescription>
                <typeLogData>double</typeLogData>
              </logCurveInfo>
                         
            </log>
        </logs>""")   
        self.logVerify._log_Datum_defined(True) 
        self.assertTrue(wtl.control_prim.fail.called) 
            
    def test_test_mnemonicsAreUnique(self):  
        wtl.store_prim.WITSMLServer.xml_out.set(XML_LOG_1410_OK)               
        self.logVerify._test_mnemonicsAreUnique(True) 
        self.assertFalse(wtl.control_prim.fail.called)  
      
    def test_test_mnemonicsAreUnique_Bad(self):   
        wtl.store_prim.WITSMLServer.xml_out.set("""
        <logs xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" version="1.4.1.0">
            <log uidWell="wellUid" uidWellbore="wellboreUid" uid="uid">
              <nameWell>DS Demo</nameWell>
              <nameWellbore>DS Demo</nameWellbore>
              <name>Downhole_Depth</name>
              <serviceCompany>Halliburton</serviceCompany>
              <indexType>measured depth</indexType>
              <startIndex uom="ft">1640</startIndex>
              <endIndex uom="ft">1640</endIndex>
              <stepIncrement uom="ft">0</stepIncrement>
              <direction>increasing</direction>   
              <indexCurve>DEP</indexCurve>
              <logCurveInfo uid="DEP">
              <mnemonic namingSystem="DEP">DEP</mnemonic>
              <classWitsml>measured depth of hole</classWitsml>
              <unit>ft</unit>
              <mnemAlias namingSystem="Depth">Depth</mnemAlias>
              <wellDatum uidRef="xx">yy</wellDatum>
              <minIndex uom="ft">1627</minIndex>
              <maxIndex uom="ft">1640</maxIndex>
              <curveDescription>Depth</curveDescription>
              <typeLogData>double</typeLogData>
              </logCurveInfo>
              <logCurveInfo uid="EWXT">
              <mnemonic namingSystem="EWXT">EWXT</mnemonic>
              <classWitsml>unknown</classWitsml>
              <unit>min</unit>
              <mnemAlias namingSystem="EWXT">EWXT</mnemAlias>
              <minIndex uom="ft">1627</minIndex>
              <maxIndex uom="ft">1640</maxIndex>
              <curveDescription>EWXT</curveDescription>
              <typeLogData>double</typeLogData>
              </logCurveInfo>
            <logData>
              <mnemonicList>DEP,EWXT,EWXT,R15P,C39P,DTEMP,DGRC</mnemonicList>
              <unitList>ft,min,ohm.m,ohm.m,mmho/m,degF,gAPI</unitList>
              <data>1627,0,10,20,30,40,50</data>
              <data>1628,1,11,21,31,41,51</data>
              <data>1628,2,12,22,32,42,52</data>
              <data>1631,3,13,23,33,43,53</data>
              <data>1636,4,14,24,34,44,54</data>
              <data>1636,5,15,25,35,45,55</data>
              <data>1637,6,16,26,36,46,56</data>
              <data>1640,7,17,27,37,47,57</data>
            </logData>
            <commonData>
              <dTimLastChange>2012-10-04T13:21:46-05:00</dTimLastChange>
              <defaultDatum uidRef="DF">Derrick Floor</defaultDatum>
            </commonData>       
            </log>
        </logs>""")   
        self.logVerify._test_mnemonicsAreUnique(True) 
        self.assertTrue(wtl.control_prim.fail.called)       
                    
    def test_start_end_index_depth_ok(self):
        wtl.store_prim.WITSMLServer.xml_out.set(XML_LOG_1410_OK)
        self.logVerify._log_validate_start_end_index_depth(True) 
        self.assertFalse(wtl.control_prim.fail.called)
   
    def test_start_end_index_depth_bad_1(self):
        wtl.store_prim.WITSMLServer.xml_out.set("""
        <logs xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" version="1.4.1.0">
            <log uidWell="wellUid" uidWellbore="wellboreUid" uid="uid">
              <nameWell>DS Demo</nameWell>
              <nameWellbore>DS Demo</nameWellbore>
              <name>Downhole_Depth</name>
              <serviceCompany>Halliburton</serviceCompany>
              <indexType>measured depth</indexType>
              <startIndex uom="ft">1640</startIndex>
              <endIndex uom="ft">1640</endIndex>
              <stepIncrement uom="ft">0</stepIncrement>
              <direction>increasing</direction>              
            </log>
        </logs>""")   
        self.logVerify._log_validate_start_end_index_depth(True) 
        self.assertFalse(wtl.control_prim.fail.called)
   
    def test_start_end_index_time_bad_1(self):
        # startIndex > endIndex
        wtl.store_prim.WITSMLServer.xml_out.set("""
<logs xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" version="1.4.1.0" xmlns="http://www.witsml.org/schemas/1series">
  <log uidWell="a872cd21-97ca-4cfd-8e17-d37fdf0760fe" uidWellbore="2e474c7d-fc7f-4e61-abbf-950f6afa38ca" uid="d2VsbEViYXNlZFpnbG9iYWxfcGR0WlRN">
    <nameWell>Realtime-Sim01</nameWell>
    <nameWellbore>Realtime-Sim01</nameWellbore>
    <name>Global_PDT_Time</name>
    <objectGrowing>false</objectGrowing>
    <serviceCompany>Halliburton</serviceCompany>
    <indexType>date time</indexType>
    <stepIncrement uom="Euc">0</stepIncrement>
    <startDateTimeIndex>2012-09-26T21:24:07-05:00</startDateTimeIndex>
    <endDateTimeIndex>2012-08-26T21:24:43-05:00</endDateTimeIndex>
    <direction>increasing</direction>
    <indexCurve>DateTime</indexCurve>
    <logCurveInfo uid="DateTime">
      <mnemonic namingSystem="DateTime">DateTime</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>s</unit>
      <mnemAlias namingSystem="Time &amp; Date">Time &amp; Date</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:43-05:00</maxDateTimeIndex>
      <curveDescription>Time &amp; Date</curveDescription>
      <typeLogData>date time</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="HDTVD">
      <mnemonic namingSystem="HDTVD">HDTVD</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>ft</unit>
      <mnemAlias namingSystem="Hole Depth TVD">Hole Depth TVD</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:43-05:00</maxDateTimeIndex>
      <curveDescription>Hole Depth TVD</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logData>
      <mnemonicList>DateTime,HDTVD</mnemonicList>
      <unitList>s,ft</unitList>
      <data>2012-08-26T21:24:07-05:00,32.9999694824219</data>
      <data>2012-08-26T21:24:08-05:00,</data>
      <data>2012-08-26T21:24:09-05:00,</data>
      <data>2012-08-26T21:24:12-05:00,33.0337677001953</data>
      <data>2012-08-26T21:24:17-05:00,33.0760192871094</data>
      <data>2012-08-26T21:24:22-05:00,33.1182708740234</data>
      <data>2012-08-26T21:24:27-05:00,33.1605224609375</data>
      <data>2012-08-26T21:24:32-05:00,33.202766418457</data>
      <data>2012-08-26T21:24:38-05:00,33.2450180053711</data>
      <data>2012-08-26T21:24:43-05:00,33.2872657775879</data>
    </logData>
    <commonData>
      <dTimLastChange>2012-11-07T14:54:46-06:00</dTimLastChange>
      <defaultDatum uidRef="KB">Kelly Bushing</defaultDatum>
    </commonData>
  </log>
</logs>""") 
        self.logVerify._log_validate_start_end_index_time(True) 
        self.assertTrue(wtl.control_prim.fail.called) 
   
    def test_start_end_index_time_bad_2(self):
        # last index != endIndex
        wtl.store_prim.WITSMLServer.xml_out.set("""
<logs xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" version="1.4.1.0" xmlns="http://www.witsml.org/schemas/1series">
  <log uidWell="a872cd21-97ca-4cfd-8e17-d37fdf0760fe" uidWellbore="2e474c7d-fc7f-4e61-abbf-950f6afa38ca" uid="d2VsbEViYXNlZFpnbG9iYWxfcGR0WlRN">
    <nameWell>Realtime-Sim01</nameWell>
    <nameWellbore>Realtime-Sim01</nameWellbore>
    <name>Global_PDT_Time</name>
    <objectGrowing>false</objectGrowing>
    <serviceCompany>Halliburton</serviceCompany>
    <indexType>date time</indexType>
    <stepIncrement uom="Euc">0</stepIncrement>
    <startDateTimeIndex>2012-08-26T21:24:07-05:00</startDateTimeIndex>
    <endDateTimeIndex>2012-08-26T21:24:43-05:00</endDateTimeIndex>
    <direction>increasing</direction>
    <indexCurve>DateTime</indexCurve>
    <logCurveInfo uid="DateTime">
      <mnemonic namingSystem="DateTime">DateTime</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>s</unit>
      <mnemAlias namingSystem="Time &amp; Date">Time &amp; Date</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:43-05:00</maxDateTimeIndex>
      <curveDescription>Time &amp; Date</curveDescription>
      <typeLogData>date time</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="HDTVD">
      <mnemonic namingSystem="HDTVD">HDTVD</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>ft</unit>
      <mnemAlias namingSystem="Hole Depth TVD">Hole Depth TVD</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:43-05:00</maxDateTimeIndex>
      <curveDescription>Hole Depth TVD</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logData>
      <mnemonicList>DateTime,HDTVD</mnemonicList>
      <unitList>s,ft</unitList>
      <data>2012-08-26T21:24:07-05:00,32.9999694824219</data>
      <data>2012-08-26T21:24:08-05:00,</data>
      <data>2012-08-26T21:24:09-05:00,</data>
      <data>2012-08-26T21:24:12-05:00,33.0337677001953</data>
      <data>2012-08-26T21:24:17-05:00,33.0760192871094</data>
      <data>2012-08-26T21:24:22-05:00,33.1182708740234</data>
      <data>2012-08-26T21:24:27-05:00,33.1605224609375</data>
      <data>2012-08-26T21:24:32-05:00,33.202766418457</data>
      <data>2012-08-26T21:24:38-05:00,33.2450180053711</data>
      <data>2012-09-26T21:24:43-05:00,33.2872657775879</data>
    </logData>
    <commonData>
      <dTimLastChange>2012-11-07T14:54:46-06:00</dTimLastChange>
      <defaultDatum uidRef="KB">Kelly Bushing</defaultDatum>
    </commonData>
  </log>
</logs>""") 
        self.logVerify._log_validate_start_end_index_time(True) 
        self.assertTrue(wtl.control_prim.fail.called)   
   
    def test_do_log_curve_info_mnemonics_match_mnemonicList_bad_1(self):
        # invalid mnemonic EWXT2
        wtl.store_prim.WITSMLServer.xml_out.set("""
              <logs xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" version="1.4.1.0">
              <log uidWell="wellUid" uidWellbore="wellboreUid" uid="uid">
                <nameWell>DS Demo</nameWell>
                <nameWellbore>DS Demo</nameWellbore>
                <name>Downhole_Depth</name>
                <serviceCompany>Halliburton</serviceCompany>
                <indexType>measured depth</indexType>
                <startIndex uom="ft">1627</startIndex>
                <endIndex uom="ft">1640</endIndex>
                <stepIncrement uom="ft">0</stepIncrement>
                <direction>increasing</direction>
                <indexCurve>DEP</indexCurve>
                <logCurveInfo uid="DEP">
                  <mnemonic namingSystem="DEP">DEP</mnemonic>
                  <classWitsml>measured depth of hole</classWitsml>
                  <unit>ft</unit>
                  <mnemAlias namingSystem="Depth">Depth</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>Depth</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="EWXT">
                  <mnemonic namingSystem="EWXT">EWXT2</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>min</unit>
                  <mnemAlias namingSystem="EWXT">EWXT</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>EWXT</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="R39P">
                  <mnemonic namingSystem="R39P">R39P</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>ohm.m</unit>
                  <mnemAlias namingSystem="R39P">R39P</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>R39P</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="R15P">
                  <mnemonic namingSystem="R15P">R15P</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>ohm.m</unit>
                  <mnemAlias namingSystem="EWR Phase Res">EWR Phase Res</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>EWR Phase Res</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="C39P">
                  <mnemonic namingSystem="C39P">C39P</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>mmho/m</unit>
                  <mnemAlias namingSystem="C39P">C39P</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>C39P</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="DTEMP">
                  <mnemonic namingSystem="DTEMP">DTEMP</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>degF</unit>
                  <mnemAlias namingSystem="DTEMP">DTEMP</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>DTEMP</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="DGRC">
                  <mnemonic namingSystem="DGRC">DGRC</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>gAPI</unit>
                  <mnemAlias namingSystem="DGRC">DGRC</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>DGRC</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logData>
                  <mnemonicList>DEP,EWXT,R39P,R15P,C39P,DTEMP,DGRC</mnemonicList>
                  <unitList>ft,min,ohm.m,ohm.m,mmho/m,degF,gAPI</unitList>
                  <data>1627,0,10,20,30,40,50</data>
                  <data>1628,1,11,21,31,41,51</data>
                  <data>1628,2,12,22,32,42,52</data>
                  <data>1631,3,13,23,33,43,53</data>
                  <data>1636,4,14,24,34,44,54</data>
                  <data>1636,5,15,25,35,45,55</data>
                  <data>1637,6,16,26,36,46,56</data>
                  <data>1640,7,17,27,37,47,57</data>
                </logData>
                <commonData>
                  <dTimLastChange>2012-10-04T13:21:46-05:00</dTimLastChange>
                  <defaultDatum uidRef="DF">Derrick Floor</defaultDatum>
                </commonData>
              </log>
            </logs>""")        
        self.logVerify._test_do_log_curve_info_mnemonics_match_mnemonicList(True)
        self.assertTrue(wtl.control_prim.fail.called)    
  
   
    def test_index_curve_bad(self):
        # no index curve defined
        wtl.store_prim.WITSMLServer.xml_out.set("""
              <logs xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" version="1.4.1.0">
              <log uidWell="wellUid" uidWellbore="wellboreUid" uid="uid">
                <nameWell>DS Demo</nameWell>
                <nameWellbore>DS Demo</nameWellbore>
                <name>Downhole_Depth</name>
                <serviceCompany>Halliburton</serviceCompany>
                <indexType>measured depth</indexType>
                <startIndex uom="ft">1627</startIndex>
                <endIndex uom="ft">1640</endIndex>
                <stepIncrement uom="ft">0</stepIncrement>
                <direction>increasing</direction>
                <!--<indexCurve>DEP</indexCurve>-->
                <logCurveInfo uid="DEP">
                  <mnemonic namingSystem="DEP">DEP</mnemonic>
                  <classWitsml>measured depth of hole</classWitsml>
                  <unit>ft</unit>
                  <mnemAlias namingSystem="Depth">Depth</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>Depth</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="EWXT">
                  <mnemonic namingSystem="EWXT">EWXT2</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>min</unit>
                  <mnemAlias namingSystem="EWXT">EWXT</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>EWXT</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="R39P">
                  <mnemonic namingSystem="R39P">R39P</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>ohm.m</unit>
                  <mnemAlias namingSystem="R39P">R39P</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>R39P</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="R15P">
                  <mnemonic namingSystem="R15P">R15P</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>ohm.m</unit>
                  <mnemAlias namingSystem="EWR Phase Res">EWR Phase Res</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>EWR Phase Res</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="C39P">
                  <mnemonic namingSystem="C39P">C39P</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>mmho/m</unit>
                  <mnemAlias namingSystem="C39P">C39P</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>C39P</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="DTEMP">
                  <mnemonic namingSystem="DTEMP">DTEMP</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>degF</unit>
                  <mnemAlias namingSystem="DTEMP">DTEMP</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>DTEMP</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="DGRC">
                  <mnemonic namingSystem="DGRC">DGRC</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>gAPI</unit>
                  <mnemAlias namingSystem="DGRC">DGRC</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>DGRC</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logData>
                  <mnemonicList>DEP,EWXT,R39P,R15P,C39P,DTEMP,DGRC</mnemonicList>
                  <unitList>ft,min,ohm.m,ohm.m,mmho/m,degF,gAPI</unitList>
                  <data>1627,0,10,20,30,40,50</data>
                  <data>1628,1,11,21,31,41,51</data>
                  <data>1628,2,12,22,32,42,52</data>
                  <data>1631,3,13,23,33,43,53</data>
                  <data>1636,4,14,24,34,44,54</data>
                  <data>1636,5,15,25,35,45,55</data>
                  <data>1637,6,16,26,36,46,56</data>
                  <data>1640,7,17,27,37,47,57</data>
                </logData>
                <commonData>
                  <dTimLastChange>2012-10-04T13:21:46-05:00</dTimLastChange>
                  <defaultDatum uidRef="DF">Derrick Floor</defaultDatum>
                </commonData>
              </log>
            </logs>""")        
        self.logVerify.test_index_curve(True) 
        self.assertTrue(wtl.control_prim.fail.called)           
  
    def test_index_curve_bad_2(self):  
        # index curve not in logCurveInfo
        wtl.store_prim.WITSMLServer.xml_out.set("""
              <logs xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" version="1.4.1.0">
              <log uidWell="wellUid" uidWellbore="wellboreUid" uid="uid">
                <nameWell>DS Demo</nameWell>
                <nameWellbore>DS Demo</nameWellbore>
                <name>Downhole_Depth</name>
                <serviceCompany>Halliburton</serviceCompany>
                <indexType>measured depth</indexType>
                <startIndex uom="ft">1627</startIndex>
                <endIndex uom="ft">1640</endIndex>
                <stepIncrement uom="ft">0</stepIncrement>
                <direction>increasing</direction>
                <indexCurve>DEP</indexCurve>
                <logCurveInfo uid="DEP">
                  <mnemonic namingSystem="DEP">DEP2</mnemonic>
                  <classWitsml>measured depth of hole</classWitsml>
                  <unit>ft</unit>
                  <mnemAlias namingSystem="Depth">Depth</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>Depth</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="EWXT">
                  <mnemonic namingSystem="EWXT">EWXT2</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>min</unit>
                  <mnemAlias namingSystem="EWXT">EWXT</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>EWXT</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="R39P">
                  <mnemonic namingSystem="R39P">R39P</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>ohm.m</unit>
                  <mnemAlias namingSystem="R39P">R39P</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>R39P</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="R15P">
                  <mnemonic namingSystem="R15P">R15P</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>ohm.m</unit>
                  <mnemAlias namingSystem="EWR Phase Res">EWR Phase Res</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>EWR Phase Res</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="C39P">
                  <mnemonic namingSystem="C39P">C39P</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>mmho/m</unit>
                  <mnemAlias namingSystem="C39P">C39P</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>C39P</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="DTEMP">
                  <mnemonic namingSystem="DTEMP">DTEMP</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>degF</unit>
                  <mnemAlias namingSystem="DTEMP">DTEMP</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>DTEMP</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="DGRC">
                  <mnemonic namingSystem="DGRC">DGRC</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>gAPI</unit>
                  <mnemAlias namingSystem="DGRC">DGRC</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>DGRC</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logData>
                  <mnemonicList>DEP,EWXT,R39P,R15P,C39P,DTEMP,DGRC</mnemonicList>
                  <unitList>ft,min,ohm.m,ohm.m,mmho/m,degF,gAPI</unitList>
                  <data>1627,0,10,20,30,40,50</data>
                  <data>1628,1,11,21,31,41,51</data>
                  <data>1628,2,12,22,32,42,52</data>
                  <data>1631,3,13,23,33,43,53</data>
                  <data>1636,4,14,24,34,44,54</data>
                  <data>1636,5,15,25,35,45,55</data>
                  <data>1637,6,16,26,36,46,56</data>
                  <data>1640,7,17,27,37,47,57</data>
                </logData>
                <commonData>
                  <dTimLastChange>2012-10-04T13:21:46-05:00</dTimLastChange>
                  <defaultDatum uidRef="DF">Derrick Floor</defaultDatum>
                </commonData>
              </log>
            </logs>""")        
        self.logVerify.test_index_curve(True) 
        self.assertTrue(wtl.control_prim.fail.called)            
  
    def test_index_curve_bad_3(self): 
        # index curve not in mnemonicList
        wtl.store_prim.WITSMLServer.xml_out.set("""
              <logs xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" version="1.4.1.0">
              <log uidWell="wellUid" uidWellbore="wellboreUid" uid="uid">
                <nameWell>DS Demo</nameWell>
                <nameWellbore>DS Demo</nameWellbore>
                <name>Downhole_Depth</name>
                <serviceCompany>Halliburton</serviceCompany>
                <indexType>measured depth</indexType>
                <startIndex uom="ft">1627</startIndex>
                <endIndex uom="ft">1640</endIndex>
                <stepIncrement uom="ft">0</stepIncrement>
                <direction>increasing</direction>
                <indexCurve>DEP</indexCurve>
                <logCurveInfo uid="DEP">
                  <mnemonic namingSystem="DEP">DEP</mnemonic>
                  <classWitsml>measured depth of hole</classWitsml>
                  <unit>ft</unit>
                  <mnemAlias namingSystem="Depth">Depth</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>Depth</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="EWXT">
                  <mnemonic namingSystem="EWXT">EWXT2</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>min</unit>
                  <mnemAlias namingSystem="EWXT">EWXT</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>EWXT</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="R39P">
                  <mnemonic namingSystem="R39P">R39P</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>ohm.m</unit>
                  <mnemAlias namingSystem="R39P">R39P</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>R39P</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="R15P">
                  <mnemonic namingSystem="R15P">R15P</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>ohm.m</unit>
                  <mnemAlias namingSystem="EWR Phase Res">EWR Phase Res</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>EWR Phase Res</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="C39P">
                  <mnemonic namingSystem="C39P">C39P</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>mmho/m</unit>
                  <mnemAlias namingSystem="C39P">C39P</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>C39P</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="DTEMP">
                  <mnemonic namingSystem="DTEMP">DTEMP</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>degF</unit>
                  <mnemAlias namingSystem="DTEMP">DTEMP</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>DTEMP</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="DGRC">
                  <mnemonic namingSystem="DGRC">DGRC</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>gAPI</unit>
                  <mnemAlias namingSystem="DGRC">DGRC</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>DGRC</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logData>
                  <mnemonicList>DEP2,EWXT,R39P,R15P,C39P,DTEMP,DGRC</mnemonicList>
                  <unitList>ft,min,ohm.m,ohm.m,mmho/m,degF,gAPI</unitList>
                  <data>1627,0,10,20,30,40,50</data>
                  <data>1628,1,11,21,31,41,51</data>
                  <data>1628,2,12,22,32,42,52</data>
                  <data>1631,3,13,23,33,43,53</data>
                  <data>1636,4,14,24,34,44,54</data>
                  <data>1636,5,15,25,35,45,55</data>
                  <data>1637,6,16,26,36,46,56</data>
                  <data>1640,7,17,27,37,47,57</data>
                </logData>
                <commonData>
                  <dTimLastChange>2012-10-04T13:21:46-05:00</dTimLastChange>
                  <defaultDatum uidRef="DF">Derrick Floor</defaultDatum>
                </commonData>
              </log>
            </logs>""")        
        self.logVerify.test_index_curve(True) 
        self.assertTrue(wtl.control_prim.fail.called)           
   
    def test_log_curve_info_min_max_depth_bad_1(self): 
        # depth index out of range.
        wtl.store_prim.WITSMLServer.xml_out.set("""
              <logs xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" version="1.4.1.0">
              <log uidWell="wellUid" uidWellbore="wellboreUid" uid="uid">
                <nameWell>DS Demo</nameWell>
                <nameWellbore>DS Demo</nameWellbore>
                <name>Downhole_Depth</name>
                <serviceCompany>Halliburton</serviceCompany>
                <indexType>measured depth</indexType>
                <startIndex uom="ft">1627</startIndex>
                <endIndex uom="ft">1640</endIndex>
                <stepIncrement uom="ft">0</stepIncrement>
                <direction>increasing</direction>
                <indexCurve>DEP</indexCurve>
                <logCurveInfo uid="DEP">
                  <mnemonic namingSystem="DEP">DEP</mnemonic>
                  <classWitsml>measured depth of hole</classWitsml>
                  <unit>ft</unit>
                  <mnemAlias namingSystem="Depth">Depth</mnemAlias>
                  <minIndex uom="ft">1626</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>Depth</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="EWXT">
                  <mnemonic namingSystem="EWXT">EWXT2</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>min</unit>
                  <mnemAlias namingSystem="EWXT">EWXT</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>EWXT</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="R39P">
                  <mnemonic namingSystem="R39P">R39P</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>ohm.m</unit>
                  <mnemAlias namingSystem="R39P">R39P</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>R39P</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="R15P">
                  <mnemonic namingSystem="R15P">R15P</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>ohm.m</unit>
                  <mnemAlias namingSystem="EWR Phase Res">EWR Phase Res</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>EWR Phase Res</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="C39P">
                  <mnemonic namingSystem="C39P">C39P</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>mmho/m</unit>
                  <mnemAlias namingSystem="C39P">C39P</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>C39P</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="DTEMP">
                  <mnemonic namingSystem="DTEMP">DTEMP</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>degF</unit>
                  <mnemAlias namingSystem="DTEMP">DTEMP</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>DTEMP</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="DGRC">
                  <mnemonic namingSystem="DGRC">DGRC</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>gAPI</unit>
                  <mnemAlias namingSystem="DGRC">DGRC</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>DGRC</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
              </log>
            </logs>""")        
        self.logVerify.test_log_curve_info_min_max_depth(True) 
        self.assertTrue(wtl.control_prim.fail.called)       
       
    def test_log_curve_info_min_max_time_bad_1(self):  
        # DateTime out of range.
        wtl.store_prim.WITSMLServer.xml_out.set("""
<logs xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" version="1.4.1.0" xmlns="http://www.witsml.org/schemas/1series">
  <log uidWell="a872cd21-97ca-4cfd-8e17-d37fdf0760fe" uidWellbore="2e474c7d-fc7f-4e61-abbf-950f6afa38ca" uid="d2VsbEViYXNlZFpnbG9iYWxfcGR0WlRN">
    <nameWell>Realtime-Sim01</nameWell>
    <nameWellbore>Realtime-Sim01</nameWellbore>
    <name>Global_PDT_Time</name>
    <objectGrowing>false</objectGrowing>
    <serviceCompany>Halliburton</serviceCompany>
    <indexType>date time</indexType>
    <stepIncrement uom="Euc">0</stepIncrement>
    <startDateTimeIndex>2012-08-26T21:24:07-05:00</startDateTimeIndex>
    <endDateTimeIndex>2012-08-26T21:24:43-05:00</endDateTimeIndex>
    <direction>increasing</direction>
    <indexCurve>DateTime</indexCurve>
    <logCurveInfo uid="DateTime">
      <mnemonic namingSystem="DateTime">DateTime</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>s</unit>
      <mnemAlias namingSystem="Time &amp; Date">Time &amp; Date</mnemAlias>
      <minDateTimeIndex>2012-09-26T21:24:07-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:43-05:00</maxDateTimeIndex>
      <curveDescription>Time &amp; Date</curveDescription>
      <typeLogData>date time</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="HDTVD">
      <mnemonic namingSystem="HDTVD">HDTVD</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>ft</unit>
      <mnemAlias namingSystem="Hole Depth TVD">Hole Depth TVD</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:43-05:00</maxDateTimeIndex>
      <curveDescription>Hole Depth TVD</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logData>
      <mnemonicList>DateTime,HDTVD</mnemonicList>
      <unitList>s,ft</unitList>
      <data>2012-08-26T21:24:07-05:00,32.9999694824219</data>
      <data>2012-08-26T21:24:08-05:00,</data>
      <data>2012-08-26T21:24:09-05:00,</data>
      <data>2012-08-26T21:24:12-05:00,33.0337677001953</data>
      <data>2012-08-26T21:24:17-05:00,33.0760192871094</data>
      <data>2012-08-26T21:24:22-05:00,33.1182708740234</data>
      <data>2012-08-26T21:24:27-05:00,33.1605224609375</data>
      <data>2012-08-26T21:24:32-05:00,33.202766418457</data>
      <data>2012-08-26T21:24:38-05:00,33.2450180053711</data>
      <data>2012-08-26T21:24:43-05:00,33.2872657775879</data>
    </logData>
    <commonData>
      <dTimLastChange>2012-11-07T14:54:46-06:00</dTimLastChange>
      <defaultDatum uidRef="KB">Kelly Bushing</defaultDatum>
    </commonData>
  </log>
</logs>""") 
        self.logVerify.test_log_curve_info_min_max_time(True)
        self.assertTrue(wtl.control_prim.fail.called)  
 
       
        
    def test_log_curve_info_min_max_depth_uom_bad1(self):   
        # R39P maxIndex uom different
        wtl.store_prim.WITSMLServer.xml_out.set("""
              <logs xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" version="1.4.1.0">
              <log uidWell="wellUid" uidWellbore="wellboreUid" uid="uid">
                <nameWell>DS Demo</nameWell>
                <nameWellbore>DS Demo</nameWellbore>
                <name>Downhole_Depth</name>
                <serviceCompany>Halliburton</serviceCompany>
                <indexType>measured depth</indexType>
                <startIndex uom="ft">1627</startIndex>
                <endIndex uom="ft">1640</endIndex>
                <stepIncrement uom="ft">0</stepIncrement>
                <direction>increasing</direction>
                <indexCurve>DEP</indexCurve>
                <logCurveInfo uid="DEP">
                  <mnemonic namingSystem="DEP">DEP</mnemonic>
                  <classWitsml>measured depth of hole</classWitsml>
                  <unit>ft</unit>
                  <mnemAlias namingSystem="Depth">Depth</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>Depth</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="EWXT">
                  <mnemonic namingSystem="EWXT">EWXT2</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>min</unit>
                  <mnemAlias namingSystem="EWXT">EWXT</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>EWXT</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="R39P">
                  <mnemonic namingSystem="R39P">R39P</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>ohm.m</unit>
                  <mnemAlias namingSystem="R39P">R39P</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="m">1640</maxIndex>
                  <curveDescription>R39P</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="R15P">
                  <mnemonic namingSystem="R15P">R15P</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>ohm.m</unit>
                  <mnemAlias namingSystem="EWR Phase Res">EWR Phase Res</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>EWR Phase Res</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="C39P">
                  <mnemonic namingSystem="C39P">C39P</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>mmho/m</unit>
                  <mnemAlias namingSystem="C39P">C39P</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>C39P</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="DTEMP">
                  <mnemonic namingSystem="DTEMP">DTEMP</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>degF</unit>
                  <mnemAlias namingSystem="DTEMP">DTEMP</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>DTEMP</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="DGRC">
                  <mnemonic namingSystem="DGRC">DGRC</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>gAPI</unit>
                  <mnemAlias namingSystem="DGRC">DGRC</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>DGRC</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
              </log>
            </logs>""")  
        self.logVerify.test_log_curve_info_min_max_depth_uom(True)
        self.assertTrue(wtl.control_prim.fail.called)          
                   
   
    def test_get_dataContainsCorrectNumberOfCurves_bad1(self):   
        # third data line has bad value for last curve, should be double, but its a string
        wtl.store_prim.WITSMLServer.xml_out.set("""
              <logs xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" version="1.4.1.0">
              <log uidWell="wellUid" uidWellbore="wellboreUid" uid="uid">
                <nameWell>DS Demo</nameWell>
                <nameWellbore>DS Demo</nameWellbore>
                <name>Downhole_Depth</name>
                <serviceCompany>Halliburton</serviceCompany>
                <indexType>measured depth</indexType>
                <startIndex uom="ft">1627</startIndex>
                <endIndex uom="ft">1640</endIndex>
                <stepIncrement uom="ft">0</stepIncrement>
                <direction>increasing</direction>
                <indexCurve>DEP</indexCurve>
                <logCurveInfo uid="DEP">
                  <mnemonic namingSystem="DEP">DEP</mnemonic>
                  <classWitsml>measured depth of hole</classWitsml>
                  <unit>ft</unit>
                  <mnemAlias namingSystem="Depth">Depth</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>Depth</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="EWXT">
                  <mnemonic namingSystem="EWXT">EWXT</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>min</unit>
                  <mnemAlias namingSystem="EWXT">EWXT</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>EWXT</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="R39P">
                  <mnemonic namingSystem="R39P">R39P</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>ohm.m</unit>
                  <mnemAlias namingSystem="R39P">R39P</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>R39P</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="R15P">
                  <mnemonic namingSystem="R15P">R15P</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>ohm.m</unit>
                  <mnemAlias namingSystem="EWR Phase Res">EWR Phase Res</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>EWR Phase Res</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="C39P">
                  <mnemonic namingSystem="C39P">C39P</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>mmho/m</unit>
                  <nullValue>-999.25</nullValue>
                  <mnemAlias namingSystem="C39P">C39P</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>C39P</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="DTEMP">
                  <mnemonic namingSystem="DTEMP">DTEMP</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>degF</unit>
                  <mnemAlias namingSystem="DTEMP">DTEMP</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>DTEMP</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="DGRC">
                  <mnemonic namingSystem="DGRC">DGRC</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>gAPI</unit>
                  <mnemAlias namingSystem="DGRC">DGRC</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>DGRC</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logData>
                  <mnemonicList>DEP,EWXT,R39P,R15P,C39P,DTEMP,DGRC</mnemonicList>
                  <unitList>ft,min,ohm.m,ohm.m,mmho/m,degF,gAPI</unitList>
                  <data>1627,0,10,20,-999.25,40,50</data>
                  <data>1628,1,11,21,31,41,51</data>
                  <data>1628,2,12,22,32,42,bill</data> <!-- bad -->
                  <data>1631,3,13,23,33,43,53</data>
                  <data>1636,4,14,24,34,44,54</data>
                  <data>1636,5,15,25,35,45,55</data>
                  <data>1637,6,16,26,36,46,56</data>
                  <data>1640,7,17,27,37,47,57</data>
                </logData>
                <commonData>
                  <dTimLastChange>2012-10-04T13:21:46-05:00</dTimLastChange>
                  <defaultDatum uidRef="DF">Derrick Floor</defaultDatum>
                </commonData>
              </log>
            </logs>""")        
        self.logVerify._test_get_dataContainsCorrectDataType(True) 
        self.assertTrue(wtl.control_prim.fail.called)          
        
       
           
    def test_get_direction_of_data_matches_header_depth_bad(self):          
        # third data line has bad value for last curve, should be double, but its a string
        wtl.store_prim.WITSMLServer.xml_out.set("""
              <logs xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" version="1.4.1.0">
              <log uidWell="wellUid" uidWellbore="wellboreUid" uid="uid">
                <nameWell>DS Demo</nameWell>
                <nameWellbore>DS Demo</nameWellbore>
                <name>Downhole_Depth</name>
                <serviceCompany>Halliburton</serviceCompany>
                <indexType>measured depth</indexType>
                <startIndex uom="ft">1627</startIndex>
                <endIndex uom="ft">1640</endIndex>
                <stepIncrement uom="ft">0</stepIncrement>
                <direction>increasing</direction>
                <indexCurve>DEP</indexCurve>
                <logCurveInfo uid="DEP">
                  <mnemonic namingSystem="DEP">DEP</mnemonic>
                  <classWitsml>measured depth of hole</classWitsml>
                  <unit>ft</unit>
                  <mnemAlias namingSystem="Depth">Depth</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>Depth</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="EWXT">
                  <mnemonic namingSystem="EWXT">EWXT</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>min</unit>
                  <mnemAlias namingSystem="EWXT">EWXT</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>EWXT</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="R39P">
                  <mnemonic namingSystem="R39P">R39P</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>ohm.m</unit>
                  <mnemAlias namingSystem="R39P">R39P</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>R39P</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="R15P">
                  <mnemonic namingSystem="R15P">R15P</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>ohm.m</unit>
                  <mnemAlias namingSystem="EWR Phase Res">EWR Phase Res</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>EWR Phase Res</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="C39P">
                  <mnemonic namingSystem="C39P">C39P</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>mmho/m</unit>
                  <mnemAlias namingSystem="C39P">C39P</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>C39P</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="DTEMP">
                  <mnemonic namingSystem="DTEMP">DTEMP</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>degF</unit>
                  <mnemAlias namingSystem="DTEMP">DTEMP</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>DTEMP</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logCurveInfo uid="DGRC">
                  <mnemonic namingSystem="DGRC">DGRC</mnemonic>
                  <classWitsml>unknown</classWitsml>
                  <unit>gAPI</unit>
                  <mnemAlias namingSystem="DGRC">DGRC</mnemAlias>
                  <minIndex uom="ft">1627</minIndex>
                  <maxIndex uom="ft">1640</maxIndex>
                  <curveDescription>DGRC</curveDescription>
                  <typeLogData>double</typeLogData>
                </logCurveInfo>
                <logData>
                  <mnemonicList>DEP,EWXT,R39P,R15P,C39P,DTEMP,DGRC</mnemonicList>
                  <unitList>ft,min,ohm.m,ohm.m,mmho/m,degF,gAPI</unitList>
                  <data>1627,0,10,20,30,40,50</data>
                  <data>1628,1,11,21,31,41,51</data>
                  <data>1628,2,12,22,32,42,52</data>
                  <data>1631,3,13,23,33,43,53</data>
                  <data>1636,4,14,24,34,44,54</data>
                  <data>1636,5,15,25,35,45,55</data>
                  <data>1637,6,16,26,36,46,56</data>
                  <data>1640,7,17,27,37,47,57</data>
                </logData>
                <commonData>
                  <dTimLastChange>2012-10-04T13:21:46-05:00</dTimLastChange>
                  <defaultDatum uidRef="DF">Derrick Floor</defaultDatum>
                </commonData>
              </log>
            </logs>""")        
        self.logVerify._test_get_direction_of_data_matches_header_depth(True) 
        self.assertTrue(wtl.control_prim.fail.called)         

           
    def test_log_curve_first_last_value_depth_bad_1(self):  
        # first data line has null value for C39P
        wtl.store_prim.WITSMLServer.xml_out.set(         
"""<logs xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" version="1.4.1.0">
  <log uidWell="wellUid" uidWellbore="wellboreUid" uid="uid">
    <nameWell>DS Demo</nameWell>
    <nameWellbore>DS Demo</nameWellbore>
    <name>Downhole_Depth</name>
    <serviceCompany>Halliburton</serviceCompany>
    <indexType>measured depth</indexType>
    <startIndex uom="ft">1627</startIndex>
    <endIndex uom="ft">1640</endIndex>
    <stepIncrement uom="ft">0</stepIncrement>
    <direction>increasing</direction>
    <indexCurve>DEP</indexCurve>
    <logCurveInfo uid="DEP">
      <mnemonic namingSystem="DEP">DEP</mnemonic>
      <classWitsml>measured depth of hole</classWitsml>
      <unit>ft</unit>
      <mnemAlias namingSystem="Depth">Depth</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1640</maxIndex>
      <curveDescription>Depth</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="EWXT">
      <mnemonic namingSystem="EWXT">EWXT</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>min</unit>
      <mnemAlias namingSystem="EWXT">EWXT</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1640</maxIndex>
      <curveDescription>EWXT</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="R39P">
      <mnemonic namingSystem="R39P">R39P</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>ohm.m</unit>
      <mnemAlias namingSystem="R39P">R39P</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1640</maxIndex>
      <curveDescription>R39P</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="R15P">
      <mnemonic namingSystem="R15P">R15P</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>ohm.m</unit>
      <mnemAlias namingSystem="EWR Phase Res">EWR Phase Res</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1640</maxIndex>
      <curveDescription>EWR Phase Res</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="C39P">
      <mnemonic namingSystem="C39P">C39P</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>mmho/m</unit>
      <mnemAlias namingSystem="C39P">C39P</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1640</maxIndex>
      <curveDescription>C39P</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="DTEMP">
      <mnemonic namingSystem="DTEMP">DTEMP</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>degF</unit>
      <mnemAlias namingSystem="DTEMP">DTEMP</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1640</maxIndex>
      <curveDescription>DTEMP</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="DGRC">
      <mnemonic namingSystem="DGRC">DGRC</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>gAPI</unit>
      <mnemAlias namingSystem="DGRC">DGRC</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1640</maxIndex>
      <curveDescription>DGRC</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logData>
      <mnemonicList>DEP,EWXT,R39P,R15P,C39P,DTEMP,DGRC</mnemonicList>
      <unitList>ft,min,ohm.m,ohm.m,mmho/m,degF,gAPI</unitList>
      <data>1627,0,10,20,,40,50</data>
      <data>1628,1,11,21,31,41,51</data>
      <data>1629,2,12,22,32,42,52</data>
      <data>1631,3,13,23,33,43,53</data>
      <data>1635,4,14,24,34,44,54</data>
      <data>1636,5,15,25,35,45,55</data>
      <data>1637,6,16,26,36,46,56</data>
      <data>1640,7,17,27,37,47,57</data>
    </logData>
    <commonData>
      <dTimLastChange>2012-10-04T13:21:46-05:00</dTimLastChange>
      <defaultDatum uidRef="DF">Derrick Floor</defaultDatum>
    </commonData>
  </log>
</logs>""")
        self.logVerify.test_log_curve_first_last_value_depth(True)
        self.assertTrue(wtl.control_prim.fail.called)           
             
           
    def test_log_curve_first_last_value_depth_bad_2(self):   
        # last data line has null value for DGRC
        wtl.store_prim.WITSMLServer.xml_out.set(         
"""<logs xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" version="1.4.1.0">
  <log uidWell="wellUid" uidWellbore="wellboreUid" uid="uid">
    <nameWell>DS Demo</nameWell>
    <nameWellbore>DS Demo</nameWellbore>
    <name>Downhole_Depth</name>
    <serviceCompany>Halliburton</serviceCompany>
    <indexType>measured depth</indexType>
    <startIndex uom="ft">1627</startIndex>
    <endIndex uom="ft">1640</endIndex>
    <stepIncrement uom="ft">0</stepIncrement>
    <direction>increasing</direction>
    <indexCurve>DEP</indexCurve>
    <logCurveInfo uid="DEP">
      <mnemonic namingSystem="DEP">DEP</mnemonic>
      <classWitsml>measured depth of hole</classWitsml>
      <unit>ft</unit>
      <mnemAlias namingSystem="Depth">Depth</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1640</maxIndex>
      <curveDescription>Depth</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="EWXT">
      <mnemonic namingSystem="EWXT">EWXT</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>min</unit>
      <mnemAlias namingSystem="EWXT">EWXT</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1640</maxIndex>
      <curveDescription>EWXT</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="R39P">
      <mnemonic namingSystem="R39P">R39P</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>ohm.m</unit>
      <mnemAlias namingSystem="R39P">R39P</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1640</maxIndex>
      <curveDescription>R39P</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="R15P">
      <mnemonic namingSystem="R15P">R15P</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>ohm.m</unit>
      <mnemAlias namingSystem="EWR Phase Res">EWR Phase Res</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1640</maxIndex>
      <curveDescription>EWR Phase Res</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="C39P">
      <mnemonic namingSystem="C39P">C39P</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>mmho/m</unit>
      <mnemAlias namingSystem="C39P">C39P</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1640</maxIndex>
      <curveDescription>C39P</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="DTEMP">
      <mnemonic namingSystem="DTEMP">DTEMP</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>degF</unit>
      <mnemAlias namingSystem="DTEMP">DTEMP</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1640</maxIndex>
      <curveDescription>DTEMP</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="DGRC">
      <mnemonic namingSystem="DGRC">DGRC</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>gAPI</unit>
      <mnemAlias namingSystem="DGRC">DGRC</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1640</maxIndex>
      <curveDescription>DGRC</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logData>
      <mnemonicList>DEP,EWXT,R39P,R15P,C39P,DTEMP,DGRC</mnemonicList>
      <unitList>ft,min,ohm.m,ohm.m,mmho/m,degF,gAPI</unitList>
      <data>1627,0,10,20,30,40,50</data>
      <data>1628,1,11,21,31,41,51</data>
      <data>1629,2,12,22,32,42,52</data>
      <data>1631,3,13,23,33,43,53</data>
      <data>1635,4,14,24,34,44,54</data>
      <data>1636,5,15,25,35,45,55</data>
      <data>1637,6,16,26,36,46,56</data>
      <data>1640,7,17,27,37,47,</data>
    </logData>
    <commonData>
      <dTimLastChange>2012-10-04T13:21:46-05:00</dTimLastChange>
      <defaultDatum uidRef="DF">Derrick Floor</defaultDatum>
    </commonData>
  </log>
</logs>""")
        self.logVerify.test_log_curve_first_last_value_depth(True) 
        self.assertTrue(wtl.control_prim.fail.called)           
             
        
    def test_log_curve_first_last_value_depth_bad_3(self): 
        # first data line has null value for C39P, with nullValue = -999.25 in curve header
        wtl.store_prim.WITSMLServer.xml_out.set(         
"""<logs xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" version="1.4.1.0">
  <log uidWell="wellUid" uidWellbore="wellboreUid" uid="uid">
    <nameWell>DS Demo</nameWell>
    <nameWellbore>DS Demo</nameWellbore>
    <name>Downhole_Depth</name>
    <serviceCompany>Halliburton</serviceCompany>
    <indexType>measured depth</indexType>
    <startIndex uom="ft">1627</startIndex>
    <endIndex uom="ft">1640</endIndex>
    <stepIncrement uom="ft">0</stepIncrement>
    <direction>increasing</direction>
    <indexCurve>DEP</indexCurve>
    <logCurveInfo uid="DEP">
      <mnemonic namingSystem="DEP">DEP</mnemonic>
      <classWitsml>measured depth of hole</classWitsml>
      <unit>ft</unit>
      <mnemAlias namingSystem="Depth">Depth</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1640</maxIndex>
      <curveDescription>Depth</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="EWXT">
      <mnemonic namingSystem="EWXT">EWXT</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>min</unit>
      <mnemAlias namingSystem="EWXT">EWXT</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1640</maxIndex>
      <curveDescription>EWXT</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="R39P">
      <mnemonic namingSystem="R39P">R39P</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>ohm.m</unit>
      <mnemAlias namingSystem="R39P">R39P</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1640</maxIndex>
      <curveDescription>R39P</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="R15P">
      <mnemonic namingSystem="R15P">R15P</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>ohm.m</unit>
      <mnemAlias namingSystem="EWR Phase Res">EWR Phase Res</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1640</maxIndex>
      <curveDescription>EWR Phase Res</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="C39P">
      <mnemonic namingSystem="C39P">C39P</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>mmho/m</unit>
      <nullValue>-999.25</nullValue>
      <mnemAlias namingSystem="C39P">C39P</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1640</maxIndex>
      <curveDescription>C39P</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="DTEMP">
      <mnemonic namingSystem="DTEMP">DTEMP</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>degF</unit>
      <mnemAlias namingSystem="DTEMP">DTEMP</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1640</maxIndex>
      <curveDescription>DTEMP</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="DGRC">
      <mnemonic namingSystem="DGRC">DGRC</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>gAPI</unit>
      <mnemAlias namingSystem="DGRC">DGRC</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1640</maxIndex>
      <curveDescription>DGRC</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logData>
      <mnemonicList>DEP,EWXT,R39P,R15P,C39P,DTEMP,DGRC</mnemonicList>
      <unitList>ft,min,ohm.m,ohm.m,mmho/m,degF,gAPI</unitList>
      <data>1627,0,10,20,-999.25,40,50</data>
      <data>1628,1,11,21,31,41,51</data>
      <data>1629,2,12,22,32,42,52</data>
      <data>1631,3,13,23,33,43,53</data>
      <data>1635,4,14,24,34,44,54</data>
      <data>1636,5,15,25,35,45,55</data>
      <data>1637,6,16,26,36,46,56</data>
      <data>1640,7,17,27,37,47,57</data>
    </logData>
    <commonData>
      <dTimLastChange>2012-10-04T13:21:46-05:00</dTimLastChange>
      <defaultDatum uidRef="DF">Derrick Floor</defaultDatum>
    </commonData>
  </log>
</logs>""")
        self.logVerify.test_log_curve_first_last_value_depth(True)
        self.assertTrue(wtl.control_prim.fail.called)           
              
       
    def test_log_curve_first_last_value_depth_bad_4(self):  
        # first data line has null value for C39P, with nullValue = -999.25 in log header
        wtl.store_prim.WITSMLServer.xml_out.set(         
"""<logs xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" version="1.4.1.0">
  <log uidWell="wellUid" uidWellbore="wellboreUid" uid="uid">
    <nameWell>DS Demo</nameWell>
    <nameWellbore>DS Demo</nameWellbore>
    <name>Downhole_Depth</name>
    <serviceCompany>Halliburton</serviceCompany>
    <indexType>measured depth</indexType>
    <startIndex uom="ft">1627</startIndex>
    <endIndex uom="ft">1640</endIndex>
    <stepIncrement uom="ft">0</stepIncrement>
    <direction>increasing</direction>
    <indexCurve>DEP</indexCurve>
    <nullValue>-999.25</nullValue>
    <logCurveInfo uid="DEP">
      <mnemonic namingSystem="DEP">DEP</mnemonic>
      <classWitsml>measured depth of hole</classWitsml>
      <unit>ft</unit>
      <mnemAlias namingSystem="Depth">Depth</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1640</maxIndex>
      <curveDescription>Depth</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="EWXT">
      <mnemonic namingSystem="EWXT">EWXT</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>min</unit>
      <mnemAlias namingSystem="EWXT">EWXT</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1640</maxIndex>
      <curveDescription>EWXT</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="R39P">
      <mnemonic namingSystem="R39P">R39P</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>ohm.m</unit>
      <mnemAlias namingSystem="R39P">R39P</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1640</maxIndex>
      <curveDescription>R39P</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="R15P">
      <mnemonic namingSystem="R15P">R15P</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>ohm.m</unit>
      <mnemAlias namingSystem="EWR Phase Res">EWR Phase Res</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1640</maxIndex>
      <curveDescription>EWR Phase Res</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="C39P">
      <mnemonic namingSystem="C39P">C39P</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>mmho/m</unit>
      <mnemAlias namingSystem="C39P">C39P</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1640</maxIndex>
      <curveDescription>C39P</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="DTEMP">
      <mnemonic namingSystem="DTEMP">DTEMP</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>degF</unit>
      <mnemAlias namingSystem="DTEMP">DTEMP</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1640</maxIndex>
      <curveDescription>DTEMP</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="DGRC">
      <mnemonic namingSystem="DGRC">DGRC</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>gAPI</unit>
      <mnemAlias namingSystem="DGRC">DGRC</mnemAlias>
      <minIndex uom="ft">1627</minIndex>
      <maxIndex uom="ft">1640</maxIndex>
      <curveDescription>DGRC</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logData>
      <mnemonicList>DEP,EWXT,R39P,R15P,C39P,DTEMP,DGRC</mnemonicList>
      <unitList>ft,min,ohm.m,ohm.m,mmho/m,degF,gAPI</unitList>
      <data>1627,0,10,20,-999.25,40,50</data>
      <data>1628,1,11,21,31,41,51</data>
      <data>1629,2,12,22,32,42,52</data>
      <data>1631,3,13,23,33,43,53</data>
      <data>1635,4,14,24,34,44,54</data>
      <data>1636,5,15,25,35,45,55</data>
      <data>1637,6,16,26,36,46,56</data>
      <data>1640,7,17,27,37,47,57</data>
    </logData>
    <commonData>
      <dTimLastChange>2012-10-04T13:21:46-05:00</dTimLastChange>
      <defaultDatum uidRef="DF">Derrick Floor</defaultDatum>
    </commonData>
  </log>
</logs>""")
        self.logVerify.test_log_curve_first_last_value_depth(True) 
        self.assertTrue(wtl.control_prim.fail.called)                         

           
    def test_log_curve_first_last_value_time_bad_1(self):  
        # last data line has null value for HDTVD
        wtl.store_prim.WITSMLServer.xml_out.set("""
<logs xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" version="1.4.1.0" xmlns="http://www.witsml.org/schemas/1series">
  <log uidWell="a872cd21-97ca-4cfd-8e17-d37fdf0760fe" uidWellbore="2e474c7d-fc7f-4e61-abbf-950f6afa38ca" uid="d2VsbEViYXNlZFpnbG9iYWxfcGR0WlRN">
    <nameWell>Realtime-Sim01</nameWell>
    <nameWellbore>Realtime-Sim01</nameWellbore>
    <name>Global_PDT_Time</name>
    <objectGrowing>false</objectGrowing>
    <serviceCompany>Halliburton</serviceCompany>
    <indexType>date time</indexType>
    <stepIncrement uom="Euc">0</stepIncrement>
    <startDateTimeIndex>2012-08-26T21:24:07-05:00</startDateTimeIndex>
    <endDateTimeIndex>2012-08-26T21:24:43-05:00</endDateTimeIndex>
    <direction>increasing</direction>
    <indexCurve>DateTime</indexCurve>
    <logCurveInfo uid="DateTime">
      <mnemonic namingSystem="DateTime">DateTime</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>s</unit>
      <mnemAlias namingSystem="Time &amp; Date">Time &amp; Date</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:43-05:00</maxDateTimeIndex>
      <curveDescription>Time &amp; Date</curveDescription>
      <typeLogData>date time</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="HDTVD">
      <mnemonic namingSystem="HDTVD">HDTVD</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>ft</unit>
      <mnemAlias namingSystem="Hole Depth TVD">Hole Depth TVD</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:43-05:00</maxDateTimeIndex>
      <curveDescription>Hole Depth TVD</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="HDEP">
      <mnemonic namingSystem="HDEP">HDEP</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>ft</unit>
      <mnemAlias namingSystem="Hole Depth">Hole Depth</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:43-05:00</maxDateTimeIndex>
      <curveDescription>Hole Depth</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="RSPD">
      <mnemonic namingSystem="RSPD">RSPD</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>ft/min</unit>
      <mnemAlias namingSystem="Running Speed">Running Speed</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:12-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:43-05:00</maxDateTimeIndex>
      <curveDescription>Running Speed</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="OBS">
      <mnemonic namingSystem="OBS">OBS</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>Unitless</unit>
      <mnemAlias namingSystem="On Btm Status">On Btm Status</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:43-05:00</maxDateTimeIndex>
      <curveDescription>On Btm Status</curveDescription>
      <typeLogData>string</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="BPOS">
      <mnemonic namingSystem="BPOS">BPOS</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>ft</unit>
      <mnemAlias namingSystem="Block Position">Block Position</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:43-05:00</maxDateTimeIndex>
      <curveDescription>Block Position</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="TVD">
      <mnemonic namingSystem="TVD">TVD</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>ft</unit>
      <mnemAlias namingSystem="TVD">TVD</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:43-05:00</maxDateTimeIndex>
      <curveDescription>TVD</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="DEPTH">
      <mnemonic namingSystem="DEPTH">DEPTH</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>ft</unit>
      <mnemAlias namingSystem="Depth">Depth</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:43-05:00</maxDateTimeIndex>
      <curveDescription>Depth</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="ISLS">
      <mnemonic namingSystem="ISLS">ISLS</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>Unitless</unit>
      <mnemAlias namingSystem="In Slips Status">In Slips Status</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:43-05:00</maxDateTimeIndex>
      <curveDescription>In Slips Status</curveDescription>
      <typeLogData>long</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="TDA">
      <mnemonic namingSystem="TDA">TDA</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>Unitless</unit>
      <mnemAlias namingSystem="T/D Activity">T/D Activity</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:43-05:00</maxDateTimeIndex>
      <curveDescription>T/D Activity</curveDescription>
      <typeLogData>string</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="ROPI">
      <mnemonic namingSystem="ROPI">ROPI</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>ft/h</unit>
      <mnemAlias namingSystem="ROP Inst">ROP Inst</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:38-05:00</maxDateTimeIndex>
      <curveDescription>ROP Inst</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logData>
      <mnemonicList>DateTime,HDTVD,HDEP,RSPD,OBS,BPOS,TVD,DEPTH,ISLS,TDA,ROPI</mnemonicList>
      <unitList>s,ft,ft,ft/min,Unitless,ft,ft,ft,Unitless,Unitless,ft/h</unitList>
      <data>2012-08-26T21:24:07-05:00,32.9999694824219,110,,Off,0,28.069995880127,105.069999694824,0,Trip In,60.0000038146973,</data>
      <data>2012-08-26T21:24:08-05:00,,,,,,,,,,60.0000038146973,</data>
      <data>2012-08-26T21:24:09-05:00,,,,,,,,,,,10.0084500014782</data>
      <data>2012-08-26T21:24:12-05:00,33.0337677001953,110.033798217773,58.7431983947754,On,39.9662017822266,33.0337715148926,110.033799999952,0,Drilling,,</data>
      <data>2012-08-26T21:24:17-05:00,33.0760192871094,110.076049804688,0.5,On,39.9239501953125,33.0760192871094,110.076050001383,0,Drilling,,</data>
      <data>2012-08-26T21:24:22-05:00,33.1182708740234,110.118301391602,0.5,On,39.8816986083984,33.1182708740234,110.118300000827,0,Drilling,,</data>
      <data>2012-08-26T21:24:27-05:00,33.1605224609375,110.160552978516,0.5,On,39.8394508361816,33.1605186462402,110.16055000027,0,Drilling,,</data>
      <data>2012-08-26T21:24:32-05:00,33.202766418457,110.202796936035,0.5,On,39.7971992492676,33.2027702331543,110.202800001701,0,Drilling,,</data>
      <data>2012-08-26T21:24:38-05:00,33.2450180053711,110.245048522949,0.5,On,39.7549514770508,33.2450180053711,110.245050001144,0,Drilling,60.0000038146973,</data>
      <data>2012-08-26T21:24:43-05:00,,110.287300109863,0.5,On,39.7126998901367,33.2872657775879,110.287300000588,0,Drilling,,</data>
    </logData>
    <commonData>
      <dTimLastChange>2012-11-07T14:54:46-06:00</dTimLastChange>
      <defaultDatum uidRef="KB">Kelly Bushing</defaultDatum>
    </commonData>
  </log>
</logs>""")
        self.logVerify.test_log_curve_first_last_value_time(True)   
        self.assertTrue(wtl.control_prim.fail.called)        
                                                            
 
    def test_log_curve_first_last_value_time_bad_2(self):   
        # last data line has curve null value for HDTVD
        wtl.store_prim.WITSMLServer.xml_out.set("""
<logs xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" version="1.4.1.0" xmlns="http://www.witsml.org/schemas/1series">
  <log uidWell="a872cd21-97ca-4cfd-8e17-d37fdf0760fe" uidWellbore="2e474c7d-fc7f-4e61-abbf-950f6afa38ca" uid="d2VsbEViYXNlZFpnbG9iYWxfcGR0WlRN">
    <nameWell>Realtime-Sim01</nameWell>
    <nameWellbore>Realtime-Sim01</nameWellbore>
    <name>Global_PDT_Time</name>
    <objectGrowing>false</objectGrowing>
    <serviceCompany>Halliburton</serviceCompany>
    <indexType>date time</indexType>
    <stepIncrement uom="Euc">0</stepIncrement>
    <startDateTimeIndex>2012-08-26T21:24:07-05:00</startDateTimeIndex>
    <endDateTimeIndex>2012-08-26T21:24:43-05:00</endDateTimeIndex>
    <direction>increasing</direction>
    <indexCurve>DateTime</indexCurve>
    <logCurveInfo uid="DateTime">
      <mnemonic namingSystem="DateTime">DateTime</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>s</unit>
      <mnemAlias namingSystem="Time &amp; Date">Time &amp; Date</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:43-05:00</maxDateTimeIndex>
      <curveDescription>Time &amp; Date</curveDescription>
      <typeLogData>date time</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="HDTVD">
      <mnemonic namingSystem="HDTVD">HDTVD</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>ft</unit>
      <nullValue>-999.25</nullValue>
      <mnemAlias namingSystem="Hole Depth TVD">Hole Depth TVD</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:43-05:00</maxDateTimeIndex>
      <curveDescription>Hole Depth TVD</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="HDEP">
      <mnemonic namingSystem="HDEP">HDEP</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>ft</unit>
      <mnemAlias namingSystem="Hole Depth">Hole Depth</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:43-05:00</maxDateTimeIndex>
      <curveDescription>Hole Depth</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="RSPD">
      <mnemonic namingSystem="RSPD">RSPD</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>ft/min</unit>
      <mnemAlias namingSystem="Running Speed">Running Speed</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:12-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:43-05:00</maxDateTimeIndex>
      <curveDescription>Running Speed</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="OBS">
      <mnemonic namingSystem="OBS">OBS</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>Unitless</unit>
      <mnemAlias namingSystem="On Btm Status">On Btm Status</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:43-05:00</maxDateTimeIndex>
      <curveDescription>On Btm Status</curveDescription>
      <typeLogData>string</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="BPOS">
      <mnemonic namingSystem="BPOS">BPOS</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>ft</unit>
      <mnemAlias namingSystem="Block Position">Block Position</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:43-05:00</maxDateTimeIndex>
      <curveDescription>Block Position</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="TVD">
      <mnemonic namingSystem="TVD">TVD</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>ft</unit>
      <mnemAlias namingSystem="TVD">TVD</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:43-05:00</maxDateTimeIndex>
      <curveDescription>TVD</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="DEPTH">
      <mnemonic namingSystem="DEPTH">DEPTH</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>ft</unit>
      <mnemAlias namingSystem="Depth">Depth</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:43-05:00</maxDateTimeIndex>
      <curveDescription>Depth</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="ISLS">
      <mnemonic namingSystem="ISLS">ISLS</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>Unitless</unit>
      <mnemAlias namingSystem="In Slips Status">In Slips Status</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:43-05:00</maxDateTimeIndex>
      <curveDescription>In Slips Status</curveDescription>
      <typeLogData>long</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="TDA">
      <mnemonic namingSystem="TDA">TDA</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>Unitless</unit>
      <mnemAlias namingSystem="T/D Activity">T/D Activity</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:43-05:00</maxDateTimeIndex>
      <curveDescription>T/D Activity</curveDescription>
      <typeLogData>string</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="ROPI">
      <mnemonic namingSystem="ROPI">ROPI</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>ft/h</unit>
      <mnemAlias namingSystem="ROP Inst">ROP Inst</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:07-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:38-05:00</maxDateTimeIndex>
      <curveDescription>ROP Inst</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logData>
      <mnemonicList>DateTime,HDTVD,HDEP,RSPD,OBS,BPOS,TVD,DEPTH,ISLS,TDA,ROPI</mnemonicList>
      <unitList>s,ft,ft,ft/min,Unitless,ft,ft,ft,Unitless,Unitless,ft/h</unitList>
      <data>2012-08-26T21:24:07-05:00,32.9999694824219,110,,Off,0,28.069995880127,105.069999694824,0,Trip In,60.0000038146973,</data>
      <data>2012-08-26T21:24:08-05:00,,,,,,,,,,60.0000038146973,</data>
      <data>2012-08-26T21:24:09-05:00,,,,,,,,,,,10.0084500014782</data>
      <data>2012-08-26T21:24:12-05:00,33.0337677001953,110.033798217773,58.7431983947754,On,39.9662017822266,33.0337715148926,110.033799999952,0,Drilling,,</data>
      <data>2012-08-26T21:24:17-05:00,33.0760192871094,110.076049804688,0.5,On,39.9239501953125,33.0760192871094,110.076050001383,0,Drilling,,</data>
      <data>2012-08-26T21:24:22-05:00,33.1182708740234,110.118301391602,0.5,On,39.8816986083984,33.1182708740234,110.118300000827,0,Drilling,,</data>
      <data>2012-08-26T21:24:27-05:00,33.1605224609375,110.160552978516,0.5,On,39.8394508361816,33.1605186462402,110.16055000027,0,Drilling,,</data>
      <data>2012-08-26T21:24:32-05:00,33.202766418457,110.202796936035,0.5,On,39.7971992492676,33.2027702331543,110.202800001701,0,Drilling,,</data>
      <data>2012-08-26T21:24:38-05:00,33.2450180053711,110.245048522949,0.5,On,39.7549514770508,33.2450180053711,110.245050001144,0,Drilling,60.0000038146973,</data>
      <data>2012-08-26T21:24:43-05:00,-999.25,110.287300109863,0.5,On,39.7126998901367,33.2872657775879,110.287300000588,0,Drilling,,</data>
    </logData>
    <commonData>
      <dTimLastChange>2012-11-07T14:54:46-06:00</dTimLastChange>
      <defaultDatum uidRef="KB">Kelly Bushing</defaultDatum>
    </commonData>
  </log>
</logs>""")
        self.logVerify.test_log_curve_first_last_value_time(True) 
        self.assertTrue(wtl.control_prim.fail.called)           
                                                         
           
           
    def test_full_log_depth_ok(self):
        wtl.store_prim.WITSMLServer.xml_out.set(XML_LOG_1410_OK)
        self.logVerify.test_full_log(verbose=True)  
        self.assertFalse(wtl.control_prim.fail.called)               
        
    def test_full_elpase_time_log_depth_ok(self):
        wtl.store_prim.WITSMLServer.xml_out.set(XML_ELAPSE_TIME_LOG_1410_OK)
        self.logVerify.test_full_log(verbose=True)  
        self.assertFalse(wtl.control_prim.fail.called)        
        
    def test_header_only_log_allowFailure_depth_ok(self):
        wtl.store_prim.WITSMLServer.xml_out.set(XML_LOG_HEADER_1410_OK)
        self.logVerify.test_header_only_log(verbose=True) 
        self.assertFalse(wtl.control_prim.fail.called)    
        
    def test_full_log_time_ok(self):
        wtl.store_prim.WITSMLServer.xml_out.set(XML_LOG_1410_TIME_OK)
        self.logVerify.test_full_log(verbose=True)
        self.assertFalse(wtl.control_prim.fail.called)           
                
    def test_full_log_up_log_ok(self):            
        wtl.store_prim.WITSMLServer.xml_out.set(XML_LOG_1410_UP_LOG_OK)
        self.logVerify.test_full_log(verbose=True)
        self.assertFalse(wtl.control_prim.fail.called)           
                
    def test_header_only_log_allowFailure_time_ok(self):
        wtl.store_prim.WITSMLServer.xml_out.set(XML_LOG_HEADER_1410_TIME_OK)
        self.logVerify.test_header_only_log(verbose=True) 
        self.assertFalse(wtl.control_prim.fail.called)                 
        
    def test_full_only_log_allowFailure_depth_array_ok(self):
        wtl.store_prim.WITSMLServer.xml_out.set(XML_LOG_1410_ARRAY_OK)
        self.logVerify.test_full_log(verbose=True) 
        self.assertFalse(wtl.control_prim.fail.called)          
    
    def test_log_curve_array_header(self):
        wtl.store_prim.WITSMLServer.xml_out.set(XML_LOG_1410_ARRAY_OK)        
        self.logVerify.test_log_curve_array_header(verbose=True)
        self.assertFalse(wtl.control_prim.fail.called)             
        
    def test_get_direction_of_data_matches_header_time(self): 
        wtl.store_prim.WITSMLServer.xml_out.set(XML_LOG_1410_TIME_OK)
        self.logVerify._test_get_direction_of_data_matches_header_time(verbose=True)
        self.assertFalse(wtl.control_prim.fail.called)            
        
    def test_uplog_with_absent_direction_bad(self):   
        # direction tag is missing which assume increasing log
        wtl.store_prim.WITSMLServer.xml_out.set("""
<logs version="1.4.1.1" xmlns="http://www.witsml.org/schemas/1series">
  <log uidWell=" Test_Well" uidWellbore="MW_Up_Test_Wb" uid="L-10-50_Test">
    <nameWell> Test_Well</nameWell>
    <nameWellbore>MW Update Test Wellbore</nameWellbore>
    <name>Log 10 50</name>
    <objectGrowing>false</objectGrowing>
    <indexType>measured depth</indexType>
    <startIndex uom="ft">1000</startIndex>
    <endIndex uom="ft">972.3</endIndex>
    <indexCurve>Depth</indexCurve>
    <logCurveInfo>
      <mnemonic>Depth</mnemonic>
      <unit>ft</unit>
      <nullValue>-999.25</nullValue>
      <minIndex uom="ft">972.3</minIndex>
      <maxIndex uom="ft">1000</maxIndex>
      <curveDescription>measured depth index</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo>
      <mnemonic>ChannelA</mnemonic>
      <unit>psi</unit>
      <minIndex uom="ft">972.3</minIndex>
      <maxIndex uom="ft">998.3</maxIndex>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo>
      <mnemonic>ChannelB</mnemonic>
      <unit>klbf</unit>
      <minIndex uom="ft">973.3</minIndex>
      <maxIndex uom="ft">1000</maxIndex>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logData>
      <mnemonicList>Depth,ChannelA,ChannelB</mnemonicList>
      <unitList>m,psi,klbf</unitList>
      <data>1000,,2</data>
      <data>999.3,,7</data>
      <data>998.3,11,12</data>
      <data>972.3,141,</data>
    </logData>
  </log>
</logs>        
        """)
        self.logVerify.test_full_log(verbose=True) 
        self.assertTrue(wtl.control_prim.fail.called)        
        
    def test_uplog_with_invalid_min_max_curve_indexes_bad(self):   
        # curve min and max index are suppose to be direction independent
        wtl.store_prim.WITSMLServer.xml_out.set("""
<logs version="1.4.1.1" xmlns="http://www.witsml.org/schemas/1series">
  <log uidWell=" Test_Well" uidWellbore="MW_Up_Test_Wb" uid="L-10-50_Test">
    <nameWell> Test_Well</nameWell>
    <nameWellbore>MW Update Test Wellbore</nameWellbore>
    <name>Log 10 50</name>
    <objectGrowing>false</objectGrowing>
    <indexType>measured depth</indexType>
    <startIndex uom="ft">1000</startIndex>
    <endIndex uom="ft">972.3</endIndex>
    <direction>decreasing</direction>    
    <indexCurve>Depth</indexCurve>
    <logCurveInfo>
      <mnemonic>Depth</mnemonic>
      <unit>ft</unit>
      <nullValue>-999.25</nullValue>
      <minIndex uom="ft">1000</minIndex>
      <maxIndex uom="ft">972.3</maxIndex>      
      <curveDescription>measured depth index</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo>
      <mnemonic>ChannelA</mnemonic>
      <unit>psi</unit>
      <minIndex uom="ft">998.3</minIndex>
      <maxIndex uom="ft">972.3</maxIndex>      
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo>
      <mnemonic>ChannelB</mnemonic>
      <unit>klbf</unit>
      <minIndex uom="ft">1000</minIndex>
      <maxIndex uom="ft">973.3</maxIndex>      
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logData>
      <mnemonicList>Depth,ChannelA,ChannelB</mnemonicList>
      <unitList>m,psi,klbf</unitList>
      <data>1000,,2</data>
      <data>999.3,,7</data>
      <data>998.3,11,12</data>
      <data>972.3,141,</data>
    </logData>
  </log>
</logs>        
        """)
        self.logVerify.test_full_log(verbose=True) 
        self.assertTrue(wtl.control_prim.fail.called)        
              
    def test_test_requestLatestValues_full_log(self): 
        wtl.store_prim.WITSMLServer.xml_out.set(XML_LOG_REQUESTLATEST_VALUE_1411_DEPTH_OK)
        self.logVerify.test_requestLatestValues_full_log()
        self.assertFalse(wtl.control_prim.fail.called)            
        
    # ok, all values on one row
    def test_test_requestLatestValues_full_log_2(self): 
        wtl.store_prim.WITSMLServer.xml_out.set("""
<logs version="1.4.1.1" xmlns="http://www.witsml.org/schemas/1series">
    <log uidWell="a872cd21-97ca-4cfd-8e17-d37fdf0760fe" uidWellbore="2e474c7d-fc7f-4e61-abbf-950f6afa38ca" uid="6f2d65ae-a7b9-4f7a-b477-002ff81ec3cc">
        <nameWell>Realtime-Sim01</nameWell>
        <nameWellbore>Realtime-Sim01</nameWellbore>
        <name>Global_PDT_Depth</name>
        <objectGrowing>false</objectGrowing>
        <serviceCompany>Halliburton</serviceCompany>
        <indexType>measured depth</indexType>
        <startIndex uom="ft">1</startIndex>
        <endIndex uom="ft">1</endIndex>
        <stepIncrement uom="ft">1</stepIncrement>
        <direction>increasing</direction>
        <indexCurve>DEP</indexCurve>
        <logCurveInfo uid="DEP">
            <mnemonic namingSystem="DEP">DEP</mnemonic>
            <classWitsml>measured depth of hole</classWitsml>
            <unit>ft</unit>
            <mnemAlias namingSystem="Depth">Depth</mnemAlias>
            <minIndex uom="ft">1</minIndex>
            <maxIndex uom="ft">1</maxIndex>
            <curveDescription>Depth</curveDescription>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="CURVE1">
            <mnemonic namingSystem="CURVE1">CURVE1</mnemonic>
            <classWitsml>unknown</classWitsml>
            <unit>ft/h</unit>
            <mnemAlias namingSystem="CURVE1">CURVE1</mnemAlias>
            <minIndex uom="ft">1</minIndex>
            <maxIndex uom="ft">1</maxIndex>
            <curveDescription>CURVE1</curveDescription>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="CURVE2">
            <mnemonic namingSystem="CURVE2">CURVE2</mnemonic>
            <classWitsml>unknown</classWitsml>
            <unit>ft/h</unit>
            <mnemAlias namingSystem="CURVE2">CURVE2</mnemAlias>
            <minIndex uom="ft">1</minIndex>
            <maxIndex uom="ft">1</maxIndex>
            <curveDescription>CURVE2</curveDescription>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="CURVE3">
            <mnemonic namingSystem="CURVE3">CURVE3</mnemonic>
            <classWitsml>unknown</classWitsml>
            <unit>ft/h</unit>
            <mnemAlias namingSystem="CURVE3">CURVE3</mnemAlias>
            <minIndex uom="ft">1</minIndex>
            <maxIndex uom="ft">1</maxIndex>
            <curveDescription>CURVE3</curveDescription>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logData>
            <mnemonicList>DEP,CURVE1,CURVE2,CURVE3</mnemonicList>
            <unitList>ft,ft/h,ft/h,ft/h</unitList>
            <data>1,10,100,1000</data>
        </logData>
        <commonData>
            <dTimLastChange>2012-11-07T16:54:46-06:00</dTimLastChange>
            <defaultDatum uidRef="KB">Kelly Bushing</defaultDatum>
        </commonData>
    </log>
</logs> 
""")
        self.logVerify.test_requestLatestValues_full_log(verbose=True)
        self.assertFalse(wtl.control_prim.fail.called)          

    # 3 values
    def test_test_requestLatestValues_full_log_3(self): 
        wtl.store_prim.WITSMLServer.xml_out.set("""
<logs version="1.4.1.1" xmlns="http://www.witsml.org/schemas/1series">
    <log uidWell="a872cd21-97ca-4cfd-8e17-d37fdf0760fe" uidWellbore="2e474c7d-fc7f-4e61-abbf-950f6afa38ca" uid="6f2d65ae-a7b9-4f7a-b477-002ff81ec3cc">
        <nameWell>Realtime-Sim01</nameWell>
        <nameWellbore>Realtime-Sim01</nameWellbore>
        <name>Global_PDT_Depth</name>
        <objectGrowing>false</objectGrowing>
        <serviceCompany>Halliburton</serviceCompany>
        <indexType>measured depth</indexType>
        <startIndex uom="ft">1</startIndex>
        <endIndex uom="ft">5</endIndex>
        <stepIncrement uom="ft">1</stepIncrement>
        <direction>increasing</direction>
        <indexCurve>DEP</indexCurve>
        <logCurveInfo uid="DEP">
            <mnemonic namingSystem="DEP">DEP</mnemonic>
            <classWitsml>measured depth of hole</classWitsml>
            <unit>ft</unit>
            <mnemAlias namingSystem="Depth">Depth</mnemAlias>
            <minIndex uom="ft">1</minIndex>
            <maxIndex uom="ft">5</maxIndex>
            <curveDescription>Depth</curveDescription>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="CURVE1">
            <mnemonic namingSystem="CURVE1">CURVE1</mnemonic>
            <classWitsml>unknown</classWitsml>
            <unit>ft/h</unit>
            <mnemAlias namingSystem="CURVE1">CURVE1</mnemAlias>
            <minIndex uom="ft">1</minIndex>
            <maxIndex uom="ft">3</maxIndex>
            <curveDescription>CURVE1</curveDescription>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="CURVE2">
            <mnemonic namingSystem="CURVE2">CURVE2</mnemonic>
            <classWitsml>unknown</classWitsml>
            <unit>ft/h</unit>
            <mnemAlias namingSystem="CURVE2">CURVE2</mnemAlias>
            <minIndex uom="ft">3</minIndex>
            <maxIndex uom="ft">5</maxIndex>
            <curveDescription>CURVE2</curveDescription>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="CURVE3">
            <mnemonic namingSystem="CURVE3">CURVE3</mnemonic>
            <classWitsml>unknown</classWitsml>
            <unit>ft/h</unit>
            <mnemAlias namingSystem="CURVE3">CURVE3</mnemAlias>
            <minIndex uom="ft">2</minIndex>
            <maxIndex uom="ft">4</maxIndex>
            <curveDescription>CURVE3</curveDescription>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logData>
            <mnemonicList>DEP,CURVE1,CURVE2,CURVE3</mnemonicList>
            <unitList>ft,ft/h,ft/h,ft/h</unitList>
            <data>1,10,,</data>
            <data>2,11,,1000</data>
            <data>3,12,100,1001</data>
            <data>4,,101,1002</data>
            <data>5,,102,</data>                                                
        </logData>
        <commonData>
            <dTimLastChange>2012-11-07T16:54:46-06:00</dTimLastChange>
            <defaultDatum uidRef="KB">Kelly Bushing</defaultDatum>
        </commonData>
    </log>
</logs> 
""")
        self.logVerify.test_requestLatestValues_full_log(numberOfExpectedValues=3,verbose=True)
        self.assertFalse(wtl.control_prim.fail.called)          

    # 3 values, CURVE2 has 4 values
    def test_test_requestLatestValues_full_log_bad(self): 
        wtl.store_prim.WITSMLServer.xml_out.set("""
<logs version="1.4.1.1" xmlns="http://www.witsml.org/schemas/1series">
    <log uidWell="a872cd21-97ca-4cfd-8e17-d37fdf0760fe" uidWellbore="2e474c7d-fc7f-4e61-abbf-950f6afa38ca" uid="6f2d65ae-a7b9-4f7a-b477-002ff81ec3cc">
        <nameWell>Realtime-Sim01</nameWell>
        <nameWellbore>Realtime-Sim01</nameWellbore>
        <name>Global_PDT_Depth</name>
        <objectGrowing>false</objectGrowing>
        <serviceCompany>Halliburton</serviceCompany>
        <indexType>measured depth</indexType>
        <startIndex uom="ft">1</startIndex>
        <endIndex uom="ft">5</endIndex>
        <stepIncrement uom="ft">1</stepIncrement>
        <direction>increasing</direction>
        <indexCurve>DEP</indexCurve>
        <logCurveInfo uid="DEP">
            <mnemonic namingSystem="DEP">DEP</mnemonic>
            <classWitsml>measured depth of hole</classWitsml>
            <unit>ft</unit>
            <mnemAlias namingSystem="Depth">Depth</mnemAlias>
            <minIndex uom="ft">1</minIndex>
            <maxIndex uom="ft">5</maxIndex>
            <curveDescription>Depth</curveDescription>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="CURVE1">
            <mnemonic namingSystem="CURVE1">CURVE1</mnemonic>
            <classWitsml>unknown</classWitsml>
            <unit>ft/h</unit>
            <mnemAlias namingSystem="CURVE1">CURVE1</mnemAlias>
            <minIndex uom="ft">1</minIndex>
            <maxIndex uom="ft">3</maxIndex>
            <curveDescription>CURVE1</curveDescription>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="CURVE2">
            <mnemonic namingSystem="CURVE2">CURVE2</mnemonic>
            <classWitsml>unknown</classWitsml>
            <unit>ft/h</unit>
            <mnemAlias namingSystem="CURVE2">CURVE2</mnemAlias>
            <minIndex uom="ft">2</minIndex>
            <maxIndex uom="ft">5</maxIndex>
            <curveDescription>CURVE2</curveDescription>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="CURVE3">
            <mnemonic namingSystem="CURVE3">CURVE3</mnemonic>
            <classWitsml>unknown</classWitsml>
            <unit>ft/h</unit>
            <mnemAlias namingSystem="CURVE3">CURVE3</mnemAlias>
            <minIndex uom="ft">2</minIndex>
            <maxIndex uom="ft">4</maxIndex>
            <curveDescription>CURVE3</curveDescription>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logData>
            <mnemonicList>DEP,CURVE1,CURVE2,CURVE3</mnemonicList>
            <unitList>ft,ft/h,ft/h,ft/h</unitList>
            <data>1,10,,</data>
            <data>2,11,99,1000</data>
            <data>3,12,100,1001</data>
            <data>4,,101,1002</data>
            <data>5,,102,</data>                                                
        </logData>
        <commonData>
            <dTimLastChange>2012-11-07T16:54:46-06:00</dTimLastChange>
            <defaultDatum uidRef="KB">Kelly Bushing</defaultDatum>
        </commonData>
    </log>
</logs> 
""")        
        self.logVerify.test_requestLatestValues_full_log(numberOfExpectedValues=3,verbose=True)
        self.assertTrue(wtl.control_prim.fail.called)   
    
    # 1 values, 3 curves, should not have 5 rows
    def test_test_requestLatestValues_full_log_bad_maxRows(self): 
        wtl.store_prim.WITSMLServer.xml_out.set("""
<logs version="1.4.1.1" xmlns="http://www.witsml.org/schemas/1series">
    <log uidWell="a872cd21-97ca-4cfd-8e17-d37fdf0760fe" uidWellbore="2e474c7d-fc7f-4e61-abbf-950f6afa38ca" uid="6f2d65ae-a7b9-4f7a-b477-002ff81ec3cc">
        <nameWell>Realtime-Sim01</nameWell>
        <nameWellbore>Realtime-Sim01</nameWellbore>
        <name>Global_PDT_Depth</name>
        <objectGrowing>false</objectGrowing>
        <serviceCompany>Halliburton</serviceCompany>
        <indexType>measured depth</indexType>
        <startIndex uom="ft">1</startIndex>
        <endIndex uom="ft">5</endIndex>
        <stepIncrement uom="ft">1</stepIncrement>
        <direction>increasing</direction>
        <indexCurve>DEP</indexCurve>
        <logCurveInfo uid="DEP">
            <mnemonic namingSystem="DEP">DEP</mnemonic>
            <classWitsml>measured depth of hole</classWitsml>
            <unit>ft</unit>
            <mnemAlias namingSystem="Depth">Depth</mnemAlias>
            <minIndex uom="ft">1</minIndex>
            <maxIndex uom="ft">5</maxIndex>
            <curveDescription>Depth</curveDescription>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="CURVE1">
            <mnemonic namingSystem="CURVE1">CURVE1</mnemonic>
            <classWitsml>unknown</classWitsml>
            <unit>ft/h</unit>
            <mnemAlias namingSystem="CURVE1">CURVE1</mnemAlias>
            <minIndex uom="ft">1</minIndex>
            <maxIndex uom="ft">3</maxIndex>
            <curveDescription>CURVE1</curveDescription>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="CURVE2">
            <mnemonic namingSystem="CURVE2">CURVE2</mnemonic>
            <classWitsml>unknown</classWitsml>
            <unit>ft/h</unit>
            <mnemAlias namingSystem="CURVE2">CURVE2</mnemAlias>
            <minIndex uom="ft">2</minIndex>
            <maxIndex uom="ft">5</maxIndex>
            <curveDescription>CURVE2</curveDescription>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="CURVE3">
            <mnemonic namingSystem="CURVE3">CURVE3</mnemonic>
            <classWitsml>unknown</classWitsml>
            <unit>ft/h</unit>
            <mnemAlias namingSystem="CURVE3">CURVE3</mnemAlias>
            <minIndex uom="ft">2</minIndex>
            <maxIndex uom="ft">4</maxIndex>
            <curveDescription>CURVE3</curveDescription>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logData>
            <mnemonicList>DEP,CURVE1,CURVE2,CURVE3</mnemonicList>
            <unitList>ft,ft/h,ft/h,ft/h</unitList>
            <data>1,10,,</data>
            <data>2,11,99,1000</data>
            <data>3,12,100,1001</data>
            <data>4,,101,1002</data>
            <data>5,,102,</data>                                                
        </logData>
        <commonData>
            <dTimLastChange>2012-11-07T16:54:46-06:00</dTimLastChange>
            <defaultDatum uidRef="KB">Kelly Bushing</defaultDatum>
        </commonData>
    </log>
</logs> 
""")        
        self.logVerify.test_requestLatestValues_full_log(numberOfExpectedValues=1,verbose=True)
        self.assertTrue(wtl.control_prim.fail.called)   
    
    
    # 1 values, time
    def test_test_requestLatestValues_full_log_time(self): 
        wtl.store_prim.WITSMLServer.xml_out.set("""        
<logs xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" version="1.4.1.1" xmlns="http://www.witsml.org/schemas/1series">
    <log uidWell="a872cd21-97ca-4cfd-8e17-d37fdf0760fe" uidWellbore="2e474c7d-fc7f-4e61-abbf-950f6afa38ca" uid="6350971f-ebfc-4307-8161-2637a57cdbb0">
        <nameWell>Realtime-Sim01</nameWell>
        <nameWellbore>Realtime-Sim01</nameWellbore>
        <name>Global_PDT_Time</name>
        <objectGrowing>false</objectGrowing>
        <serviceCompany>Halliburton</serviceCompany>
        <indexType>date time</indexType>
        <stepIncrement uom="Euc">0</stepIncrement>
        <startDateTimeIndex>2012-11-07T16:54:44-05:00</startDateTimeIndex>
        <endDateTimeIndex>2012-11-07T16:54:44-05:00</endDateTimeIndex>
        <direction>increasing</direction>
        <indexCurve>DateTime</indexCurve>
        <logCurveInfo uid="DateTime">
            <mnemonic namingSystem="DateTime">DateTime</mnemonic>
            <classWitsml>unknown</classWitsml>
            <unit>s</unit>
            <mnemAlias namingSystem="Time &amp; Date">Time &amp; Date</mnemAlias>
            <minDateTimeIndex>2012-11-07T16:54:44-05:00</minDateTimeIndex>
            <maxDateTimeIndex>2012-11-07T16:54:44-05:00</maxDateTimeIndex>
            <curveDescription>Time &amp; Date</curveDescription>
            <typeLogData>date time</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="DEP">
            <mnemonic namingSystem="DEP">DEP</mnemonic>
            <classWitsml>unknown</classWitsml>
            <unit>ft</unit>
            <mnemAlias namingSystem="Depth">Depth</mnemAlias>
            <minDateTimeIndex>2012-11-07T16:54:44-05:00</minDateTimeIndex>
            <maxDateTimeIndex>2012-11-07T16:54:44-05:00</maxDateTimeIndex>
            <curveDescription>Depth</curveDescription>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="Gas-Total-Avg">
            <mnemonic namingSystem="Gas Total Avg">Gas Total Avg</mnemonic>
            <classWitsml>unknown</classWitsml>
            <unit>unit</unit>
            <mnemAlias namingSystem="Gas Hydrcbn Avg">Gas Hydrcbn Avg</mnemAlias>
            <minDateTimeIndex>2012-11-07T16:54:44-05:00</minDateTimeIndex>
            <maxDateTimeIndex>2012-11-07T16:54:44-05:00</maxDateTimeIndex>
            <curveDescription>Gas Hydrcbn Avg</curveDescription>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logData>
            <mnemonicList>DateTime,DEP,Gas Total Avg</mnemonicList>
            <unitList>s,ft,unit</unitList>
            <data>2012-11-07T16:54:44-05:00,42216.4460912929,1</data>
        </logData>
        <commonData>
            <dTimLastChange>2012-11-07T16:54:46-06:00</dTimLastChange>
            <defaultDatum uidRef="KB">Kelly Bushing</defaultDatum>
        </commonData>
    </log>
</logs> 
""")
        self.logVerify.test_requestLatestValues_full_log(numberOfExpectedValues=1,verbose=True)
        self.assertFalse(wtl.control_prim.fail.called)          
      
    def test_decreasing_time_log(self):   
        wtl.store_prim.WITSMLServer.xml_out.set("""        
<logs xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" version="1.4.1.0" xmlns="http://www.witsml.org/schemas/1series">
  <log uidWell="a872cd21-97ca-4cfd-8e17-d37fdf0760fe" uidWellbore="2e474c7d-fc7f-4e61-abbf-950f6afa38ca" uid="d2VsbEViYXNlZFpnbG9iYWxfcGR0WlRN">
    <nameWell>Realtime-Sim01</nameWell>
    <nameWellbore>Realtime-Sim01</nameWellbore>
    <name>Global_PDT_Time</name>
    <objectGrowing>false</objectGrowing>
    <serviceCompany>Halliburton</serviceCompany>
    <indexType>date time</indexType>
    <stepIncrement uom="Euc">0</stepIncrement>
    <startDateTimeIndex>2012-08-26T21:24:43-05:00</startDateTimeIndex>
    <endDateTimeIndex>2012-08-26T21:24:22-05:00</endDateTimeIndex>
    <direction>decreasing</direction>
    <indexCurve>DateTime</indexCurve>
    <logCurveInfo uid="DateTime">
      <mnemonic namingSystem="DateTime">DateTime</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>s</unit>
      <mnemAlias namingSystem="Time &amp; Date">Time &amp; Date</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:22-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:43-05:00</maxDateTimeIndex>
      <curveDescription>Time &amp; Date</curveDescription>
      <typeLogData>date time</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="HDTVD">
      <mnemonic namingSystem="HDTVD">HDTVD</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>ft</unit>
      <mnemAlias namingSystem="Hole Depth TVD">Hole Depth TVD</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:22-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:43-05:00</maxDateTimeIndex>
      <curveDescription>Hole Depth TVD</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logCurveInfo uid="HDEP">
      <mnemonic namingSystem="HDEP">HDEP</mnemonic>
      <classWitsml>unknown</classWitsml>
      <unit>ft</unit>
      <mnemAlias namingSystem="Hole Depth">Hole Depth</mnemAlias>
      <minDateTimeIndex>2012-08-26T21:24:22-05:00</minDateTimeIndex>
      <maxDateTimeIndex>2012-08-26T21:24:43-05:00</maxDateTimeIndex>
      <curveDescription>Hole Depth</curveDescription>
      <typeLogData>double</typeLogData>
    </logCurveInfo>
    <logData>
      <mnemonicList>DateTime,HDTVD,HDEP</mnemonicList>
      <unitList>s,ft,ft</unitList>
      <data>2012-08-26T21:24:43-05:00,33.2872657775879,110.287300109863</data>      
      <data>2012-08-26T21:24:38-05:00,33.2450180053711,110.245048522949</data>      
      <data>2012-08-26T21:24:32-05:00,33.202766418457,110.202796936035</data>      
      <data>2012-08-26T21:24:27-05:00,33.1605224609375,110.160552978516</data>      
      <data>2012-08-26T21:24:22-05:00,33.1182708740234,110.118301391602</data>
    </logData>
    <commonData>
      <dTimLastChange>2012-11-07T14:54:46-06:00</dTimLastChange>
      <defaultDatum uidRef="KB">Kelly Bushing</defaultDatum>
    </commonData>
  </log>
</logs>""")   
        self.logVerify.test_full_log(verbose=True) 
        self.assertFalse(wtl.control_prim.fail.called)         

    # order of indexes in data section are random
    def test_test_unknown_direction_full_log(self): 
        wtl.store_prim.WITSMLServer.xml_out.set("""
<logs version="1.4.1.1" xmlns="http://www.witsml.org/schemas/1series">
    <log uidWell="a872cd21-97ca-4cfd-8e17-d37fdf0760fe" uidWellbore="2e474c7d-fc7f-4e61-abbf-950f6afa38ca" uid="6f2d65ae-a7b9-4f7a-b477-002ff81ec3cc">
        <nameWell>Realtime-Sim01</nameWell>
        <nameWellbore>Realtime-Sim01</nameWellbore>
        <name>Global_PDT_Depth</name>
        <objectGrowing>false</objectGrowing>
        <serviceCompany>Halliburton</serviceCompany>
        <indexType>measured depth</indexType>
        <startIndex uom="ft">1</startIndex>
        <endIndex uom="ft">5</endIndex>
        <stepIncrement uom="ft">1</stepIncrement>
        <direction>unknown</direction>
        <indexCurve>DEP</indexCurve>
        <logCurveInfo uid="DEP">
            <mnemonic namingSystem="DEP">DEP</mnemonic>
            <classWitsml>measured depth of hole</classWitsml>
            <unit>ft</unit>
            <mnemAlias namingSystem="Depth">Depth</mnemAlias>
            <minIndex uom="ft">1</minIndex>
            <maxIndex uom="ft">5</maxIndex>
            <curveDescription>Depth</curveDescription>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="CURVE1">
            <mnemonic namingSystem="CURVE1">CURVE1</mnemonic>
            <classWitsml>unknown</classWitsml>
            <unit>ft/h</unit>
            <mnemAlias namingSystem="CURVE1">CURVE1</mnemAlias>
            <minIndex uom="ft">1</minIndex>
            <maxIndex uom="ft">4</maxIndex>
            <curveDescription>CURVE1</curveDescription>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="CURVE2">
            <mnemonic namingSystem="CURVE2">CURVE2</mnemonic>
            <classWitsml>unknown</classWitsml>
            <unit>ft/h</unit>
            <mnemAlias namingSystem="CURVE2">CURVE2</mnemAlias>
            <minIndex uom="ft">2</minIndex>
            <maxIndex uom="ft">5</maxIndex>
            <curveDescription>CURVE2</curveDescription>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logCurveInfo uid="CURVE3">
            <mnemonic namingSystem="CURVE3">CURVE3</mnemonic>
            <classWitsml>unknown</classWitsml>
            <unit>ft/h</unit>
            <mnemAlias namingSystem="CURVE3">CURVE3</mnemAlias>
            <minIndex uom="ft">2</minIndex>
            <maxIndex uom="ft">4</maxIndex>
            <curveDescription>CURVE3</curveDescription>
            <typeLogData>double</typeLogData>
        </logCurveInfo>
        <logData>
            <mnemonicList>DEP,CURVE1,CURVE2,CURVE3</mnemonicList>
            <unitList>ft,ft/h,ft/h,ft/h</unitList>
            <data>1,10,,</data>
            <data>4,11,99,1000</data>
            <data>3,12,100,1001</data>
            <data>2,,101,1002</data>
            <data>5,,102,</data>                                                
        </logData>
        <commonData>
            <dTimLastChange>2012-11-07T16:54:46-06:00</dTimLastChange>
            <defaultDatum uidRef="KB">Kelly Bushing</defaultDatum>
        </commonData>
    </log>
</logs> 
""")        
        self.logVerify.test_full_log(verbose=True)
        self.assertFalse(wtl.control_prim.fail.called)   
        
        
        
if __name__ == '__main__':
    unittest.main()
