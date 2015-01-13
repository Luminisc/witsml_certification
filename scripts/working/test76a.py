#! /usr/bin/env python
from wtl.witsml import *

test(
     purpose = "Verify the server supports requestLatestValues behaviour.",
     reference =  "6.6.2.1 OptionsIn Keywords -> requestLatestValues",
     reference_text = "",
     functionality_required =   ["WMLS_GetFromStore:log"],
     data_schemas = ["1.4.1.0", "1.4.1.1"],
    )

#########
# SETUP #
#########

log('No setup is needed for this test.')

#############
# TEST BODY #
#############

log('Script test procedure start')

#Get mnemonic list and choose 2 curves (including the index curve)
WMLS_GetFromStore(WMLTYPEIN_LOG,
                  """<logs xmlns='http://www.witsml.org/schemas/1series' version="$server_schema_version$">
                         <log uidWell='$server_w1_uid$' uidWellbore='$server_w1_wb1_uid$' uid='$server_w1_wb1_log1_uid$'>
                         </log>                      
                       </logs>
                  """ ,OptionsIn={'returnElements':'all'})
check_ReturnValue_Success()



mnemonics = get_XMLout_Mnemonics_List()

index = 0
mn = ""
while index < len(mnemonics):
    if len(mn) > 0:
        mn = mn + "," 
    mn = mn + mnemonics[index]
    index = index +1
    
print mn

set("mn", mn)             
                              
                              
queryType = get_XMLout_Element_String('indexType')

# Save all the data first to verify last values
maxIndexList = ''
if queryType == 'measured depth':
    maxIndexList = get_XMLout_RecurringElement_List('maxIndex');   
else:
    maxIndexList =  get_XMLout_RecurringElement_List('maxDateTimeIndex')

dirMnemonicLastIndexMap = {}
dirTestResult = {}

index = 0
while index < len(mnemonics):
    dirMnemonicLastIndexMap[mnemonics[index]] = maxIndexList[index]
    if mnemonics[index] != queryType: # if it's not index curve, add to check list
        dirTestResult[mnemonics[index]] = 0 
    index = index + 1

#Use SQ-015 to retrieve the entire log (don't care about truncations)
WMLS_GetFromStore(WMLTYPEIN_LOG, """<?xml version="1.0" encoding="UTF-8"?>
                                     <logs xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                                         <log uidWell="$server_w1_uid$" uidWellbore="$server_w1_wb1_uid$" uid="$server_w1_wb1_log1_uid$">
                                             <logData>
                                                 <mnemonicList>$mn$</mnemonicList>
                                                 <data></data>
                                             </logData>      
                                         </log>
                                     </logs>
                                  """,
                                  OptionsIn={'requestLatestValues':'1'})    

check_ReturnValue_Success()
mnList  = get_XMLout_Element_String('mnemonicList').split(",")

# Save the lastestValues
output = get_XMLout_RecurringElement_List('data')

for row in output:
    j = 0
    vList = row.split(",")
    iv = vList[0] # get index value
    for v in vList:        
        if len(v) > 0 and mnList[j] != queryType and dirMnemonicLastIndexMap.has_key(mnList[j]) and dirMnemonicLastIndexMap[mnList[j]] == iv:
                dirTestResult[mnList[j]] = 1 # found a match. 
        j = j + 1
                
finalResult = 1
for v in dirTestResult.values():
    if v == 0:
        finalResult = 0

log('Script test procedure end')

if(finalResult == 0):
    fail()
else:
    success()
