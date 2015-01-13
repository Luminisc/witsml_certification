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

from distutils.core import setup

try:
    setup(name='WTL',
          version='1.0',
          description='WITSML Test Library',
          author='Jose Guterman',
          author_email='jguterman@teytech.com',
          url='http://www.pason.com',      
          packages=['wtl'],
          package_data={'wtl':['WMLS.WSDL']},
          package_dir={'wtl': 'src/wtl'},
          )
    
    setup(name='WSVT',
          version='1.0',
          description='WITSML Schema Validation Tool',
          author='Denys Metelskyy',
          author_email='denys.metelskyy@petrodaq.com',
          url='https://www.petrodaq.com',      
          packages=['wsvt'],
          package_data={'wsvt': ["schemas/WITSML_v1.3.1.1_Data_Schema/*.xsd",
                                 "schemas/WITSML_v1.4.1.0_Data_Schema/witsml_v1.4.1_data/xsd_schemas/*.xsd",
                                 "schemas/WITSML_v1.4.1.0_Data_Schema/abstract_v1.0/xsd_schemas/*.xsd",
                                 "schemas/WITSML_v1.4.1.0_Data_Schema/aggregate_1.0/xsd_schemas/*.xsd",
                                 "schemas/WITSML_v1.4.1.0_Data_Schema/witsml_v1.4.1_data/generated_read_schemas/*.xsd",
                                 "schemas/WITSML_v1.4.1.0_Data_Schema/witsml_v1.4.1_data/generated_write_schemas/*.xsd",
                                 "schemas/WITSML_v1.4.1.0_Data_Schema/witsml_v1.4.1_data/generated_delete_schemas/*.xsd",
                                 "schemas/WITSML_v1.4.1.0_Data_Schema/witsml_v1.4.1_data/generated_update_schemas/*.xsd",
                                 "schemas/WITSML_v1.4.1.1_Data_Schema/witsml_v1.4.1.1_data/xsd_schemas/*.xsd",
                                 "schemas/WITSML_v1.4.1.1_Data_Schema/abstract_v1.0/xsd_schemas/*.xsd",
                                 "schemas/WITSML_v1.4.1.1_Data_Schema/aggregate_1.0/xsd_schemas/*.xsd",
                                 "schemas/WITSML_v1.4.1.1_Data_Schema/witsml_v1.4.1.1_data/generated_read_schemas/*.xsd",
                                 "schemas/WITSML_v1.4.1.1_Data_Schema/witsml_v1.4.1.1_data/generated_write_schemas/*.xsd",
                                 "schemas/WITSML_v1.4.1.1_Data_Schema/witsml_v1.4.1.1_data/generated_delete_schemas/*.xsd",
                                 "schemas/WITSML_v1.4.1.1_Data_Schema/witsml_v1.4.1.1_data/generated_update_schemas/*.xsd"] },
          package_dir = {'wsvt': 'src/wsvt'},
          )
    
    
    setup(name='WITSMLTools',
          version='1.0',
          description='WITSML Tools Library',
          author='Denys Metelskyy',
          author_email='denys.metelskyy@petrodaq.com',
          url='https://www.petrodaq.com',      
          packages=['wtools'],
          package_data={'wtools':['WMLS.WSDL']},
          package_dir = {'wtools': 'src/wtools'},
          )
    
    
    setup(name='WCMP',
          version='1.0',
          description='WITSML Dataset Comparison Library',
          author='Denys Metelskyy',
          author_email='denys.metelskyy@petrodaq.com',
          url='https://www.petrodaq.com',      
          packages=['wcmp'],
          package_dir = {'wcmp': 'src/wcmp'},
          package_data={'wcmp': ["witsml1411/*.py" ] }
          )
    
except SystemExit, msg:
    print "Installation Failed: Error: %s" % msg
    exit(-1)
        
print "Installation Complete"