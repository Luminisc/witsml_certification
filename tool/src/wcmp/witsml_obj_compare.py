'''
Created on Feb 23, 2013

@organization: PetroDAQ Inc
@author: Denys Metelskyy
@contact: 2121 Golden Rd, Suite 1-A. The Woodlands, TX 77381. denys.metelskyy@petrodaq.com  
'''


import pyxb
import iso8601
import StringIO;
import collections;

from lxml import etree;
from lxml import objectify;

import sys;






INDEX_TYPE_TIME = 0;
INDEX_TYPE_DEPTH = 1;






def report_good( st, diff_only, current_path  ):
    if (diff_only == True):
        return "";
    return '<font color="green">OK   :'+st+'</font><br>';

def report_bad( st , diff_only , current_path ):
    if (current_path == None):
        current_path = ["***"];
    if (diff_only == True):
        return "Comparison Fail : "+st+ "   Node : "+ str("/".join(current_path)) +"\n";
    return '<font color="red">FAIL  :'+st+'</font><br>';

def report_ignored( st , diff_only , current_path):
    if (diff_only == True):
        return "";
    return '<font color="grey">SKIP :'+st+'</font><br>';

def report_neutral( st , diff_only , current_path ):
    if (diff_only == True):
        return "";
    return '<font color="blue">      '+st+'</font><br>';


def append_node( path_ , nd_ ):
    """ 
    summary:
        adds node to the path and return result 
        
    parameters:
        path_ - path where node should be added 
        nd_ - node that need to be added to path 
        
    result:
        return path with added node
    """
    
    if path_ is None:
        path_ = [];
        pass;
    else:
        pass; 
    rez = [];
    for nd in path_:
        rez.append( nd );
    rez.append( nd_ );
    return rez;





def parseLogCurveValueAsDatatype(value, datatype, nullvalue):
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
        #return round(float(value),ROUND_DIGITS);
        return float(value);
        
    if (datatype == "date time"):
        #return common.xsd_dateTime_to_datetime(value);
        return iso8601.parse_date( value );
        
    if (datatype == "string"):
        return value;
    print "uknown datatype:"+datatype
    raise RuntimeError( "unknown datatype:"+datatype );

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

class LogDataParser:
    
    def __init__(self):
        self.curves = [];
        self.data = []
        self.index_type = INDEX_TYPE_DEPTH;
        self.start = None;
        self.end = None;
        self.lastAddedIndex = None;
    
    def preview(self):
        """
        Utility function display data (used for debugging purposes)
        """
        
        curves_str = "";
        ix = 0;
        for curve in self.curves:
            curves_str = curves_str+"\t"+curve.mnemonic+"("+str(ix)+")";
            ix = ix + 1
        print curves_str;
        for data_row in self.data:
            data_str = "";
            ix = 0;
            for data_point in data_row.values:
                data_str = data_str+"\t"+str(data_point)+"("+str(ix)+")"
                ix = ix + 1
            print data_str

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
        
        if ( 'nullValue' in  obj.__dict__ ):
            self.nullvalue = obj.nullValue;
        
        if ( 'startDateTimeIndex' in  obj.__dict__ ):
            self.start = iso8601.parse_date( str(obj.startDateTimeIndex) );
            #self.start_as_double = basic_utils.xsd_dateTime_to_datetime(self.start);
            self.index_type = INDEX_TYPE_TIME;
                
        if ( 'endDateTimeIndex' in  obj.__dict__ ):
            self.end = iso8601.parse_date( str( obj.endDateTimeIndex) );
            #self.end_as_double = basic_utils.xsd_dateTime_to_datetime(self.end);
            self.index_type = INDEX_TYPE_TIME;
                
        if ( 'startIndex' in  obj.__dict__ ):
            self.start = float( str(obj.startIndex) );
            #self.start_as_double = float( self.start );
            self.index_type = INDEX_TYPE_DEPTH;
        
        if ( 'endIndex' in  obj.__dict__ ):
            self.end = float( str(obj.endIndex) );
            #self.end_as_double = float( self.end );
            self.index_type = INDEX_TYPE_DEPTH;
        
        for crv_iter in obj.logCurveInfo:
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
        
        #print etree.tostring( obj, pretty_print = True );
        
        for logData_iter in obj.logData:
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
                    raise RuntimeError("There is new curve '"+new_mnemonics[mnemonic_i]+"' in log array, that was not seen in header")
                    
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
                        new_row.values[ curve_index ] =    parseLogCurveValueAsDatatype(values[i], self.curves[curve_index].datatype , self.curves[curve_index].nullvalue );
                    except:
                        print "What fail : datarow "+str(data_iter);
                        
                        print (" curve = '"+ 
                               self.curves[curve_index].mnemonic + 
                               "' datatype: (" + 
                               self.curves[curve_index].datatype + 
                               ") attempted to parse value: '"+values[i]+"' column #"+str(curve_index));
                               
                        raise;
                if len(self.data)>1:
                    if (self.data[len(self.data)-1].index == new_row.index):
                        continue;
                self.data.append(new_row);

    


def compareDouble(value1, value2):
    return value2-value1 < 0.0001;
    
""" unit of measurement conversion to base unit system """
def convertValueInImperialSystem( value_ , uom_ ):
    value = float(value_);
    uom = uom_.upper().strip();
    if uom == "M":
        return (value * 3.28084 , "ft"  );
    elif uom == "CM":
        return (value * 0.393701 , "in"  );
    elif uom == "DEGC":
        return ( (9/5) * value + 32 , "degF"  );
    elif uom == "KPA":
        return ( value * 0.145 , "degF"  );
    elif uom == "M/S":
        return ( value * 3.28084 , "ft/s"  );
    elif uom == "M/HR":
        return ( value * 3.28084 , "ft/hr"  );
    elif uom == "G/CM3":
        return ( value * 8.34540445 , "lb/galUS"  );
    elif uom == "L/MIN":
        return ( value * 0.264172 , "galUS/min"  );
    elif uom == "L":
        return ( value * 0.264172 , "galUS"  );
    return (value, uom_)


""" compare simple types convers string to internal type and normalizes """
def compareSimpleTypeNode( element_type , original_node , inspected_node ,report, depth , diff_only , current_path ):
        depth_str = "";
        if not diff_only:
            for i in range(depth):
                depth_str += "&nbsp;&nbsp;&nbsp;&nbsp;";
        txt = depth_str + ">" + str(original_node) + " =?= " + str(inspected_node) +"  ";
        if issubclass(element_type, pyxb.binding.datatypes.int):
            txt += "( as int )"
            rez = int(original_node) == int(inspected_node);
        if issubclass(element_type, pyxb.binding.datatypes.long):
            txt += "( as long )"
            rez = int(original_node) == int(inspected_node);
        if issubclass(element_type, pyxb.binding.datatypes.float):
            txt += "( as float )"
            rez = compareDouble( float(original_node), float(inspected_node) )
        if issubclass(element_type, pyxb.binding.datatypes.double):
            txt += "( as double )"
            rez = compareDouble( float(original_node), float(inspected_node) )
        if issubclass(element_type, pyxb.binding.datatypes.boolean):
            txt += "( as str )"
            rez = str(original_node) == str(inspected_node)
        if issubclass(element_type, pyxb.binding.datatypes.datetime.datetime):
            txt += "( as datetime )"
            rez = iso8601.parse_date(original_node) == iso8601.parse_date(inspected_node);
        else:
            txt += "( as generic )"
            rez = str(original_node) == str(inspected_node);
        
        txt += " Equal ? : "+str(rez);
        
        if (rez):
            report.write( report_good(txt,diff_only, current_path) );
        else:
            report.write( report_bad(txt,diff_only, current_path) ); 
                     
        return rez;

def doesCollectionItemsHaveUIDKey( col1, col2 ):
    """
    summary: 
        check is two collections contain uid key
        
    parameters:
        col1 - collection #1
        col2 - collection #2
        
    returns:
        returns boolean flag whether uid key exists in both collections 
    """
    
    for i in col1:
        if not ( "uid" in i.attrib ):
            return False;
    for i in col2:
        if not ( "uid" in i.attrib ):
            return False;
    return True;
    
    
def doesCollectionItemsHaveKey( col1, col2 , key ):
    """
    summary: 
        check is two collections contain given key ( for ordering )
        
    parameters:
        col1 - collection #1
        col2 - collection #2
        key - key for which collections should be scanned
        
    returns:
        returns boolean flag whether given key exists in both collections 
    """
    
    for i in col1:
        if not ( key in i.__dict__ ):
            return False;
    for i in col2:
        if not ( key in i.__dict__ ):
            return False;
    return True;
    
def orderCollectionSimple( col ):
    nd = {}
    for c in col:
        nd[c.text] = c;
    rez = [];
    for k,v in sorted(dict.iteritems(nd)):
        rez.append(v);
    return rez;
    
    
    
def orderCollection( tp , unordered_original ,unordered_inspected , report, space , diff_only , current_path  ):
    """
    summary: 
        orders two collections for comparison
        
    parameters:
        tp - node type
        unordered_original  - original collection to be ordered
        unordered_inspected - inspected collection to be ordered
        report - string IO for reporting
        space - indent used in reporing
        diff_only - flag is report should be different items only
        current_path - path for current node to indicate in report
    
    returns:
        tuple of two ordered collections original, inspected 
    """
      
    report.write( report_neutral(space+" trying to order collection of type '"+str(tp._ExpandedName.localName())+"'", diff_only, current_path ) );
    key = None; 
    if ( doesCollectionItemsHaveUIDKey( unordered_original , unordered_inspected ) ):
        key = "uid";

    rez_original = [];
    rez_inspected = [];
    #
    if key is None:    
        #
        if tp._IsSimpleTypeContent():
            
            
            rez_original = orderCollectionSimple(unordered_original);
            rez_inspected = orderCollectionSimple(unordered_inspected);
            """
            for k in unordered_original:
                print k.text;
            
            for k in unordered_inspected:
                rez_inspected.append(k);
            """
            
        else:
            for k in unordered_original:
                rez_original.append(k);
            #
            for k in unordered_inspected:
                rez_inspected.append(k);
        #
        #
    else:        
        report.write( report_neutral(space+"using '"+key+"' as a key for collection" , diff_only , current_path ) );
        original_map = collections.OrderedDict();
        for k in unordered_original:
            #rez_original.append(k);
            original_map[ k.attrib[key] ] = k 
        #
        inspected_map = collections.OrderedDict();
        for k in unordered_inspected:
            inspected_map[ k.attrib[key] ] = k;
        #
        report.write( report_neutral(space+"setting original collection order" , diff_only , current_path ) );
        pos = 0;
        for k, v in iter(sorted(original_map.iteritems()) ):
            rez_original.append(v);
            pos+=1;
            report.write( report_neutral(space+" element #%d ( %s = '%s' ) " % ( pos, key, v.attrib[key] ) , diff_only , current_path ) );
        #
        pos = 0;
        #
        report.write( report_neutral(space+"setting inspected collection order", diff_only , current_path ) );
        for k, v in iter(sorted(inspected_map.iteritems()) ): 
            rez_inspected.append(v);
            pos+=1;
            report.write( report_neutral(space+" element #%d ( %s = '%s' ) " % ( pos, key, v.attrib[key] ) , diff_only , current_path) );
    report.write( report_neutral(space+" : " , diff_only , current_path) );
    return rez_original, rez_inspected;
    #localName()
    
def compareLogData(space, original , inspected, original_log , inspected_log, report , diff_only , current_path ):
    """
    summary: 
        compare <logData> section
        
    parameters:
        space - reporting indent
        original - orginal xml node object
        inspected - inspected orginal xml node object
        original_log - pointer to log which this log data belong to
        inspected_log - pointer to log which this log data belong to (inspected)
        report - string IO for reporting
        diff_only - flag is report should be different items only
        current_path - path for current node to indicate in report
    
    returns:
        boolean flag is objects are equal
    """
      
    #
    #
    #
    report.write( report_neutral(space+"Comparing log object" , diff_only , current_path) );
    if len(original_log.curves) != len(inspected_log.curves):
        report.write( report_bad( space+"Logs have different amount of curves" , diff_only , current_path) );
        return False;
    #
    mm_o = {};
    for c in original_log.curves:
        mm_o[c.mnemonic] = c
    #    
    mm_i = {};
    for c in inspected_log.curves:
        mm_i[c.mnemonic] = c
    #    
    #
    oc = str(original.mnemonicList.text).split(",");
    ic = str(original.mnemonicList.text).split(",");
    #
    ou = str(original.unitList.text).split(",");
    iu = str(original.unitList.text).split(",");
    #
    rez = True;
    #
    for itr in range( len(oc) ):
        if (mm_o[oc[itr]].uom != mm_i[oc[itr]].uom):
            report.write( report_bad( space+"Different UOM for curves '"+oc[itr]+"' :   '"+mm_o[oc[itr]].uom+"' != '"+mm_i[oc[itr]].uom+"'" , diff_only , current_path) );
            rez = False;
        else:
            report.write( report_good( space+"Same UOM '"+oc[itr]+"' :   '"+mm_o[oc[itr]].uom+"' == '"+mm_i[oc[itr]].uom+"'" , diff_only , current_path ) );
    #
    report.write( report_neutral(space+"Comparing log data" , diff_only , current_path ) );
    #
    for row_i in range( len(original_log.data) ):
        #report.write( report_neutral(space+"index = "+str(  original_log.data[row_i] ) ) );
        original_index_value = original_log.data[row_i].index
        inspected_index_value = inspected_log.data[row_i].index
        if (original_log.index_type == INDEX_TYPE_DEPTH):
            if ( not compareDouble( float( original_index_value ) , float ( inspected_index_value ) ) ):
                rez = False;
                report.write( report_bad( space + "different index : '" + str(original_index_value)+"' != '"+str(inspected_index_value)+"'", diff_only , current_path) );
            else:
                report.write( report_good( space + " current index : '" + str(original_index_value)+"' == '"+str(inspected_index_value)+"'", diff_only , current_path) );
        else:
            if (original_index_value != inspected_index_value):
                rez = False;
                report.write( report_bad( space + "different index : '" + str(original_index_value)+"' != '"+str(inspected_index_value)+"'", diff_only , current_path) );
            else:
                report.write( report_good( space + " current index : '" + str(original_index_value)+"' == '"+str(inspected_index_value)+"'", diff_only , current_path) );
        #                             
        #  
        for crv_i in range( len( original_log.curves ) ):
            v1 = original_log.data[ row_i].values[  original_log.getCurveIndex( original_log.curves[crv_i].mnemonic ) ]
            v2 = inspected_log.data[row_i].values[ inspected_log.getCurveIndex( original_log.curves[crv_i].mnemonic ) ]
            same = False;
            if (original_log.curves[crv_i].datatype == "double"):
                same = compareDouble(v1, v2);
                #
            elif (original_log.curves[crv_i].datatype == "date time"):
                same = v1 == v2;
                #
            else:
                same = v1 == v2;
                #
            if (same):
                report.write( report_good( space + " >>>> validating datapoint : ["+original_log.curves[crv_i].mnemonic+"]'" + str(v1)+"' == '"+str(v2)+"'" , diff_only, current_path) );
            else:
                report.write( report_bad( space + " >>>> validating datapoint : ["+original_log.curves[crv_i].mnemonic+"]'" + str(v1)+"' != '"+str(v2)+"'" , diff_only , current_path) );
                rez = False
    return rez;

"""this function compares two complex types recursively"""
def doesWITSMLObjectsEqual( element_type , original_node , inspected_node , rez , report, depth, diff_only , current_path):
    """
    summary: 
        compares two complex objects recursively
        
    parameters:
        element_type - type of WITSML node
        xml_original - Original XML object
        xml_inspected - Inspected XML object
        rez - result flag carried through recursion
        report - string IO for reporting 
        depth - integer value to indicate indent in report 
        diff_only - flag is report should be different items only
        current_path - path for current node to indicate in report
    
    returns:
        boolean flag is objects are equal
    """
      
    #
    # building report string 
    #
    #
    if (diff_only):
        space = "";
    else:
        space = " ";
        for i in range(depth):
            space += "&nbsp;&nbsp;&nbsp;&nbsp;";
    result = rez;    
    # comparison of generic measure elements ( value and uom )
    if  ( ( element_type._ExpandedName.localName() == "genericMeasure" ) or 
        ( element_type._ExpandedName.localName() == "planeAngleMeasure" ) or 
        ( element_type._ExpandedName.localName() == "lengthMeasure" ) or 
        ( element_type._ExpandedName.localName() == "measuredDepthCoord" ) or
        ( element_type._ExpandedName.localName() == "volumePerVolumeMeasure" )or
        ( element_type._ExpandedName.localName() == "equivalentPerMassMeasure" )
         ):
        txt = space+"comparing using genericMeasure/planeAngleMeasure/lengthMeasure normalization logic  ";
        txt += " text = '"+str(original_node.text)+"'";
        txt += " uom = '"+str(original_node.attrib["uom"])+"'";
        #
        v_original,uom_original  = convertValueInImperialSystem( original_node.text, original_node.attrib["uom"]  );
        v_inspected,uom_inspected = convertValueInImperialSystem( inspected_node.text, inspected_node.attrib["uom"] );
        #
        txt += " Normalized ( %s[%s] == %s[%s] )" % (v_original,uom_original , v_inspected,uom_inspected) 
        rx = compareDouble( v_original , v_inspected );
        txt += " Equal : " +str( rx )
        #
        if (rx):
            report.write( report_good(txt , diff_only , current_path) );
        else:
            report.write( report_bad(txt , diff_only , current_path) ); 
        return rx;
    #                   
    elif ( element_type._ExpandedName.localName() == "dimensionlessMeasure" ):
        txt = space+"comparing using dimensionlessMeasure normalization logic  ";
        txt += " text = "+str(original_node.text);
        txt += " uom = "+str(original_node.attrib["uom"]);
        #
        v_original,uom_original  = convertValueInImperialSystem( original_node.text, original_node.attrib["uom"] );
        v_inspected,uom_inspected = convertValueInImperialSystem( inspected_node.text, inspected_node.attrib["uom"] ); 
        #
        txt += " Normalized ( %s[%s] == %s[%s] )" % (v_original,uom_original , v_inspected,uom_inspected) 
        rx = compareDouble( v_original , v_inspected );
        txt += " Equal : " +str( rx )
        #
        if (rx):
            report.write( report_good(txt, diff_only , current_path) );
        else:
            report.write( report_bad(txt , diff_only , current_path) ); 
        return rx;
    else:        
        ppp = current_path[:];
        for a in element_type._AttributeMap:
            current_path = ppp[:]
            current_path = append_node( current_path , a.localName() );
            report.write( report_neutral(space+" attrib: '"+a.localName()+"'", diff_only , current_path ) );
            if ( a.localName() in original_node.attrib ):
                #was value
                if ( a.localName() != "uid" ) and ( a.localName() != "uidWell" ) and ( a.localName() != "uidWellbore" ):
                    #
                    if not ( a.localName() in inspected_node.attrib ):
                        report.write( report_bad( space+"Missing attribute '%s' in inspected XML " % a.localName() , diff_only , current_path ) );
                        result = result and False;
                    else:
                        result = result and compareSimpleTypeNode( element_type._AttributeMap[a].dataType() , 
                                                    original_node.attrib[ a.localName() ]  , 
                                                    inspected_node.attrib[ a.localName() ] ,
                                                    report,  
                                                    depth,
                                                    diff_only,
                                                    current_path );
                else:
                    report.write( report_ignored(space+"skipping (non data attrib) "+a.localName() , diff_only, current_path) );
                
            else:
                #missing
                report.write( report_ignored(space+"skipping not used attrib "+a.localName() , diff_only , current_path) );
        #
        #
        # checking if content is simple 
        #
        if element_type._IsSimpleTypeContent():
            #
            #
            # comparison of simple objects
            #
            result = result and compareSimpleTypeNode( element_type , original_node.text,  inspected_node.text ,report, depth , diff_only , current_path );
        else:
            #
            #
            # comparison of complex objects
            #
            for elm in element_type._ElementMap:#
                current_path = ppp[:]
                current_path = append_node( current_path , elm.localName() );
                e = element_type._ElementMap[elm];
                report.write( report_neutral(space+" "+elm.localName() , diff_only , current_path) );
                #
                plural_str = "";
                if ( e.isPlural() ):
                    plural_str = "[]"
                    pass;
                #
                sub_element_type = element_type._ElementMap[elm]._ElementDeclaration__elementBinding.typeDefinition();
                is_complex = not sub_element_type._IsSimpleTypeContent()
                #
                complex_str = "simple";
                if ( is_complex ):
                    complex_str = "complex"
                #
                if ( elm.localName() in original_node.__dict__ ):
                    #
                    # 
                    # Checking for elements that ment to be different
                    #
                    if ( elm.localName() == "dTimCreation" ):
                        report.write( report_good( space+"intentionally skipping 'dTimCreation' which is ment to be different " , diff_only , current_path ) );
                        continue;
                    
                    if ( elm.localName() == "isActive" ):
                        report.write( report_good( space+"intentionally skipping 'isActive' which is ment to be different " , diff_only , current_path ) );
                        continue;
                    
                    if ( elm.localName() == "dTimLastChange" ):
                        report.write( report_good( space+"intentionally skipping 'dTimLastChange' which is ment to be different " , diff_only , current_path) );
                        continue;

                    if ( elm.localName() == "documentInfo" ):
                        report.write( report_good( space+"intentionally skipping 'documentInfo' which is ment to be different " ,diff_only , current_path ) );
                        continue;

                    if ( elm.localName() == "mdMn" ):
                        report.write( report_good( space+"intentionally skipping 'mdMn' which is a non writeable field  " , diff_only  ,current_path ) );
                        continue;

                    if ( elm.localName() == "mdMx" ):
                        report.write( report_good( space+"intentionally skipping 'mdMx' which is a non writeable field  " , diff_only , current_path ) );
                        continue;

                    if ( elm.localName() == "objectGrowing" ):
                        report.write( report_good( space+"intentionally skipping 'objectGrowing' which is a non writeable field  " , diff_only , current_path ) );
                        continue;
                    #
                    if not ( elm.localName() in inspected_node.__dict__ ):
                        report.write( report_bad( space+"Missing element '%s' in inspected XML " % elm.localName() , diff_only , current_path ) );
                        r = False;
                        result = result and r;

                    #
                    #
                    # Special processing of logData section
                    #
                    if ( elm.localName() ==  "logData"  ) :
                        if ( element_type._ElementMap[elm]._ElementDeclaration__elementBinding.typeDefinition()._ExpandedName.localName() == "cs_logData" ) :
                            
                            try:
                                report.write( report_neutral( space+"Parsing original log object data section" , diff_only , current_path ));
                                original_log = LogDataParser();
                                original_log.parseLogObjectHeader(original_node);
                                original_log.parseLogObjectData(original_node);
                                #
                                report.write( report_neutral( space+"Parsing inspected log object data section" , diff_only , current_path));
                                inspected_log = LogDataParser();
                                inspected_log.parseLogObjectHeader(inspected_node);
                                inspected_log.parseLogObjectData(inspected_node);
                                #
                                report.write( report_neutral( space+"Running comparison" , diff_only , current_path));
                                result = result and compareLogData( space , original_node.logData,inspected_node.logData,  original_log , inspected_log, report , diff_only , current_path);
                                #report.write( report_bad( space+" comparing data section "  ) );
                            except RuntimeError, et:
                                report.write( report_bad( space+"Can comparison failed with exception "+str(et) , diff_only , current_path ) );
                                result = False;
                            continue;
                            
                    
                    #
                    # Comparison of plural objects
                    #
                    if ( e.isPlural() ):
                        ordered_original = original_node.__dict__[elm.localName()];
                        ordered_inspected = inspected_node.__dict__[elm.localName()];
                        #
                        # Checking length if it not same no point to compare items
                        #
                        if ( len(ordered_original) !=  len(ordered_inspected) ):
                            report.write( report_bad( space+"collection comparison FAILED : original collection has %d items, and inspected has %d " % ( len(ordered_original) ,  len(ordered_inspected)) , diff_only , current_path) );
                        else:
                            report.write( report_good( space+"collection comparison passed : original collection has %d items, and inspected has %d " % ( len(ordered_original) ,  len(ordered_inspected)  ) , diff_only , current_path ) );
                            pass;
                        #
                        #
                        # ordering two collections
                        #
                        ordered_original, ordered_inspected = orderCollection( element_type._ElementMap[elm]._ElementDeclaration__elementBinding.typeDefinition() , ordered_original ,ordered_inspected , report, space,  diff_only , current_path );
                        #
                        # recursively running comparison function
                        #
                        for element_pos in range( len(ordered_original) ):
                            if 1:
                                r = doesWITSMLObjectsEqual( sub_element_type , 
                                                           ordered_original[element_pos] , 
                                                           ordered_inspected[element_pos]  ,
                                                           result ,
                                                           report,
                                                           depth + 4,
                                                           diff_only,
                                                           current_path 
                                                           )
                                
                            else:
                                report.write( report_bad( space+"missing element '%s'" % ( elm.localName() ) , diff_only, current_path) );
                                r = False;
                            result = result and r;
                              
                    else:
                            #
                            # Comparison non plural objects
                            #
                            if (elm.localName() in inspected_node.__dict__):
                                r = doesWITSMLObjectsEqual( sub_element_type , 
                                                               original_node[elm.localName()] , 
                                                               inspected_node[elm.localName()]  ,
                                                               result ,
                                                               report,
                                                               depth + 4 , 
                                                               diff_only ,
                                                               current_path  
                                                               )
                            else:
                                report.write( report_bad( space+"missing element '%s'" % ( elm.localName() ) , diff_only , current_path ) );
                                r = False;
                            result = result and r;    
                    
                else:
                    report.write( report_good( space+"skipping not used element : "+elm.localName() + plural_str , diff_only , current_path ) );
    if not diff_only:        
        report.write("<br>");
    return result;

""" compare generic object with given type, amd two XML's """
def compare_genetic( type_, xml_original , xml_inspected , diff_only ):
    """
    summary: 
        compares objects of given type, original, and inspected xml document.
        
    parameters:
        type_ - Datatype of WITSML object that will be compared
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
        
    obj_original = objectify.fromstring( xml_original );
    obj_inspected = objectify.fromstring( xml_inspected );
    report = StringIO.StringIO()
    current_path = [];
    rez = doesWITSMLObjectsEqual( type_ , obj_original , obj_inspected , True , report, 0, diff_only , current_path); 
    return (rez, report.getvalue())


    
    
    
    
    
#
#
#
#
#
#  1.4.1.1
#
#
#
#
#
    
    
    
    
    
    
""" function to compare specific WITSML objects """
def witsml1411_compare_obj_attachments( xml_original , xml_inspected , diff_only = False ):  
    """
    summary: 
        compares WITSML 1.4.1.1 attachments objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
    
    import witsml1411.witsml1411_obj_attachment as witsml1411_obj_attachment
    return compare_genetic( witsml1411_obj_attachment.obj_attachments, xml_original , xml_inspected , diff_only )

def witsml1411_compare_obj_bhaRuns( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares WITSML 1.4.1.1 bhaRuns objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """

    import witsml1411.witsml1411_obj_bhaRun as witsml1411_obj_bhaRun
    return compare_genetic( witsml1411_obj_bhaRun.obj_bhaRuns, xml_original , xml_inspected , diff_only )
    
def witsml1411_compare_obj_cementJobs( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural cementJob objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """

    import witsml1411.witsml1411_obj_cementJob as witsml1411_obj_cementJob
    return compare_genetic( witsml1411_obj_cementJob.obj_cementJobs, xml_original , xml_inspected , diff_only)
    
def witsml1411_compare_obj_changeLogs( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural changeLog objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
    import witsml1411.witsml1411_obj_changeLog as witsml1411_obj_changeLog
    return compare_genetic( witsml1411_obj_changeLog.obj_changeLogs, xml_original , xml_inspected , diff_only)
    
def witsml1411_compare_obj_convCores( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural convCore objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
        
    import witsml1411.witsml1411_obj_convCore as witsml1411_obj_convCore
    return compare_genetic( witsml1411_obj_convCore.obj_convCores, xml_original , xml_inspected , diff_only)
    
def witsml1411_compare_obj_coordinateReferenceSystems( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural coordinateReferenceSystems objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
    
    import witsml1411.witsml1411_obj_coordinateReferenceSystem as witsml1411_obj_coordinateReferenceSystem
    return compare_genetic( witsml1411_obj_coordinateReferenceSystem.obj_coordinateReferenceSystems, xml_original , xml_inspected , diff_only)
    
def witsml1411_compare_obj_drillReports( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural drillReport objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
    
    import witsml1411.witsml1411_obj_drillReport as witsml1411_obj_drillReport
    return compare_genetic( witsml1411_obj_drillReport.drillReports, xml_original , xml_inspected , diff_only )
    
def witsml1411_compare_obj_fluidsReports( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural fluidsReport objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
        
    import witsml1411.witsml1411_obj_fluidsReport as witsml1411_obj_fluidsReport
    return compare_genetic( witsml1411_obj_fluidsReport.obj_fluidsReports, xml_original , xml_inspected , diff_only )
    
def witsml1411_compare_obj_formationMarkers( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural formationMarker objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
        
    import witsml1411.witsml1411_obj_formationMarker as witsml1411_obj_formationMarker
    return compare_genetic( witsml1411_obj_formationMarker.obj_formationMarkers, xml_original , xml_inspected , diff_only)
    
def witsml1411_compare_obj_logs( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural log objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
            
    import witsml1411.witsml1411_obj_log as witsml1411_obj_log
    return compare_genetic( witsml1411_obj_log.obj_logs, xml_original , xml_inspected , diff_only )
    
def witsml1411_compare_obj_messages( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural message objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
        
    import witsml1411.witsml1411_obj_message as witsml1411_obj_message
    return compare_genetic( witsml1411_obj_message.obj_messages, xml_original , xml_inspected , diff_only )
    
def witsml1411_compare_obj_mudLogs( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural mudLog objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
        
    import witsml1411.witsml1411_obj_mudLog as witsml1411_obj_mudLog
    return compare_genetic( witsml1411_obj_mudLog.obj_mudLogs, xml_original , xml_inspected , diff_only )
    
def witsml1411_compare_obj_objectGroups( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural objectGroup objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
        
    import witsml1411.witsml1411_obj_objectGroup as witsml1411_obj_objectGroup
    return compare_genetic( witsml1411_obj_objectGroup.obj_objectGroups, xml_original , xml_inspected  , diff_only)

def witsml1411_compare_obj_opsReports( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural opsReport objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1411.witsml1411_obj_opsReport as witsml1411_obj_opsReport
    return compare_genetic( witsml1411_obj_opsReport.obj_opsReports, xml_original , xml_inspected , diff_only )

def witsml1411_compare_obj_rigs( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural rig objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1411.witsml1411_obj_rig as witsml1411_obj_rig
    return compare_genetic( witsml1411_obj_rig.obj_rigs, xml_original , xml_inspected )

def witsml1411_compare_obj_risks( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural risk objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1411.witsml1411_obj_risk as witsml1411_obj_risk
    return compare_genetic( witsml1411_obj_risk.obj_risks, xml_original , xml_inspected )

def witsml1411_compare_obj_sidewallCores( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural risk sidewallCore giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1411.witsml1411_obj_sidewallCore as witsml1411_obj_sidewallCore
    return compare_genetic( witsml1411_obj_sidewallCore.obj_sidewallCores, xml_original , xml_inspected , diff_only)

def witsml1411_compare_obj_stimJobs( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural stimJob objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1411.witsml1411_obj_stimJob as witsml1411_obj_stimJob
    return compare_genetic( witsml1411_obj_stimJob.obj_stimJobs, xml_original , xml_inspected )

def witsml1411_compare_obj_surveyPrograms( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural surveyProgram objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1411.witsml1411_obj_surveyProgram as witsml1411_obj_surveyProgram
    return compare_genetic( witsml1411_obj_surveyProgram.obj_surveyPrograms, xml_original , xml_inspected  , diff_only)

def witsml1411_compare_obj_targets( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural target objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1411.witsml1411_obj_target as witsml1411_obj_target
    return compare_genetic( witsml1411_obj_target.obj_targets, xml_original , xml_inspected , diff_only)

def witsml1411_compare_obj_toolErrorModels( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural toolErrorModel objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1411.witsml1411_obj_toolErrorModel as witsml1411_obj_toolErrorModel
    return compare_genetic( witsml1411_obj_toolErrorModel.obj_toolErrorModels, xml_original , xml_inspected , diff_only )

def witsml1411_compare_obj_toolErrorTermSets( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural toolErrorTermSet objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1411.witsml1411_obj_toolErrorTermSet as witsml1411_obj_toolErrorTermSet
    return compare_genetic( witsml1411_obj_toolErrorTermSet.obj_toolErrorTermSets, xml_original , xml_inspected  , diff_only)

def witsml1411_compare_obj_trajectorys( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural trajectory objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1411.witsml1411_obj_trajectory as witsml1411_obj_trajectory
    return compare_genetic( witsml1411_obj_trajectory.obj_trajectorys, xml_original , xml_inspected , diff_only )

def witsml1411_compare_obj_tubulars( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural tubular objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1411.witsml1411_obj_tubular as witsml1411_obj_tubular
    return compare_genetic( witsml1411_obj_tubular.obj_tubulars, xml_original , xml_inspected , diff_only)

def witsml1411_compare_obj_wbGeometry( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural wbGeomertry objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1411.witsml1411_obj_wbGeometry as witsml1411_obj_wbGeometry
    return compare_genetic( witsml1411_obj_wbGeometry.obj_wbGeometrys, xml_original , xml_inspected , diff_only)

def witsml1411_compare_obj_wells( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural well objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1411.witsml1411_obj_well as witsml1411_obj_well
    return compare_genetic( witsml1411_obj_well.obj_wells, xml_original , xml_inspected , diff_only)

def witsml1411_compare_obj_wellbores( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural wellbore objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1411.witsml1411_obj_wellbore as witsml1411_obj_wellbore
    return compare_genetic( witsml1411_obj_wellbore.obj_wellbores, xml_original , xml_inspected , diff_only)


    
#
#
#
#
#  1.4.1.0
#
#
#


    
    
""" function to compare specific WITSML objects """
def witsml1410_compare_obj_attachments( xml_original , xml_inspected , diff_only = False ):  
    """
    summary: 
        compares WITSML 1.4.1.0 attachments objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
    
    import witsml1410.witsml1410_obj_attachment as witsml1410_obj_attachment
    return compare_genetic( witsml1410_obj_attachment.obj_attachments, xml_original , xml_inspected , diff_only )

def witsml1410_compare_obj_bhaRuns( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares WITSML 1.4.1.0 bhaRuns objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """

    import witsml1410.witsml1410_obj_bhaRun as witsml1410_obj_bhaRun
    return compare_genetic( witsml1410_obj_bhaRun.obj_bhaRuns, xml_original , xml_inspected , diff_only )
    
def witsml1410_compare_obj_cementJobs( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural cementJob objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """

    import witsml1410.witsml1410_obj_cementJob as witsml1410_obj_cementJob
    return compare_genetic( witsml1410_obj_cementJob.obj_cementJobs, xml_original , xml_inspected , diff_only)
    
def witsml1410_compare_obj_changeLogs( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural changeLog objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
    import witsml1410.witsml1410_obj_changeLog as witsml1410_obj_changeLog
    return compare_genetic( witsml1410_obj_changeLog.obj_changeLogs, xml_original , xml_inspected , diff_only)
    
def witsml1410_compare_obj_convCores( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural convCore objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
        
    import witsml1410.witsml1410_obj_convCore as witsml1410_obj_convCore
    return compare_genetic( witsml1410_obj_convCore.obj_convCores, xml_original , xml_inspected , diff_only)
    
def witsml1410_compare_obj_coordinateReferenceSystems( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural coordinateReferenceSystems objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
    
    import witsml1410.witsml1410_obj_coordinateReferenceSystem as witsml1410_obj_coordinateReferenceSystem
    return compare_genetic( witsml1410_obj_coordinateReferenceSystem.obj_coordinateReferenceSystems, xml_original , xml_inspected , diff_only)
    
def witsml1410_compare_obj_drillReports( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural drillReport objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
    
    import witsml1410.witsml1410_obj_drillReport as witsml1410_obj_drillReport
    return compare_genetic( witsml1410_obj_drillReport.drillReports, xml_original , xml_inspected , diff_only )
    
def witsml1410_compare_obj_fluidsReports( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural fluidsReport objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
        
    import witsml1410.witsml1410_obj_fluidsReport as witsml1410_obj_fluidsReport
    return compare_genetic( witsml1410_obj_fluidsReport.obj_fluidsReports, xml_original , xml_inspected , diff_only )
    
def witsml1410_compare_obj_formationMarkers( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural formationMarker objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
        
    import witsml1410.witsml1410_obj_formationMarker as witsml1410_obj_formationMarker
    return compare_genetic( witsml1410_obj_formationMarker.obj_formationMarkers, xml_original , xml_inspected , diff_only)
    
def witsml1410_compare_obj_logs( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural log objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
            
    import witsml1410.witsml1410_obj_log as witsml1410_obj_log
    return compare_genetic( witsml1410_obj_log.obj_logs, xml_original , xml_inspected , diff_only )
    
def witsml1410_compare_obj_messages( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural message objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
        
    import witsml1410.witsml1410_obj_message as witsml1410_obj_message
    return compare_genetic( witsml1410_obj_message.obj_messages, xml_original , xml_inspected , diff_only )
    
def witsml1410_compare_obj_mudLogs( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural mudLog objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
        
    import witsml1410.witsml1410_obj_mudLog as witsml1410_obj_mudLog
    return compare_genetic( witsml1410_obj_mudLog.obj_mudLogs, xml_original , xml_inspected , diff_only )
    
def witsml1410_compare_obj_objectGroups( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural objectGroup objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
        
    import witsml1410.witsml1410_obj_objectGroup as witsml1410_obj_objectGroup
    return compare_genetic( witsml1410_obj_objectGroup.obj_objectGroups, xml_original , xml_inspected  , diff_only)

def witsml1410_compare_obj_opsReports( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural opsReport objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1410.witsml1410_obj_opsReport as witsml1410_obj_opsReport
    return compare_genetic( witsml1410_obj_opsReport.obj_opsReports, xml_original , xml_inspected , diff_only )

def witsml1410_compare_obj_rigs( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural rig objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1410.witsml1410_obj_rig as witsml1410_obj_rig
    return compare_genetic( witsml1410_obj_rig.obj_rigs, xml_original , xml_inspected )

def witsml1410_compare_obj_risks( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural risk objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1410.witsml1410_obj_risk as witsml1410_obj_risk
    return compare_genetic( witsml1410_obj_risk.obj_risks, xml_original , xml_inspected )

def witsml1410_compare_obj_sidewallCores( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural risk sidewallCore giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1410.witsml1410_obj_sidewallCore as witsml1410_obj_sidewallCore
    return compare_genetic( witsml1410_obj_sidewallCore.obj_sidewallCores, xml_original , xml_inspected , diff_only)

def witsml1410_compare_obj_stimJobs( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural stimJob objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1410.witsml1410_obj_stimJob as witsml1410_obj_stimJob
    return compare_genetic( witsml1410_obj_stimJob.obj_stimJobs, xml_original , xml_inspected )

def witsml1410_compare_obj_surveyPrograms( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural surveyProgram objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1410.witsml1410_obj_surveyProgram as witsml1410_obj_surveyProgram
    return compare_genetic( witsml1410_obj_surveyProgram.obj_surveyPrograms, xml_original , xml_inspected  , diff_only)

def witsml1410_compare_obj_targets( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural target objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1410.witsml1410_obj_target as witsml1410_obj_target
    return compare_genetic( witsml1410_obj_target.obj_targets, xml_original , xml_inspected , diff_only)

def witsml1410_compare_obj_toolErrorModels( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural toolErrorModel objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1410.witsml1410_obj_toolErrorModel as witsml1410_obj_toolErrorModel
    return compare_genetic( witsml1410_obj_toolErrorModel.obj_toolErrorModels, xml_original , xml_inspected , diff_only )

def witsml1410_compare_obj_toolErrorTermSets( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural toolErrorTermSet objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1410.witsml1410_obj_toolErrorTermSet as witsml1410_obj_toolErrorTermSet
    return compare_genetic( witsml1410_obj_toolErrorTermSet.obj_toolErrorTermSets, xml_original , xml_inspected  , diff_only)

def witsml1410_compare_obj_trajectorys( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural trajectory objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1410.witsml1410_obj_trajectory as witsml1410_obj_trajectory
    return compare_genetic( witsml1410_obj_trajectory.obj_trajectorys, xml_original , xml_inspected , diff_only )

def witsml1410_compare_obj_tubulars( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural tubular objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1410.witsml1410_obj_tubular as witsml1410_obj_tubular
    return compare_genetic( witsml1410_obj_tubular.obj_tubulars, xml_original , xml_inspected , diff_only)

def witsml1410_compare_obj_wbGeometry( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural wbGeomertry objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1410.witsml1410_obj_wbGeometry as witsml1410_obj_wbGeometry
    return compare_genetic( witsml1410_obj_wbGeometry.obj_wbGeometrys, xml_original , xml_inspected , diff_only)

def witsml1410_compare_obj_wells( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural well objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1410.witsml1410_obj_well as witsml1410_obj_well
    return compare_genetic( witsml1410_obj_well.obj_wells, xml_original , xml_inspected , diff_only)

def witsml1410_compare_obj_wellbores( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural wellbore objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1410.witsml1410_obj_wellbore as witsml1410_obj_wellbore
    return compare_genetic( witsml1410_obj_wellbore.obj_wellbores, xml_original , xml_inspected , diff_only)

#
#
#
#
#
#  1.3.1.1
#
#
#
#
#


def witsml1311_compare_obj_bhaRuns( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares WITSML 1.3.1.1 bhaRuns objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """

    import witsml1311.witsml1311_obj_bhaRun as witsml1311_obj_bhaRun
    return compare_genetic( witsml1311_obj_bhaRun.obj_bhaRuns, xml_original , xml_inspected , diff_only )
    
def witsml1311_compare_obj_cementJobs( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural cementJob objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """

    import witsml1311.witsml1311_obj_cementJob as witsml1311_obj_cementJob
    return compare_genetic( witsml1311_obj_cementJob.obj_cementJobs, xml_original , xml_inspected , diff_only)
    
def witsml1311_compare_obj_changeLogs( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural changeLog objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
    import witsml1311.witsml1311_obj_changeLog as witsml1311_obj_changeLog
    return compare_genetic( witsml1311_obj_changeLog.obj_changeLogs, xml_original , xml_inspected , diff_only)
    
def witsml1311_compare_obj_convCores( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural convCore objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
        
    import witsml1311.witsml1311_obj_convCore as witsml1311_obj_convCore
    return compare_genetic( witsml1311_obj_convCore.obj_convCores, xml_original , xml_inspected , diff_only)
    
def witsml1311_compare_obj_coordinateReferenceSystems( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural coordinateReferenceSystems objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
    
    import witsml1311.witsml1311_obj_coordinateReferenceSystem as witsml1311_obj_coordinateReferenceSystem
    return compare_genetic( witsml1311_obj_coordinateReferenceSystem.obj_coordinateReferenceSystems, xml_original , xml_inspected , diff_only)
    
def witsml1311_compare_obj_drillReports( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural drillReport objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
    
    import witsml1311.witsml1311_obj_drillReport as witsml1311_obj_drillReport
    return compare_genetic( witsml1311_obj_drillReport.drillReports, xml_original , xml_inspected , diff_only )
    
def witsml1311_compare_obj_fluidsReports( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural fluidsReport objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
        
    import witsml1311.witsml1311_obj_fluidsReport as witsml1311_obj_fluidsReport
    return compare_genetic( witsml1311_obj_fluidsReport.obj_fluidsReports, xml_original , xml_inspected , diff_only )
    
def witsml1311_compare_obj_formationMarkers( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural formationMarker objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
        
    import witsml1311.witsml1311_obj_formationMarker as witsml1311_obj_formationMarker
    return compare_genetic( witsml1311_obj_formationMarker.obj_formationMarkers, xml_original , xml_inspected , diff_only)
    
def witsml1311_compare_obj_logs( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural log objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
            
    import witsml1311.witsml1311_obj_log as witsml1311_obj_log
    return compare_genetic( witsml1311_obj_log.obj_logs, xml_original , xml_inspected , diff_only )
    
def witsml1311_compare_obj_messages( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural message objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
        
    import witsml1311.witsml1311_obj_message as witsml1311_obj_message
    return compare_genetic( witsml1311_obj_message.obj_messages, xml_original , xml_inspected , diff_only )
    
def witsml1311_compare_obj_mudLogs( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural mudLog objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
        
    import witsml1311.witsml1311_obj_mudLog as witsml1311_obj_mudLog
    return compare_genetic( witsml1311_obj_mudLog.obj_mudLogs, xml_original , xml_inspected , diff_only )
    
def witsml1311_compare_obj_objectGroups( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural objectGroup objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
        
    import witsml1311.witsml1311_obj_objectGroup as witsml1311_obj_objectGroup
    return compare_genetic( witsml1311_obj_objectGroup.obj_objectGroups, xml_original , xml_inspected  , diff_only)

def witsml1311_compare_obj_opsReports( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural opsReport objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1311.witsml1311_obj_opsReport as witsml1311_obj_opsReport
    return compare_genetic( witsml1311_obj_opsReport.obj_opsReports, xml_original , xml_inspected , diff_only )

def witsml1311_compare_obj_rigs( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural rig objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1311.witsml1311_obj_rig as witsml1311_obj_rig
    return compare_genetic( witsml1311_obj_rig.obj_rigs, xml_original , xml_inspected )

def witsml1311_compare_obj_risks( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural risk objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1311.witsml1311_obj_risk as witsml1311_obj_risk
    return compare_genetic( witsml1311_obj_risk.obj_risks, xml_original , xml_inspected )

def witsml1311_compare_obj_sidewallCores( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural risk sidewallCore giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1311.witsml1311_obj_sidewallCore as witsml1311_obj_sidewallCore
    return compare_genetic( witsml1311_obj_sidewallCore.obj_sidewallCores, xml_original , xml_inspected , diff_only)

def witsml1311_compare_obj_stimJobs( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural stimJob objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1311.witsml1311_obj_stimJob as witsml1311_obj_stimJob
    return compare_genetic( witsml1311_obj_stimJob.obj_stimJobs, xml_original , xml_inspected )

def witsml1311_compare_obj_surveyPrograms( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural surveyProgram objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1311.witsml1311_obj_surveyProgram as witsml1311_obj_surveyProgram
    return compare_genetic( witsml1311_obj_surveyProgram.obj_surveyPrograms, xml_original , xml_inspected  , diff_only)

def witsml1311_compare_obj_targets( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural target objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1311.witsml1311_obj_target as witsml1311_obj_target
    return compare_genetic( witsml1311_obj_target.obj_targets, xml_original , xml_inspected , diff_only)

def witsml1311_compare_obj_toolErrorModels( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural toolErrorModel objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1311.witsml1311_obj_toolErrorModel as witsml1311_obj_toolErrorModel
    return compare_genetic( witsml1311_obj_toolErrorModel.obj_toolErrorModels, xml_original , xml_inspected , diff_only )

def witsml1311_compare_obj_toolErrorTermSets( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural toolErrorTermSet objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1311.witsml1311_obj_toolErrorTermSet as witsml1311_obj_toolErrorTermSet
    return compare_genetic( witsml1311_obj_toolErrorTermSet.obj_toolErrorTermSets, xml_original , xml_inspected  , diff_only)

def witsml1311_compare_obj_trajectorys( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural trajectory objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1311.witsml1311_obj_trajectory as witsml1311_obj_trajectory
    return compare_genetic( witsml1311_obj_trajectory.obj_trajectorys, xml_original , xml_inspected , diff_only )

def witsml1311_compare_obj_tubulars( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural tubular objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1311.witsml1311_obj_tubular as witsml1311_obj_tubular
    return compare_genetic( witsml1311_obj_tubular.obj_tubulars, xml_original , xml_inspected , diff_only)

def witsml1311_compare_obj_wbGeometry( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural wbGeomertry objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1311.witsml1311_obj_wbGeometry as witsml1311_obj_wbGeometry
    return compare_genetic( witsml1311_obj_wbGeometry.obj_wbGeometrys, xml_original , xml_inspected , diff_only)

def witsml1311_compare_obj_wells( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural well objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1311.witsml1311_obj_well as witsml1311_obj_well
    return compare_genetic( witsml1311_obj_well.obj_wells, xml_original , xml_inspected , diff_only)

def witsml1311_compare_obj_wellbores( xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural wellbore objects giving original, and inspected xml document.
        
    parameters:
        xml_original - Original XML document 
        xml_inspected - Inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
      
    import witsml1311.witsml1311_obj_wellbore as witsml1311_obj_wellbore
    return compare_genetic( witsml1311_obj_wellbore.obj_wellbores, xml_original , xml_inspected , diff_only)



ComparisonFunctions = {


    '1.3.1.1':{
        'bhaRun'                        : witsml1311_compare_obj_bhaRuns                    ,
        'cementJob'                     : witsml1311_compare_obj_cementJobs                 ,
        'convCore'                      : witsml1311_compare_obj_convCores                  ,
        'coordinateReferenceSystem'     : witsml1311_compare_obj_coordinateReferenceSystems ,
        'drillReport'                   : witsml1311_compare_obj_drillReports               ,
        'fluidsReport'                  : witsml1311_compare_obj_fluidsReports              ,
        'formationMarker'               : witsml1311_compare_obj_formationMarkers           ,
        'log'                           : witsml1311_compare_obj_logs                       ,
        'message'                       : witsml1311_compare_obj_messages                   ,
        'mudLog'                        : witsml1311_compare_obj_mudLogs                    ,
        'objectGroup'                   : witsml1311_compare_obj_objectGroups               ,
        'opsReport'                     : witsml1311_compare_obj_opsReports                 ,
        'rig'                           : witsml1311_compare_obj_rigs                       ,
        'risk'                          : witsml1311_compare_obj_risks                      ,
        'sidewallCore'                  : witsml1311_compare_obj_sidewallCores              ,
        'stimJob'                       : witsml1311_compare_obj_stimJobs                   ,
        'surveyProgram'                 : witsml1311_compare_obj_surveyPrograms             ,
        'target'                        : witsml1311_compare_obj_targets                    ,
        'toolErrorModel'                : witsml1311_compare_obj_toolErrorModels            ,
        'toolErrorTermSet'              : witsml1311_compare_obj_toolErrorTermSets          ,
        'trajectory'                    : witsml1311_compare_obj_trajectorys                ,
        'tubular'                       : witsml1311_compare_obj_tubulars                   ,
        'wbGeometry'                    : witsml1311_compare_obj_wbGeometry                 ,
        'well'                          : witsml1311_compare_obj_wells                      ,
        'wellbore'                      : witsml1311_compare_obj_wellbores                  ,
    },


    '1.4.1.0':{
        'attachment'                    : witsml1410_compare_obj_attachments                ,
        'bhaRun'                        : witsml1410_compare_obj_bhaRuns                    ,
        'cementJob'                     : witsml1410_compare_obj_cementJobs                 ,
        'changeLog'                     : witsml1410_compare_obj_changeLogs                 ,
        'convCore'                      : witsml1410_compare_obj_convCores                  ,
        'coordinateReferenceSystem'     : witsml1410_compare_obj_coordinateReferenceSystems ,
        'drillReport'                   : witsml1410_compare_obj_drillReports               ,
        'fluidsReport'                  : witsml1410_compare_obj_fluidsReports              ,
        'formationMarker'               : witsml1410_compare_obj_formationMarkers           ,
        'log'                           : witsml1410_compare_obj_logs                       ,
        'message'                       : witsml1410_compare_obj_messages                   ,
        'mudLog'                        : witsml1410_compare_obj_mudLogs                    ,
        'objectGroup'                   : witsml1410_compare_obj_objectGroups               ,
        'opsReport'                     : witsml1410_compare_obj_opsReports                 ,
        'rig'                           : witsml1410_compare_obj_rigs                       ,
        'risk'                          : witsml1410_compare_obj_risks                      ,
        'sidewallCore'                  : witsml1410_compare_obj_sidewallCores              ,
        'stimJob'                       : witsml1410_compare_obj_stimJobs                   ,
        'surveyProgram'                 : witsml1410_compare_obj_surveyPrograms             ,
        'target'                        : witsml1410_compare_obj_targets                    ,
        'toolErrorModel'                : witsml1410_compare_obj_toolErrorModels            ,
        'toolErrorTermSet'              : witsml1410_compare_obj_toolErrorTermSets          ,
        'trajectory'                    : witsml1410_compare_obj_trajectorys                ,
        'tubular'                       : witsml1410_compare_obj_tubulars                   ,
        'wbGeometry'                    : witsml1410_compare_obj_wbGeometry                 ,
        'well'                          : witsml1410_compare_obj_wells                      ,
        'wellbore'                      : witsml1410_compare_obj_wellbores                  ,
    },

    '1.4.1.1':{
        'attachment'                    : witsml1411_compare_obj_attachments                ,
        'bhaRun'                        : witsml1411_compare_obj_bhaRuns                    ,
        'cementJob'                     : witsml1411_compare_obj_cementJobs                 ,
        'changeLog'                     : witsml1411_compare_obj_changeLogs                 ,
        'convCore'                      : witsml1411_compare_obj_convCores                  ,
        'coordinateReferenceSystem'     : witsml1411_compare_obj_coordinateReferenceSystems ,
        'drillReport'                   : witsml1411_compare_obj_drillReports               ,
        'fluidsReport'                  : witsml1411_compare_obj_fluidsReports              ,
        'formationMarker'               : witsml1411_compare_obj_formationMarkers           ,
        'log'                           : witsml1411_compare_obj_logs                       ,
        'message'                       : witsml1411_compare_obj_messages                   ,
        'mudLog'                        : witsml1411_compare_obj_mudLogs                    ,
        'objectGroup'                   : witsml1411_compare_obj_objectGroups               ,
        'opsReport'                     : witsml1411_compare_obj_opsReports                 ,
        'rig'                           : witsml1411_compare_obj_rigs                       ,
        'risk'                          : witsml1411_compare_obj_risks                      ,
        'sidewallCore'                  : witsml1411_compare_obj_sidewallCores              ,
        'stimJob'                       : witsml1411_compare_obj_stimJobs                   ,
        'surveyProgram'                 : witsml1411_compare_obj_surveyPrograms             ,
        'target'                        : witsml1411_compare_obj_targets                    ,
        'toolErrorModel'                : witsml1411_compare_obj_toolErrorModels            ,
        'toolErrorTermSet'              : witsml1411_compare_obj_toolErrorTermSets          ,
        'trajectory'                    : witsml1411_compare_obj_trajectorys                ,
        'tubular'                       : witsml1411_compare_obj_tubulars                   ,
        'wbGeometry'                    : witsml1411_compare_obj_wbGeometry                 ,
        'well'                          : witsml1411_compare_obj_wells                      ,
        'wellbore'                      : witsml1411_compare_obj_wellbores                  ,
    }

}

def removeLoadedModules():
    while 1:
        was_garbage = False;
        for m in sys.modules:
            if (m.startswith("wcmp.")) or (m.startswith("pyxb.")):
                was_garbage = True;
                del (sys.modules[m]) 
                break;
        if (not was_garbage):
            break;

def compareWITSMLObject(schema_version, object_type, xml_original , xml_inspected  , diff_only = False):
    """
    summary: 
        compares two plural well objects giving original, and inspected xml document.
        
    parameters:
        schema_version - comparison version like "1.3.1.1" / "1.4.1.0" / "1.4.1.1"
        object_type - WMLType like "log" ,"mudlog" ... 
        xml_original - original XML document 
        xml_inspected - inspected XML document
        diff_only - flag indicate report shall contain only difference information, or full HTML comparison report
        
    returns:
        tuple of  comparison result , report string 
    """
    # 
    if ( schema_version in ComparisonFunctions ):
        if ( object_type in ComparisonFunctions[schema_version] ):
            rx = ComparisonFunctions[schema_version][object_type]( xml_original , xml_inspected  , diff_only);   
            removeLoadedModules();
            return rx;
    #
    removeLoadedModules();
    return False,"Can not locate comparison function "+schema_version+"/"+object_type+" ";

if __name__ == '__main__':
    pass;

