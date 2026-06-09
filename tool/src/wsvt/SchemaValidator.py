'''
Created on Oct 31, 2012

@author: metelskyyd
'''

from lxml import etree
from lxml import objectify

class WITSMLSchemaParser:
    
    def __init__(self, xsd_filename):
        self.xsd_filename = xsd_filename;
        self.parser = None;
        
    def getParser(self):
        if self.parser is None :
            schema = etree.XMLSchema(file = open( self.xsd_filename,'r'));
            self.parser = objectify.makeparser(schema = schema);
        return self.parser;

class WITSMLSchemaValidator:
    '''
    this class will be a interface for validations 
    '''

    def __init__(self, schemas_root):
        '''
        Constructor
        '''
        self.GENERIC_SCHEMA     = 0;
        self.READ_SCHEMA        = 1;
        self.WRITE_SCHEMA       = 2;
        self.DELETE_SCHEMA      = 3;
        self.UPDATE_SCHEMA      = 4;
        
        self.OBJ_TYPE_ATTACHMENT                 = 'attachment'
        self.OBJ_TYPE_BHARUN                     = 'bhaRun'
        self.OBJ_TYPE_CEMENTJOB                  = 'cementJob'
        self.OBJ_TYPE_CHANGELOG                  = 'changeLog'
        self.OBJ_TYPE_CONVCORE                   = 'convCore'
        self.OBJ_TYPE_COORDINATEREFERENCESYSTEM  = 'coordinateReferenceSystem'
        self.OBJ_TYPE_DRILLREPORT                = 'drillReport'
        self.OBJ_TYPE_FLUIDSREPORT               = 'fluidsReport'
        self.OBJ_TYPE_FORMATIONMARKER            = 'formationMarker'
        self.OBJ_TYPE_LOG                        = 'log'
        self.OBJ_TYPE_MESSAGE                    = 'message'
        self.OBJ_TYPE_MUDLOG                     = 'mudLog'
        self.OBJ_TYPE_OBJECTGROUP                = 'objectGroup'
        self.OBJ_TYPE_OPSREPORT                  = 'opsReport'
        self.OBJ_TYPE_RIG                        = 'rig'
        self.OBJ_TYPE_RISK                       = 'risk'
        self.OBJ_TYPE_SIDEWALLCORE               = 'sidewallCore'
        self.OBJ_TYPE_STIMJOB                    = 'stimJob'
        self.OBJ_TYPE_SURVEYPROGRAM              = 'surveyProgram'
        self.OBJ_TYPE_TARGET                     = 'target'
        self.OBJ_TYPE_TOOLERRORMODEL             = 'toolErrorModel'
        self.OBJ_TYPE_TOOLERRORTERSET            = 'toolErrorTermSet'
        self.OBJ_TYPE_TRAJECTORY                 = 'trajectory'
        self.OBJ_TYPE_TUBULAR                    = 'tubular'
        self.OBJ_TYPE_WBGEOMETRY                 = 'wbGeometry'
        self.OBJ_TYPE_WELL                       = 'well'
        self.OBJ_TYPE_WELLBORE                   = 'wellbore'
        
        self.known_schema_types = [
                                    self.GENERIC_SCHEMA     ,
                                    self.READ_SCHEMA        ,
                                    self.WRITE_SCHEMA       ,
                                    self.DELETE_SCHEMA      ,
                                    self.UPDATE_SCHEMA      
                              ]
        
        self.known_object_types = [
                                    self.OBJ_TYPE_ATTACHMENT                 ,
                                    self.OBJ_TYPE_BHARUN                     ,
                                    self.OBJ_TYPE_CEMENTJOB                  ,
                                    self.OBJ_TYPE_CHANGELOG                  ,
                                    self.OBJ_TYPE_CONVCORE                   ,
                                    self.OBJ_TYPE_COORDINATEREFERENCESYSTEM  ,
                                    self.OBJ_TYPE_DRILLREPORT                ,
                                    self.OBJ_TYPE_FLUIDSREPORT               ,
                                    self.OBJ_TYPE_FORMATIONMARKER            ,
                                    self.OBJ_TYPE_LOG                        ,
                                    self.OBJ_TYPE_MESSAGE                    ,
                                    self.OBJ_TYPE_MUDLOG                     ,
                                    self.OBJ_TYPE_OBJECTGROUP                ,
                                    self.OBJ_TYPE_OPSREPORT                  ,
                                    self.OBJ_TYPE_RIG                        ,
                                    self.OBJ_TYPE_RISK                       ,
                                    self.OBJ_TYPE_SIDEWALLCORE               ,
                                    self.OBJ_TYPE_STIMJOB                    ,
                                    self.OBJ_TYPE_SURVEYPROGRAM              ,
                                    self.OBJ_TYPE_TARGET                     ,
                                    self.OBJ_TYPE_TOOLERRORMODEL             ,
                                    self.OBJ_TYPE_TOOLERRORTERSET            ,
                                    self.OBJ_TYPE_TRAJECTORY                 ,
                                    self.OBJ_TYPE_TUBULAR                    ,
                                    self.OBJ_TYPE_WBGEOMETRY                 ,
                                    self.OBJ_TYPE_WELL                       ,
                                    self.OBJ_TYPE_WELLBORE                   
                            ]
        
        self.WITSML_VERSION_1311 = "1.3.1.1"
        self.WITSML_VERSION_1410 = "1.4.1.0"
        self.WITSML_VERSION_1411 = "1.4.1.1"
        
        self.known_schema_versions = [ self.WITSML_VERSION_1311 ,
                                 self.WITSML_VERSION_1410 ,
                                 self.WITSML_VERSION_1411 
                            ];
        self.parsers = {};
        self.instantinateParsers(schemas_root);
    
    
    def addParser(self, schema_version , schema_type , object_type, xsd_filename ):
        #reasuring version node exists
        if not ( schema_version in self.parsers ):
            self.parsers[schema_version] = {};
            
        #reasuring schema type exists
        if not ( schema_type in self.parsers[schema_version] ):
            self.parsers[schema_version][schema_type] = {};
            
        #checking for duplicate
        if ( object_type in self.parsers[schema_version][schema_type] ):
            raise Exception("Internal Error : Duplicate detected")
        
        #creating parser
        
        self.parsers[schema_version][schema_type][object_type] = WITSMLSchemaParser( xsd_filename ); 
        
    
    def instantinateParsers(self , schemas_root):
        print("building validation parsers for WITSML API 1.3.1.1")
        """ 
        1.3.1.1 
        """
        witsml_1311_root = schemas_root+"/WITSML_v1.3.1.1_Data_Schema/";
        self.addParser( self.WITSML_VERSION_1311 , self.GENERIC_SCHEMA , self.OBJ_TYPE_BHARUN, witsml_1311_root+"obj_bhaRun.xsd" );
        self.addParser( self.WITSML_VERSION_1311 , self.GENERIC_SCHEMA , self.OBJ_TYPE_CEMENTJOB, witsml_1311_root+"obj_cementJob.xsd" );
        self.addParser( self.WITSML_VERSION_1311 , self.GENERIC_SCHEMA , self.OBJ_TYPE_CONVCORE, witsml_1311_root+"obj_convCore.xsd" );
        self.addParser( self.WITSML_VERSION_1311 , self.GENERIC_SCHEMA , self.OBJ_TYPE_FLUIDSREPORT, witsml_1311_root+"obj_fluidsReport.xsd" );
        self.addParser( self.WITSML_VERSION_1311 , self.GENERIC_SCHEMA , self.OBJ_TYPE_FORMATIONMARKER, witsml_1311_root+"obj_formationMarker.xsd" );
        self.addParser( self.WITSML_VERSION_1311 , self.GENERIC_SCHEMA , self.OBJ_TYPE_LOG, witsml_1311_root+"obj_log.xsd" );
        self.addParser( self.WITSML_VERSION_1311 , self.GENERIC_SCHEMA , self.OBJ_TYPE_MESSAGE, witsml_1311_root+"obj_message.xsd" );
        self.addParser( self.WITSML_VERSION_1311 , self.GENERIC_SCHEMA , self.OBJ_TYPE_MUDLOG, witsml_1311_root+"obj_mudLog.xsd" );
        self.addParser( self.WITSML_VERSION_1311 , self.GENERIC_SCHEMA , self.OBJ_TYPE_OPSREPORT, witsml_1311_root+"obj_opsReport.xsd" );
        self.addParser( self.WITSML_VERSION_1311 , self.GENERIC_SCHEMA , self.OBJ_TYPE_RIG, witsml_1311_root+"obj_rig.xsd" );
        self.addParser( self.WITSML_VERSION_1311 , self.GENERIC_SCHEMA , self.OBJ_TYPE_RISK, witsml_1311_root+"obj_risk.xsd" );
        self.addParser( self.WITSML_VERSION_1311 , self.GENERIC_SCHEMA , self.OBJ_TYPE_SIDEWALLCORE, witsml_1311_root+"obj_sidewallCore.xsd" );
        self.addParser( self.WITSML_VERSION_1311 , self.GENERIC_SCHEMA , self.OBJ_TYPE_SURVEYPROGRAM, witsml_1311_root+"obj_surveyProgram.xsd" );
        self.addParser( self.WITSML_VERSION_1311 , self.GENERIC_SCHEMA , self.OBJ_TYPE_TARGET, witsml_1311_root+"obj_target.xsd" );
        self.addParser( self.WITSML_VERSION_1311 , self.GENERIC_SCHEMA , self.OBJ_TYPE_TRAJECTORY, witsml_1311_root+"obj_trajectory.xsd" );
        self.addParser( self.WITSML_VERSION_1311 , self.GENERIC_SCHEMA , self.OBJ_TYPE_TUBULAR, witsml_1311_root+"obj_tubular.xsd" );
        self.addParser( self.WITSML_VERSION_1311 , self.GENERIC_SCHEMA , self.OBJ_TYPE_WBGEOMETRY, witsml_1311_root+"obj_wbGeometry.xsd" );
        self.addParser( self.WITSML_VERSION_1311 , self.GENERIC_SCHEMA , self.OBJ_TYPE_WELL, witsml_1311_root+"obj_well.xsd" );
        self.addParser( self.WITSML_VERSION_1311 , self.GENERIC_SCHEMA , self.OBJ_TYPE_WELLBORE, witsml_1311_root+"obj_wellbore.xsd" );
        print("building validation parsers for WITSML API 1.4.1.0")
        """ 
        1.4.1.0 
        """
        witsml_1410_root = schemas_root+"/WITSML_v1.4.1.0_Data_Schema/witsml_v1.4.1_data/xsd_schemas/";
        self.addParser( self.WITSML_VERSION_1410 , self.GENERIC_SCHEMA , self.OBJ_TYPE_BHARUN,          witsml_1410_root + "obj_bhaRun.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.GENERIC_SCHEMA , self.OBJ_TYPE_CEMENTJOB,       witsml_1410_root + "obj_cementJob.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.GENERIC_SCHEMA , self.OBJ_TYPE_CHANGELOG,       witsml_1410_root + "obj_changeLog.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.GENERIC_SCHEMA , self.OBJ_TYPE_CONVCORE,        witsml_1410_root + "obj_convCore.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.GENERIC_SCHEMA , self.OBJ_TYPE_FLUIDSREPORT,    witsml_1410_root + "obj_fluidsReport.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.GENERIC_SCHEMA , self.OBJ_TYPE_FORMATIONMARKER, witsml_1410_root + "obj_formationMarker.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.GENERIC_SCHEMA , self.OBJ_TYPE_LOG,             witsml_1410_root + "obj_log.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.GENERIC_SCHEMA , self.OBJ_TYPE_MESSAGE,         witsml_1410_root + "obj_message.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.GENERIC_SCHEMA , self.OBJ_TYPE_MUDLOG,          witsml_1410_root + "obj_mudLog.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.GENERIC_SCHEMA , self.OBJ_TYPE_OPSREPORT,       witsml_1410_root + "obj_opsReport.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.GENERIC_SCHEMA , self.OBJ_TYPE_RIG,             witsml_1410_root + "obj_rig.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.GENERIC_SCHEMA , self.OBJ_TYPE_RISK,            witsml_1410_root + "obj_risk.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.GENERIC_SCHEMA , self.OBJ_TYPE_SIDEWALLCORE,    witsml_1410_root + "obj_sidewallCore.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.GENERIC_SCHEMA , self.OBJ_TYPE_SURVEYPROGRAM,   witsml_1410_root + "obj_surveyProgram.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.GENERIC_SCHEMA , self.OBJ_TYPE_TARGET,          witsml_1410_root + "obj_target.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.GENERIC_SCHEMA , self.OBJ_TYPE_TRAJECTORY,      witsml_1410_root + "obj_trajectory.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.GENERIC_SCHEMA , self.OBJ_TYPE_TUBULAR,         witsml_1410_root + "obj_tubular.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.GENERIC_SCHEMA , self.OBJ_TYPE_WBGEOMETRY,      witsml_1410_root + "obj_wbGeometry.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.GENERIC_SCHEMA , self.OBJ_TYPE_WELL,            witsml_1410_root + "obj_well.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.GENERIC_SCHEMA , self.OBJ_TYPE_WELLBORE,        witsml_1410_root + "obj_wellbore.xsd" );
        """read schema"""
        witsml_1410_root = schemas_root+"/WITSML_v1.4.1.0_Data_Schema/witsml_v1.4.1_data/generated_read_schemas/";
        self.addParser( self.WITSML_VERSION_1410 , self.READ_SCHEMA , self.OBJ_TYPE_BHARUN,          witsml_1410_root + "obj_bhaRun.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.READ_SCHEMA , self.OBJ_TYPE_CEMENTJOB,       witsml_1410_root + "obj_cementJob.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.READ_SCHEMA , self.OBJ_TYPE_CHANGELOG,       witsml_1410_root + "obj_changeLog.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.READ_SCHEMA , self.OBJ_TYPE_CONVCORE,        witsml_1410_root + "obj_convCore.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.READ_SCHEMA , self.OBJ_TYPE_FLUIDSREPORT,    witsml_1410_root + "obj_fluidsReport.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.READ_SCHEMA , self.OBJ_TYPE_FORMATIONMARKER, witsml_1410_root + "obj_formationMarker.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.READ_SCHEMA , self.OBJ_TYPE_LOG,             witsml_1410_root + "obj_log.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.READ_SCHEMA , self.OBJ_TYPE_MESSAGE,         witsml_1410_root + "obj_message.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.READ_SCHEMA , self.OBJ_TYPE_MUDLOG,          witsml_1410_root + "obj_mudLog.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.READ_SCHEMA , self.OBJ_TYPE_OPSREPORT,       witsml_1410_root + "obj_opsReport.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.READ_SCHEMA , self.OBJ_TYPE_RIG,             witsml_1410_root + "obj_rig.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.READ_SCHEMA , self.OBJ_TYPE_RISK,            witsml_1410_root + "obj_risk.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.READ_SCHEMA , self.OBJ_TYPE_SIDEWALLCORE,    witsml_1410_root + "obj_sidewallCore.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.READ_SCHEMA , self.OBJ_TYPE_SURVEYPROGRAM,   witsml_1410_root + "obj_surveyProgram.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.READ_SCHEMA , self.OBJ_TYPE_TARGET,          witsml_1410_root + "obj_target.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.READ_SCHEMA , self.OBJ_TYPE_TRAJECTORY,      witsml_1410_root + "obj_trajectory.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.READ_SCHEMA , self.OBJ_TYPE_TUBULAR,         witsml_1410_root + "obj_tubular.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.READ_SCHEMA , self.OBJ_TYPE_WBGEOMETRY,      witsml_1410_root + "obj_wbGeometry.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.READ_SCHEMA , self.OBJ_TYPE_WELL,            witsml_1410_root + "obj_well.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.READ_SCHEMA , self.OBJ_TYPE_WELLBORE,        witsml_1410_root + "obj_wellbore.xsd" );
        """write schema"""
        witsml_1410_root = schemas_root+"/WITSML_v1.4.1.0_Data_Schema/witsml_v1.4.1_data/generated_write_schemas/";
        self.addParser( self.WITSML_VERSION_1410 , self.WRITE_SCHEMA , self.OBJ_TYPE_BHARUN,          witsml_1410_root + "obj_bhaRun.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.WRITE_SCHEMA , self.OBJ_TYPE_CEMENTJOB,       witsml_1410_root + "obj_cementJob.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.WRITE_SCHEMA , self.OBJ_TYPE_CHANGELOG,       witsml_1410_root + "obj_changeLog.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.WRITE_SCHEMA , self.OBJ_TYPE_CONVCORE,        witsml_1410_root + "obj_convCore.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.WRITE_SCHEMA , self.OBJ_TYPE_FLUIDSREPORT,    witsml_1410_root + "obj_fluidsReport.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.WRITE_SCHEMA , self.OBJ_TYPE_FORMATIONMARKER, witsml_1410_root + "obj_formationMarker.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.WRITE_SCHEMA , self.OBJ_TYPE_LOG,             witsml_1410_root + "obj_log.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.WRITE_SCHEMA , self.OBJ_TYPE_MESSAGE,         witsml_1410_root + "obj_message.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.WRITE_SCHEMA , self.OBJ_TYPE_MUDLOG,          witsml_1410_root + "obj_mudLog.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.WRITE_SCHEMA , self.OBJ_TYPE_OPSREPORT,       witsml_1410_root + "obj_opsReport.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.WRITE_SCHEMA , self.OBJ_TYPE_RIG,             witsml_1410_root + "obj_rig.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.WRITE_SCHEMA , self.OBJ_TYPE_RISK,            witsml_1410_root + "obj_risk.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.WRITE_SCHEMA , self.OBJ_TYPE_SIDEWALLCORE,    witsml_1410_root + "obj_sidewallCore.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.WRITE_SCHEMA , self.OBJ_TYPE_SURVEYPROGRAM,   witsml_1410_root + "obj_surveyProgram.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.WRITE_SCHEMA , self.OBJ_TYPE_TARGET,          witsml_1410_root + "obj_target.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.WRITE_SCHEMA , self.OBJ_TYPE_TRAJECTORY,      witsml_1410_root + "obj_trajectory.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.WRITE_SCHEMA , self.OBJ_TYPE_TUBULAR,         witsml_1410_root + "obj_tubular.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.WRITE_SCHEMA , self.OBJ_TYPE_WBGEOMETRY,      witsml_1410_root + "obj_wbGeometry.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.WRITE_SCHEMA , self.OBJ_TYPE_WELL,            witsml_1410_root + "obj_well.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.WRITE_SCHEMA , self.OBJ_TYPE_WELLBORE,        witsml_1410_root + "obj_wellbore.xsd" );
        """delete schema"""
        witsml_1410_root = schemas_root+"/WITSML_v1.4.1.0_Data_Schema/witsml_v1.4.1_data/generated_delete_schemas/";
        self.addParser( self.WITSML_VERSION_1410 , self.DELETE_SCHEMA , self.OBJ_TYPE_BHARUN,          witsml_1410_root + "obj_bhaRun.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.DELETE_SCHEMA , self.OBJ_TYPE_CEMENTJOB,       witsml_1410_root + "obj_cementJob.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.DELETE_SCHEMA , self.OBJ_TYPE_CHANGELOG,       witsml_1410_root + "obj_changeLog.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.DELETE_SCHEMA , self.OBJ_TYPE_CONVCORE,        witsml_1410_root + "obj_convCore.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.DELETE_SCHEMA , self.OBJ_TYPE_FLUIDSREPORT,    witsml_1410_root + "obj_fluidsReport.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.DELETE_SCHEMA , self.OBJ_TYPE_FORMATIONMARKER, witsml_1410_root + "obj_formationMarker.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.DELETE_SCHEMA , self.OBJ_TYPE_LOG,             witsml_1410_root + "obj_log.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.DELETE_SCHEMA , self.OBJ_TYPE_MESSAGE,         witsml_1410_root + "obj_message.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.DELETE_SCHEMA , self.OBJ_TYPE_MUDLOG,          witsml_1410_root + "obj_mudLog.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.DELETE_SCHEMA , self.OBJ_TYPE_OPSREPORT,       witsml_1410_root + "obj_opsReport.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.DELETE_SCHEMA , self.OBJ_TYPE_RIG,             witsml_1410_root + "obj_rig.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.DELETE_SCHEMA , self.OBJ_TYPE_RISK,            witsml_1410_root + "obj_risk.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.DELETE_SCHEMA , self.OBJ_TYPE_SIDEWALLCORE,    witsml_1410_root + "obj_sidewallCore.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.DELETE_SCHEMA , self.OBJ_TYPE_SURVEYPROGRAM,   witsml_1410_root + "obj_surveyProgram.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.DELETE_SCHEMA , self.OBJ_TYPE_TARGET,          witsml_1410_root + "obj_target.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.DELETE_SCHEMA , self.OBJ_TYPE_TRAJECTORY,      witsml_1410_root + "obj_trajectory.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.DELETE_SCHEMA , self.OBJ_TYPE_TUBULAR,         witsml_1410_root + "obj_tubular.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.DELETE_SCHEMA , self.OBJ_TYPE_WBGEOMETRY,      witsml_1410_root + "obj_wbGeometry.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.DELETE_SCHEMA , self.OBJ_TYPE_WELL,            witsml_1410_root + "obj_well.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.DELETE_SCHEMA , self.OBJ_TYPE_WELLBORE,        witsml_1410_root + "obj_wellbore.xsd" );
        """update schema"""
        witsml_1410_root = schemas_root+"/WITSML_v1.4.1.0_Data_Schema/witsml_v1.4.1_data/generated_update_schemas/";
        self.addParser( self.WITSML_VERSION_1410 , self.UPDATE_SCHEMA , self.OBJ_TYPE_BHARUN,          witsml_1410_root + "obj_bhaRun.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.UPDATE_SCHEMA , self.OBJ_TYPE_CEMENTJOB,       witsml_1410_root + "obj_cementJob.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.UPDATE_SCHEMA , self.OBJ_TYPE_CHANGELOG,       witsml_1410_root + "obj_changeLog.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.UPDATE_SCHEMA , self.OBJ_TYPE_CONVCORE,        witsml_1410_root + "obj_convCore.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.UPDATE_SCHEMA , self.OBJ_TYPE_FLUIDSREPORT,    witsml_1410_root + "obj_fluidsReport.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.UPDATE_SCHEMA , self.OBJ_TYPE_FORMATIONMARKER, witsml_1410_root + "obj_formationMarker.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.UPDATE_SCHEMA , self.OBJ_TYPE_LOG,             witsml_1410_root + "obj_log.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.UPDATE_SCHEMA , self.OBJ_TYPE_MESSAGE,         witsml_1410_root + "obj_message.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.UPDATE_SCHEMA , self.OBJ_TYPE_MUDLOG,          witsml_1410_root + "obj_mudLog.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.UPDATE_SCHEMA , self.OBJ_TYPE_OPSREPORT,       witsml_1410_root + "obj_opsReport.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.UPDATE_SCHEMA , self.OBJ_TYPE_RIG,             witsml_1410_root + "obj_rig.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.UPDATE_SCHEMA , self.OBJ_TYPE_RISK,            witsml_1410_root + "obj_risk.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.UPDATE_SCHEMA , self.OBJ_TYPE_SIDEWALLCORE,    witsml_1410_root + "obj_sidewallCore.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.UPDATE_SCHEMA , self.OBJ_TYPE_SURVEYPROGRAM,   witsml_1410_root + "obj_surveyProgram.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.UPDATE_SCHEMA , self.OBJ_TYPE_TARGET,          witsml_1410_root + "obj_target.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.UPDATE_SCHEMA , self.OBJ_TYPE_TRAJECTORY,      witsml_1410_root + "obj_trajectory.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.UPDATE_SCHEMA , self.OBJ_TYPE_TUBULAR,         witsml_1410_root + "obj_tubular.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.UPDATE_SCHEMA , self.OBJ_TYPE_WBGEOMETRY,      witsml_1410_root + "obj_wbGeometry.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.UPDATE_SCHEMA , self.OBJ_TYPE_WELL,            witsml_1410_root + "obj_well.xsd" );
        self.addParser( self.WITSML_VERSION_1410 , self.UPDATE_SCHEMA , self.OBJ_TYPE_WELLBORE,        witsml_1410_root + "obj_wellbore.xsd" );
        print("building validation parsers for WITSML API 1.4.1.1")
        """ 
        1.4.1.1 
        """
        witsml_1411_root = schemas_root+"/WITSML_v1.4.1.1_Data_Schema/witsml_v1.4.1.1_data/xsd_schemas/";
        self.addParser( self.WITSML_VERSION_1411 , self.GENERIC_SCHEMA , self.OBJ_TYPE_BHARUN,          witsml_1411_root + "obj_bhaRun.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.GENERIC_SCHEMA , self.OBJ_TYPE_CEMENTJOB,       witsml_1411_root + "obj_cementJob.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.GENERIC_SCHEMA , self.OBJ_TYPE_CHANGELOG,       witsml_1411_root + "obj_changeLog.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.GENERIC_SCHEMA , self.OBJ_TYPE_CONVCORE,        witsml_1411_root + "obj_convCore.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.GENERIC_SCHEMA , self.OBJ_TYPE_FLUIDSREPORT,    witsml_1411_root + "obj_fluidsReport.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.GENERIC_SCHEMA , self.OBJ_TYPE_FORMATIONMARKER, witsml_1411_root + "obj_formationMarker.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.GENERIC_SCHEMA , self.OBJ_TYPE_LOG,             witsml_1411_root + "obj_log.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.GENERIC_SCHEMA , self.OBJ_TYPE_MESSAGE,         witsml_1411_root + "obj_message.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.GENERIC_SCHEMA , self.OBJ_TYPE_MUDLOG,          witsml_1411_root + "obj_mudLog.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.GENERIC_SCHEMA , self.OBJ_TYPE_OPSREPORT,       witsml_1411_root + "obj_opsReport.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.GENERIC_SCHEMA , self.OBJ_TYPE_RIG,             witsml_1411_root + "obj_rig.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.GENERIC_SCHEMA , self.OBJ_TYPE_RISK,            witsml_1411_root + "obj_risk.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.GENERIC_SCHEMA , self.OBJ_TYPE_SIDEWALLCORE,    witsml_1411_root + "obj_sidewallCore.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.GENERIC_SCHEMA , self.OBJ_TYPE_SURVEYPROGRAM,   witsml_1411_root + "obj_surveyProgram.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.GENERIC_SCHEMA , self.OBJ_TYPE_TARGET,          witsml_1411_root + "obj_target.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.GENERIC_SCHEMA , self.OBJ_TYPE_TRAJECTORY,      witsml_1411_root + "obj_trajectory.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.GENERIC_SCHEMA , self.OBJ_TYPE_TUBULAR,         witsml_1411_root + "obj_tubular.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.GENERIC_SCHEMA , self.OBJ_TYPE_WBGEOMETRY,      witsml_1411_root + "obj_wbGeometry.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.GENERIC_SCHEMA , self.OBJ_TYPE_WELL,            witsml_1411_root + "obj_well.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.GENERIC_SCHEMA , self.OBJ_TYPE_WELLBORE,        witsml_1411_root + "obj_wellbore.xsd" );
        """read schema"""
        witsml_1411_root = schemas_root+"/WITSML_v1.4.1.1_Data_Schema/witsml_v1.4.1.1_data/generated_read_schemas/";
        self.addParser( self.WITSML_VERSION_1411 , self.READ_SCHEMA , self.OBJ_TYPE_BHARUN,          witsml_1411_root + "obj_bhaRun.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.READ_SCHEMA , self.OBJ_TYPE_CEMENTJOB,       witsml_1411_root + "obj_cementJob.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.READ_SCHEMA , self.OBJ_TYPE_CHANGELOG,       witsml_1411_root + "obj_changeLog.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.READ_SCHEMA , self.OBJ_TYPE_CONVCORE,        witsml_1411_root + "obj_convCore.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.READ_SCHEMA , self.OBJ_TYPE_FLUIDSREPORT,    witsml_1411_root + "obj_fluidsReport.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.READ_SCHEMA , self.OBJ_TYPE_FORMATIONMARKER, witsml_1411_root + "obj_formationMarker.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.READ_SCHEMA , self.OBJ_TYPE_LOG,             witsml_1411_root + "obj_log.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.READ_SCHEMA , self.OBJ_TYPE_MESSAGE,         witsml_1411_root + "obj_message.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.READ_SCHEMA , self.OBJ_TYPE_MUDLOG,          witsml_1411_root + "obj_mudLog.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.READ_SCHEMA , self.OBJ_TYPE_OPSREPORT,       witsml_1411_root + "obj_opsReport.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.READ_SCHEMA , self.OBJ_TYPE_RIG,             witsml_1411_root + "obj_rig.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.READ_SCHEMA , self.OBJ_TYPE_RISK,            witsml_1411_root + "obj_risk.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.READ_SCHEMA , self.OBJ_TYPE_SIDEWALLCORE,    witsml_1411_root + "obj_sidewallCore.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.READ_SCHEMA , self.OBJ_TYPE_SURVEYPROGRAM,   witsml_1411_root + "obj_surveyProgram.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.READ_SCHEMA , self.OBJ_TYPE_TARGET,          witsml_1411_root + "obj_target.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.READ_SCHEMA , self.OBJ_TYPE_TRAJECTORY,      witsml_1411_root + "obj_trajectory.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.READ_SCHEMA , self.OBJ_TYPE_TUBULAR,         witsml_1411_root + "obj_tubular.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.READ_SCHEMA , self.OBJ_TYPE_WBGEOMETRY,      witsml_1411_root + "obj_wbGeometry.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.READ_SCHEMA , self.OBJ_TYPE_WELL,            witsml_1411_root + "obj_well.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.READ_SCHEMA , self.OBJ_TYPE_WELLBORE,        witsml_1411_root + "obj_wellbore.xsd" );
        """write schema"""
        witsml_1411_root = schemas_root+"/WITSML_v1.4.1.1_Data_Schema/witsml_v1.4.1.1_data/generated_write_schemas/";
        self.addParser( self.WITSML_VERSION_1411 , self.WRITE_SCHEMA , self.OBJ_TYPE_BHARUN,          witsml_1411_root + "obj_bhaRun.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.WRITE_SCHEMA , self.OBJ_TYPE_CEMENTJOB,       witsml_1411_root + "obj_cementJob.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.WRITE_SCHEMA , self.OBJ_TYPE_CHANGELOG,       witsml_1411_root + "obj_changeLog.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.WRITE_SCHEMA , self.OBJ_TYPE_CONVCORE,        witsml_1411_root + "obj_convCore.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.WRITE_SCHEMA , self.OBJ_TYPE_FLUIDSREPORT,    witsml_1411_root + "obj_fluidsReport.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.WRITE_SCHEMA , self.OBJ_TYPE_FORMATIONMARKER, witsml_1411_root + "obj_formationMarker.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.WRITE_SCHEMA , self.OBJ_TYPE_LOG,             witsml_1411_root + "obj_log.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.WRITE_SCHEMA , self.OBJ_TYPE_MESSAGE,         witsml_1411_root + "obj_message.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.WRITE_SCHEMA , self.OBJ_TYPE_MUDLOG,          witsml_1411_root + "obj_mudLog.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.WRITE_SCHEMA , self.OBJ_TYPE_OPSREPORT,       witsml_1411_root + "obj_opsReport.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.WRITE_SCHEMA , self.OBJ_TYPE_RIG,             witsml_1411_root + "obj_rig.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.WRITE_SCHEMA , self.OBJ_TYPE_RISK,            witsml_1411_root + "obj_risk.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.WRITE_SCHEMA , self.OBJ_TYPE_SIDEWALLCORE,    witsml_1411_root + "obj_sidewallCore.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.WRITE_SCHEMA , self.OBJ_TYPE_SURVEYPROGRAM,   witsml_1411_root + "obj_surveyProgram.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.WRITE_SCHEMA , self.OBJ_TYPE_TARGET,          witsml_1411_root + "obj_target.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.WRITE_SCHEMA , self.OBJ_TYPE_TRAJECTORY,      witsml_1411_root + "obj_trajectory.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.WRITE_SCHEMA , self.OBJ_TYPE_TUBULAR,         witsml_1411_root + "obj_tubular.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.WRITE_SCHEMA , self.OBJ_TYPE_WBGEOMETRY,      witsml_1411_root + "obj_wbGeometry.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.WRITE_SCHEMA , self.OBJ_TYPE_WELL,            witsml_1411_root + "obj_well.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.WRITE_SCHEMA , self.OBJ_TYPE_WELLBORE,        witsml_1411_root + "obj_wellbore.xsd" );
        """delete schema"""
        witsml_1411_root = schemas_root+"/WITSML_v1.4.1.1_Data_Schema/witsml_v1.4.1.1_data/generated_delete_schemas/";
        self.addParser( self.WITSML_VERSION_1411 , self.DELETE_SCHEMA , self.OBJ_TYPE_BHARUN,          witsml_1411_root + "obj_bhaRun.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.DELETE_SCHEMA , self.OBJ_TYPE_CEMENTJOB,       witsml_1411_root + "obj_cementJob.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.DELETE_SCHEMA , self.OBJ_TYPE_CHANGELOG,       witsml_1411_root + "obj_changeLog.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.DELETE_SCHEMA , self.OBJ_TYPE_CONVCORE,        witsml_1411_root + "obj_convCore.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.DELETE_SCHEMA , self.OBJ_TYPE_FLUIDSREPORT,    witsml_1411_root + "obj_fluidsReport.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.DELETE_SCHEMA , self.OBJ_TYPE_FORMATIONMARKER, witsml_1411_root + "obj_formationMarker.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.DELETE_SCHEMA , self.OBJ_TYPE_LOG,             witsml_1411_root + "obj_log.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.DELETE_SCHEMA , self.OBJ_TYPE_MESSAGE,         witsml_1411_root + "obj_message.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.DELETE_SCHEMA , self.OBJ_TYPE_MUDLOG,          witsml_1411_root + "obj_mudLog.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.DELETE_SCHEMA , self.OBJ_TYPE_OPSREPORT,       witsml_1411_root + "obj_opsReport.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.DELETE_SCHEMA , self.OBJ_TYPE_RIG,             witsml_1411_root + "obj_rig.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.DELETE_SCHEMA , self.OBJ_TYPE_RISK,            witsml_1411_root + "obj_risk.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.DELETE_SCHEMA , self.OBJ_TYPE_SIDEWALLCORE,    witsml_1411_root + "obj_sidewallCore.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.DELETE_SCHEMA , self.OBJ_TYPE_SURVEYPROGRAM,   witsml_1411_root + "obj_surveyProgram.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.DELETE_SCHEMA , self.OBJ_TYPE_TARGET,          witsml_1411_root + "obj_target.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.DELETE_SCHEMA , self.OBJ_TYPE_TRAJECTORY,      witsml_1411_root + "obj_trajectory.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.DELETE_SCHEMA , self.OBJ_TYPE_TUBULAR,         witsml_1411_root + "obj_tubular.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.DELETE_SCHEMA , self.OBJ_TYPE_WBGEOMETRY,      witsml_1411_root + "obj_wbGeometry.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.DELETE_SCHEMA , self.OBJ_TYPE_WELL,            witsml_1411_root + "obj_well.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.DELETE_SCHEMA , self.OBJ_TYPE_WELLBORE,        witsml_1411_root + "obj_wellbore.xsd" );
        """update schema"""
        witsml_1411_root = schemas_root+"/WITSML_v1.4.1.1_Data_Schema/witsml_v1.4.1.1_data/generated_update_schemas/";
        self.addParser( self.WITSML_VERSION_1411 , self.UPDATE_SCHEMA , self.OBJ_TYPE_BHARUN,          witsml_1411_root + "obj_bhaRun.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.UPDATE_SCHEMA , self.OBJ_TYPE_CEMENTJOB,       witsml_1411_root + "obj_cementJob.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.UPDATE_SCHEMA , self.OBJ_TYPE_CHANGELOG,       witsml_1411_root + "obj_changeLog.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.UPDATE_SCHEMA , self.OBJ_TYPE_CONVCORE,        witsml_1411_root + "obj_convCore.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.UPDATE_SCHEMA , self.OBJ_TYPE_FLUIDSREPORT,    witsml_1411_root + "obj_fluidsReport.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.UPDATE_SCHEMA , self.OBJ_TYPE_FORMATIONMARKER, witsml_1411_root + "obj_formationMarker.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.UPDATE_SCHEMA , self.OBJ_TYPE_LOG,             witsml_1411_root + "obj_log.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.UPDATE_SCHEMA , self.OBJ_TYPE_MESSAGE,         witsml_1411_root + "obj_message.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.UPDATE_SCHEMA , self.OBJ_TYPE_MUDLOG,          witsml_1411_root + "obj_mudLog.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.UPDATE_SCHEMA , self.OBJ_TYPE_OPSREPORT,       witsml_1411_root + "obj_opsReport.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.UPDATE_SCHEMA , self.OBJ_TYPE_RIG,             witsml_1411_root + "obj_rig.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.UPDATE_SCHEMA , self.OBJ_TYPE_RISK,            witsml_1411_root + "obj_risk.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.UPDATE_SCHEMA , self.OBJ_TYPE_SIDEWALLCORE,    witsml_1411_root + "obj_sidewallCore.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.UPDATE_SCHEMA , self.OBJ_TYPE_SURVEYPROGRAM,   witsml_1411_root + "obj_surveyProgram.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.UPDATE_SCHEMA , self.OBJ_TYPE_TARGET,          witsml_1411_root + "obj_target.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.UPDATE_SCHEMA , self.OBJ_TYPE_TRAJECTORY,      witsml_1411_root + "obj_trajectory.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.UPDATE_SCHEMA , self.OBJ_TYPE_TUBULAR,         witsml_1411_root + "obj_tubular.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.UPDATE_SCHEMA , self.OBJ_TYPE_WBGEOMETRY,      witsml_1411_root + "obj_wbGeometry.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.UPDATE_SCHEMA , self.OBJ_TYPE_WELL,            witsml_1411_root + "obj_well.xsd" );
        self.addParser( self.WITSML_VERSION_1411 , self.UPDATE_SCHEMA , self.OBJ_TYPE_WELLBORE,        witsml_1411_root + "obj_wellbore.xsd" );
    
    def validateXMLAgainstSchema( self , schema_version, schema_type , object_type, xml_string ):
        """ 
        check and validate does provided xml string complied with generic xml schema 
        
        parameters:
           - schema_version : which version is being validated
           - schema_type    : which type of schema we are validating against ( GENERIC_SCHEMA / READ_SCHEMA / WRITE_SCHEMA / DELETE_SCHEMA / UPDATE_SCHEMA ) 
           - object_type    : which object type is being validated  (WITSML object type)
           - xml_string     : xml for validation
        
        output:
          tuple :
             boolean , string  : success flag, and supplemental msg
        """
        if not (schema_version in self.known_schema_versions ):
            return False,"Can Not Run Validation : Schema version '"+str(schema_version)+"' is not registered in validator system";
        
        if not (schema_version in self.parsers ):
            return False,"Can Not Run Validation : There is no parsers for version '"+str(schema_version)+"' ";
        
        if not (schema_type in self.known_schema_types ):
            return False,"Can Not Run Validation : Invalid parameter for schema type";
        
        if not (schema_type in self.parsers[schema_version] ):
            return False,"Can Not Run Validation : There is no schema type '"+str(schema_type)+"'  for given version";
        
        if not (object_type in self.known_object_types ):
            return False,"Can Not Run Validation : Invalid object type '"+object_type+"'";
        
        if not (object_type in self.parsers[schema_version][schema_type] ):
            return False,"Can Not Run Validation : There is no object type '"+str(object_type)+"'  for given version / schema type";
        
        try:
            obz = objectify.fromstring( xml_string , self.parsers[schema_version][schema_type][object_type].getParser() );
            if (obz is None):
                return False,"Validation did not work'd as expected"
        except etree.XMLSyntaxError as e:
            return False , "XML is not Valid : "+str(e);
        
        return True,"XML is Valid"
    

    def validateXMLAgainstGenericSchema( self , schema_version , object_type, xml_string ):
        """
        check and validate does provided xml string complied with generic xml schema 
        parameters:
           - schema_version : which version is being validated 
           - object_type    : which object type is being validated  (WITSML object type)
           - xml_string     : xml for validation
        output:
          tuple :
             boolean , string  : success flag, and supplemental msg
        """
        return self.validateXMLAgainstSchema( schema_version, self.GENERIC_SCHEMA , object_type, xml_string )
        
        
    def validateXMLAgainstReadSchema( self , schema_version , object_type, xml_string ):
        """
        check and validate does provided xml string complied with generic xml schema 
        parameters:
           - schema_version : which version is being validated 
           - object_type    : which object type is being validated  (WITSML object type)
           - xml_string     : xml for validation
        output:
          tuple :
             boolean , string  : success flag, and supplemental msg
        """
        return self.validateXMLAgainstSchema( schema_version, self.READ_SCHEMA , object_type, xml_string )
    
    def validateXMLAgainstWriteSchema( self , schema_version , object_type, xml_string ):
        """
        check and validate does provided xml string complied with generic xml schema 
        parameters:
           - schema_version : which version is being validated 
           - object_type    : which object type is being validated  (WITSML object type)
           - xml_string     : xml for validation
        output:
          tuple :
             boolean , string  : success flag, and supplemental msg
        """
        return self.validateXMLAgainstSchema( schema_version, self.WRITE_SCHEMA , object_type, xml_string )
    
    def validateXMLAgainstDeleteSchema( self , schema_version , object_type, xml_string ):
        """
        check and validate does provided xml string complied with generic xml schema 
        parameters:
           - schema_version : which version is being validated 
           - object_type    : which object type is being validated  (WITSML object type)
           - xml_string     : xml for validation
        output:
          tuple :
             boolean , string  : success flag, and supplemental msg
        """
        return self.validateXMLAgainstSchema( schema_version, self.DELETE_SCHEMA , object_type, xml_string )
    
    def validateXMLAgainstUpdateSchema( self , schema_version , object_type, xml_string ):
        """
        check and validate does provided xml string complied with generic xml schema 
        parameters:
           - schema_version : which version is being validated 
           - object_type    : which object type is being validated  (WITSML object type)
           - xml_string     : xml for validation
        output:
          tuple :
             boolean , string  : success flag, and supplemental msg
        """
        return self.validateXMLAgainstSchema( schema_version, self.UPDATE_SCHEMA , object_type, xml_string )
    
#print "a"
#a = WITSMLSchemaValidator("/home/eflauzo/project/WITSMLSchemaValidationWorkspace/wvalidator/witsml_validator/schemas");
#print "b"
