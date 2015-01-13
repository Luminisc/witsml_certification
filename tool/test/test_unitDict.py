'''
Created on June 20, 2013

@organization: Halliburton
@author: Bill Riegel
@contact: briegel@lgc.com  
'''

import sys;
import os;
sys.path.append("../src/unitDict")
sys.path.append("../src/wtl")

import unittest
import mocking
import unitDictUtility
import unitDictConstants
import wtl.control_prim

class UnitDictTest(unittest.TestCase, mocking.MockingTestMixin):

    def setUp(self):
        unittest.TestCase.setUp(self)
        mocking.MockingTestMixin.setUp(self)

        wtl.script.Script.init()

        self.stub(wtl.control_prim, "fail")


    def tearDown(self):
        unittest.TestCase.tearDown(self)
        mocking.MockingTestMixin.tearDown(self)
        

    def test_valid_annotations(self):
        valid = unitDictUtility.is_valid_annotation("m")
        self.assertTrue(valid)
        self.assertFalse(wtl.control_prim.fail.called)

        valid = unitDictUtility.is_valid_annotation(unitDictConstants.METRE)
        self.assertTrue(valid)
        self.assertFalse(wtl.control_prim.fail.called)
                         
        valid = unitDictUtility.is_valid_annotation("ft")
        self.assertTrue(valid)
        self.assertFalse(wtl.control_prim.fail.called)

        valid = unitDictUtility.is_valid_annotation(unitDictConstants.FOOT)
        self.assertTrue(valid)
        self.assertFalse(wtl.control_prim.fail.called)
                
        valid = unitDictUtility.is_valid_annotation("in")
        self.assertTrue(valid) 
        self.assertFalse(wtl.control_prim.fail.called)

        valid = unitDictUtility.is_valid_annotation(unitDictConstants.INCH)
        self.assertTrue(valid) 
        self.assertFalse(wtl.control_prim.fail.called)
             
    def test_invalid_annotations(self):
        valid = unitDictUtility.is_valid_annotation("mmmm")
        self.assertFalse(valid)
        self.assertFalse(wtl.control_prim.fail.called)
                
        valid = unitDictUtility.is_valid_annotation("ftfff")
        self.assertFalse(valid)
        self.assertFalse(wtl.control_prim.fail.called)
                
        valid = unitDictUtility.is_valid_annotation("innn")
        self.assertFalse(valid)
        self.assertFalse(wtl.control_prim.fail.called)              
                  
    def test_convert_to_base(self):
        # convert 3 feet to meters
        value = unitDictUtility.convert_to_base(3, unitDictConstants.FOOT)
        #value = unitDictUtility.convert_to_base(3,"ft")
        self.assertTrue(self.compare(value[0],0.9144)) 
        self.assertTrue(value[1] == "m") 
        self.assertTrue(value[1] == unitDictConstants.METRE)
        self.assertFalse(wtl.control_prim.fail.called)         
        
    def test_convert_to_base_bad(self):
        # bad annotation
        value = unitDictUtility.convert_to_base(3,"ftf")
        self.assertTrue(wtl.control_prim.fail.called)                         
                     
    def test_convert_to_base_and_back(self):
        unitOfMeas = unitDictUtility.get_unit_of_measure(unitDictConstants.FOOT)
        #unitOfMeas = unitDictUtility.get_unit_of_measure("ft")
        self.assertFalse(wtl.control_prim.fail.called)
        initValue = 3
        valueBase = unitOfMeas.convertToBase(initValue)
        self.assertFalse(wtl.control_prim.fail.called)
        valueFinal = unitOfMeas.convertFromBase(valueBase)
        self.assertTrue(self.compare(initValue,valueFinal))
        self.assertFalse(wtl.control_prim.fail.called) 
                     
                      
    def test_convert_from_base(self):
        # convert 1 meter to feet
        value = unitDictUtility.convert_from_base(1,unitDictConstants.FOOT)
        #value = unitDictUtility.convert_from_base(1,"ft")
        self.assertTrue(self.compare(value,3.2808)) 
        self.assertFalse(wtl.control_prim.fail.called)        
        
    def test_convert_from_base_bad(self): 
        # bad annotation               
        value = unitDictUtility.convert_from_base(3,"ftf")
        self.assertTrue(wtl.control_prim.fail.called) 
         
                
    def test_convert_unit_to_unit(self):
        # convert 12 inches to 1 feet
        value = unitDictUtility.convert_to_unit(12, unitDictConstants.INCH, unitDictConstants.FOOT) 
        self.assertTrue(self.compare(value,1.0))                             
        self.assertFalse(wtl.control_prim.fail.called)                       
        # convert 32 degF to 0 degC
        value = unitDictUtility.convert_to_unit(32, unitDictConstants.DEGREE_FAHRENHEIT, unitDictConstants.DEGREES_CELSIUS)
        self.assertTrue(self.compare(value,0.0))      
        self.assertFalse(wtl.control_prim.fail.called)                         
                                               
    def test_convert_unit_to_unit_bad(self):
        # convert 12 inches to 1 feet
        value = unitDictUtility.convert_to_unit(12, unitDictConstants.INCH, unitDictConstants.DEGREES_CELSIUS) 
        #value = unitDictUtility.convert_to_unit(12, "in", "degC")  
        self.assertTrue(wtl.control_prim.fail.called)  

        # provide non float value
        value = unitDictUtility.convert_to_unit("abc", unitDictConstants.INCH, unitDictConstants.METRE) 
        #value = unitDictUtility.convert_to_unit("abc", "in", "m")  
        self.assertTrue(wtl.control_prim.fail.called) 
        
        # convert between two base units
        value = unitDictUtility.convert_to_unit(12, unitDictConstants.KELVIN, unitDictConstants.METRE) 
        #value = unitDictUtility.convert_to_unit(12, "K", "m")  
        self.assertTrue(wtl.control_prim.fail.called)                  
              
    def test_can_convert_units(self):
        # convert 12 inches to 1 feet
        canConvert = unitDictUtility.can_convert_units(unitDictConstants.INCH, unitDictConstants.FOOT)
        #canConvert = unitDictUtility.can_convert_units("in", "ft")
        self.assertTrue(canConvert)
        self.assertFalse(wtl.control_prim.fail.called)
        
        canConvert = unitDictUtility.can_convert_units(unitDictConstants.DEGREES_CELSIUS, unitDictConstants.KELVIN)
        #canConvert = unitDictUtility.can_convert_units("degC", "K")
        self.assertTrue(canConvert)
        self.assertFalse(wtl.control_prim.fail.called) 
        
        canConvert = unitDictUtility.can_convert_units(unitDictConstants.INCH, unitDictConstants.KELVIN)
        #canConvert = unitDictUtility.can_convert_units("in", "K")
        self.assertFalse(canConvert)
        self.assertFalse(wtl.control_prim.fail.called)                  
                            
    def compare(self,value1,value2):
        diff = abs( value1 - value2 )
        return diff < 0.0001        #self.assertTrue( result );

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
