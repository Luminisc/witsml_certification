#! /usr/bin/env python
from wtl.witsml import *

test(
     purpose = "Verify the dTimChange in changeHistory matches the value of dTimLastChange in the corresponding data-object.",
     reference =  "9.3.4.4  Specifics of Updating the changeLog",
     reference_text = "The value of dTimChange in a changeHistory element MUST match the value of dTimLastChange in the corresponding data-object when the changeHistory entry is added.",
     functionality_required =   ["WMLS_GetFromStore:well",
                                 "WMLS_GetFromStore:changeLog"],
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

log('Script procedure start')

# Use SQ-003 (Get Details for a Well) to retrieve the Well object related to the changeLog object 
WMLS_GetFromStore(WMLTYPEIN_WELL,"""
                  <wells xmlns='http://www.witsml.org/schemas/1series' version='$server_schema_version$'>
                        <well uid='$server_w1_uid$'/>
                  </wells>
                  """,OptionsIn={'returnElements':'all'})  
check_ReturnValue_Success()
set("dTimLastChange", get_XMLout_Element_String("dTimLastChange"))

# Send a GetFromStore query for the changeLog object.
WMLS_GetFromStore(WMLTYPEIN_CHANGELOG, """<changeLogs xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                            <changeLog uidObject='$server_w1_uid$'>
                                                <objectType>well</objectType> 
                                            </changeLog>
                                          </changeLogs>
                                  """,OptionsIn={'returnElements':'all'})
check_ReturnValue_Success()

# Verify the dTimLastChange in the well object object matches the dTimChange in the last changeHistory of the changeLog
check_XMLout_ElementIncluded('dTimChange')
check_timestamp_Equals(get_XMLout_Element_String("/changeLogs/changeLog/changeHistory[last()]/dTimChange"), get("dTimLastChange"))
partial_success("The dTimLastChange in the well object matches the dTimChange in the last changeHistory of the changeLog.")

log('Script procedure end')

success()
