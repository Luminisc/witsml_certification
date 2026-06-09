'''
Created on Apr 23, 2013

@author: eflauzo
'''
import unittest
import sys;
import os;
sys.path.append("../src/wcmp");

import witsml_obj_compare;

XML_ORIGINAL = """<?xml version="1.0" encoding="UTF-8"?>
                <trajectorys xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                    <trajectory uidWell="Energistics-well-0001" uidWellbore="Energistics-w1-wellbore-0001" uid="Energistics-w1-wb1-trajectory-0001">
                        <nameWell>Energistics Certification Well 1</nameWell>
                        <nameWellbore>Energistics Certification Well 1 Wellbore 1</nameWellbore>
                        <name>Energistics Certification Well 1 Wellbore 1 Trajectory 1</name>
                        <dTimTrajStart>2001-10-31T08:15:00.000Z</dTimTrajStart>
                        <dTimTrajEnd>2001-11-03T16:30:00.000Z</dTimTrajEnd>
                        <mdMn uom="ft">0</mdMn>
                        <mdMx uom="ft">14089.3</mdMx>
                        <serviceCompany>Anadrill</serviceCompany>
                        <magDeclUsed uom="dega">-4.038</magDeclUsed>
                        <gridCorUsed uom="dega">0.99961</gridCorUsed>
                        <aziVertSect uom="dega">82.700</aziVertSect>
                        <dispNsVertSectOrig uom="ft">0</dispNsVertSectOrig>
                        <dispEwVertSectOrig uom="ft">0</dispEwVertSectOrig>
                        <definitive>true</definitive>
                        <memory>true</memory>
                        <finalTraj>true</finalTraj>
                        <aziRef>grid north</aziRef>
                        
                        <trajectoryStation uid="TRJ1">
                            <dTimStn>2001-10-21T08:15:00.000Z</dTimStn>
                            <typeTrajStation>tie in point</typeTrajStation>
                            <md uom="ft">0</md>
                            <tvd uom="ft">0</tvd>
                            <incl uom="dega">0</incl>
                            <azi uom="dega">47.3</azi>
                            <mtf uom="dega">47.3</mtf>
                            <gtf uom="dega">0</gtf>
                            <dispNs uom="ft">0</dispNs>
                            <dispEw uom="ft">0</dispEw>
                            <vertSect uom="ft">0</vertSect>
                            <dls uom="dega/ft">0</dls>
                            <rateTurn uom="dega/ft">0</rateTurn>
                            <rateBuild uom="dega/ft">0</rateBuild>
                            <mdDelta uom="ft">0</mdDelta>
                            <tvdDelta uom="ft">0</tvdDelta>
                            <modelToolError>good gyro</modelToolError>
                            <gravTotalUncert uom="m/s2">0</gravTotalUncert>
                            <dipAngleUncert uom="dega">0</dipAngleUncert>
                            <magTotalUncert uom="nT">0</magTotalUncert>
                            <gravAccelCorUsed>false</gravAccelCorUsed>
                            <magXAxialCorUsed>false</magXAxialCorUsed>
                            <sagCorUsed>false</sagCorUsed>
                            <magDrlstrCorUsed>false</magDrlstrCorUsed>
                            <statusTrajStation>position</statusTrajStation>
                        </trajectoryStation>
                        
                        
                        <trajectoryStation uid="TRJ2">
                            <dTimStn>2001-10-21T08:16:00.000Z</dTimStn>
                            <typeTrajStation>magnetic MWD</typeTrajStation>
                            <md uom="ft">1000.1</md>
                            <tvd uom="ft">1000.1</tvd>
                            <incl uom="dega">0</incl>
                            <azi uom="dega">180.0</azi>
                            <mtf uom="dega">47.3</mtf>
                            <gtf uom="dega">0</gtf>
                            <dispNs uom="ft">0</dispNs>
                            <dispEw uom="ft">0</dispEw>
                            <vertSect uom="ft">0</vertSect>
                            <dls uom="dega/ft">0</dls>
                            <rateTurn uom="dega/ft">0</rateTurn>
                            <rateBuild uom="dega/ft">0</rateBuild>
                            <mdDelta uom="ft">0</mdDelta>
                            <tvdDelta uom="ft">0</tvdDelta>
                            <modelToolError>good gyro</modelToolError>
                            <gravTotalUncert uom="m/s2">0</gravTotalUncert>
                            <dipAngleUncert uom="dega">0</dipAngleUncert>
                            <magTotalUncert uom="nT">0</magTotalUncert>
                            <gravAccelCorUsed>false</gravAccelCorUsed>
                            <magXAxialCorUsed>false</magXAxialCorUsed>
                            <sagCorUsed>false</sagCorUsed>
                            <magDrlstrCorUsed>false</magDrlstrCorUsed>
                            <statusTrajStation>position</statusTrajStation>
                        </trajectoryStation>
                        
                        
                        <commonData>
                            <itemState>plan</itemState>
                            <comments>These are the comments associated with the trajectory data object.</comments>
                        </commonData>
                    </trajectory>
                </trajectorys>
                """

class TestTrajectoryComparison(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testEqualNoChange(self):
        XML_INSPECT = """<?xml version="1.0" encoding="UTF-8"?>
                <trajectorys xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                    <trajectory uidWell="Energistics-well-0001" uidWellbore="Energistics-w1-wellbore-0001" uid="Energistics-w1-wb1-trajectory-0001">
                        <nameWell>Energistics Certification Well 1</nameWell>
                        <nameWellbore>Energistics Certification Well 1 Wellbore 1</nameWellbore>
                        <name>Energistics Certification Well 1 Wellbore 1 Trajectory 1</name>
                        <dTimTrajStart>2001-10-31T08:15:00.000Z</dTimTrajStart>
                        <dTimTrajEnd>2001-11-03T16:30:00.000Z</dTimTrajEnd>
                        <mdMn uom="ft">0</mdMn>
                        <mdMx uom="ft">14089.3</mdMx>
                        <serviceCompany>Anadrill</serviceCompany>
                        <magDeclUsed uom="dega">-4.038</magDeclUsed>
                        <gridCorUsed uom="dega">0.99961</gridCorUsed>
                        <aziVertSect uom="dega">82.700</aziVertSect>
                        <dispNsVertSectOrig uom="ft">0</dispNsVertSectOrig>
                        <dispEwVertSectOrig uom="ft">0</dispEwVertSectOrig>
                        <definitive>true</definitive>
                        <memory>true</memory>
                        <finalTraj>true</finalTraj>
                        <aziRef>grid north</aziRef>
                        
                        <trajectoryStation uid="TRJ1">
                            <dTimStn>2001-10-21T08:15:00.000Z</dTimStn>
                            <typeTrajStation>tie in point</typeTrajStation>
                            <md uom="ft">0</md>
                            <tvd uom="ft">0</tvd>
                            <incl uom="dega">0</incl>
                            <azi uom="dega">47.3</azi>
                            <mtf uom="dega">47.3</mtf>
                            <gtf uom="dega">0</gtf>
                            <dispNs uom="ft">0</dispNs>
                            <dispEw uom="ft">0</dispEw>
                            <vertSect uom="ft">0</vertSect>
                            <dls uom="dega/ft">0</dls>
                            <rateTurn uom="dega/ft">0</rateTurn>
                            <rateBuild uom="dega/ft">0</rateBuild>
                            <mdDelta uom="ft">0</mdDelta>
                            <tvdDelta uom="ft">0</tvdDelta>
                            <modelToolError>good gyro</modelToolError>
                            <gravTotalUncert uom="m/s2">0</gravTotalUncert>
                            <dipAngleUncert uom="dega">0</dipAngleUncert>
                            <magTotalUncert uom="nT">0</magTotalUncert>
                            <gravAccelCorUsed>false</gravAccelCorUsed>
                            <magXAxialCorUsed>false</magXAxialCorUsed>
                            <sagCorUsed>false</sagCorUsed>
                            <magDrlstrCorUsed>false</magDrlstrCorUsed>
                            <statusTrajStation>position</statusTrajStation>
                        </trajectoryStation>
                        
                        
                        <trajectoryStation uid="TRJ2">
                            <dTimStn>2001-10-21T08:16:00.000Z</dTimStn>
                            <typeTrajStation>magnetic MWD</typeTrajStation>
                            <md uom="ft">1000.1</md>
                            <tvd uom="ft">1000.1</tvd>
                            <incl uom="dega">0</incl>
                            <azi uom="dega">180.0</azi>
                            <mtf uom="dega">47.3</mtf>
                            <gtf uom="dega">0</gtf>
                            <dispNs uom="ft">0</dispNs>
                            <dispEw uom="ft">0</dispEw>
                            <vertSect uom="ft">0</vertSect>
                            <dls uom="dega/ft">0</dls>
                            <rateTurn uom="dega/ft">0</rateTurn>
                            <rateBuild uom="dega/ft">0</rateBuild>
                            <mdDelta uom="ft">0</mdDelta>
                            <tvdDelta uom="ft">0</tvdDelta>
                            <modelToolError>good gyro</modelToolError>
                            <gravTotalUncert uom="m/s2">0</gravTotalUncert>
                            <dipAngleUncert uom="dega">0</dipAngleUncert>
                            <magTotalUncert uom="nT">0</magTotalUncert>
                            <gravAccelCorUsed>false</gravAccelCorUsed>
                            <magXAxialCorUsed>false</magXAxialCorUsed>
                            <sagCorUsed>false</sagCorUsed>
                            <magDrlstrCorUsed>false</magDrlstrCorUsed>
                            <statusTrajStation>position</statusTrajStation>
                        </trajectoryStation>
                        
                        
                        <commonData>
                            <itemState>plan</itemState>
                            <comments>These are the comments associated with the trajectory data object.</comments>
                        </commonData>
                    </trajectory>
                </trajectorys>
                """
        result, report = witsml_obj_compare.witsml1411_compare_obj_trajectorys( XML_ORIGINAL , XML_INSPECT , True)
        print(report);
        self.assertTrue( result );
        pass
    
    
    def testTrajectoryFail_different_serviceCompany(self):
        XML_INSPECT = """<?xml version="1.0" encoding="UTF-8"?>
                <trajectorys xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                    <trajectory uidWell="Energistics-well-0001" uidWellbore="Energistics-w1-wellbore-0001" uid="Energistics-w1-wb1-trajectory-0001">
                        <nameWell>Energistics Certification Well 1</nameWell>
                        <nameWellbore>Energistics Certification Well 1 Wellbore 1</nameWellbore>
                        <name>Energistics Certification Well 1 Wellbore 1 Trajectory 1</name>
                        <dTimTrajStart>2001-10-31T08:15:00.000Z</dTimTrajStart>
                        <dTimTrajEnd>2001-11-03T16:30:00.000Z</dTimTrajEnd>
                        <mdMn uom="ft">0</mdMn>
                        <mdMx uom="ft">14089.3</mdMx>
                        <serviceCompany>Anadrill2</serviceCompany>
                        <magDeclUsed uom="dega">-4.038</magDeclUsed>
                        <gridCorUsed uom="dega">0.99961</gridCorUsed>
                        <aziVertSect uom="dega">82.700</aziVertSect>
                        <dispNsVertSectOrig uom="ft">0</dispNsVertSectOrig>
                        <dispEwVertSectOrig uom="ft">0</dispEwVertSectOrig>
                        <definitive>true</definitive>
                        <memory>true</memory>
                        <finalTraj>true</finalTraj>
                        <aziRef>grid north</aziRef>
                        
                        <trajectoryStation uid="TRJ1">
                            <dTimStn>2001-10-21T08:15:00.000Z</dTimStn>
                            <typeTrajStation>tie in point</typeTrajStation>
                            <md uom="ft">0</md>
                            <tvd uom="ft">0</tvd>
                            <incl uom="dega">0</incl>
                            <azi uom="dega">47.3</azi>
                            <mtf uom="dega">47.3</mtf>
                            <gtf uom="dega">0</gtf>
                            <dispNs uom="ft">0</dispNs>
                            <dispEw uom="ft">0</dispEw>
                            <vertSect uom="ft">0</vertSect>
                            <dls uom="dega/ft">0</dls>
                            <rateTurn uom="dega/ft">0</rateTurn>
                            <rateBuild uom="dega/ft">0</rateBuild>
                            <mdDelta uom="ft">0</mdDelta>
                            <tvdDelta uom="ft">0</tvdDelta>
                            <modelToolError>good gyro</modelToolError>
                            <gravTotalUncert uom="m/s2">0</gravTotalUncert>
                            <dipAngleUncert uom="dega">0</dipAngleUncert>
                            <magTotalUncert uom="nT">0</magTotalUncert>
                            <gravAccelCorUsed>false</gravAccelCorUsed>
                            <magXAxialCorUsed>false</magXAxialCorUsed>
                            <sagCorUsed>false</sagCorUsed>
                            <magDrlstrCorUsed>false</magDrlstrCorUsed>
                            <statusTrajStation>position</statusTrajStation>
                        </trajectoryStation>
                        
                        
                        <trajectoryStation uid="TRJ2">
                            <dTimStn>2001-10-21T08:16:00.000Z</dTimStn>
                            <typeTrajStation>magnetic MWD</typeTrajStation>
                            <md uom="ft">1000.1</md>
                            <tvd uom="ft">1000.1</tvd>
                            <incl uom="dega">0</incl>
                            <azi uom="dega">180.0</azi>
                            <mtf uom="dega">47.3</mtf>
                            <gtf uom="dega">0</gtf>
                            <dispNs uom="ft">0</dispNs>
                            <dispEw uom="ft">0</dispEw>
                            <vertSect uom="ft">0</vertSect>
                            <dls uom="dega/ft">0</dls>
                            <rateTurn uom="dega/ft">0</rateTurn>
                            <rateBuild uom="dega/ft">0</rateBuild>
                            <mdDelta uom="ft">0</mdDelta>
                            <tvdDelta uom="ft">0</tvdDelta>
                            <modelToolError>good gyro</modelToolError>
                            <gravTotalUncert uom="m/s2">0</gravTotalUncert>
                            <dipAngleUncert uom="dega">0</dipAngleUncert>
                            <magTotalUncert uom="nT">0</magTotalUncert>
                            <gravAccelCorUsed>false</gravAccelCorUsed>
                            <magXAxialCorUsed>false</magXAxialCorUsed>
                            <sagCorUsed>false</sagCorUsed>
                            <magDrlstrCorUsed>false</magDrlstrCorUsed>
                            <statusTrajStation>position</statusTrajStation>
                        </trajectoryStation>
                        
                        
                        <commonData>
                            <itemState>plan</itemState>
                            <comments>These are the comments associated with the trajectory data object.</comments>
                        </commonData>
                    </trajectory>
                </trajectorys>
                """
        result, report = witsml_obj_compare.witsml1411_compare_obj_trajectorys( XML_ORIGINAL , XML_INSPECT , True)
        print(report);
        self.assertFalse( result );
        pass
    
    
    def testObjectIsEqual_StationsInReversedOrder(self):
        XML_INSPECT = """<?xml version="1.0" encoding="UTF-8"?>
                <trajectorys xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                    <trajectory uidWell="Energistics-well-0001" uidWellbore="Energistics-w1-wellbore-0001" uid="Energistics-w1-wb1-trajectory-0001">
                        <nameWell>Energistics Certification Well 1</nameWell>
                        <nameWellbore>Energistics Certification Well 1 Wellbore 1</nameWellbore>
                        <name>Energistics Certification Well 1 Wellbore 1 Trajectory 1</name>
                        <dTimTrajStart>2001-10-31T08:15:00.000Z</dTimTrajStart>
                        <dTimTrajEnd>2001-11-03T16:30:00.000Z</dTimTrajEnd>
                        <mdMn uom="ft">0</mdMn>
                        <mdMx uom="ft">14089.3</mdMx>
                        <serviceCompany>Anadrill</serviceCompany>
                        <magDeclUsed uom="dega">-4.038</magDeclUsed>
                        <gridCorUsed uom="dega">0.99961</gridCorUsed>
                        <aziVertSect uom="dega">82.700</aziVertSect>
                        <dispNsVertSectOrig uom="ft">0</dispNsVertSectOrig>
                        <dispEwVertSectOrig uom="ft">0</dispEwVertSectOrig>
                        <definitive>true</definitive>
                        <memory>true</memory>
                        <finalTraj>true</finalTraj>
                        <aziRef>grid north</aziRef>
                        
                        
                        <trajectoryStation uid="TRJ2">
                            <dTimStn>2001-10-21T08:16:00.000Z</dTimStn>
                            <typeTrajStation>magnetic MWD</typeTrajStation>
                            <md uom="ft">1000.1</md>
                            <tvd uom="ft">1000.1</tvd>
                            <incl uom="dega">0</incl>
                            <azi uom="dega">180.0</azi>
                            <mtf uom="dega">47.3</mtf>
                            <gtf uom="dega">0</gtf>
                            <dispNs uom="ft">0</dispNs>
                            <dispEw uom="ft">0</dispEw>
                            <vertSect uom="ft">0</vertSect>
                            <dls uom="dega/ft">0</dls>
                            <rateTurn uom="dega/ft">0</rateTurn>
                            <rateBuild uom="dega/ft">0</rateBuild>
                            <mdDelta uom="ft">0</mdDelta>
                            <tvdDelta uom="ft">0</tvdDelta>
                            <modelToolError>good gyro</modelToolError>
                            <gravTotalUncert uom="m/s2">0</gravTotalUncert>
                            <dipAngleUncert uom="dega">0</dipAngleUncert>
                            <magTotalUncert uom="nT">0</magTotalUncert>
                            <gravAccelCorUsed>false</gravAccelCorUsed>
                            <magXAxialCorUsed>false</magXAxialCorUsed>
                            <sagCorUsed>false</sagCorUsed>
                            <magDrlstrCorUsed>false</magDrlstrCorUsed>
                            <statusTrajStation>position</statusTrajStation>
                        </trajectoryStation>
                        
                        
                        <trajectoryStation uid="TRJ1">
                            <dTimStn>2001-10-21T08:15:00.000Z</dTimStn>
                            <typeTrajStation>tie in point</typeTrajStation>
                            <md uom="ft">0</md>
                            <tvd uom="ft">0</tvd>
                            <incl uom="dega">0</incl>
                            <azi uom="dega">47.3</azi>
                            <mtf uom="dega">47.3</mtf>
                            <gtf uom="dega">0</gtf>
                            <dispNs uom="ft">0</dispNs>
                            <dispEw uom="ft">0</dispEw>
                            <vertSect uom="ft">0</vertSect>
                            <dls uom="dega/ft">0</dls>
                            <rateTurn uom="dega/ft">0</rateTurn>
                            <rateBuild uom="dega/ft">0</rateBuild>
                            <mdDelta uom="ft">0</mdDelta>
                            <tvdDelta uom="ft">0</tvdDelta>
                            <modelToolError>good gyro</modelToolError>
                            <gravTotalUncert uom="m/s2">0</gravTotalUncert>
                            <dipAngleUncert uom="dega">0</dipAngleUncert>
                            <magTotalUncert uom="nT">0</magTotalUncert>
                            <gravAccelCorUsed>false</gravAccelCorUsed>
                            <magXAxialCorUsed>false</magXAxialCorUsed>
                            <sagCorUsed>false</sagCorUsed>
                            <magDrlstrCorUsed>false</magDrlstrCorUsed>
                            <statusTrajStation>position</statusTrajStation>
                        </trajectoryStation>
                        
                        <commonData>
                            <itemState>plan</itemState>
                            <comments>These are the comments associated with the trajectory data object.</comments>
                        </commonData>
                    </trajectory>
                </trajectorys>
                """
        result, report = witsml_obj_compare.witsml1411_compare_obj_trajectorys( XML_ORIGINAL , XML_INSPECT , True)
        print(report);
        self.assertTrue( result );
        pass


    def testmdMxIsDifferentButWithinTollerance(self):
        XML_INSPECT = """<?xml version="1.0" encoding="UTF-8"?>
                <trajectorys xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                    <trajectory uidWell="Energistics-well-0001" uidWellbore="Energistics-w1-wellbore-0001" uid="Energistics-w1-wb1-trajectory-0001">
                        <nameWell>Energistics Certification Well 1</nameWell>
                        <nameWellbore>Energistics Certification Well 1 Wellbore 1</nameWellbore>
                        <name>Energistics Certification Well 1 Wellbore 1 Trajectory 1</name>
                        <dTimTrajStart>2001-10-31T08:15:00.000Z</dTimTrajStart>
                        <dTimTrajEnd>2001-11-03T16:30:00.000Z</dTimTrajEnd>
                        <mdMn uom="ft">0</mdMn>
                        <mdMx uom="ft">14089.30001</mdMx>
                        <serviceCompany>Anadrill</serviceCompany>
                        <magDeclUsed uom="dega">-4.038</magDeclUsed>
                        <gridCorUsed uom="dega">0.99961</gridCorUsed>
                        <aziVertSect uom="dega">82.700</aziVertSect>
                        <dispNsVertSectOrig uom="ft">0</dispNsVertSectOrig>
                        <dispEwVertSectOrig uom="ft">0</dispEwVertSectOrig>
                        <definitive>true</definitive>
                        <memory>true</memory>
                        <finalTraj>true</finalTraj>
                        <aziRef>grid north</aziRef>
                        
                        <trajectoryStation uid="TRJ1">
                            <dTimStn>2001-10-21T08:15:00.000Z</dTimStn>
                            <typeTrajStation>tie in point</typeTrajStation>
                            <md uom="ft">0</md>
                            <tvd uom="ft">0</tvd>
                            <incl uom="dega">0.0</incl>
                            <azi uom="dega">47.3</azi>
                            <mtf uom="dega">47.3</mtf>
                            <gtf uom="dega">0</gtf>
                            <dispNs uom="ft">0</dispNs>
                            <dispEw uom="ft">0</dispEw>
                            <vertSect uom="ft">0</vertSect>
                            <dls uom="dega/ft">0</dls>
                            <rateTurn uom="dega/ft">0</rateTurn>
                            <rateBuild uom="dega/ft">0</rateBuild>
                            <mdDelta uom="ft">0</mdDelta>
                            <tvdDelta uom="ft">0</tvdDelta>
                            <modelToolError>good gyro</modelToolError>
                            <gravTotalUncert uom="m/s2">0</gravTotalUncert>
                            <dipAngleUncert uom="dega">0</dipAngleUncert>
                            <magTotalUncert uom="nT">0</magTotalUncert>
                            <gravAccelCorUsed>false</gravAccelCorUsed>
                            <magXAxialCorUsed>false</magXAxialCorUsed>
                            <sagCorUsed>false</sagCorUsed>
                            <magDrlstrCorUsed>false</magDrlstrCorUsed>
                            <statusTrajStation>position</statusTrajStation>
                        </trajectoryStation>
                        
                        
                        <trajectoryStation uid="TRJ2">
                            <dTimStn>2001-10-21T08:16:00.000Z</dTimStn>
                            <typeTrajStation>magnetic MWD</typeTrajStation>
                            <md uom="ft">1000.1</md>
                            <tvd uom="ft">1000.1</tvd>
                            <incl uom="dega">0</incl>
                            <azi uom="dega">180.0</azi>
                            <mtf uom="dega">47.3</mtf>
                            <gtf uom="dega">0</gtf>
                            <dispNs uom="ft">0</dispNs>
                            <dispEw uom="ft">0</dispEw>
                            <vertSect uom="ft">0</vertSect>
                            <dls uom="dega/ft">0</dls>
                            <rateTurn uom="dega/ft">0</rateTurn>
                            <rateBuild uom="dega/ft">0</rateBuild>
                            <mdDelta uom="ft">0</mdDelta>
                            <tvdDelta uom="ft">0</tvdDelta>
                            <modelToolError>good gyro</modelToolError>
                            <gravTotalUncert uom="m/s2">0</gravTotalUncert>
                            <dipAngleUncert uom="dega">0</dipAngleUncert>
                            <magTotalUncert uom="nT">0</magTotalUncert>
                            <gravAccelCorUsed>false</gravAccelCorUsed>
                            <magXAxialCorUsed>false</magXAxialCorUsed>
                            <sagCorUsed>false</sagCorUsed>
                            <magDrlstrCorUsed>false</magDrlstrCorUsed>
                            <statusTrajStation>position</statusTrajStation>
                        </trajectoryStation>
                        
                        
                        <commonData>
                            <itemState>plan</itemState>
                            <comments>These are the comments associated with the trajectory data object.</comments>
                        </commonData>
                    </trajectory>
                </trajectorys>
                """
        result, report = witsml_obj_compare.witsml1411_compare_obj_trajectorys( XML_ORIGINAL , XML_INSPECT , True)
        print(report);
        self.assertTrue( result );
        pass

    def testDifferentInclination(self):
        XML_INSPECT = """<?xml version="1.0" encoding="UTF-8"?>
                <trajectorys xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                    <trajectory uidWell="Energistics-well-0001" uidWellbore="Energistics-w1-wellbore-0001" uid="Energistics-w1-wb1-trajectory-0001">
                        <nameWell>Energistics Certification Well 1</nameWell>
                        <nameWellbore>Energistics Certification Well 1 Wellbore 1</nameWellbore>
                        <name>Energistics Certification Well 1 Wellbore 1 Trajectory 1</name>
                        <dTimTrajStart>2001-10-31T08:15:00.000Z</dTimTrajStart>
                        <dTimTrajEnd>2001-11-03T16:30:00.000Z</dTimTrajEnd>
                        <mdMn uom="ft">0</mdMn>
                        <mdMx uom="ft">14089.3</mdMx>
                        <serviceCompany>Anadrill</serviceCompany>
                        <magDeclUsed uom="dega">-4.038</magDeclUsed>
                        <gridCorUsed uom="dega">0.99961</gridCorUsed>
                        <aziVertSect uom="dega">82.700</aziVertSect>
                        <dispNsVertSectOrig uom="ft">0</dispNsVertSectOrig>
                        <dispEwVertSectOrig uom="ft">0</dispEwVertSectOrig>
                        <definitive>true</definitive>
                        <memory>true</memory>
                        <finalTraj>true</finalTraj>
                        <aziRef>grid north</aziRef>
                        
                        <trajectoryStation uid="TRJ1">
                            <dTimStn>2001-10-21T08:15:00.000Z</dTimStn>
                            <typeTrajStation>tie in point</typeTrajStation>
                            <md uom="ft">0</md>
                            <tvd uom="ft">0</tvd>
                            <incl uom="dega">2</incl>
                            <azi uom="dega">47.3</azi>
                            <mtf uom="dega">47.3</mtf>
                            <gtf uom="dega">0</gtf>
                            <dispNs uom="ft">0</dispNs>
                            <dispEw uom="ft">0</dispEw>
                            <vertSect uom="ft">0</vertSect>
                            <dls uom="dega/ft">0</dls>
                            <rateTurn uom="dega/ft">0</rateTurn>
                            <rateBuild uom="dega/ft">0</rateBuild>
                            <mdDelta uom="ft">0</mdDelta>
                            <tvdDelta uom="ft">0</tvdDelta>
                            <modelToolError>good gyro</modelToolError>
                            <gravTotalUncert uom="m/s2">0</gravTotalUncert>
                            <dipAngleUncert uom="dega">0</dipAngleUncert>
                            <magTotalUncert uom="nT">0</magTotalUncert>
                            <gravAccelCorUsed>false</gravAccelCorUsed>
                            <magXAxialCorUsed>false</magXAxialCorUsed>
                            <sagCorUsed>false</sagCorUsed>
                            <magDrlstrCorUsed>false</magDrlstrCorUsed>
                            <statusTrajStation>position</statusTrajStation>
                        </trajectoryStation>
                        
                        
                        <trajectoryStation uid="TRJ2">
                            <dTimStn>2001-10-21T08:16:00.000Z</dTimStn>
                            <typeTrajStation>magnetic MWD</typeTrajStation>
                            <md uom="ft">1000.1</md>
                            <tvd uom="ft">1000.1</tvd>
                            <incl uom="dega">0</incl>
                            <azi uom="dega">180.0</azi>
                            <mtf uom="dega">47.3</mtf>
                            <gtf uom="dega">0</gtf>
                            <dispNs uom="ft">0</dispNs>
                            <dispEw uom="ft">0</dispEw>
                            <vertSect uom="ft">0</vertSect>
                            <dls uom="dega/ft">0</dls>
                            <rateTurn uom="dega/ft">0</rateTurn>
                            <rateBuild uom="dega/ft">0</rateBuild>
                            <mdDelta uom="ft">0</mdDelta>
                            <tvdDelta uom="ft">0</tvdDelta>
                            <modelToolError>good gyro</modelToolError>
                            <gravTotalUncert uom="m/s2">0</gravTotalUncert>
                            <dipAngleUncert uom="dega">0</dipAngleUncert>
                            <magTotalUncert uom="nT">0</magTotalUncert>
                            <gravAccelCorUsed>false</gravAccelCorUsed>
                            <magXAxialCorUsed>false</magXAxialCorUsed>
                            <sagCorUsed>false</sagCorUsed>
                            <magDrlstrCorUsed>false</magDrlstrCorUsed>
                            <statusTrajStation>position</statusTrajStation>
                        </trajectoryStation>
                        
                        
                        <commonData>
                            <itemState>plan</itemState>
                            <comments>These are the comments associated with the trajectory data object.</comments>
                        </commonData>
                    </trajectory>
                </trajectorys>
                """
        result, report = witsml_obj_compare.witsml1411_compare_obj_trajectorys( XML_ORIGINAL , XML_INSPECT , True)
        print(report);
        self.assertFalse( result );
        pass
  


    def testChanged_aziVertSect(self):
        XML_INSPECT = """<?xml version="1.0" encoding="UTF-8"?>
                <trajectorys xmlns="http://www.witsml.org/schemas/1series" version="$server_schema_version$">
                    <trajectory uidWell="Energistics-well-0001" uidWellbore="Energistics-w1-wellbore-0001" uid="Energistics-w1-wb1-trajectory-0001">
                        <nameWell>Energistics Certification Well 1</nameWell>
                        <nameWellbore>Energistics Certification Well 1 Wellbore 1</nameWellbore>
                        <name>Energistics Certification Well 1 Wellbore 1 Trajectory 1</name>
                        <dTimTrajStart>2001-10-31T08:15:00.000Z</dTimTrajStart>
                        <dTimTrajEnd>2001-11-03T16:30:00.000Z</dTimTrajEnd>
                        <mdMn uom="ft">0</mdMn>
                        <mdMx uom="ft">14089.3</mdMx>
                        <serviceCompany>Anadrill</serviceCompany>
                        <magDeclUsed uom="dega">-4.038</magDeclUsed>
                        <gridCorUsed uom="dega">0.99961</gridCorUsed>
                        <aziVertSect uom="dega">83.700</aziVertSect>
                        <dispNsVertSectOrig uom="ft">0</dispNsVertSectOrig>
                        <dispEwVertSectOrig uom="ft">0</dispEwVertSectOrig>
                        <definitive>true</definitive>
                        <memory>true</memory>
                        <finalTraj>true</finalTraj>
                        <aziRef>grid north</aziRef>
                        
                        <trajectoryStation uid="TRJ1">
                            <dTimStn>2001-10-21T08:15:00.000Z</dTimStn>
                            <typeTrajStation>tie in point</typeTrajStation>
                            <md uom="ft">0</md>
                            <tvd uom="ft">0</tvd>
                            <incl uom="dega">0</incl>
                            <azi uom="dega">47.3</azi>
                            <mtf uom="dega">47.3</mtf>
                            <gtf uom="dega">0</gtf>
                            <dispNs uom="ft">0</dispNs>
                            <dispEw uom="ft">0</dispEw>
                            <vertSect uom="ft">0</vertSect>
                            <dls uom="dega/ft">0</dls>
                            <rateTurn uom="dega/ft">0</rateTurn>
                            <rateBuild uom="dega/ft">0</rateBuild>
                            <mdDelta uom="ft">0</mdDelta>
                            <tvdDelta uom="ft">0</tvdDelta>
                            <modelToolError>good gyro</modelToolError>
                            <gravTotalUncert uom="m/s2">0</gravTotalUncert>
                            <dipAngleUncert uom="dega">0</dipAngleUncert>
                            <magTotalUncert uom="nT">0</magTotalUncert>
                            <gravAccelCorUsed>false</gravAccelCorUsed>
                            <magXAxialCorUsed>false</magXAxialCorUsed>
                            <sagCorUsed>false</sagCorUsed>
                            <magDrlstrCorUsed>false</magDrlstrCorUsed>
                            <statusTrajStation>position</statusTrajStation>
                        </trajectoryStation>
                        
                        
                        <trajectoryStation uid="TRJ2">
                            <dTimStn>2001-10-21T08:16:00.000Z</dTimStn>
                            <typeTrajStation>magnetic MWD</typeTrajStation>
                            <md uom="ft">1000.1</md>
                            <tvd uom="ft">1000.1</tvd>
                            <incl uom="dega">0</incl>
                            <azi uom="dega">180.0</azi>
                            <mtf uom="dega">47.3</mtf>
                            <gtf uom="dega">0</gtf>
                            <dispNs uom="ft">0</dispNs>
                            <dispEw uom="ft">0</dispEw>
                            <vertSect uom="ft">0</vertSect>
                            <dls uom="dega/ft">0</dls>
                            <rateTurn uom="dega/ft">0</rateTurn>
                            <rateBuild uom="dega/ft">0</rateBuild>
                            <mdDelta uom="ft">0</mdDelta>
                            <tvdDelta uom="ft">0</tvdDelta>
                            <modelToolError>good gyro</modelToolError>
                            <gravTotalUncert uom="m/s2">0</gravTotalUncert>
                            <dipAngleUncert uom="dega">0</dipAngleUncert>
                            <magTotalUncert uom="nT">0</magTotalUncert>
                            <gravAccelCorUsed>false</gravAccelCorUsed>
                            <magXAxialCorUsed>false</magXAxialCorUsed>
                            <sagCorUsed>false</sagCorUsed>
                            <magDrlstrCorUsed>false</magDrlstrCorUsed>
                            <statusTrajStation>position</statusTrajStation>
                        </trajectoryStation>
                        
                        
                        <commonData>
                            <itemState>plan</itemState>
                            <comments>These are the comments associated with the trajectory data object.</comments>
                        </commonData>
                    </trajectory>
                </trajectorys>
                """
        result, report = witsml_obj_compare.witsml1411_compare_obj_trajectorys( XML_ORIGINAL , XML_INSPECT , True)
        print(report);
        self.assertFalse( result );
        pass
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()