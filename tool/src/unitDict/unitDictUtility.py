# System imports
import os
import sys
from . import unitOfMeasure
from . import unitDictGenerated
import wtl.control_prim
import wtl.testlog as testlog

__dictOfUnitOfMeasures = None
_log = testlog.log

def unit_dict_utility_init():  
     global __dictOfUnitOfMeasures 
     __dictOfUnitOfMeasures = unitDictGenerated.buildUnitDict()  

def get_unit_of_measure(annotation):
    """
         Get the unitOfMeasurment object for this annotation
         
        Parameters:
          annotation:  input annotation
          
        Returns:
              unitOfMeasurement object                  
    """
    if annotation in __dictOfUnitOfMeasures:
        return __dictOfUnitOfMeasures[annotation]
    else:
        return None

def is_valid_annotation(annotation):
    """
         Is this annotation valid ( i.e. does it exist in the unitGenerated dictionary
         
        Parameters:
          annotation:  input annotation
          
        Returns:
              True if valid annotation, False if not                    
    """
    unitOfMeasure = get_unit_of_measure(annotation)
    if ( unitOfMeasure is not None ):
        return True
    else:
       return False
 
def convert_to_base(sourceValue, sourceUnit):
    """
         Convert the provided unit ( sourceUnit ) from its base value
         
        Parameters:
          sourceValue:  value to convert
          sourceUnit:   unit of the value given 
          
        Returns:
              tuple ( base value, base Unit )                  
    """     
    unitOfMeasure = get_unit_of_measure(sourceUnit)
    if ( unitOfMeasure is not None ):
       baseValue =  unitOfMeasure.convertToBase(sourceValue)
       baseUnit = unitOfMeasure.baseUnit if unitOfMeasure.baseUnit is not None  else unitOfMeasure.annotation
       return ( baseValue, baseUnit)
    else:
       _fail("invalid sourceUnit " + sourceUnit)

def convert_from_base(sourceValue, sourceUnit):
    """
         Convert the provided unit ( sourceUnit ) to its base value
         
        Parameters:
          sourceValue:  base value to convert
          sourceUnit:   unit of the desired result
          
        Returns:
              value in desired Unit                 
    """    
    unitOfMeasure = get_unit_of_measure(sourceUnit)
    if ( unitOfMeasure is not None ):
       return unitOfMeasure.convertFromBase(sourceValue)
    else:
       _fail("invalid sourceUnit " + sourceUnit)

def convert_to_unit(sourceValue, sourceUnit, destUnit):
    """
        Convert the given value to another value that share the same base unit 
        
        Parameters:
          sourceValue:  input value
          sourceUnit:   input unit
          destUnit:     desired unit of return
          
        Returns:
              value in destUnit             
    """        
    if ( sourceValue is not None ):
        try:
           float(sourceValue)
        except ValueError:
           _fail("sourceValue is not a float " + sourceValue)
           return None
    else:
        _fail("sourceValue is None")
        return None
    
    canConvert = can_convert_units(sourceUnit, destUnit, doFail = True )
    if ( canConvert == False ):
        return None
    
    unitOfMeasSource = get_unit_of_measure(sourceUnit)
    unitOfMeasDest = get_unit_of_measure(destUnit)
    
    baseUnitValue = unitOfMeasSource.convertToBase(sourceValue)
    convertedValue = unitOfMeasDest.convertFromBase(baseUnitValue)
    return convertedValue
 
def can_convert_units(sourceUnit, destUnit, doFail = False ):
    """
        Test to validate the given units can be converted 
        
        Parameters:
          sourceUnit:   input unit
          destUnit:     desired unit of return
          doFail:       if true fail, if false just report failure
          
        Returns:
              True if can convert, False if not           
    """  
    if sourceUnit is None:
        message = "sourceUnit is None"
        if ( doFail ):
           _fail(message)
        else:
            _log(message)
        return False
    
    if destUnit is None:
        message = "destUnit is None"
        if ( doFail ):
            _fail(message)
        else:
            _log(message)
        return False
    
    # if the two units are the same, return value due to no needed conversion
    if ( sourceUnit == destUnit ):
        return sourceValue
                 
    unitOfMeasSource = get_unit_of_measure(sourceUnit)
    if ( unitOfMeasSource is None ):
        message = "sourceUnit " + sourceUnit + " is invalid annotation "
        if ( doFail ):
            _fail(message)
        else:
            _log(message)
        return False
    
    unitOfMeasDest = get_unit_of_measure(destUnit)
    if ( unitOfMeasDest is None ):
        message = "destUnit " + destUnit + " is invalid annotation "
        if ( doFail ):
            _fail(message)
        else:
            _log(message)
        return False
    
    sourceBaseUnit = unitOfMeasSource.get_base_unit()
    destBaseUnit = unitOfMeasDest.get_base_unit()
    
    if ( sourceBaseUnit is None and destBaseUnit is None):
        message = "sourceUnit "  + sourceUnit + " destUnit " + destUnit + " : both sourceBaseUnit and destBaseUnit is None, cannot convert between different baseUnits "
        if ( doFail ):
            _fail(message)
        else:
            _log(message)
        return False        
             
    if ( sourceBaseUnit is None and destBaseUnit != sourceUnit ):
        message = "sourceUnit "  + sourceUnit + " destUnit " + destUnit + " : source is baseUnit and does not match the dest base unit of " + destBaseUnit
        if ( doFail ):
            _fail(message)
        else:
            _log(message)
        return False
    
    if ( destBaseUnit is None and sourceBaseUnit != destUnit ):
        message = "sourceUnit "  + sourceUnit + " destUnit " + destUnit + " : dest is baseUnit and does not match the source base unit of " + sourceBaseUnit 
        if ( doFail ):
            _fail(message)
        else:
            _log(message)
        return False
    
    if ( destBaseUnit is not None and sourceBaseUnit is not None and destBaseUnit != sourceBaseUnit ):
        message = "sourceUnit "  + sourceUnit + " destUnit " + destUnit + " : dest base unit " + destBaseUnit + " and source base unit " + sourceBaseUnit + " do not match "
        if ( doFail ):
            _fail(message)
        else:
            _log(message)
        return False 
    
    return True;    
       
def _fail( message ):
          message = 'FAILED: ' +  message
          _log(message )
          wtl.control_prim.fail(message)        
        
unit_dict_utility_init()
