'''
Created on Oct 31, 2012

@author: metelskyyd
'''
import unittest
import os
import sys

from wsvt.SchemaValidator import WITSMLSchemaValidator;

validator = WITSMLSchemaValidator(os.path.join(sys.modules['wsvt'].__path__[0],'schemas'));

class Test(unittest.TestCase):

    

    def testValidationSuccess(self):
        global validator;
        is_valid, message =  validator.validateXMLAgainstReadSchema("1.4.1.1","log", open("log.xml",'r').read() );
        self.assertTrue(is_valid);

    def testValidationFailVersion(self):
        global validator;
        is_valid, message =  validator.validateXMLAgainstReadSchema("1.4.1.2","log", open("log.xml",'r').read() );
        self.assertFalse(is_valid);

    def testValidationFailXML(self):
        global validator;
        is_valid, message =  validator.validateXMLAgainstReadSchema("1.4.1.1","log", open("well.xml",'r').read() );
        self.assertFalse(is_valid);

    def testValidationFailType(self):
        global validator;
        is_valid, message =  validator.validateXMLAgainstReadSchema("1.4.1.1","well", open("log.xml",'r').read() );
        self.assertFalse(is_valid);

if __name__ == "__main__":
    unittest.main()
