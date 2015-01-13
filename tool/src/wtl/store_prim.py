#******************************************************************************
# Copyright (c) 2011 Pason Systems Corp.
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

# System imports
import os
import sys
from suds.client import Client
from suds.transport.http import HttpAuthenticated

# Application imports
import script
import utils
import testlog
import response
import wtl.capability
import wtl.globals
import log_verify
from wsvt.SchemaValidator import WITSMLSchemaValidator;

validator = None

#******************************************************************************
#
# WITSML server interface
#
class WITSMLServer: 
    """ Encapsulation of WITSML server interactions """

    # Client handle
    client = None

    # Response Variables
    result = response.ReturnValue(None)
    capabilities_out = response.XMLValue(None)
    xml_out =  response.XMLValue(None)
    supp_msg_out = response.ReturnValue(None)

    log_verify_object = log_verify.LogVerify(xml_out)

    @staticmethod
    def connect(url, username, password, userProxy):
        """ Prepare connection handle to WITSML server
        Parameters:
          url: WITSML server URL
          username: Username to be used for authentication
          password: User's password
          userProxy: Proxy in the form 'http://USERNAME:PASSWORD@HOST:PortNumber'
                           example: 'http://userName:passworkd@myProxy.com:80'
        """

        wsdl_file = os.path.join(sys.modules['wtl'].__path__[0], "WMLS.WSDL")
        t = HttpAuthenticated(username=username, password=password)
        WITSMLServer.client = Client("file:" + wsdl_file, transport=t, location=url)
        WITSMLServer.client.set_options(headers={'User-Agent':'WITSML-Test-Library/1.0'})
        if (userProxy): 
            proxyClient = dict( http = userProxy, https = userProxy ) 
            WITSMLServer.client.set_options(proxy=proxyClient)  

    @staticmethod
    def store_primitive_fail(fail_message):
        """
        Make the script fail
    
        Parameters:
          fail message:  String indicating the fail reason
      
        Return:
          Nothing
        """
    
        wtl.script.Script.get_current_script().fail(fail_message)

    @staticmethod
    def log_store_action(action):
        """ Log a WITSML store API action """

        testlog.wtl_log("  > %s..." %action, no_new_line=True)

    @staticmethod
    def log_store_result(result):
        """ Log the result of a WITSML store API action """

        testlog.wtl_log(result)

    @staticmethod
    def clear_response():
        """ Clear previous WITSML server response """

        WITSMLServer.result.clear()
        WITSMLServer.capabilities_out.clear()
        WITSMLServer.xml_out.clear()
        WITSMLServer.supp_msg_out.clear()

    @staticmethod
    def get_version():
        """ Execute the WMLS_GetVersion API and save the server response """

        WITSMLServer.log_store_action("sending WMLS_GetVersion request")
        WITSMLServer.clear_response()
        versions = None
        try:
            versions = WITSMLServer.client.service.WMLS_GetVersion()
        except:
            WITSMLServer.log_store_result('Failed')
            return False

        WITSMLServer.log_store_result('Response received')
        WITSMLServer.result.set(versions, log='Return Result')
        return True
    
    @staticmethod
    def get_cap(OptionsIn={}):
        """
        Execute the WMLS_GetCap API and save the server response
        
        Parameters:
          See the WITSML STORE Application Program Interface (API)
        
          OptionsIn: A dictionary in the form 'option':'value'
                     The OptionsIn string is encoded by this function
                     Example: {'dataVersion':'1.3.1.1'}
                     
        Returns:
          True if response received, or False otherwise
        """
        WITSMLServer.log_store_action("sending WMLS_GetCap request")
        WITSMLServer.clear_response()
        try:
            reply = WITSMLServer.client.service.WMLS_GetCap(utils.encode_options_in(OptionsIn))
        except:
            WITSMLServer.log_store_result('Failed')
            return False
        if reply:
            WITSMLServer.log_store_result("Response received")
            WITSMLServer.result.set(reply['Result'], log='Return Result')
            WITSMLServer.capabilities_out.set(reply['CapabilitiesOut'], log='CapabilitiesOut')
            WITSMLServer.supp_msg_out.set(reply['SuppMsgOut'], log='SuppMsgOut')
        else:
            WITSMLServer.log_store_result("Response not received") 
            return False
    
        return True

    @staticmethod
    def add_to_store(WMLtypeIn, XMLin, OptionsIn={}, CapabilitiesIn=""):
        """
        Execute the WMLS_AddToStore API and save the server response
        
        Parameters:
          See the WITSML STORE Application Program Interface (API)
        
        
          WMLtypeIn: A string containing the object name
                     Example: 'well'
                     WMLtypeIn values for all objects are defined in witsml.py
                     Example WMLTYPEIN_WELL 
        
          Xmlin:     A string containing the XML document.   
                     This string can contain variable substitutions ($...$),
                     file substitutions (#...#) and  conditional substitutions
                     (^...?...:...^)
        
          OptionsIn: A dictionary in the form 'option':'value'
                     The OptionsIn string is encoded by this function
                     Example: {'compressionMethod':'gzip'}

          CapabilitiesIn:  A string containing the XML document

        Returns:
          True if response received, or False otherwise
        """
        
        WITSMLServer.log_store_action("sending WMLS_AddToStore request")
        WITSMLServer.clear_response()
        try:
            reply = WITSMLServer.client.service.WMLS_AddToStore(WMLtypeIn, utils.process_string(XMLin), utils.encode_options_in(OptionsIn), CapabilitiesIn)
        except:
            WITSMLServer.log_store_result('Failed')
            return False
        if reply:
            WITSMLServer.log_store_result("Response received")
            WITSMLServer.result.set(reply['Result'], log='Return Result')
            WITSMLServer.supp_msg_out.set(reply['SuppMsgOut'], log='SuppMsgOut')
        else:
            WITSMLServer.log_store_result("Response not received")
            return False
    
        return True
    
    @staticmethod
    def delete_from_store(WMLtypeIn, QueryIn, OptionsIn={}, CapabilitiesIn =""):
        """
        Execute the WMLS_DeleteFromStore API and save the server response
        
        Parameters:
          See the WITSML STORE Application Program Interface (API)
        
        
          WMLtypeIn: A string containing the object name
                     Example: 'well'
                     WMLtypeIn values for all objects are defined in witsml.py
                     Example WMLTYPEIN_WELL 
        
          QueryIn:   A string containing the XML document.   
                     This string can contain variable substitutions ($...$),
                     file substitutions (#...#) and  conditional substitutions
                     (^...?...:...^)
        
          OptionsIn: A dictionary in the form 'option':'value'
                     The OptionsIn string is encoded by this function
                     Example: {'cascadeDelete':'true'}

          CapabilitiesIn:  A string containing the XML document

        Returns:
          True if response received, or False otherwise
        """

        WITSMLServer.log_store_action("sending WMLS_DeleteFromStore request")
        WITSMLServer.clear_response()
        try:
            reply = WITSMLServer.client.service.WMLS_DeleteFromStore(WMLtypeIn, utils.process_string(QueryIn), utils.encode_options_in(OptionsIn), CapabilitiesIn)
        except:
            WITSMLServer.log_store_result('Failed')
            return False
        if reply:
            WITSMLServer.log_store_result("Response received")
            WITSMLServer.result.set(reply['Result'], log='Return Result')
            WITSMLServer.supp_msg_out.set(reply['SuppMsgOut'], log='SuppMsgOut')
        else:
            WITSMLServer.log_store_result("Response not received")
            return False
    
        return True
    
    @staticmethod
    def get_from_store(WMLtypeIn, QueryIn, OptionsIn={}, CapabilitiesIn =""):
        """
        Execute the WMLS_GetFromStore API and save the server response
        
        Parameters:
          See the WITSML STORE Application Program Interface (API)
               
          WMLtypeIn: A string containing the object name
                     Example: 'well'
                     WMLtypeIn values for all objects are defined in witsml.py
                     Example WMLTYPEIN_WELL 
        
          QueryIn:   A string containing the XML document.   
                     This string can contain variable substitutions ($...$),
                     file substitutions (#...#) and  conditional substitutions
                     (^...?...:...^)
        
          OptionsIn: A dictionary in the form 'option':'value'
                     The OptionsIn string is encoded by this function
                     Example: {'returnElements':'all'}

          CapabilitiesIn:  A string containing the XML document

        Returns:
          True if response received, or False otherwise
        """

        WITSMLServer.log_store_action("sending WMLS_GetFromStore request")
        WITSMLServer.clear_response()
        try:
            reply = WITSMLServer.client.service.WMLS_GetFromStore(WMLtypeIn, utils.process_string(QueryIn), utils.encode_options_in(OptionsIn), CapabilitiesIn)
        except:
            WITSMLServer.log_store_result('Failed')
            return False
        if reply:
            WITSMLServer.log_store_result("Response received")
            WITSMLServer.result.set(reply['Result'], log='Return Result')
            WITSMLServer.xml_out.set(reply['XMLout'], log='XMLout')
            WITSMLServer.supp_msg_out.set(reply['SuppMsgOut'], log='SuppMsgOut')          

            if (wtl.config.enable_schema_validation):
                if (WITSMLServer.result.get() > 0):
                    WITSMLServer.log_store_action("validating schema")
                    global validator;
                    version = WITSMLServer.xml_out.get_version()
                    data_object =  WITSMLServer.xml_out.get_object_name()
                    document = WITSMLServer.xml_out.get_original_value()
                    is_valid, message =  validator.validateXMLAgainstReadSchema(version, data_object, document)
                    if (is_valid):
                        WITSMLServer.log_store_result("Ok")
                        return True
                    else:
                        WITSMLServer.log_store_result("Not Ok - %s"%(message))
                        WITSMLServer.store_primitive_fail(message)
                        return False
        else:
            WITSMLServer.log_store_result("Response not received")
            return False
    
        return True
    
    @staticmethod
    def update_in_store(WMLtypeIn, XMLin, OptionsIn={}, CapabilitiesIn =""):
        """
        Execute the WMLS_UpdateInStore API and save the server response
        
        Parameters:
          See the WITSML STORE Application Program Interface (API)
        
        
          WMLtypeIn: A string containing the object name
                     Example: 'well'
                     WMLtypeIn values for all objects are defined in witsml.py
                     Example WMLTYPEIN_WELL 
        
          XMLin:     A string containing the XML document.   
                     This string can contain variable substitutions ($...$),
                     file substitutions (#...#) and  conditional substitutions
                     (^...?...:...^)
        
          OptionsIn: A dictionary in the form 'option':'value'
                     The OptionsIn string is encoded by this function
                     Example: {'compressionMethod':'gzip'}

          CapabilitiesIn:  A string containing the XML document

        Returns:
          True if response received, or False otherwise
        """

        WITSMLServer.log_store_action("sending WMLS_UpdateInStore request")
        WITSMLServer.clear_response()
        try:
            reply = WITSMLServer.client.service.WMLS_UpdateInStore(WMLtypeIn, utils.process_string(XMLin), utils.encode_options_in(OptionsIn), CapabilitiesIn)
        except:
            WITSMLServer.log_store_result('Failed')
            return False
        if reply:
            WITSMLServer.log_store_result("Response received")
            WITSMLServer.result.set(reply['Result'], log='Return Result')
            WITSMLServer.supp_msg_out.set(reply['SuppMsgOut'], log='SuppMsgOut')
        else:
            WITSMLServer.log_store_result("Response not received")
            return False
    
        return True
    
    @staticmethod
    def get_base_msg(ReturnValueIn):
        """
        Execute the WMLS_GetBaseMsg API and save the server response
        
        Parameters:
          See the WITSML STORE Application Program Interface (API)
                
          ReturnValueIn: A string or integer containing the return value
                         Examples: -101  or '-101' 

        Returns:
          True if response received, or False otherwise
        """
        
        WITSMLServer.log_store_action("sending WMLS_GetBaseMsg request")
        WITSMLServer.clear_response()
        try:
            message = WITSMLServer.client.service.WMLS_GetBaseMsg(ReturnValueIn)
        except:
            WITSMLServer.log_store_result('Failed')
            return False
    
        WITSMLServer.log_store_result("Response received")
        WITSMLServer.result.set(message, log='Return Result')
        return True

    @staticmethod
    def init():
        """
        Initialize the WITSML store interface by connecting to the WITSML
        server and retrieving the schema versions supported (via 
        WMLS_GetVersion) and the server capabilities for all the schema 
        versions supported (via WMLS_GetCap)
        
        The server information retrieved is saved in global variables       
        """

        if (wtl.config.enable_schema_validation):
            global validator
            validator = WITSMLSchemaValidator(os.path.join(sys.modules['wsvt'].__path__[0],'schemas'))
        
        WITSMLServer.connect(utils.get_variable_value('server_URL'),
                utils.get_variable_value('server_username'),
                utils.get_variable_value('server_password'),
                utils.get_variable_value('server_proxy_URL'))
        
        # Check server connectivity and get version and capabilities 
        testlog.wtl_log("Getting server information...")
        
        # Save the schema versions supported by the server
        testlog.wtl_log("  Getting schema versions...")
        if (WITSMLServer.get_version()):
            wtl.globals.set(wtl.globals.GBL_SERVER_SCHEMA_VERSIONS, WITSMLServer.result.get().split(','))
        else:
            testlog.wtl_log("!!!WARNING - Cannot get schema versions supported by the server")

        # Save the server capabilities
        schema_version = wtl.utils.get_variable_value('server_schema_version')
        if schema_version in wtl.globals.get(wtl.globals.GBL_SERVER_SCHEMA_VERSIONS): 
            if (WITSMLServer.get_cap(OptionsIn={"dataVersion":schema_version})):
                wtl.globals.set(wtl.globals.GBL_SERVER_CAPABILITIES, wtl.capability.WITSMLStoreCapabilities(schema_version, WITSMLServer.capabilities_out.get()))
            else:
                testlog.wtl_log("!!!WARNING - Cannot get capabilities from the server for schema version %s" %(schema_version))
        else:
            testlog.wtl_log("!!!WARNING - Schema version for testing IS NOT supported by the server")
            
