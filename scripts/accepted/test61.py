#! /usr/bin/env python
from wtl.witsml import *

test(
     purpose = "Verify the server supports SQ-018 - What changes have been made in a mudLog or multiple mudLogs since a specified time",
     reference =  "6.6.5",
     reference_text = "All WITSML servers that support the function MUST support these queries",
     functionality_required =   ['WMLS_GetFromStore:changeLog',
                                 'WMLS_GetFromStore:mudLog',
                                 'WMLS_UpdateInStore:mudLog',
                                 'WMLS_DeleteFromStore:mudLog'],
     data_schemas = ["1.4.1.0", "1.4.1.1"],
    )

#########
# SETUP #
#########
           
log('No setup is needed for this test.')
log('')

#############
# TEST BODY #
#############

log('Script start')

# Call GetfromStore to retrieve the dTimLastChange of the mudLog object. 
WMLS_GetFromStore(WMLTYPEIN_MUDLOG, """<?xml version="1.0" encoding="utf-8"?>
                                    <mudLogs xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                        <mudLog uidWell="$server_w3_uid$" uidWellbore="$server_w3_wb1_uid$" uid="$server_w3_wb1_mudlog1_uid$">
                                          <commonData>
                                            <dTimLastChange/>
                                          </commonData>
                                        </mudLog>
                                    </mudLogs>""")  
check_ReturnValue_Success()
set('tml', get_XMLout_Element_String('dTimLastChange'))

# Pause for at least one second to make sure the update time is different that the dTimLastChange
pause(1)

# Define a geologyInterval uid to use for update an delete
set('geologyInterval_uid', 'Certification-Test-61-geologyInterval')

# Call UpdateInStore to add a single geologyInterval. 
WMLS_UpdateInStore(WMLTYPEIN_MUDLOG,"""<?xml version="1.0" encoding="UTF-8"?>
                                    <mudLogs xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                        <mudLog uidWell="$server_w3_uid$" uidWellbore="$server_w3_wb1_uid$" uid="$server_w3_wb1_mudlog1_uid$">
                                            <geologyInterval uid="$geologyInterval_uid$">
                                                <typeLithology>cuttings</typeLithology>
                                                <mdTop uom="ft">8000</mdTop> 
                                                <mdBottom uom="ft">9000</mdBottom>
                                            </geologyInterval>
                                        </mudLog>
                                    </mudLogs>""")  
check_ReturnValue_Success()

# Call DeleteFromStore to delete a single geologyInterval. 
WMLS_DeleteFromStore(WMLTYPEIN_MUDLOG,"""<?xml version="1.0" encoding="UTF-8"?>
                                    <mudLogs xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                        <mudLog uidWell="$server_w3_uid$" uidWellbore="$server_w3_wb1_uid$" uid="$server_w3_wb1_mudlog1_uid$">
                                            <geologyInterval uid="$geologyInterval_uid$"/>
                                        </mudLog>
                                    </mudLogs>""")  
check_ReturnValue_Success()

# Now we have to make sure the changes are detected by the server
pause_for_changeDetectionPeriod()

# Use SQ-018 with a dTimLastChange and dTimChange of the mudLog from the first GetFromStore query.
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

# Verify that the response contains a ChangeLog object for the corresponding mudLog with only
# two changeHistory entries with changeType = 'update' and dTimChange is greater than the provided dTimChange
check_XMLout_AttributeValue('changeLog', 'uidWell','$server_w3_uid$')
check_XMLout_AttributeValue('changeLog', 'uidWellbore','$server_w3_wb1_uid$')
check_XMLout_AttributeValue('changeLog', 'uidObject','$server_w3_wb1_mudlog1_uid$')
partial_success('The correct changeLog object received')

check_XMLout_RecurringElementValue('changeType', ['update', 'update'])
partial_success("Two 'update' changeHistory entries received")

times = get_XMLout_RecurringElement_List('dTimChange')   
check_timestamp_Greaterthan(times[0], get('tml'))
partial_success('dTimChange of first changeHistory entry is correct')
check_timestamp_Greaterthan(times[1], get('tml'))  
partial_success('dTimChange of second changeHistory entry is correct')

log('Script procedure end')

success()
