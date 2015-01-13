#! /usr/bin/env python
from wtl.witsml import *

test(
     purpose = "",
     reference =  "",
     reference_text = "",
     functionality_required =   ["WMLS_GetFromStore:well",
                                 "WMLS_GetFromStore:wellbore",
                                 "WMLS_GetFromStore:log",
                                 "WMLS_GetFromStore:changeLog"],
     data_schemas = ["1.4.1.0", "1.4.1.1"],
    )

#########
# SETUP #
#########

log('Setup')

# get well name
log("Retrieving well 3 name")
WMLS_GetFromStore(WMLTYPEIN_WELL, """<?xml version="1.0" encoding="UTF-8"?>
                                     <wells xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                         <well uid="$server_w3_uid$">
                                           <name/>
                                         </well>
                                     </wells>
                                  """)  
check_ReturnValue_Success()                                  
set('expected_well_name', get_XMLout_Element_String('name'))

# get wellbore name
log("Retrieving w3_wb1 name")
WMLS_GetFromStore(WMLTYPEIN_WELLBORE, """<?xml version="1.0" encoding="UTF-8"?>
                                     <wellbores xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                       <wellbore uidWell="$server_w3_uid$" uid='$server_w3_wb1_uid$'>      
                                           <name/>
                                       </wellbore>
                                     </wellbores>
                                  """)
check_ReturnValue_Success()                               
set('expected_wellbore_name', get_XMLout_Element_String('name'))

# get log name
log("Retrieving w3_wb1 name")
WMLS_GetFromStore(WMLTYPEIN_LOG, """<?xml version="1.0" encoding="UTF-8"?>
                                     <logs xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                       <log uidWell="$server_w3_uid$" uidWellbore='$server_w3_wb1_uid$' uid='$server_w3_wb1_log1_uid$'>      
                                           <name/>
                                       </log>
                                     </logs>
                                  """)
check_ReturnValue_Success()                               
set('expected_log_name', get_XMLout_Element_String('name'))


log('')



#############
# TEST BODY #
#############

log('Script procedure start')


WMLS_GetFromStore(WMLTYPEIN_CHANGELOG, """<changeLogs xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                       <changeLog uidWell="$server_w3_uid$" uidWellbore = "$server_w3_wb1_uid$" uidObject="$server_w3_wb1_log1_uid$">
                                          </changeLog>
                                    </changeLogs>
                                  """,OptionsIn={'returnElements':'all'})

#WMLS_GetFromStore(WMLTYPEIN_CHANGELOG, """<changeLogs xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
#                                        <changeLog uidWell="$server_w3_uid$" uidWellbore = "$server_w3_wb1_uid$" uidObject="$server_w3_wb1_log1_uid$">
#                                            <nameWell/>
#                                            <nameWellbore/>
#                                            <nameObject/>
#                                        </changeLog>
#                                    </changeLogs>
#                                  """,OptionsIn={})

check_ReturnValue_Success()

#'/changeLogs/changeLog[@uidObject="$well_uid$"]/changeHistory/changeType'
check_XMLout_ElementValue('/changeLogs/changeLog/nameWell', get('expected_well_name'))
check_XMLout_ElementValue('/changeLogs/changeLog/nameWellbore', get('expected_wellbore_name'))
check_XMLout_ElementValue('/changeLogs/changeLog/nameObject', get('expected_log_name'))

#check attributes
#print get_XMLout_RecurringElement_List('/changeLogs/changeLog[@uidWell="$server_w3_uid$"]/nameObject')
if (get('expected_log_name') <> get_XMLout_Element_String('/changeLogs/changeLog[@uidWell="$server_w3_uid$"]/nameObject')):
    fail("changeLog uidWell attribute is not set correctly"
         )
#check_XMLout_ElementValue('/changeLogs/changeLog[@uidWell="$server_w3_uid$"]/nameObject', get('expected_log_name'))
#check_XMLout_ElementValue('/changeLogs/changeLog[@uidWellbore="$server_w3_wb1_uid$"]/nameObject', get('expected_log_name'))
#check_XMLout_AttributeValue('/changeLogs/changeLog[@uidWell="$server_w3_uid$"]', get('expected_log_name'))

log('Script procedure end')


success()
