from wtl.witsml import *



test(
     purpose = "",
     reference =  "",
     reference_text = "",
     functionality_required =   ["WMLS_AddToStore:log" ,
                                 "WMLS_UpdateInStore:log",
                                 "WMLS_GetFromStore:log"],
     data_schemas = ["1.4.1.0", "1.4.1.1"],
    )

#########
# SETUP #
#########

log('Setup start')

log("Retrieving well and wellbore name")
WMLS_GetFromStore(WMLTYPEIN_WELLBORE, """<?xml version="1.0" encoding="UTF-8"?>
                                     <wellbores xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                        <wellbore uidWell="$server_w1_uid$" uid="$server_w1_wb1_uid$"/>
                                     </wellbores>
                                  """, OptionsIn={'returnElements':'id-only'})  
check_ReturnValue_Success();
set('well_name', get_XMLout_Element_String('nameWell'))
set('wellbore_name', get_XMLout_Element_String('name'))

log('Setup end')
log('')

#############
# TEST BODY #
#############

log('Script procedure start')

##################################################################################
##ADD a log with two curves and 3 indexes                                       ##
##################################################################################
WMLS_AddToStore(WMLTYPEIN_LOG, """<?xml version="1.0" encoding="utf-8"?>
                                   <logs xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                      <log uidWell="$server_w1_uid$" uidWellbore="$server_w1_wb1_uid$">
                                         <nameWell>$well_name$</nameWell>
                                         <nameWellbore>$wellbore_name$</nameWellbore>
                                         <name>Energistics Certification Wellbore Test82</name>
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
                                             <minIndex uom="m">499</minIndex>
                                             <maxIndex uom="m">509.01</maxIndex>
                                             <curveDescription>Vertical depth</curveDescription>
                                             <sensorOffset uom="m">0</sensorOffset>
                                             <traceState>raw</traceState>
                                             <typeLogData>double</typeLogData>
                                         </logCurveInfo>
                                         <logCurveInfo uid="lci-3">
                                             <mnemonic>Bit Dist</mnemonic>
                                             <classWitsml>measured depth of DST bottom</classWitsml>
                                             <unit>m</unit>
                                             <mnemAlias>distBit</mnemAlias>
                                             <minIndex uom="m">499</minIndex>
                                             <maxIndex uom="m">509.01</maxIndex>
                                             <curveDescription>Distance drilled by bit</curveDescription>
                                             <sensorOffset uom="m">0</sensorOffset>
                                             <traceState>raw</traceState>
                                             <typeLogData>double</typeLogData>
                                         </logCurveInfo>
                                         <logCurveInfo uid="lci-4">
                                             <mnemonic>TQ on btm</mnemonic>
                                             <classWitsml>torque (average)</classWitsml>
                                             <unit>kft.lbf</unit>
                                             <mnemAlias>tqOnBot</mnemAlias>
                                             <minIndex uom="m">499</minIndex>
                                             <maxIndex uom="m">509.01</maxIndex>
                                             <curveDescription>On bottom torque</curveDescription>
                                             <sensorOffset uom="m">0</sensorOffset>
                                             <traceState>raw</traceState>
                                             <typeLogData>double</typeLogData>
                                         </logCurveInfo>
                                         <logData>
                                             <mnemonicList>Mdepth,Vdepth,Bit Dist,TQ on btm</mnemonicList>
                                             <unitList>m,m,m,kft.lbf</unitList>
                                             <data>499,498.99,1.25,0</data>
                                             <data>500.01,500,1.9,0.01</data>
                                             <data>501.03,501.02,2.92,0.02</data>
                                             <data>502.01,502,3.9,0.06</data>
                                             <data>503.01,503,4.9,0.11</data>
                                             <data>504.05,504.04,5.94,0.18</data>
                                             <data>505.03,505.00,612.03,1.83</data>
                                             <data>506.04,505.95,613.04,1.9</data>
                                             <data>507.04,506.91,614.04,1.97</data>
                                             <data>508.01,507.84,615.01,2</data>
                                             <data>509.01,508.75,,2.08</data>
                                             <!-- has last row with a null for the 3rd curve -->
                                         </logData>
                                      </log>
                                   </logs>
                                """)  

check_ReturnValue_Success();
partial_success("Add to store succeeded")

set('uid', get_SuppMsgOut_uid_String())
log_variable('uid')
new_object_created(WMLTYPEIN_LOG, "$uid$", uidWellbore="$server_w1_wb1_uid$", uidWell="$server_w1_uid$")




##################################################################################
## Update the log                                                               ##
##################################################################################
WMLS_UpdateInStore(WMLTYPEIN_LOG, """<?xml version="1.0" encoding="utf-8"?>
                                   <logs xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                      <log uidWell="$server_w1_uid$" uidWellbore="$server_w1_wb1_uid$" uid="$uid$">
                                        <startIndex uom="m">599</startIndex>
                                        <endIndex uom="m">609.01</endIndex>
                                        <logData>
                                            <mnemonicList>Mdepth,Vdepth,Bit Dist,TQ on btm</mnemonicList>
                                            <unitList>m,m,m,kft.lbf</unitList>
                                            <data>509.01,,616.01,2.08</data>
                                            <data>510,508.99,611.25,3</data>
                                            <data>510.01,510,611.9, 3.01</data>
                                            <data>511.03,511.02,612.92,3.02</data>
                                            <data>512.01,512,613.9, 3.06</data>
                                            <data>513.01,513,614.9, 3.11</data>
                                            <data>514.05,514.04,615.94,3.18</data>
                                            <data>515.03,515.00,622.03,4.83</data>
                                            <data>516.04,515.95,623.04,4.9</data>
                                            <data>517.04,516.91,624.04,4.97</data>
                                            <data>518.01,517.84,625.01,5</data>
                                            <data>519.01,518.75,626.01,5.08</data>
                                        </logData>
                                      </log>
                                   </logs>
                                """)
check_ReturnValue_Success()

######################################################################################
##Check to see if the value of CHANNELA at index 1002 is not cleared by the update  ##
######################################################################################


WMLS_GetFromStore(WMLTYPEIN_LOG, """<?xml version="1.0" encoding="utf-8"?>
                                   <logs xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                      <log uidWell="$server_w1_uid$" uidWellbore="$server_w1_wb1_uid$" uid="$uid$"/>
                                   </logs>
                                """,OptionsIn={'returnElements':'all'})
check_ReturnValue_Success()
check_XMLout_NumberOfObjects(1)

# Verify that the data expected
data = [(499,   498.99,  1.25,0),
        (500.01,500,     1.9, 0.01),
        (501.03,501.02,  2.92,0.02),
        (502.01,502,     3.9, 0.06),
        (503.01,503,     4.9, 0.11),
        (504.05,504.04,  5.94,0.18),
        (505.03,505.00,612.03,1.83),
        (506.04,505.95,613.04,1.9),
        (507.04,506.91,614.04,1.97),
        (508.01,507.84,615.01,2),
        (509.01,508.75,616.01,2.08),
        (510,   508.99,611.25,3),
        (510.01,510,   611.9, 3.01),
        (511.03,511.02,612.92,3.02),
        (512.01,512,   613.9, 3.06),
        (513.01,513,   614.9, 3.11),
        (514.05,514.04,615.94,3.18),
        (515.03,515.00,622.03,4.83),
        (516.04,515.95,623.04,4.9),
        (517.04,516.91,624.04,4.97),
        (518.01,517.84,625.01,5),
        (519.01,518.75,626.01,5.08)]
check_logData_AllData(data, index_error_margin=1, error_margin=1)

log('Script procedure end')

success()
