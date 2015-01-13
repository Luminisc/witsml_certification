#! /usr/bin/env python
from wtl.witsml import *
import re

test(
     purpose = "Verify a server supports OptionsIn return-elements=id-only",
     reference =  "6.6.2.1  WMLS_GetFromStore - OptionsIn Keywords",
     reference_text = "returnElements:  All values except 'requested' are an alternative to specifying empty values for data item selection such that the server MUST treat the template as if the indicated elements and attributes had explicitly been specified in the template.",
     functionality_required = ["WMLS_GetFromStore:well"],
     data_schemas = ["1.4.1.0", "1.4.1.1"],
    )

#########
# SETUP #
#########

log('No setup is needed for this test')
log('')

#############
# TEST BODY #
#############

log('Script procedure start')

# Use SQ-001 (Get ID of All Wells) with OptionsIn returnelements=id-only
WMLS_GetFromStore(WMLTYPEIN_WELL, """<?xml version="1.0" encoding="UTF-8"?>
                                     <wells xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                        <well/>
                                     </wells>
                                  """,OptionsIn={'returnElements':'id-only'})  
check_ReturnValue_Success()

#Verify server returns list of wells with name and uid only.  No other elements are returned.
set ("n",get_XMLout_NumberOfObjects_Int())
l = []
l.append('wells')
l.append('wells[version]')
for i in range (0, get("n")):
    l.append('well')
    l.append('well[uid]')
    l.append('name')
check_XMLout_OnlyIncluded(l)
partial_success("Get ID of all wells query with OptionsIn returnelements=id-only returns only names and uids of wells.")
log('Script procedure end')
success()
