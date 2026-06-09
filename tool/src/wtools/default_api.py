'''
Created on Jun 22, 2012

@organization: PetroDAQ Inc
@author: Denys Metelskyy
@contact: 2121 Golden Rd, Suite 1-A. The Woodlands, TX 77381. denys.metelskyy@petrodaq.com  
'''
import sys
import xml.dom.minidom
import string
from . import common;
import os;
import string;

from suds.client import Client
from suds.transport.http import HttpAuthenticated

from lxml import etree

import base64
import traceback

from lxml import etree
from lxml import objectify

import wtl.witsml as witsml_cert;
import wtl.store_prim as store_prim


WITSML_OBJ_WELL         = "well"
WITSML_OBJ_WELLBORE     = "wellbore"
WITSML_OBJ_LOG          = "log"
WITSML_OBJ_TRAJECTORY   = "trajectory"
WITSML_OBJ_MUDLOG       = "mudLog"

WITSML_VERSION_1311 = "1.3.1.1"
WITSML_VERSION_1410 = "1.4.1.0"
WITSML_VERSION_1411 = "1.4.1.1"

class HTML_Exception:
    def __init__(self):
        print("Raised HTML Exception")
        pass


class WITSML_Exception:
    def __init__(self, result_code, result):
        print("Raised Exception : "+str(result_code)+" '"+result+"' ");
        pass

class GetFromStoreResponse:
    def __init__ (self):
        self.XMLout = None;
        self.SuppMsgOut = None;
        self.Result = 0;

    def __repr__(self):
        return "GetFromStoreResponse : %d %s %s" % (self.Result , self.SuppMsgOut , self.XMLout  )

        
class AddToStoreResponse:
    def __init__ (self):
        self.SuppMsgOut = None;
        self.Result = 0;

    def __repr__(self):
        return "AddToStoreResponse : %d %s" % (self.Result , self.SuppMsgOut  )


class DeleteFromStoreResponse:
    def __init__ (self):
        self.SuppMsgOut = None;
        self.Result = 0;

    def __repr__(self):
        return "DeleteFromStoreResponse : %d %s" % (self.Result , self.SuppMsgOut  )


class UpdateInStoreResponse:
    def __init__ (self):
        self.SuppMsgOut = None;
        self.Result = 0;

    def __repr__(self):
        return "UpdateInStoreResponse : %d %s" % (self.Result , self.SuppMsgOut  )


        
class GetCapResponse:
    def __init__ (self):
        self.CapabilitiesOut = None;
        self.SuppMsgOut = None;
        self.Result = 0;
    
    def __repr__(self):
        return "GetCapResponse : %d %s %s" % (self.Result , self.SuppMsgOut , self.CapabilitiesOut )
        
class GetVersionResponse:
    def __init__ (self):
        self.Result = "";
    def __repr__(self):
        return "GetVersionResponse : "+str(self.Result)



class WITSML_API:
    
    """wrapper for WITSML API, on reply it will also check error code and if it < 1 then exception will be raised"""
    
    def __init__(self):
        #self.debug = False;
        self.debug = True;
        self.seq = 0;
        """creating soap client"""
        
    def logQueryIfNeeded(self, operation , query):
        if ( self.debug ):
            self.seq = self.seq + 1;
            #query = etree.tostring( etree.fromstring( query ) , pretty_print=True) 
            query = common.wipeComments(query);
            output_filename = "c:/witsml_trace/"+str(self.seq)+"_query_"+operation+".xml";
            d = os.path.dirname(output_filename)
            if not os.path.exists(d):
                os.makedirs(d)
            f = open(output_filename,"w");
            f.write(query);
            f.close();

    
    def checkResultCode(self , value , msg):
        if ( value <=0 ) :
            print("Error Detected!!!! ERROR CODE : #"+str(value)+" msg:"+msg);
            raise WITSML_Exception(value , msg)
        pass
    
    #def WMLS_GetCap(self):
    #    r = self.client.WMLS_GetCap(OptionsIn = self.options_in);
    #    result = GetCapResponse()
    #    result.Result = r["Result"];
    #    result.CapabilitiesOut = r["CapabilitiesOut"].encode('ascii', 'ignore');
    #    self.logQueryIfNeeded( "GetCap_Out" , result.CapabilitiesOut);
    
    def WMLS_GetVersion(self, OptionsIn = {}):
        #r = witsml_cert.WMLS_GetVersion(OptionsIn = OptionsIn);
        result = GetVersionResponse();
        if not witsml_cert.WMLS_GetVersion():
                raise WITSML_Exception(-10000, "Can not perform get version" )
        result.Result = witsml_cert.get_ReturnValue();
        self.logQueryIfNeeded( "Version_Out" , result.Result);
        return result;
    
    def WMLS_GetFromStore(self, QueryIn, WMLtypeIn, OptionsIn = {} , CapabilitiesIn = ""):
            self.logQueryIfNeeded( "GetFromStore_Request" , QueryIn);
            #r = self.client.service.WMLS_GetFromStore(WMLtypeIn, QueryIn, OptionsIn, CapabilitiesIn)
            
            success = witsml_cert.WMLS_GetFromStore(WMLtypeIn = WMLtypeIn, QueryIn=QueryIn, OptionsIn = OptionsIn, CapabilitiesIn =CapabilitiesIn);
            
            if not success:
                raise WITSML_Exception(-10000, "Can not perform get from store" )
            
            result = GetFromStoreResponse() ;
            result.Result = witsml_cert.get_ReturnValue();
            result.SuppMsgOut = witsml_cert.get_SuppMsgOut_String()
            try:
                self.checkResultCode(result.Result , result.SuppMsgOut);
            except:
                print("query fail :\n"+QueryIn);
                raise;
            
            result.XMLout = store_prim.WITSMLServer.xml_out.get();
            
            self.logQueryIfNeeded( "GetFromStore_Response" , result.XMLout);
            return result;

    def WMLS_AddToStore(self, XMLin, WMLtypeIn, OptionsIn = {} , CapabilitiesIn = ""):
            self.logQueryIfNeeded( "AddToStore_Request" , XMLin);
            
            
            
            success = witsml_cert.WMLS_AddToStore(WMLtypeIn = WMLtypeIn, XMLin=XMLin, OptionsIn = OptionsIn, CapabilitiesIn =CapabilitiesIn);
            
            if not success:
                raise WITSML_Exception(-10000, "Can not perform get from store" )
            
            
            #r = self.client.service.WMLS_AddToStore(WMLtypeIn, XMLin, OptionsIn , CapabilitiesIn);
            result = AddToStoreResponse() ;
            result.Result = witsml_cert.get_ReturnValue();
            result.SuppMsgOut = witsml_cert.get_SuppMsgOut_String()
            try:
                self.checkResultCode( result.Result, result.SuppMsgOut );
            except:
                print("What fail : "+XMLin)
            return result;

    def WMLS_UpdateInStore(self, XMLin, WMLtypeIn, OptionsIn = {} , CapabilitiesIn = ""):
            self.logQueryIfNeeded( "UpdateInStore_Request" , XMLin);
            
            #r = self.client.service.WMLS_UpdateInStore(WMLtypeIn = WMLtypeIn, XMLin = XMLin, CapabilitiesIn = CapabilitiesIn, OptionsIn = OptionsIn);
            
            success = witsml_cert.WMLS_UpdateInStore(WMLtypeIn = WMLtypeIn, XMLin=XMLin, OptionsIn = OptionsIn, CapabilitiesIn =CapabilitiesIn);
            if not success:
                raise WITSML_Exception(-10000, "Can not perform update in store" )

            result = UpdateInStoreResponse() ;
            result.Result = witsml_cert.get_ReturnValue();
            result.SuppMsgOut = witsml_cert.get_SuppMsgOut_String()
            self.checkResultCode(result.Result, result.SuppMsgOut)
            return result;

    def WMLS_DeleteFromStore(self, QueryIn, WMLtypeIn, OptionsIn = {} , CapabilitiesIn = ""):
            self.logQueryIfNeeded( "DeleteFromStore_Request" , QueryIn);
            #
            success = witsml_cert.WMLS_DeleteFromStore(WMLtypeIn = WMLtypeIn, QueryIn = QueryIn, CapabilitiesIn = CapabilitiesIn, OptionsIn = OptionsIn);
            if not success:
                raise WITSML_Exception(-10000, "Can not perform delte from store" )
            #
            #r = self.client.service.WMLS_DeleteFromStore(WMLtypeIn = WMLtypeIn, QueryIn = QueryIn, CapabilitiesIn = CapabilitiesIn, OptionsIn = OptionsIn);
            #
            result = DeleteFromStoreResponse() ;
            #
            result.Result = witsml_cert.get_ReturnValue();
            result.SuppMsgOut = witsml_cert.get_SuppMsgOut_String()
            #
            self.checkResultCode(result.Result , result.SuppMsgOut) 
            return result;
        
        
    def isWellExists(self, schema_version, well_uid):
            #
            query = string.Template("""<wells xmlns="http://www.witsml.org/schemas/1series" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="$version">
                                          <well uid="$uid">
                                            <name />
                                          </well>
                                        </wells>""" ).substitute( version = schema_version,  uid = well_uid);
            #
            response = self.WMLS_GetFromStore( QueryIn = query, 
                               WMLtypeIn = WITSML_OBJ_WELL , 
                             );
            wells = objectify.fromstring( response.XMLout );                 
            if not ( 'well' in  wells.__dict__ ):
                return False;
            return True;
        
    def addWell(self, schema_version, well_uid , well_name):
            #
            query = string.Template("""<wells xmlns="http://www.witsml.org/schemas/1series" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="$version">
                                          <well uid="$uid">
                                            <name>$name</name>
                                          </well>
                                        </wells>""" ).substitute( version = schema_version,  uid = well_uid, name = well_name);
                                    #
            response = self.WMLS_AddToStore( 
                               QueryIn = query, 
                               WMLtypeIn = WITSML_OBJ_WELL , 
                             );
            return True;
        
    def isWellboreExists(self, schema_version, well_uid, wellbore_uid):
            #
            query = string.Template("""<wellbores xmlns="http://www.witsml.org/schemas/1series" version="$version">
                                          <wellbore uidWell="$well_uid" uid="$wellbore_uid">
                                          </wellbore>
                                        </wellbores>""" ).substitute( version = schema_version,  
                                                                      well_uid = well_uid,
                                                                      wellbore_uid = wellbore_uid);
            #
            response = self.WMLS_GetFromStore( QueryIn = query, 
                               WMLtypeIn = WITSML_OBJ_WELLBORE , 
                             );
            #                 
            wellbores = objectify.fromstring( response.XMLout );                 
            if not ( 'wellbore' in  wellbores.__dict__ ):
                return False;
            return True;
    
    def addWellbore(self, schema_version, well_uid , well_name , wellbore_uid , wellbore_name ):
            #
            query = string.Template("""<wellbores xmlns="http://www.witsml.org/schemas/1series" version="$version">
                                          <wellbore uidWell="$well_uid" uid="$wellbore_uid">
                                            <nameWell>$well_name</nameWell>
                                            <name>$wellbore_name</name>
                                          </wellbore>
                                        </wellbores>""" ).substitute( version = schema_version,
                                                                      well_uid = well_uid,
                                                                      well_name = well_name,
                                                                      wellbore_uid = wellbore_uid,
                                                                      wellbore_name = wellbore_name);
            #
            response = self.WMLS_AddToStore( QueryIn = query, 
                               WMLtypeIn = WITSML_OBJ_WELLBORE , 
                             );
            #                 
            return True;



    def isLogExists(self, schema_version, well_uid  , wellbore_uid , log_uid ):
            #
            query = string.Template("""<logs xmlns="http://www.witsml.org/schemas/1series" version="$version">
                                          <log uidWell="$well_uid" uidWellbore="$wellbore_uid" uid="$log_uid">                    
                                          </log>
                                        </logs>""" ).substitute(   
                                                                    version = schema_version,
                                                                    well_uid = well_uid,
                                                                    wellbore_uid = wellbore_uid,
                                                                    log_uid = log_uid 
                                                                );
            #
            response = self.WMLS_GetFromStore( 
                                                QueryIn = query, 
                                                WMLtypeIn = WITSML_OBJ_LOG , 
                                            );
            #                 
            return True;
        
    def deleteLog(self, schema_version, well_uid  , wellbore_uid , log_uid ):
            #
            query = string.Template("""<logs xmlns="http://www.witsml.org/schemas/1series" version="$version">
                                          <log uidWell="$well_uid" uidWellbore="$wellbore_uid" uid="$log_uid">                    
                                          </log>
                                        </logs>""" ).substitute(   
                                                                    version = schema_version,
                                                                    well_uid = well_uid,
                                                                    wellbore_uid = wellbore_uid,
                                                                    log_uid = log_uid 
                                                                );
            #
            response = self.WMLS_DeleteFromStore( 
                                                QueryIn = query, 
                                                WMLtypeIn = WITSML_OBJ_LOG , 
                                            );
            #                 
            return True;