
'''
Created on Jun 28, 2012

rewrited on Feb 7, 2013


@organization: PetroDAQ Inc
@author: Denys Metelskyy
@contact: 2121 Golden Rd, Suite 1-A. The Woodlands, TX 77381. denys.metelskyy@petrodaq.com  
'''

INDEX_TYPE_TIME = 0;
INDEX_TYPE_DEPTH = 1;

import string
import sys

import wtools.default_api as default_api
import wtools.common as common;

#import subprocess;

from lxml import etree
from lxml import objectify

#from wtl.witsml as witsml_api

ROUND_DIGITS = 3;

#exception when log does not make sense 
class InconsistentLogException:
    def __init__(self, msg):
        self.msg = msg;
        pass;

class CanNotLoadObjectException:
    def __init__(self, msg):
        self.msg = msg;
        print("EXCEPTION : "+msg)
        pass;

class LogAlreadyExistsException:
    def __init__(self, msg):
        self.msg = msg;
        print("EXCEPTION : "+msg)
        pass;
    
class GenericStoreException:
    def __init__(self, msg):
        self.msg = msg;
        print("EXCEPTION : "+msg)
        pass;


#def 
#check_ReturnValue_Value

def parseValueAsDatatype(value, datatype, nullvalue):
    """ 
    summary:
        converts value as string using datatype, and null value
        
    parameters:
        value - value as sting
        datatype - datatype string (as in witsml) "double", "date time" , "string"
        
    result:
        return value in internal type (ether double, datetime, string...)
    """
    if value == nullvalue:
        return None;
    if (datatype == "int"):
        return int(value);
    if (datatype == "double"):
        return round(float(value),ROUND_DIGITS);
    if (datatype == "date time"):
        return common.xsd_dateTime_to_datetime(value);
    if (datatype == "string"):
        return value;
    print("uknown datatype:"+datatype)
    raise ValueError();

def valueToString(value, datatype, nullvalue):
    """ 
    summary:
        converts value in internal type to string using datatype, and null value
        
    parameters:
        value - value in internal datatype (eather double, datetime, or string...)
        datatype - datatype string (as in witsml) "double", "date time" , "string"
        
    result:
        return value as string (ether double, datetime, string...)
    """
    if value == None:
        return nullvalue;
    if (datatype == "int"):
        return str(value);
    if (datatype == "double"):
        return str(value);
    if (datatype == "date time"):
        return str(common.datetime_to_xsd_dateTime(value));
    if (datatype == "string"):
        return value;
    print("uknown datatype:"+datatype)
    raise ValueError();

#log object implementation
class LogCurveInfo:
    
    """
    Keeps curve definition
    """
    
    def __init__(self , mnemonic_param, uom_param, datatype_param, nullvalue_param):
        """ 
        summary:
            constructor : creates LogCurveInfo using given parameters
        """
        self.mnemonic = mnemonic_param;
        self.uom = uom_param;
        self.datatype = datatype_param;
        self.nullvalue = nullvalue_param;
        pass
    
class LogDataRow:
    """
      Keeps internal representation of datarow, stores index of the row, index type, and array of values 
    """
    
    def __init__(self, index_type_param,  index_param , size_param ):
        """ 
        summary:
            constructor : creates row of data with given index type, index, and count of curves
        """
        self.index_type = index_type_param;
        self.index = index_param;
        self.values = [];
        for ix in range(size_param):
            self.values.append( None );

class LogDataObject:
    """
    This class keep internal representaion of log data (curve definition, and data)
    """
    def __init__(self):
        self.clean();
        
    
    def clean(self):
        """
        Wipes Log dataobject
        """
        self.curves = [];
        self.data = []
        self.index_type = INDEX_TYPE_DEPTH;
        self.start = None;
        self.end = None;
        self.lastAddedIndex = None;
    
    def getIndexTypeAsString(self):
        """
        User readable representation of index type, returns "Depth" and "Time" depending on Log object time
        """
        if ( self.index_type == INDEX_TYPE_DEPTH ):
            return "Depth"
        if ( self.index_type == INDEX_TYPE_TIME ):
            return "Time"
        return "unknown";
    
    def logError(self, str_param):
        print(("ERROR : "+str_param));
    
    def preview(self):
        """
        Utility function display data (used for debugging purposes)
        """
        curves_str = "";
        ix = 0;
        for curve in self.curves:
            curves_str = curves_str+"\t"+curve.mnemonic+"("+str(ix)+")";
            ix = ix + 1
        print(curves_str);
        for data_row in self.data:
            data_str = "";
            ix = 0;
            for data_point in data_row.values:
                data_str = data_str+"\t"+str(data_point)+"("+str(ix)+")"
                ix = ix + 1
            print(data_str)
        
    
    def objectify(self, schema, xml_str):
        """
        summary:
            creates object from XML string, ideally would use schematron but now not all the stores give replys according to schema
            so currently parsing is done without schema.
        
        parameters:
           schema - it is instance of wtools_schemas_witsml1410
           xml_str - xml, that need to be converted to object 
        
        returns:
           ether objectified lxml object or raise exception
        """
        obj = objectify.fromstring(xml_str);
        
        if not ( "log" in obj.__dict__ ):
            raise CanNotLoadObjectException("There is no log in returned plural logs (no log with such uid?)");
        
        if ( len(obj.log)<=0 ):
            self.logError ("This plural logs does not contain any log");
            return None;
        
        if ( len(obj.log)>1 ):
            self.logError ("This plural logs contains more then one log object");
            return None;
        
        return obj;
    
    def parseLogObjectHeader( self, obj ):
        """ 
        summary:
           parses and interprets header from gived objectified object
        
        params:
           obj - objectfied xml that contains header
         
        returns:
           nothing (I don't know why there is return True in the end of method, TODO: check)
        """
        self.start = "???";
        self.end = "???";
        
        self.nullvalue = "";
        
        if ( 'nullValue' in  obj.log[0].__dict__ ):
            self.nullvalue = obj.log[0].nullValue;
        
        if ( 'startDateTimeIndex' in  obj.log[0].__dict__ ):
            self.start = common.xsd_dateTime_to_datetime( str(obj.log[0].startDateTimeIndex) );
            #self.start_as_double = basic_utils.xsd_dateTime_to_datetime(self.start);
            self.index_type = INDEX_TYPE_TIME;
                
        if ( 'endDateTimeIndex' in  obj.log[0].__dict__ ):
            self.end = common.xsd_dateTime_to_datetime( str( obj.log[0].endDateTimeIndex) );
            #self.end_as_double = basic_utils.xsd_dateTime_to_datetime(self.end);
            self.index_type = INDEX_TYPE_TIME;
                
        if ( 'startIndex' in  obj.log[0].__dict__ ):
            self.start = float( str(obj.log[0].startIndex) );
            #self.start_as_double = float( self.start );
            self.index_type = INDEX_TYPE_DEPTH;
        
        if ( 'endIndex' in  obj.log[0].__dict__ ):
            self.end = float( str(obj.log[0].endIndex) );
            #self.end_as_double = float( self.end );
            self.index_type = INDEX_TYPE_DEPTH;
        
        for crv_iter in obj.log[0].logCurveInfo:
            #crv_iter.attrib["uid"]
            crv_uom = "";
            crv_datatype = "";
            crv_nullvalue = self.nullvalue;
            
            if "unit" in crv_iter.__dict__:
                crv_uom = crv_iter.unit;
            
            if "typeLogData" in crv_iter.__dict__:
                crv_datatype = crv_iter.typeLogData;
            
            if "nullValue" in crv_iter.__dict__:
                crv_nullvalue = crv_iter.nullValue;
            
            crv = LogCurveInfo( crv_iter.mnemonic, crv_uom , crv_datatype , crv_nullvalue );
            self.curves.append( crv )
        return True;
    
    def findRow(self, index):
        """ Locates row by given index"""
        """is empty ? - add new one """ 
        if len( self.data )<=0:
            nr = LogDataRow( self.index_type, index, len(self.curves) );
            self.data.append(nr);
            return nr;
        """looking for match"""
        for i in range(len(self.data)):
            if ( self.data[i].isIndexEqual( index ) ):
                return self.data[i]
        """nothig found ???? -add new one"""
        nr = LogDataRow( self.index_type, index, len(self.curves) );
        self.data.append(nr);
        return nr;
    
    
    
    def getCurveIndex(self, mnemonic):
        """
        gets column index by given mnemonic, for curve
        """
        ix = 0;
        for c in self.curves:
            if c.mnemonic == mnemonic:
                return ix;
            ix = ix + 1
        return -1;

    def lastIndexValue(self):
        """
        gets last index number
        """
        if (len(self.data)<=0):
            return None;
        return self.data[ len(self.data)-1 ].values[0];

    def parseLogObjectData( self, obj ):
        for logData_iter in obj.log[0].logData:
            new_mnemonics = logData_iter.mnemonicList.text.split(",")
            foreign_local_mnemonic_map = [];
            
            for mnemonic_i in range( len(new_mnemonics) ):
                
                found_curve = False;
                for curve_i in range( len ( self.curves  )) :
                    if (new_mnemonics[mnemonic_i] == self.curves[curve_i].mnemonic):
                        found_curve = True;
                        foreign_local_mnemonic_map.append(curve_i);
                        break;
                if (not found_curve):
                    #this needs to be more gracefully handled (maybe)
                    raise InconsistentLogException("There is new curve in log array, that was not seen in header")
                    
            #print foreign_local_mnemonic_map
            for data_iter in logData_iter.data:
                #print basic_utils.get_object_attrs(data_iter);
                values = data_iter.text.split(",");
                #index = None;
                new_row = LogDataRow( self.index_type,  None , len(self.curves) )
                for i in range( len( values ) ):
                    if (i == 0):
                            #addValue( mnemonics[i] + " = " + values[i]
                        new_row.index = values[ 0 ];
                    curve_index = foreign_local_mnemonic_map[i];
                    #print curve_index;
                    try:
                        new_row.values[ curve_index ] =    parseValueAsDatatype(values[i], self.curves[curve_index].datatype , self.curves[curve_index].nullvalue );
                    except:
                        print("What fail : datarow "+str(data_iter));
                        
                        print((" curve = '"+ 
                               self.curves[curve_index].mnemonic + 
                               "' datatype: (" + 
                               self.curves[curve_index].datatype + 
                               ") attempted to parse value: '"+values[i]+"' column #"+str(curve_index)));
                               
                        raise;
                if len(self.data)>1:
                    if (self.data[len(self.data)-1].index == new_row.index):
                        continue;
                self.data.append(new_row);

    
    def sortCurvesIntoAlphabeticOrder(self,obj):
        if len( obj.log[0].logCurveInfo ) <= 1:
            print("No curves to be sorted Object contains only Index curve")        
        #storing curves
        index_crv = None;
        data_curves = [];
        #
        pos = obj.log[0].index( obj.log[0].logCurveInfo );
        #    
        for crv_ix in range( len(obj.log[0].logCurveInfo) ):
            if (crv_ix == 0):
                index_crv = obj.log[0].logCurveInfo[crv_ix];
            else:
                data_curves.append( obj.log[0].logCurveInfo[crv_ix] );
        #
        mm = {};
        for c in range( len(data_curves) ):
            mm[ data_curves[c].mnemonic ] = data_curves[c];
        #
        pos+=1;
        obj.log[0].insert(pos, index_crv) 
        for k in mm:
            pos+=1;
            obj.log[0].insert(pos, mm[k]) #obj.log[0].logCurveInfo.append(  );
        pass;

    def sortDataAlphabetic(self):
        
        #reordering data
        for r in self.data:
            mm = {};
            for i in range(len(self.curves)):
                if (i!=0):
                    mm[ self.curves[i].mnemonic ] = r.values[i];
            r.values = [ r.values[0] ];
            for k in mm:
                r.values.append( mm[k] );
        #reordering curves
        mm = {};
        for i in range(len(self.curves)):
            if (i!=0):
                mm[ self.curves[i].mnemonic ] = self.curves[i];
        #
        sorted_curves = [ self.curves[0] ];
        for k in mm:
            sorted_curves.append( mm[k] );
        self.curves = sorted_curves;
        
                    
    
    def backToXMLObject(self, onheader_smpl , include_data, drop_nodes_for_comparison = False , start_data_row = 0, max_row_count = -1 , ns = "http://www.witsml.org/schemas/1series"):
        """
        summary:
           using original header this method will produce new XML object 
        
        parameters:
           onheader_smpl              - on which header do manipulations (will not mutate)
           include_data               - boolean flag saying weather or not include data section in resulting XML
           drop_nodes_for_comparison  - boolean flag saying whether drop or not drop all nodes that does not act in comparison
           start_data_row             - first data row that need to be included in resulting XML
           max_row_count              - maximum rows that can be included in result.
        
        returns:
          xml object and last+1 included row tuple
        """
        
        EF = objectify.ElementMaker(annotate=False, namespace=ns, nsmap={None : ns})
        onheader = objectify.fromstring(  etree.tostring(onheader_smpl)  )
        
        self.sortCurvesIntoAlphabeticOrder(onheader);
        self.sortDataAlphabetic();
        #open("c:/XXXXXXX.txt","w").write( etree.tostring( onheader , pretty_print=True) );
        #return;
    
        if include_data: 
            onheader.log[0].logData = EF.logData();
            new_mnemonic_list = "";
            new_unit_list = "";
            for curve_i in self.curves:
                if ( len(new_mnemonic_list) > 0 ):
                    new_mnemonic_list = new_mnemonic_list + ","
                    new_unit_list = new_unit_list + ","
                new_mnemonic_list = new_mnemonic_list + curve_i.mnemonic
                new_unit_list = new_unit_list + curve_i.uom
            pass;
            mnemonic_list_node = EF.mnemonicList(new_mnemonic_list);
            onheader.log[0].logData[0].append(mnemonic_list_node);
            pass;
            uom_list_node = EF.unitList(new_unit_list);
            onheader.log[0].logData[0].append(uom_list_node);
            pass;
            row_countdown = max_row_count;
            if ( row_countdown <= 0 ) :
                row_countdown = len( self.data ); 
            row_i = start_data_row;
            while 1:
                row_countdown = row_countdown -1;
                if  row_countdown < 0 :
                    #required amount of rows scanned
                    break;
                if  row_i >= len(self.data) :
                    #index out of bounds
                    break;
                row = self.data[row_i] 
                data_row_csv = "";
                for data_i in range( len(self.curves) ):
                    if data_i > 0:
                        data_row_csv = data_row_csv + ",";
                    data_row_csv = data_row_csv + valueToString( row.values[data_i], self.curves[data_i].datatype ,  self.curves[data_i].nullvalue   )
                data_node = EF.data(data_row_csv);
                onheader.log[0].logData[0].append(data_node);
                row_i = row_i + 1;
        pass;
        if drop_nodes_for_comparison:
                    if ("nameWell" in onheader.log[0].__dict__):
                        onheader.log[0].remove(onheader.log[0].nameWell);
                    
                    if ("nameWellbore" in onheader.log[0].__dict__):
                        onheader.log[0].remove(onheader.log[0].nameWellbore);
                        
                    if ("name" in onheader.log[0].__dict__):
                        onheader.log[0].remove(onheader.log[0].name);
                    
                    if ("objectGrowing" in onheader.log[0].__dict__):
                        onheader.log[0].remove(onheader.log[0].objectGrowing);
                    onheader.log[0].attrib["uidWell"] = "";
                    onheader.log[0].attrib["uidWellbore"] = "";
                    onheader.log[0].attrib["uid"] = "";
                    if ( 'creationDate' in  onheader.log[0].__dict__ ):
                        onheader.log[0].remove(onheader.log[0].creationDate)
                    pass;
                    for crv in onheader.log[0].logCurveInfo:
                        crv.attrib["uid"] = "";
                    pass;
                    if ("commonData" in onheader.log[0].__dict__):
                        if ("dTimCreation" in onheader.log[0].commonData.__dict__ ):
                            onheader.log[0].commonData.remove(onheader.log[0].commonData.dTimCreation)
                        if ("dTimLastChange" in onheader.log[0].commonData.__dict__ ):
                            onheader.log[0].commonData.remove(onheader.log[0].commonData.dTimLastChange)        #
        return (onheader, row_i);
    
    def serialize(self, ooo):
        return etree.tostring( self.backToXMLObject(ooo) , pretty_print=True) ;







class LogObject:
    """ Represendation of log object copy of original xml header, and parsed data """
    def __init__(self, ver):
        self.objectified_native_header = None;
        self.logDataObject = None;
        self.maxRowPerRequest = 500;
        #import wtools_witsml_api_witsml_cert as apic;
        self.api = default_api.WITSML_API();
        #self.wmls_type = default_api.WITSML_OBJ_LOG
        #self.parser = None;
        self.schema_version = ver;
        self.read_schema_parser = None;
        self.write_schema_parser = None;
        
    
    def CheckHeaderInformation(self):
        """ validates header """
        if ( self.logDataObject.start == None ):
            raise CanNotLoadObjectException("Can not determine log object start index");
        
        if ( self.logDataObject.end == None ):
            raise CanNotLoadObjectException("Can not determine log object end index");
        
        if (( self.logDataObject.end - self.logDataObject.start) == 0 ):
            raise CanNotLoadObjectException("Object contains empty interval range"); #actually should be just a warning
    
    def LoadObjectFromStore(self,  well_uid, wellbore_uid, log_uid):
        """ 
        summary:
            loads log object from store
        
        parameters:
            api          - instance of wtools_witsml_api
            schema       - instance of wtools_schemas_witsml1310 (not used currently only for future schematron reference)
            well_uid     - well uid string
            wellbore_uid - wellbore uid string
            log_uid      - log uid string
            
        returns:
            nothing
        """
        print("Loading log object from store");
        self.LoadHeaderFromStore(well_uid, wellbore_uid, log_uid)
        self.CheckHeaderInformation();
        request_position = self.logDataObject.start;
        while (1):
            print("new request pos = "+str(request_position));
            if (self.logDataObject.index_type == INDEX_TYPE_TIME):
                query = string.Template( """<logs xmlns="http://www.witsml.org/schemas/1series" version="$version">
                                                  <log uidWell="$uidWell" uidWellbore="$uidWellbore" uid="$uidLog">
                                                    <nameWell></nameWell>
                                                    <nameWellbore></nameWellbore>
                                                    <name></name>
                                                    <startIndex uom="">$startIndex</startIndex>
                                                    <endIndex uom="">$endIndex</endIndex>
                                                    <startDateTimeIndex>$startTimeIndex</startDateTimeIndex>
                                                    <endDateTimeIndex>$endTimeIndex</endDateTimeIndex>
                                                  </log>
                                                </logs>""" ).substitute(
                                                                    version = self.schema_version,
                                                                    uidWell = well_uid,
                                                                    uidWellbore = wellbore_uid,
                                                                    uidLog = log_uid,
                                                                    startIndex = "",
                                                                    endIndex = "",
                                                                    startTimeIndex = common.datetime_to_xsd_dateTime(request_position),
                                                                    endTimeIndex = "")
            else:
                query = string.Template(self.get_GetDataTemplate()).substitute(
                        uidWell = well_uid,
                        uidWellbore = wellbore_uid,
                        uidLog = log_uid,
                        startIndex = str(request_position),
                        endIndex = "",
                        startTimeIndex = "",
                        endTimeIndex = "") 
            print("requesting data from WITSML store...");
            
            #WMLS_GetFromStore
            
            response = self.api.WMLS_GetFromStore(    QueryIn = query, 
                                                      WMLtypeIn = default_api.WITSML_OBJ_LOG ,                                           
                                                      OptionsIn = { 
                                                                       "maxReturnNodes" : str(self.maxRowPerRequest),
                                                                       "returnElements" :"data-only"
                                                                    } 
                                                  );
                                          
                                                       
            print("processing reply from WITSML store...")
            object_from_store = objectify.fromstring( response.XMLout );
            try:
                self.logDataObject.parseLogObjectData(object_from_store)
            except:
                print("\n FYI: Original Header was :\n"+etree.tostring( self.objectified_native_header , pretty_print=True))
                raise ;            
            print("XML parsed")
            if (response.Result == 1):
                break;
            request_position = self.logDataObject.lastIndexValue();
            print("loaded : "+str( len(self.logDataObject.data) )+" rows ...");
            print("");
        print("Loading Done. Total Loaded : "+str( len(self.logDataObject.data) )+" rows");    
    
    def LoadHeaderFromStore(self ,  well_uid, wellbore_uid, log_uid):
            """ 
            summary:
                loads header of log object object from store
            
            parameters:
                #api          - instance of wtools_witsml_api
                #schema       - instance of wtools_schemas_witsml1310 (not used currently only for future schematron reference)
                well_uid     - well uid string
                wellbore_uid - wellbore uid string
                log_uid      - log uid string
                
            returns:
                nothing
            """
            print("Getting log object header from store");
            query = string.Template( """<logs xmlns="http://www.witsml.org/schemas/1series" version="$version">
                                          <log uidWell="$well_uid" uidWellbore="$wellbore_uid" uid="$log_uid">                    
                                          </log>
                                        </logs>""" ).substitute( version = self.schema_version,
                                                                 well_uid = well_uid,
                                                                 wellbore_uid = wellbore_uid,
                                                                 log_uid = log_uid)
                                        
            response = self.api.WMLS_GetFromStore( QueryIn = query, 
                                      WMLtypeIn = default_api.WITSML_OBJ_LOG , 
                                      OptionsIn = { "returnElements" : "header-only"} );
            
            self.logDataObject = LogDataObject();            
            self.objectified_native_header = self.logDataObject.objectify( self.getReadSchemaParser() , response.XMLout)
            self.logDataObject.parseLogObjectHeader( self.objectified_native_header )
    
    
    
    def LoadObjectFromString(self,  string_xml):
            """ 
            summary:
                loads header of log object object from disk
            
            parameters:
                api          - instance of wtools_witsml_api
                schema       - instance of wtools_schemas_witsml1310 (not used currently only for future schematron reference)
                string_xml   - WITSML XML to load string
                
            returns:
                nothing
            """
            print("Loading XML Log Object From string...");
            #f = file(filename,'r')
            #xml = string
            xml = string_xml;
            self.logDataObject = LogDataObject();
            self.objectified_native_header = self.logDataObject.objectify( self.getReadSchemaParser() , xml)
            self.logDataObject.parseLogObjectHeader( self.objectified_native_header )
            self.CheckHeaderInformation();
            self.logDataObject.parseLogObjectData( self.objectified_native_header );
            
    
    
            
    def LoadObjectFromDisk(self, filename):
            """ 
            summary:
                loads header of log object object from disk
            
            parameters:
                api          - instance of wtools_witsml_api
                schema       - instance of wtools_schemas_witsml1310 (not used currently only for future schematron reference)
                filename     - filename string
                
            returns:
                nothing
            """
            print("Loading XML Log Object From disk...");
            f = file(filename,'r')
            xml = f.read()
            self.LoadObjectFromString(self.api, self.parser ,  xml);
            

    def SaveObjectToDisk(self, filename):
        """ 
        summary:
            saves log object object to disk
        
        parameters:
            api          - instance of wtools_witsml_api
            schema       - instance of wtools_schemas_witsml1310 (not used currently only for future schematron reference)
            filename     - filename string
            
        returns:
            nothing
        """
        rez, next_row = self.logDataObject.backToXMLObject( self.objectified_native_header , True, False );
        target = open(filename, "w");
        xml_str = etree.tostring( rez , pretty_print=True);
        target.write( xml_str );
        target.close();

    def UploadObjectToStore(self, 
                                                    well_name,
                                                    well_uid,
                                                    wellbore_name,
                                                    wellbore_uid,
                                                    log_name,
                                                    log_uid,
                                                    replace_object_if_exists = True,
                                                    row_count_per_request = 1000):
        """ 
            summary:
                Uploads WITSML log object to WITSML store
            
            parameters:
                api          - instance of wtools_witsml_api
                schema       - instance of wtools_schemas_witsml1310 (not used currently only for future schematron reference)
                well_uid     - well uid string
                wellbore_uid - wellbore uid string
                log_uid      - log uid string
                
            returns:
                nothing
        """
        rez = objectify.fromstring(  etree.tostring(self.objectified_native_header)  )
        ns = "http://www.witsml.org/schemas/1series";
        EF = objectify.ElementMaker(annotate=False, namespace=ns, nsmap={None : ns})
        if ("nameWell" in rez.log[0].__dict__):
                rez.log[0].remove(rez.log[0].nameWell);
        #
        if ("nameWellbore" in rez.log[0].__dict__):
                rez.log[0].remove(rez.log[0].nameWellbore);
        #
        if ("name" in rez.log[0].__dict__):
                rez.log[0].remove(rez.log[0].name);
        #
        rez.log[0].insert(0, EF.nameWell( well_name ) );
        rez.log[0].insert(1, EF.nameWellbore( wellbore_name ) );
        rez.log[0].insert(2, EF.name( log_name ) );
        #
        rez.log[0].attrib["uidWell"] = well_uid;
        rez.log[0].attrib["uidWellbore"] = wellbore_uid;
        rez.log[0].attrib["uid"] = log_uid;
        #
        """ removing not required nodes (start, end index from header) """
        #

        #
        sys.stdout.write("Checking well already exists  ? "); 
        if not  self.api.isWellExists( self.schema_version , well_uid) :
            sys.stdout.write("No, Creating New One. \n");
            try:
                self.api.addWell( self.schema_version, well_uid, well_name ) 
            except:
                raise GenericStoreException("Can not create Well");
        else:
            sys.stdout.write("Yes \n");
        sys.stdout.write("Checking wellbore already exists  ? "); 
        #well_uid, wellbore_uid
        if not self.api.isWellboreExists(self.schema_version, well_uid, wellbore_uid) :
            sys.stdout.write("No, Creating New One. \n");
            try:
                self.api.addWellbore( self.schema_version, well_uid, well_name, wellbore_uid, wellbore_name)
            except:
                raise GenericStoreException("Can not create Wellbore");
        else:
            sys.stdout.write("Yes \n");
        sys.stdout.write("Checking log already exists  ? "); 
        log_exists = self.api.isLogExists(self.schema_version, well_uid, wellbore_uid, log_uid)  ;
        if (log_exists):
            sys.stdout.write("Yes \n");
            if ( not replace_object_if_exists) :
                print("We are not allowed to overwrite log ");
                raise LogAlreadyExistsException("Log object already_exists");
            print("Deleting previous log object");
            try:
                self.api.deleteLog(self.schema_version, well_uid, wellbore_uid, log_uid);
            except:
                import traceback;
                tb = traceback.format_exc();
                print(tb);
                print("Can not delete existing log object, in order to create new one");
                raise GenericStoreException("Can not delete existing log object, in order to create new one");
            log_exists = False;
        else:
            sys.stdout.write("No \n");
        #
        sys.stdout.write("Uploading new log object \n");
        start_row = 0;
        while 1:
            rezi,next_row = self.logDataObject.backToXMLObject(rez , True, False , start_row , row_count_per_request );
            
            #print xml_query;
            
            if (log_exists or (self.logDataObject.index_type == INDEX_TYPE_TIME)):
                        if ( 'startDateTimeIndex' in  rezi.log[0].__dict__ ):
                            rezi.log[0].remove(rezi.log[0].startDateTimeIndex)
                        #
                        if ( 'endDateTimeIndex' in  rezi.log[0].__dict__ ):
                            rezi.log[0].remove(rezi.log[0].endDateTimeIndex)
                        #
                        if ( 'startIndex' in  rezi.log[0].__dict__ ):
                            rezi.log[0].remove(rezi.log[0].startIndex)
                        #
                        if ( 'endIndex' in  rezi.log[0].__dict__ ):
                            rezi.log[0].remove(rezi.log[0].endIndex)
            else:
                        #todo fix this (we dont know range here)
                        if ( 'startIndex' in  rezi.log[0].__dict__ ):
                                rezi.log[0].startIndex._setText ( str( self.logDataObject.data[0].index ) );
                        
                        if ( 'endIndex' in  rezi.log[0].__dict__ ):
                                rezi.log[0].endIndex._setText ( str( self.logDataObject.lastIndexValue()) );
            
            xml_query = etree.tostring( rezi , pretty_print=True)
            
            if (not log_exists):
                sys.stdout.write("adding to store log with data range ["+str(start_row)+".."+str(next_row-1)+"] ...");                
                self.api.WMLS_AddToStore( xml_query, default_api.WITSML_OBJ_LOG);
                sys.stdout.write("OK\n");
                
            else:
                sys.stdout.write("updating in store log with data range ["+str(start_row)+".."+str(next_row-1)+"] ...");
                self.api.WMLS_UpdateInStore( xml_query, default_api.WITSML_OBJ_LOG);
                sys.stdout.write("OK\n");
            log_exists = True;
            if (next_row >= len(self.logDataObject.data) ):
                break;
            start_row = next_row;
        pass
    
    def GetNormalizedXMLForComparison(self):
        """
        returns XML string representing this object but without nodes that not play in comparison
        """
        rezi,next_row = self.logDataObject.backToXMLObject(self.objectified_native_header , True, True );
        for element in rezi.iter():
            if element.text:
                try:
                    if not (element.text.split[","]) > 1 :
                        """attempt to convert string to datetime if succeds then we replace string in element in order to normalize timestamp"""
                        as_datetime = common.xsd_dateTime_to_datetime(element.text);
                        element._setText( common.datetime_to_xsd_dateTime( as_datetime ) );
                except:
                    pass
        return etree.tostring( rezi , pretty_print=True)
    
    def getReadSchemaParser(self):
        return None;

    def getWriteSchemaParser(self):
        return None;

    
    def isEncapsulates(self, original_log):
        """
        Compare is this log is represent all of the data from original nodes. Essentially compare logs.
        """
        my_xml = self.GetNormalizedXMLForComparison();
        original_xml = original_log.GetNormalizedXMLForComparison();

        success =  common.isXMLEncapsulateAnotherXML( etree.fromstring(my_xml) , etree.fromstring(original_xml) , my_xml , original_xml)
        """
        #uncomment while debugging
        #if not success:
        if 1:
            foriginal = open("original.xml",'w');
            foriginal.write(original_xml);
            foriginal.close()
        
            finspected = open("inspected.xml",'w');
            finspected.write(my_xml);
            finspected.close()
        
            #subprocess.call(["meld", "original.xml", "inspected.xml"])
        """
        return success;











