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






def report_good( st ):
    return '<font color="green">OK   :'+st+'</font><br>';

def report_bad( st ):
    return '<font color="red">FAIL  :'+st+'</font><br>';

def report_ignored( st ):
    return '<font color="grey">SKIP :'+st+'</font><br>';

def report_neutral( st ):
    return '<font color="blue">      '+st+'</font><br>';







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
    raise RuntimeError( "uknown datatype:"+datatype );

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
def compareSimpleTypeNode( element_type , original_node , inspected_node ,report, depth=0 ):
        depth_str = "";
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
            report.write( report_good(txt) );
        else:
            report.write( report_bad(txt) ); 
                     
        return rez;

def doesCollectionItemsHaveKey( col1, col2 , key ):
    for i in col1:
        if not ( key in i.__dict__ ):
            return False;
    for i in col2:
        if not ( key in i.__dict__ ):
            return False;
    return True;
        
def orderCollection( tp , unordered_original ,unordered_inspected , report, space  ):
    
    report.write( report_neutral(space+" trying to order collection of type '"+str(tp._ExpandedName.localName())+"'" ) );
    
    key = None;
    if ( "name" in tp.__dict__) and doesCollectionItemsHaveKey(unordered_original,unordered_inspected,"name"):
        key = "name";
    elif ( "mnemonic" in tp.__dict__) and doesCollectionItemsHaveKey(unordered_original,unordered_inspected,"mnemonic"):
        key = "mnemonic";
    #
    rez_original = [];
    rez_inspected = [];
    #
    if key is None:    
        #
        for k in unordered_original:
            rez_original.append(k);
        #
        for k in unordered_inspected:
            rez_inspected.append(k);
        #
        #
    else:
        report.write( report_neutral(space+"using '"+key+"' as a key for collection" ) );
        original_map = collections.OrderedDict();
        for k in unordered_original:
            #rez_original.append(k);
            original_map[k[key].text] = k 
        #
        inspected_map = collections.OrderedDict();
        for k in unordered_inspected:
            inspected_map[k[key].text] = k;
        #
        report.write( report_neutral(space+"setting original collection order" ) );
        pos = 0;
        for k, v in iter(sorted(original_map.iteritems()) ):
            rez_original.append(v);
            pos+=1;
            report.write( report_neutral(space+" element #%d ( %s = '%s' ) " % ( pos, key, v[key].text )  ) );
        #
        pos = 0;
        #
        report.write( report_neutral(space+"setting inspected collection order" ) );
        for k, v in iter(sorted(inspected_map.iteritems()) ): 
            rez_inspected.append(v);
            pos+=1;
            report.write( report_neutral(space+" element #%d ( %s = '%s' ) " % ( pos, key, v[key].text )  ) );
    report.write( report_neutral(space+" : " ) );
    return rez_original, rez_inspected;
    #localName()
    
def compareLogData(space, original , inspected, original_log , inspected_log, report):
    #report.write( report_bad( space+"Missing element '%s' in inspected XML " % elm.localName()  ) );
    report.write( report_neutral(space+"Comparing log object" ) );
    if len(original_log.curves) != len(inspected_log.curves):
        report.write( report_bad( space+"Logs have different amount of curves") );
        return False;
    
    mm_o = {};
    for c in original_log.curves:
        mm_o[c.mnemonic] = c
        
    mm_i = {};
    for c in inspected_log.curves:
        mm_i[c.mnemonic] = c
        
    
    oc = str(original.mnemonicList.text).split(",");
    ic = str(original.mnemonicList.text).split(",");

    ou = str(original.unitList.text).split(",");
    iu = str(original.unitList.text).split(",");
    
    rez = True;
    
    for itr in range( len(oc) ):
        """
        if ( not ( oc[itr] in mm_o ) ) or ( not ( oc[itr] in mm_i ) ) :
            report.write( report_bad( space+" Curve '"+oc[itr]+"' is missing from log curve info declaration ") );
            return False;
        #
        if ( not ( ic[itr] in mm_o ) ) or ( not ( ic[itr] in mm_i ) ) :
            report.write( report_bad( space+" Curve '"+ic[itr]+"' is missing from log curve info declaration ") );
            return False;
        #
        if ( mm_o[oc[itr]].uom != ou[itr] ):
            report.write( report_bad( space+"Inconsitend log : UOM for '"+oc[itr]+"' is different in declaration ") );
            return False;
        #
        if ( mm_i[ic[itr]].uom != iu[itr] ):
            report.write( report_bad( space+"Inconsitend log : UOM for '"+ic[itr]+"' is different in declaration ") );
            return False;
        #
        """
        if (mm_o[oc[itr]].uom != mm_i[oc[itr]].uom):
            report.write( report_bad( space+"Different UOM for curves '"+oc[itr]+"' :   '"+mm_o[oc[itr]].uom+"' != '"+mm_i[oc[itr]].uom+"'") );
            rez = False;
        else:
            report.write( report_good( space+"Same UOM '"+oc[itr]+"' :   '"+mm_o[oc[itr]].uom+"' == '"+mm_i[oc[itr]].uom+"'") );
        
    report.write( report_neutral(space+"Comparing log data" ) );
    
    #menominic_indexes = {};
    #for i in inspected_log.curves:
    #    menominic_indexes[ inspected_log.curves[i].mnemonic ] = i;
    
    
    for row_i in range( len(original_log.data) ):
        #report.write( report_neutral(space+"index = "+str(  original_log.data[row_i] ) ) );
        original_index_value = original_log.data[row_i].index
        inspected_index_value = inspected_log.data[row_i].index
        if (original_log.index_type == INDEX_TYPE_DEPTH):
            if ( not compareDouble( float( original_index_value ) , float ( inspected_index_value ) ) ):
                rez = False;
                report.write( report_bad( space + "different index : '" + str(original_index_value)+"' != '"+str(inspected_index_value)+"'") );
            else:
                report.write( report_good( space + " current index : '" + str(original_index_value)+"' == '"+str(inspected_index_value)+"'") );
        else:
            if (original_index_value != inspected_index_value):
                rez = False;
                report.write( report_bad( space + "different index : '" + str(original_index_value)+"' != '"+str(inspected_index_value)+"'") );
            else:
                report.write( report_good( space + " current index : '" + str(original_index_value)+"' == '"+str(inspected_index_value)+"'") );
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
                report.write( report_good( space + " >>>> validating datapoint : ["+original_log.curves[crv_i].mnemonic+"]'" + str(v1)+"' == '"+str(v2)+"'") );
            else:
                report.write( report_bad( space + " >>>> validating datapoint : ["+original_log.curves[crv_i].mnemonic+"]'" + str(v1)+"' != '"+str(v2)+"'") );
                rez = False
    #for c in range( original.curves ):
    return rez;

"""this function compares two complex types recursively"""
def doesWITSMLObjectsEqual( element_type , original_node , inspected_node , rez , report, depth=0 ):
    
    
    space = " ";
    for i in range(depth):
        space += "&nbsp;&nbsp;&nbsp;&nbsp;";
    ##############
    
    #print etree.tostring(original_node, pretty_print = True)
    #print etree.tostring(inspected_node, pretty_print = True)
    
    #print space,element_type," with (",original_node,") as (",inspected_node,")"
    
    result = rez;

    if ( element_type._ExpandedName.localName() == "genericMeasure" ):
        txt = space+"comparing using genericMeasure normalization logic  ";
        txt += " text = '"+str(original_node.text)+"'";
        txt += " uom = '"+str(original_node.attrib["uom"])+"'";
        #
        v_original,uom_original  = convertValueInImperialSystem( original_node.text, original_node.attrib["uom"] );
        v_inspected,uom_inspected = convertValueInImperialSystem( inspected_node.text, inspected_node.attrib["uom"] );
        
        txt += " Normalized ( %s[%s] == %s[%s] )" % (v_original,uom_original , v_inspected,uom_inspected) 
        rx = compareDouble( v_original , v_inspected );
        txt += " Equal : " +str( rx )
        
        if (rx):
            report.write( report_good(txt) );
        else:
            report.write( report_bad(txt) ); 
            
        return rx;
                       
        #3obj_log.genericMeasure.uom
    elif ( element_type._ExpandedName.localName() == "dimensionlessMeasure" ):
        txt = space+"comparing using dimensionlessMeasure normalization logic  ";
        txt += " text = "+str(original_node.text);
        txt += " uom = "+str(original_node.attrib["uom"]);
        #
        v_original,uom_original  = convertValueInImperialSystem( original_node.text, original_node.attrib["uom"] );
        v_inspected,uom_inspected = convertValueInImperialSystem( inspected_node.text, inspected_node.attrib["uom"] ); 
        
        txt += " Normalized ( %s[%s] == %s[%s] )" % (v_original,uom_original , v_inspected,uom_inspected) 
        rx = compareDouble( v_original , v_inspected );
        txt += " Equal : " +str( rx )
        
        if (rx):
            report.write( report_good(txt) );
        else:
            report.write( report_bad(txt) ); 
        
        return rx;
    else:
        
        for a in element_type._AttributeMap:
            report.write( report_neutral(space+" attrib: '"+a.localName()+"'" ) );
            if ( a.localName() in original_node.attrib ):
                #was value
                if ( a.localName() != "uid" ) and ( a.localName() != "uidWell" ) and ( a.localName() != "uidWellbore" ):
                    #print space,
                    #print "comparing attribute : ",a.localName();
                    
                    if not ( a.localName() in inspected_node.attrib ):
                        report.write( report_bad( space+"Missing attribute '%s' in inspected XML " % a.localName()  ) );
                        result = result and False;
                    else:
                        result = result and compareSimpleTypeNode( element_type._AttributeMap[a].dataType() , 
                                                    original_node.attrib[ a.localName() ]  , 
                                                    inspected_node.attrib[ a.localName() ] ,
                                                    report,  
                                                    depth );
                else:
                    report.write( report_ignored(space+"skipping (non data attrib) "+a.localName()) );
                
            else:
                #missing
                report.write( report_ignored(space+"skipping not used attrib "+a.localName()) );
        #print "x"
        #""" ************************ """
        if element_type._IsSimpleTypeContent():
            result = result and compareSimpleTypeNode( element_type , original_node.text,  inspected_node.text ,report, depth );
        else:
            for elm in element_type._ElementMap:#
                e = element_type._ElementMap[elm];
                report.write( report_neutral(space+" "+elm.localName()) );
                #print "element : ", elm.localName()
                #
                #if (elm.localName())        
                plural_str = "";
                if ( e.isPlural() ):
                    plural_str = "[]"
                    pass;
                
                sub_element_type = element_type._ElementMap[elm]._ElementDeclaration__elementBinding.typeDefinition();
                is_complex = not sub_element_type._IsSimpleTypeContent()
                
                complex_str = "simple";
                if ( is_complex ):
                    complex_str = "complex"
                
                if ( elm.localName() in original_node.__dict__ ):

                    #report.write( "stepping into '"+ elm.localName() +"'" );
                    
                    if ( elm.localName() == "dTimCreation" ):
                        report.write( report_good( space+"intentionally skipping 'dTimCreation' which is ment to be different " ) );
                        continue;
     
                    if ( elm.localName() == "dTimLastChange" ):
                        report.write( report_good( space+"intentionally skipping 'dTimLastChange' which is ment to be different " ) );
                        continue;
                    
                    #report.write( "testing into '"+ elm.localName() +"'" );
                    
                    #report.write( '"'+etree.tostring(inspected_node, pretty_print = True)+'"' )
                    
                    if not ( elm.localName() in inspected_node.__dict__ ):
                        #report.write( "XXXX : "+ elm.localName() +"'" );
                        report.write( report_bad( space+"Missing element '%s' in inspected XML " % elm.localName()  ) );
                        r = False;
                        result = result and r;
                            
                    #print space,"checking element : ",elm.localName(), plural_str , " ( as " , complex_str , ") ";
                    
                    
                    if ( elm.localName() ==  "logData"  ) :
                        if ( element_type._ElementMap[elm]._ElementDeclaration__elementBinding.typeDefinition()._ExpandedName.localName() == "cs_logData" ) :
                            
                            try:
                                report.write( report_neutral( space+"Parsing original log object data section"));
                                original_log = LogDataParser();
                                original_log.parseLogObjectHeader(original_node);
                                original_log.parseLogObjectData(original_node);
                                #
                                report.write( report_neutral( space+"Parsing inspected log object data section"));
                                inspected_log = LogDataParser();
                                inspected_log.parseLogObjectHeader(inspected_node);
                                inspected_log.parseLogObjectData(inspected_node);
                                #
                                report.write( report_neutral( space+"Running comparison"));
                                result = result and compareLogData( space , original_node.logData,inspected_node.logData,  original_log , inspected_log, report);
                                #report.write( report_bad( space+" comparing data section "  ) );
                            except RuntimeError, et:
                                report.write( report_bad( space+"Can comparison failed with exception "+str(et)  ) );
                                result = False;
                            continue;
                            
                    
                    
                    if ( e.isPlural() ):
                        
                        ordered_original = original_node.__dict__[elm.localName()];
                        ordered_inspected = inspected_node.__dict__[elm.localName()];
                        
                        
                        
                        if ( len(ordered_original) !=  len(ordered_inspected) ):
                            report.write( report_bad( space+"collection comparison FAILED : original collection has %d items, and inspected has %d " % ( len(ordered_original) ,  len(ordered_inspected)) ) );
                            #print space,"collection comparison FAILED : original collection has %d items, and inspected has %d " % ( len(ordered_original) ,  len(ordered_inspected) )
                            #return False;
                        else:
                            report.write( report_good( space+"collection comparison passed : original collection has %d items, and inspected has %d " % ( len(ordered_original) ,  len(ordered_inspected) )) );
                            #print space,"collection comparison passed : original collection has %d items, and inspected has %d " % ( len(ordered_original) ,  len(ordered_inspected) )
                            pass;
                        
                        
                        ordered_original, ordered_inspected = orderCollection( element_type._ElementMap[elm]._ElementDeclaration__elementBinding.typeDefinition() , ordered_original ,ordered_inspected , report, space );
                        
                        
                        
                        
                        
                        for element_pos in range( len(ordered_original) ):
                            #print space,"checking element # %d" % element_pos;
                            #if (elm.localName() in inspected_node.__dict__):
                            if 1:
                                
                                """
                                r = doesWITSMLObjectsEqual( sub_element_type , 
                                                           original_node[elm.localName()] , 
                                                           inspected_node[elm.localName()]  ,
                                                           result ,
                                                           report,
                                                           depth + 4 )
                                """
                                
                                r = doesWITSMLObjectsEqual( sub_element_type , 
                                                           ordered_original[element_pos] , 
                                                           ordered_inspected[element_pos]  ,
                                                           result ,
                                                           report,
                                                           depth + 4 )
                                
                            else:
                                report.write( report_bad( space+"missing element '%s'" % ( elm.localName() )) );
                                r = False;
                            result = result and r;
                              
                    else:
                            if (elm.localName() in inspected_node.__dict__):
                                r = doesWITSMLObjectsEqual( sub_element_type , 
                                                               original_node[elm.localName()] , 
                                                               inspected_node[elm.localName()]  ,
                                                               result ,
                                                               report,
                                                               depth + 4 )
                            else:
                                report.write( report_bad( space+"missing element '%s'" % ( elm.localName() )) );
                                r = False;
                            result = result and r;    
                    
                else:
                    report.write( report_good( space+"skipping not used element : "+elm.localName() + plural_str ) );
                    #print space,"skipping not used element : ",elm.localName() , plural_str;
            
    report.write("<br>");
    return result;
        #iterating over elements if we are in complex object

""" compare generic object with given type, amd two XML's """
def compare_genetic( type_, xml_original , xml_inspected ):
    obj_original = objectify.fromstring( xml_original );
    obj_inspected = objectify.fromstring( xml_inspected );
    report = StringIO.StringIO()
    rez = doesWITSMLObjectsEqual( type_ , obj_original , obj_inspected , True , report, depth=0 ); 
    return (rez, report.getvalue())

    
    
""" function to compare specific WITSML objects """
def witsml1411_compare_obj_attachments( xml_original , xml_inspected ):
    import witsml1411.witsml1411_obj_attachment as witsml1411_obj_attachment
    return compare_genetic( witsml1411_obj_attachment.obj_attachments, xml_original , xml_inspected )

def witsml1411_compare_obj_bhaRuns( xml_original , xml_inspected ):
    import witsml1411.witsml1411_obj_bhaRun as witsml1411_obj_bhaRun
    return compare_genetic( witsml1411_obj_bhaRun.obj_bhaRuns, xml_original , xml_inspected )
    
def witsml1411_compare_obj_cementJobs( xml_original , xml_inspected ):
    import witsml1411.witsml1411_obj_cementJob as witsml1411_obj_cementJob
    return compare_genetic( witsml1411_obj_cementJob.obj_cementJobs, xml_original , xml_inspected )
    
def witsml1411_compare_obj_changeLogs( xml_original , xml_inspected ):
    import witsml1411.witsml1411_obj_changeLog as witsml1411_obj_changeLog
    return compare_genetic( witsml1411_obj_changeLog.obj_changeLogs, xml_original , xml_inspected )
    
def witsml1411_compare_obj_convCores( xml_original , xml_inspected ):
    import witsml1411.witsml1411_obj_convCore as witsml1411_obj_convCore
    return compare_genetic( witsml1411_obj_convCore.obj_convCores, xml_original , xml_inspected )
    
def witsml1411_compare_obj_coordinateReferenceSystems( xml_original , xml_inspected ):
    import witsml1411.witsml1411_obj_coordinateReferenceSystem as witsml1411_obj_coordinateReferenceSystem
    return compare_genetic( witsml1411_obj_coordinateReferenceSystem.obj_coordinateReferenceSystems, xml_original , xml_inspected )
    
def witsml1411_compare_obj_drillReports( xml_original , xml_inspected ):
    import witsml1411.witsml1411_obj_drillReport as witsml1411_obj_drillReport
    return compare_genetic( witsml1411_obj_drillReport.drillReports, xml_original , xml_inspected )
    
def witsml1411_compare_obj_fluidsReports( xml_original , xml_inspected ):
    import witsml1411.witsml1411_obj_fluidsReport as witsml1411_obj_fluidsReport
    return compare_genetic( witsml1411_obj_fluidsReport.obj_fluidsReports, xml_original , xml_inspected )
    
def witsml1411_compare_obj_formationMarkers( xml_original , xml_inspected ):
    import witsml1411.witsml1411_obj_formationMarker as witsml1411_obj_formationMarker
    return compare_genetic( witsml1411_obj_formationMarker.obj_formationMarkers, xml_original , xml_inspected )
    
def witsml1411_compare_obj_logs( xml_original , xml_inspected ):
    import witsml1411.witsml1411_obj_log as witsml1411_obj_log
    return compare_genetic( witsml1411_obj_log.obj_logs, xml_original , xml_inspected )
    
def witsml1411_compare_obj_messages( xml_original , xml_inspected ):
    import witsml1411.witsml1411_obj_message as witsml1411_obj_message
    return compare_genetic( witsml1411_obj_message.obj_messages, xml_original , xml_inspected )
    
def witsml1411_compare_obj_mudLogs( xml_original , xml_inspected ):
    import witsml1411.witsml1411_obj_mudLog as witsml1411_obj_mudLog
    return compare_genetic( witsml1411_obj_mudLog.obj_mudLogs, xml_original , xml_inspected )
    
def witsml1411_compare_obj_objectGroups( xml_original , xml_inspected ):
    import witsml1411.witsml1411_obj_objectGroup as witsml1411_obj_objectGroup
    return compare_genetic( witsml1411_obj_objectGroup.obj_objectGroups, xml_original , xml_inspected )

def witsml1411_compare_obj_opsReports( xml_original , xml_inspected ):
    import witsml1411.witsml1411_obj_opsReport as witsml1411_obj_opsReport
    return compare_genetic( witsml1411_obj_opsReport.obj_opsReports, xml_original , xml_inspected )

def witsml1411_compare_obj_rigs( xml_original , xml_inspected ):
    import witsml1411.witsml1411_obj_rig as witsml1411_obj_rig
    return compare_genetic( witsml1411_obj_rig.obj_rigs, xml_original , xml_inspected )

def witsml1411_compare_obj_risks( xml_original , xml_inspected ):
    import witsml1411.witsml1411_obj_risk as witsml1411_obj_risk
    return compare_genetic( witsml1411_obj_risk.obj_risks, xml_original , xml_inspected )

def witsml1411_compare_obj_sidewallCores( xml_original , xml_inspected ):
    import witsml1411.witsml1411_obj_sidewallCore as witsml1411_obj_sidewallCore
    return compare_genetic( witsml1411_obj_sidewallCore.obj_sidewallCores, xml_original , xml_inspected )

def witsml1411_compare_obj_stimJobs( xml_original , xml_inspected ):
    import witsml1411.witsml1411_obj_stimJob as witsml1411_obj_stimJob
    return compare_genetic( witsml1411_obj_stimJob.obj_stimJobs, xml_original , xml_inspected )

def witsml1411_compare_obj_surveyPrograms( xml_original , xml_inspected ):
    import witsml1411.witsml1411_obj_surveyProgram as witsml1411_obj_surveyProgram
    return compare_genetic( witsml1411_obj_surveyProgram.obj_surveyPrograms, xml_original , xml_inspected )

def witsml1411_compare_obj_targets( xml_original , xml_inspected ):
    import witsml1411.witsml1411_obj_target as witsml1411_obj_target
    return compare_genetic( witsml1411_obj_target.obj_targets, xml_original , xml_inspected )

def witsml1411_compare_obj_toolErrorModels( xml_original , xml_inspected ):
    import witsml1411.witsml1411_obj_toolErrorModel as witsml1411_obj_toolErrorModel
    return compare_genetic( witsml1411_obj_toolErrorModel.obj_toolErrorModels, xml_original , xml_inspected )

def witsml1411_compare_obj_toolErrorTermSets( xml_original , xml_inspected ):
    import witsml1411.witsml1411_obj_toolErrorTermSet as witsml1411_obj_toolErrorTermSet
    return compare_genetic( witsml1411_obj_toolErrorTermSet.obj_toolErrorTermSets, xml_original , xml_inspected )

def witsml1411_compare_obj_trajectorys( xml_original , xml_inspected ):
    import witsml1411.witsml1411_obj_trajectory as witsml1411_obj_trajectory
    return compare_genetic( witsml1411_obj_trajectory.obj_trajectorys, xml_original , xml_inspected )

def witsml1411_compare_obj_tubulars( xml_original , xml_inspected ):
    import witsml1411.witsml1411_obj_tubular as witsml1411_obj_tubular
    return compare_genetic( witsml1411_obj_tubular.obj_tubulars, xml_original , xml_inspected )

def witsml1411_compare_obj_wbGeometry( xml_original , xml_inspected ):
    import witsml1411.witsml1411_obj_wbGeometry as witsml1411_obj_wbGeometry
    return compare_genetic( witsml1411_obj_wbGeometry.obj_wbGeometrys, xml_original , xml_inspected )

def witsml1411_compare_obj_wells( xml_original , xml_inspected ):
    import witsml1411.witsml1411_obj_well as witsml1411_obj_well
    return compare_genetic( witsml1411_obj_well.obj_wells, xml_original , xml_inspected )

def witsml1411_compare_obj_wellbores( xml_original , xml_inspected ):
    import witsml1411.witsml1411_obj_wellbore as witsml1411_obj_wellbore
    return compare_genetic( witsml1411_obj_wellbore.obj_wellbores, xml_original , xml_inspected )



if __name__ == '__main__':
    pass;

