#! /usr/bin/env python
from wtl.witsml import *

test(
     purpose = "Verify the server supports SQ-018 – What changes have been made in a mudLog or multiple mudLogs since a specified time",
     reference =  "6.6.7  Standard Query Templates",
     reference_text = "All WITSML servers that support the function MUST support these queries",
     functionality_required = ["WMLS_GetFromStore:mudLog",
                               "WMLS_DeleteFromStore:mudLog",
                               "WMLS_AddToStore:mudLog"],
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

WMLS_GetFromStore(WMLTYPEIN_MUDLOG, """<?xml version="1.0" encoding="UTF-8"?>
                                     <mudLogs xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                       <mudLog uidWell="$server_w1_uid$" uidWellbore="$server_w1_wb1_uid$" uid="$server_w1_wb1_mudlog1_uid$"/> 
                                     </mudLogs>
                                  """)  

if (get_XMLout_NumberOfObjects_Int() == 1):
    WMLS_DeleteFromStore(WMLTYPEIN_MUDLOG, """<?xml version="1.0" encoding="UTF-8"?>
                                     <mudLogs xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                       <mudLog uidWell="$server_w1_uid$" uidWellbore="$server_w1_wb1_uid$" uid="$server_w1_wb1_mudlog1_uid$"/> 
                                     </mudLogs>
                                  """)
    check_ReturnValue_Success()

WMLS_AddToStore(WMLTYPEIN_MUDLOG, """<?xml version="1.0" encoding="UTF-8"?>
                                    <mudLogs xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                        <mudLog uidWell="$server_w1_uid$" uidWellbore="$server_w1_wb1_uid$" uid="$server_w1_wb1_mudlog1_uid$">
                                            <name>$server_w1_wb1_mudlog1_name$</name>
                                        </mudLog>
                                    </mudLogs>""")  
check_ReturnValue_Success()

success()
