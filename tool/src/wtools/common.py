'''
Created on Jun 28, 2012

@organization: PetroDAQ Inc
@author: Denys Metelskyy
@contact: 2121 Golden Rd, Suite 1-A. The Woodlands, TX 77381. denys.metelskyy@petrodaq.com  
'''

import datetime
import time
import wtools.iso8601 as iso8601
import sys

from subprocess import call
from lxml import etree

def datetime_to_xsd_dateTime( dt ):
    """ 
    this method converts datetime object to string in UTC
    parameters:
       dt : datetime object that need to be converted to string
    returns:
       string representing UTC, of dt
    """
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    
def xsd_dateTime_to_datetime( datetime_str ):
    """ 
    this method converts iso8601 to datetime object
    parameters:
       datetime_str : string that need to be converted to datetime
    returns:
       string datetime (or exeption will be raised)
    """
    return iso8601.parse_date(datetime_str);

def getPathForNode(node):
    """
    produces string path to node 
    parameters:
       node : lxml node element
    returns:
       string in form of /xxx/aaa/bbb/ 
    """
    node_i = node;
    rez = "";
    while node_i is not None:
        rez = str(node_i.xpath('local-name()')) + "/" + rez;
        node_i = node_i.getparent();
    return rez;

def wipeCommentsNode(nd):
    """
    removes all comment for subtree nd 
    parameters:
       node : lxml root node element which comments should be vanished
    returns:
       Nothing (mutable operation)
    """
    for element in list(nd):
        if (element.tag is etree.Comment):
            nd.remove(element);
        else:
            wipeCommentsNode(element);
    
def wipeComments(xml):
    """
    removes all comment for xml
    parameters:
       input xml string
    returns:
       xml string without commnents 
    """
    xtree = etree.fromstring(xml)
    wipeCommentsNode(xtree);
    return etree.tostring( xtree , pretty_print=True)
            

def tag_without_namespace(element):
    return str(element.xpath('local-name()'))



def isXMLEncapsulateAnotherXML( inspected_tree , original_tree , inspected_xml , original_xml , depth = 0):
    """
    Checks weather XML tree 1 encapsulates XML tree 2. It is essentially comparison of XML, It will succeed if:
        - every node of original tree is exists in inspected XML in same order (if it a text node then node text is matches) 
        - every attribute of original node exists in inspected node. 
        - comparison of subtree succeeded.
    this will require that WITSML objects (XML's) was normalized:
        - all nodes that allowed to be different are removed 
        - all attributes that are optional should be Nulled.
        - all nodes that contain datetime values need to be normalized to same format (timezone)
        - all nodes that contain double values need to be rounded to specific comparison precission
    """
    """ if logic will be verbose then space is preceding empty string that will be used to ident XML """  
    space = "";
    for sp_i in range(depth):
        space = space + "    ";
    #
    """ getting list of children from XML that need to be inspected """
    other_log_elements = list(inspected_tree)
    #
    """ this node contains text ?  - we'll compare it"""
    if (original_tree.text):
        #print "comparing : \n"+original_tree.text+" \n== \n"+inspected_tree.text+"\n\n";
        if ( len(original_tree.text.strip())>0 ):
            """text is not empty - ?"""
            if (original_tree.text != inspected_tree.text):
                    """Oops! text is different print problem and return False"""
                    print("");
                    print(space+"text is different for node ( "+ getPathForNode(original_tree) +
                                            " ) \n    '" + original_tree.text+ 
                                            "' \n != \n    '" + inspected_tree.text 
                                            );
                    print("");
                    print(space+"Different lines in XML : \n    original xml line"+str(original_tree.sourceline)+" : '"+ original_xml.splitlines(True)[original_tree.sourceline-1]+"'"+
                                                        "\n    inspected xml line"+str(inspected_tree.sourceline)+" : '"+ inspected_xml.splitlines(True)[inspected_tree.sourceline-1])+"'";
                    return False ;
    """checking attributes;"""
    for attrib_original in original_tree.items():
        """ if attribute contains "{" then it is a namespace or other weired node that we ignore """
        if (attrib_original[0].find("{") > -1):
            continue;
        """ it is regular attribute using flag to indicate is it in array"""
        found_in_inspected_attrib_list = False;
        for attrib_inspected in inspected_tree.items():
            """names (first part of tuple) is equal then its the same attribute"""
            if (attrib_original[0] == attrib_inspected[0]):
                """setting flag to found"""
                found_in_inspected_attrib_list = True;
                """if text (second part of tuple) is different then report problem and return"""
                if (attrib_original[1] != attrib_inspected[1]):
                    print space+"value for attribute : "+getPathForNode(original_tree) +"["+ attrib_original[0]+"] - Does Not Match! "
                    print space+"    '"+attrib_original[1] + "' != '" + attrib_inspected[1]+"'"
                    return False;
        """if flag was not set then it attribute is missing from inspected node"""
        if (not found_in_inspected_attrib_list):
            print "missing attribute : "+getPathForNode(original_tree) +"["+ attrib_original[0]+"]"
            return False; 
    """attributes are checked, checking sub elements and recursively call it self on new elements"""
    pos_i = -1;
    for element in list(original_tree):
        """is it a comment ? - skipping... """
        if (element.tag is etree.Comment):
            continue;
        """flag will indicate that element is not found in inspected XML"""
        found = False;
        """moving further across childs of inspected XML trying to find one we looking for"""
        while 1:
            pos_i = pos_i + 1
            """ are we of bounds ? - breaking """
            if ( pos_i >= len(other_log_elements) ):
                break;
            """ is it a comment node ? - skipping """
            if (other_log_elements[pos_i].tag is etree.Comment):
                continue;
            #print space+"checking node : "+getPathForNode(element)+element.text + ". Is this ? - " +getPathForNode(other_log_elements[pos_i])+other_log_elements[pos_i].text ;
            """checking is tag of element are same - if they are, recursively compare subtree."""
            
            #print space+"checking : '"+tag_without_namespace(other_log_elements[pos_i])+"'=='"+tag_without_namespace(element)+"'";
            if ( tag_without_namespace(other_log_elements[pos_i]) == tag_without_namespace(element) ):
                
                """comparing subtree recursevly calling it self"""
                if not isXMLEncapsulateAnotherXML( other_log_elements[pos_i] , element ,  inspected_xml , original_xml , depth+1):
                    """if subtree comparison returned False we return False to recursively go up stack"""
                    #print "X"
                    return False;
                found  = True;
                break;
        """if we did not found element we just return false"""
        if not found:
            print " Matching element is not found, attempted to find something similar to :\n "+  etree.tostring( element , pretty_print=True) 
            return False;
        else:
            pass;
    """all good we succeded in this subtree"""
    return True;
