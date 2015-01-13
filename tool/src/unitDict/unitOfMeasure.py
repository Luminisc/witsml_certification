# System imports
import os
import sys
#import witsmlUnitDict

#******************************************************************************
#
# Return value from WITSML server that is not a XML documents 
# This class is used for the Return Value and SuppMsgOut
#
class UnitOfMeasure:
    """ Return value container for non XML return values """

    def __init__(self, annotation, name, quantityTypes, baseUnit, conversionToBase, dimensionalClass, catalogName, catalogSymbol, sameUnitDict, deprecated ):
        """
        Initialization of the Unit of Measure values 
        
        Parameters:
          annotation:  annotation or mnemonic unit
          name:        name of the unit
          quantityTypes:  list of quantity types
          conversionToBase:     conversionToBase 
          dimensionalClass:     dimensionalClass
          catalogName:          catalogName
          catalogSymbol:        catalogSymbol
          sameUnitDict:         sameUnitDict
          deprecated            version it was deprecated
        """

        self.annotation = annotation
        self.name = name
        self.quantityTypes = quantityTypes 
        self.baseUnit = baseUnit
        self.conversionToBase = conversionToBase
        self.dimensionalClass = dimensionalClass
        self.catalogName = catalogName
        self.catalogSymbol = catalogSymbol
        self.sameUnitDict = sameUnitDict
        self.deprecated = deprecated
        
        
    def get_annotation(self):
        """
        Get the annotation of this unit
        """

        return self.annotation
    
    def get_base_unit(self):
        """
        Get the baseUnit of this unit, if this is a baseUnit it will be None
        """        
        return self.baseUnit 
    
    def convertToBase(self, value ):
        """
        Convert the given value to a value based on the baseUnit 
        
        Parameters:
          value:  input value
        """ 
        return self.conversionToBase.convertToBase(value)       
#        if ( self.conversionToBase is not None ):
#            return self.conversionToBase.convertToBase(value)
#        else:
#            return value
        
    def convertFromBase(self, value ):
        """
        Convert the given value assumed to be based on the baseUnit 
        
        Parameters:
          value:  input value
        """ 
        return self.conversionToBase.convertFromBase(value)            
#        if ( self.conversionToBase is not None ):
#            return self.conversionToBase.convertFromBase(value)
#        else:
#            return value
        
        
    
class Conversion( object ):
    """abstract conversion routine"""
    def convertToBase( self, value ):
        raise NotImplementedError( "Should have implemented this" )
    def convertFromBase( self, value ):    
        raise NotImplementedError( "Should have implemented this" )        

class BaseConversion ( Conversion ):
    
    def __init__(self ):
        """
        Initialization of the Unit of Measure values 
        
        """
       
    def convertToBase( self, value ):
        """
        Convert the given value to a value based on the baseUnit 
        
        Parameters:
          value:  input value
        """        
        return value
    
    def convertFromBase( self, value ):
        """
        Convert the given value assumed to be based on the baseUnit 
        
        Parameters:
          value:  input value
        """        
        return value    


class FractionConversion ( Conversion ):
    
    def __init__(self, numerator, denominator ):
        """
        Initialization of the Unit of Measure values 
        
        Parameters:
          numerator:      conversion numerator
          denominator:    conversion denominator
        """
        
        self.numerator = float(numerator) 
        self.denominator = float(denominator) 
       
    def convertToBase( self, value ):
        """
        Convert the given value to a value based on the baseUnit 
        
        Parameters:
          value:  input value
        """        
        convertedValue = value * self.numerator/self.denominator 
        return convertedValue
    
    def convertFromBase( self, value ):
        """
        Convert the given value assumed to be based on the baseUnit 
        
        Parameters:
          value:  input value
        """        
        convertedValue = value * self.denominator/self.numerator 
        return convertedValue    
    

class FactorConversion ( Conversion ):
    
    def __init__(self, factor ):
        """
        Initialization of the Unit of Measure values 
        
        Parameters:
          factor:      conversion factor
        """
        
        self.factor = float(factor)  
       
    def convertToBase( self, value ):
        """
        Convert the given value to a value based on the baseUnit 
        
        Parameters:
          value:  input value
        """        
        convertedValue = value * self.factor 
        return convertedValue
    
    def convertFromBase( self, value ):
        """
        Convert the given value assumed to be based on the baseUnit 
        
        Parameters:
          value:  input value
        """        
        convertedValue = value / self.factor 
        return convertedValue    
              
class FormulaConversion ( Conversion ):
    
    def __init__(self, a, b, c, d ):
        """
        Initialization of the Unit of Measure values 
        
        Parameters:
          a:      conversion factor
          b:      conversion factor
          c:      conversion factor
          d:      conversion factor                              
        """
        
        self.a = float(a)  
        self.b = float(b)
        self.c = float(c)
        self.d = float(d)                        
       
    def convertToBase( self, value ):
        """
        Convert the given value to a value based on the baseUnit 
        
            degF > degK
            K = ( A + ( B * degF ) ) / ( C + ( D * degF )
            K = ( 2298.35 + 5 degF ) / ( 9 + 0 degF ) 
                        
        Parameters:
          value:  input value
        """  
        return ( self.a + ( self.b * value ) ) / ( self.c + ( self.d * value ));
               
    
    def convertFromBase( self, value ):
        """
        Convert the given value assumed to be based on the baseUnit 
        
                result = ( base * C/B - A/B ) / ( 1 - (( base * D )/B )) )

                if ( _b == 0.0 && _d != 0.0 ) {
                  return (( _a / input ) - _c )/_d;
                }
                else if ( _b != 0.0 && _d == 0 ) {
                  return ( ( input * _c ) - _a  )/_b;
                }
                else if ( _b == 0.0 && _d == 0.0 ) {
                   // this will not use an input value
                   throw new RuntimeException ( " _b == 0.0 && _d == 0.0 " );
                }
                else {
                    return ((input * _c/_b) - _a/_b) /(1 - (( input * _d)/_b));
                }
        
        
        Parameters:
          value:  input value
        """        
        if (self.b == 0.0 and self.d != 0.0):
                return ((self.a / value) - self.c) / self.d
        elif (self.b != 0.0 and self.d == 0):
                return ((value * self.c) - self.a) / self.b
        elif (self.b == 0.0 and self.d == 0.0):
                # this will not use an input value
                raise ConversionError(" B == 0.0 && D == 0.0 ")
        else:
                return ((value * self.c / self.b) - self.a / self.b) / (1 - ((value * self.d) / self.b))
            
class ConversionError(Exception):
     def __init__(self, value):
         self.value = value
     def __str__(self):
         return repr(self.value)            
   
