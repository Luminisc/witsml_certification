#! /usr/bin/env python
from wtl.witsml import *
import time;

test(
     purpose = "Verify the server supports SQ-018 - What changes have been made in a mudLog or multiple mudLogs since a specified time",
     reference =  "6.6.7  Standard Query Templates",
     reference_text = "All WITSML servers that support the function MUST support these queries",
     functionality_required =   ["WMLS_DeleteFromStore:mudLog",
                                 "WMLS_UpdateInStore:mudLog",
                                 "WMLS_GetFromStore:changeLog"],
     data_schemas = ["1.4.1.0", "1.4.1.1"],
    )

#########
# SETUP #
#########

set("cdp", float(get_CapabilitiesOut_Element_String("changeDetectionPeriod")) + 1)
set("gtp", float(get_CapabilitiesOut_Element_String('/capServers/capServer/growingTimeoutPeriod[@dataObject="mudLog"]')) + 1)
log('')

set('server_w3_uid', 'Energistics-well-0003')
set('server_w3_wb1_uid', 'Energistics-w3-wellbore-0001')
set('server_w3_wb1_mudlog1_uid', 'Energistics-w3-wb1-mudlog-0001')
set('uidGI', 'Certification-Test-w3_wb1-Mudlog-0001')

set('mdTop', '8990')
set('mdBottom', '9420')

##Call UpdateInStore to add a single geologyInterval.
WMLS_UpdateInStore(WMLTYPEIN_MUDLOG,"""<?xml version="1.0" encoding="UTF-8"?>
                                    <mudLogs xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                        <mudLog uidWell="$server_w3_uid$" uidWellbore="$server_w3_wb1_uid$" uid="$server_w3_wb1_mudlog1_uid$">
                                            <geologyInterval uid="$uidGI$">
                                                <typeLithology>cuttings</typeLithology>
                                                <mdTop uom="ft">$mdTop$</mdTop> 
                                                <mdBottom uom="ft">$mdBottom$</mdBottom>
                                            </geologyInterval>
                                        </mudLog>
                                    </mudLogs>""")  
check_ReturnValue_Success()


#wait for the # of growingTimeoutPeriod seconds
log('Sleeping for GTP - ' + get('gtp') + ' sedcond(s)')
time.sleep(get('gtp'))

#############
# TEST BODY #
#############

##Call GetfromStore to retrieve the dTimLastChange of the mudLog object.
WMLS_GetFromStore(WMLTYPEIN_MUDLOG,"""<?xml version="1.0" encoding="UTF-8"?>
                                    <mudLogs xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                        <mudLog uidWell="$server_w3_uid$" uidWellbore="$server_w3_wb1_uid$" uid="$server_w3_wb1_mudlog1_uid$">
                                            <commonData>
                                                <dTimLastChange />
                                            </commonData>
                                        </mudLog>
                                    </mudLogs>""")  
check_ReturnValue_Success()
check_XMLout_NumberOfObjects(1);

set('tml', get_XMLout_Element_String('dTimLastChange'))

##Call UpdateInStore to modify single geologyInterval.
WMLS_UpdateInStore(WMLTYPEIN_MUDLOG,"""<?xml version="1.0" encoding="UTF-8"?>
                                    <mudLogs xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                        <mudLog uidWell="$server_w3_uid$" uidWellbore="$server_w3_wb1_uid$" uid="$server_w3_wb1_mudlog1_uid$">
                                            <geologyInterval uid="$uidGI$">
                                                <typeLithology>cuttings</typeLithology>
                                                <mdTop uom="ft">$mdTop$</mdTop> 
                                                <mdBottom uom="ft">$mdBottom$</mdBottom>
                                                <lithology uid="00000">
                                                    <type>Limestone</type>
                                                    <lithPc uom="%">95</lithPc>
                                                </lithology>
                                                <lithology uid="00001">
                                                    <type>Marl</type>
                                                    <lithPc uom="%">5</lithPc>
                                                </lithology>
                                                <lithostratigraphic kind="formation">Rotliegende</lithostratigraphic>
                                                <chronostratigraphic kind="period">Permian</chronostratigraphic>
                                                <chronostratigraphic kind="epoch">Cisuralian</chronostratigraphic>
                                                <chronostratigraphic kind="stage">Sakmarian</chronostratigraphic>
                                            </geologyInterval>
                                        </mudLog>
                                    </mudLogs>""")  
check_ReturnValue_Success()

#sleep for a second
#time.sleep(1)

##Call DeleteFromStore to delete a single geologyInterval.
WMLS_DeleteFromStore(WMLTYPEIN_MUDLOG,"""<?xml version="1.0" encoding="UTF-8"?>
                                    <mudLogs xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                        <mudLog uidWell="$server_w3_uid$" uidWellbore="$server_w3_wb1_uid$" uid="$server_w3_wb1_mudlog1_uid$">
                                            <geologyInterval uid="$uidGI$" />
                                        </mudLog>
                                    </mudLogs>""")  
check_ReturnValue_Success()

#sleep for a second
time.sleep(1)

#wait for the # of change-detection-period seconds
time.sleep(get('cdp'))

##Use SQ-018 with a dTimLastChange and dTimChange of the mudLog before we did any updates.
log('Retrieving ChangeLog from ' + get('tml'))
WMLS_GetFromStore(WMLTYPEIN_CHANGELOG, """<?xml version="1.0" encoding="UTF-8"?>
                                          <changeLogs xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                            <changeLog uidObject="$server_w3_wb1_mudlog1_uid$" uidWellbore="$server_w3_wb1_uid$" uidWell="$server_w3_uid$">
                                                <objectType>mudLog</objectType>
                                                <changeHistory>
                                                    <dTimChange>$tml$</dTimChange>
                                                </changeHistory>
                                                <commonData>
                                                    <dTimLastChange>$tml$</dTimLastChange>
                                                </commonData>
                                            </changeLog>
                                          </changeLogs>
                                       """,OptionsIn={'returnElements':'all'})
check_ReturnValue_Success()


#uncomment the following line to test the error message if the server does not return two elements
#set("tml", timestamp_add_seconds(get('tml'), 2))

#The response contains a ChangeLog object for the corresponding mudLog with two changeHistory entries
#with changeType = 'update' and dTimChange is greater than the previous value.  The whole changeHistory entry
#corresponds to the updates made in the procedure (i.e. startIndex, endIndex, etc)
set('count_CH', len(get_XMLout_RecurringElement_List('changeHistory')))
if (get('count_CH') != 2) :
    fail("The changeHistory entries in the ChangeLog object for the corresponding mudLog is not two (" + str(get('count_CH')) + ")")

check_timestamp_Greaterthan(get_XMLout_RecurringElement_List("dTimChange")[0], get('tml'))
check_timestamp_Greaterthan(get_XMLout_RecurringElement_List("dTimChange")[1], get('tml'))

check_XMLout_RecurringElementValue("changeType",["update","update"])

check_XMLout_ElementValue(get_XMLout_RecurringElement_List("startIndex")[0], get('mdTop'))
check_XMLout_ElementValue(get_XMLout_RecurringElement_List("endIndex")[0], get('mdBottom'))
check_XMLout_ElementValue(get_XMLout_RecurringElement_List("startIndex")[1], get('mdTop'))
check_XMLout_ElementValue(get_XMLout_RecurringElement_List("endIndex")[1], get('mdBottom'))

partial_success("The server supports SQ-018 What changes have been made in a mudLog or multiple mudLogs since a specified time")
log('Script procedure end')

#############
# CLEAN-UP #
#############

#No clean-up is needed

success()
