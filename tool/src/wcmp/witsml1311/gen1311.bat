
echo cd ..\..\schema\WITSML_v1.4.1.1_Data_Schema\witsml_v1.4.1.0_data\xsd_schemas

python c:/python27/Scripts/pyxbgen -u obj_bhaRun.xsd                       -m witsml1311_obj_bhaRun
python c:/python27/Scripts/pyxbgen -u obj_cementJob.xsd                    -m witsml1311_obj_cementJob
python c:/python27/Scripts/pyxbgen -u obj_convCore.xsd                     -m witsml1311_obj_convCore
python c:/python27/Scripts/pyxbgen -u obj_coordinateReferenceSystem.xsd    -m witsml1311_obj_coordinateReferenceSystem
python c:/python27/Scripts/pyxbgen -u obj_drillReport.xsd                  -m witsml1311_obj_drillReport
python c:/python27/Scripts/pyxbgen -u obj_fluidsReport.xsd                 -m witsml1311_obj_fluidsReport
python c:/python27/Scripts/pyxbgen -u obj_formationMarker.xsd              -m witsml1311_obj_formationMarker
python c:/python27/Scripts/pyxbgen -u obj_log.xsd                          -m witsml1311_obj_log
python c:/python27/Scripts/pyxbgen -u obj_message.xsd                      -m witsml1311_obj_message
python c:/python27/Scripts/pyxbgen -u obj_mudLog.xsd                       -m witsml1311_obj_mudLog
python c:/python27/Scripts/pyxbgen -u obj_objectGroup.xsd                  -m witsml1311_obj_objectGroup
python c:/python27/Scripts/pyxbgen -u obj_opsReport.xsd                    -m witsml1311_obj_opsReport
python c:/python27/Scripts/pyxbgen -u obj_rig.xsd                          -m witsml1311_obj_rig
python c:/python27/Scripts/pyxbgen -u obj_risk.xsd                         -m witsml1311_obj_risk
python c:/python27/Scripts/pyxbgen -u obj_sidewallCore.xsd                 -m witsml1311_obj_sidewallCore
python c:/python27/Scripts/pyxbgen -u obj_stimJob.xsd                      -m witsml1311_obj_stimJob
python c:/python27/Scripts/pyxbgen -u obj_surveyProgram.xsd                -m witsml1311_obj_surveyProgram
python c:/python27/Scripts/pyxbgen -u obj_target.xsd                       -m witsml1311_obj_target
python c:/python27/Scripts/pyxbgen -u obj_toolErrorModel.xsd               -m witsml1311_obj_toolErrorModel
python c:/python27/Scripts/pyxbgen -u obj_toolErrorTermSet.xsd             -m witsml1311_obj_toolErrorTermSet
python c:/python27/Scripts/pyxbgen -u obj_trajectory.xsd                   -m witsml1311_obj_trajectory
python c:/python27/Scripts/pyxbgen -u obj_tubular.xsd                      -m witsml1311_obj_tubular
python c:/python27/Scripts/pyxbgen -u obj_wbGeometry.xsd                   -m witsml1311_obj_wbGeometry
python c:/python27/Scripts/pyxbgen -u obj_well.xsd                         -m witsml1311_obj_well
python c:/python27/Scripts/pyxbgen -u obj_wellbore.xsd                     -m witsml1311_obj_wellbore

echo 

echo "done"

pause