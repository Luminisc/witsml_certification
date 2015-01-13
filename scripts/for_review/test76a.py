#! /usr/bin/env python
from wtl.witsml import *



test(
     purpose = "Verify the server supports requestLatestValues behavior for an increasing time log",
     reference =  "6.6.2.1",
     reference_text = "DEFAULT: normal log behavior. A server MUST support this option. If specified, return the latest n values from each curve in a log data-object. ",
     functionality_required =   ["WMLS_GetFromStore:log" ],    
     data_schemas = ["1.4.1.0", "1.4.1.1"],
    )

#########
# SETUP #
#########

#############
# TEST BODY #
#############

log('Script procedure start')

log("Retrieving log")
# Use SQ-015 (Get Log) specifying OptionsIn = requestLatestValues = 1
WMLS_GetFromStore(WMLTYPEIN_LOG,
                  """<logs xmlns="http://www.witsml.org/schemas/1series" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="$server_schema_version$">
                           <log uidWell="$server_w1_uid$" uidWellbore="$server_w1_wb1_uid$" uid="$server_w1_wb1_log2_uid$">
                           </log>
                     </logs>"""
                  ,OptionsIn={'returnElements':'all', 'requestLatestValues':'1'})

check_ReturnValue_Success()
check_XMLout_NumberOfObjects(1)

partial_success("Get from store succeeded")

# need to know what curve is the index curve
indexMnemonic = get_XMLout_Element_String("indexCurve")
mnemonicList = get_XMLout_Mnemonics_List()
maxLatestValuesTimeDateDict = {}

if ( len(mnemonicList) < 2 ):
    fail("number of curves needs to be 2 or more")
    
# see if minDateTimeIndex == maxDateTimeIndex for all curves, except index curve
for mnemonic in mnemonicList:
      if ( mnemonic != indexMnemonic):
          set('mnemonic', mnemonic)
          minDateTime = get_XMLout_Element_String("logCurveInfo[mnemonic='$mnemonic$']/minDateTimeIndex")
          maxDateTime = get_XMLout_Element_String("logCurveInfo[mnemonic='$mnemonic$']/maxDateTimeIndex")
          maxLatestValuesTimeDateDict[mnemonic] = maxDateTime
          check_timestamp_Equals(minDateTime,maxDateTime)

partial_success('Server returned the correct minDateTimeIndex/maxDateTimeIndex for each curve')
    
# Use SQ-010 (Get Log Header) specifying OptionsIn = requestLatestValues = 1 for  the curve
WMLS_GetFromStore(WMLTYPEIN_LOG, 
                    """<logs xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                         <log uidWell="$server_w1_uid$" uidWellbore="$server_w1_wb1_uid$" uid="$server_w1_wb1_log2_uid$">
                       </logs>
                    """ ,OptionsIn={'returnElements':'header-only'} )
check_ReturnValue_Success()
check_XMLout_NumberOfObjects(1)


partial_success('Server returned the latest values for each curve')
   
# see if first set of maxDateTimeIndex match second set
for mnemonic in mnemonicList:
      if ( mnemonic != indexMnemonic):
          set('mnemonic', mnemonic)          
          maxDateTime = get_XMLout_Element_String("logCurveInfo[mnemonic='$mnemonic$']/maxDateTimeIndex")
          latestValuesMaxDateTime =  maxLatestValuesTimeDateDict[mnemonic]         
          check_timestamp_Equals(maxDateTime,latestValuesMaxDateTime)

partial_success('Server returned the correct maxDateTimeIndex for each curve between queries')

log('Script procedure end')

success()