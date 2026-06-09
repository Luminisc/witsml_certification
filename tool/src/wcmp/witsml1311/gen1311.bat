@REM But probably should use 1.4.1 objects, as not all of this is part of 1.3.1.1
@REM echo cd ..\..\wsvt\schemas\WITSML_v1.3.1.1_Data_Schema

@REM python ..\..\..\..\.venv\Scripts\pyxbgen -u obj_bhaRun.xsd                       -m witsml1311_obj_bhaRun
@REM python ..\..\..\..\.venv\Scripts\pyxbgen -u obj_cementJob.xsd                    -m witsml1311_obj_cementJob
@REM python ..\..\..\..\.venv\Scripts\pyxbgen -u obj_convCore.xsd                     -m witsml1311_obj_convCore
@REM python ..\..\..\..\.venv\Scripts\pyxbgen -u obj_coordinateReferenceSystem.xsd    -m witsml1311_obj_coordinateReferenceSystem
@REM python ..\..\..\..\.venv\Scripts\pyxbgen -u obj_drillReport.xsd                  -m witsml1311_obj_drillReport
@REM python ..\..\..\..\.venv\Scripts\pyxbgen -u obj_fluidsReport.xsd                 -m witsml1311_obj_fluidsReport
@REM python ..\..\..\..\.venv\Scripts\pyxbgen -u obj_formationMarker.xsd              -m witsml1311_obj_formationMarker
@REM python ..\..\..\..\.venv\Scripts\pyxbgen -u obj_log.xsd                          -m witsml1311_obj_log
@REM python ..\..\..\..\.venv\Scripts\pyxbgen -u obj_message.xsd                      -m witsml1311_obj_message
@REM python ..\..\..\..\.venv\Scripts\pyxbgen -u obj_mudLog.xsd                       -m witsml1311_obj_mudLog
@REM python ..\..\..\..\.venv\Scripts\pyxbgen -u obj_objectGroup.xsd                  -m witsml1311_obj_objectGroup
@REM python ..\..\..\..\.venv\Scripts\pyxbgen -u obj_opsReport.xsd                    -m witsml1311_obj_opsReport
@REM python ..\..\..\..\.venv\Scripts\pyxbgen -u obj_rig.xsd                          -m witsml1311_obj_rig
@REM python ..\..\..\..\.venv\Scripts\pyxbgen -u obj_risk.xsd                         -m witsml1311_obj_risk
@REM python ..\..\..\..\.venv\Scripts\pyxbgen -u obj_sidewallCore.xsd                 -m witsml1311_obj_sidewallCore
@REM python ..\..\..\..\.venv\Scripts\pyxbgen -u obj_stimJob.xsd                      -m witsml1311_obj_stimJob
@REM python ..\..\..\..\.venv\Scripts\pyxbgen -u obj_surveyProgram.xsd                -m witsml1311_obj_surveyProgram
@REM python ..\..\..\..\.venv\Scripts\pyxbgen -u obj_target.xsd                       -m witsml1311_obj_target
@REM python ..\..\..\..\.venv\Scripts\pyxbgen -u obj_toolErrorModel.xsd               -m witsml1311_obj_toolErrorModel
@REM python ..\..\..\..\.venv\Scripts\pyxbgen -u obj_toolErrorTermSet.xsd             -m witsml1311_obj_toolErrorTermSet
@REM python ..\..\..\..\.venv\Scripts\pyxbgen -u obj_trajectory.xsd                   -m witsml1311_obj_trajectory
@REM python ..\..\..\..\.venv\Scripts\pyxbgen -u obj_tubular.xsd                      -m witsml1311_obj_tubular
@REM python ..\..\..\..\.venv\Scripts\pyxbgen -u obj_wbGeometry.xsd                   -m witsml1311_obj_wbGeometry
@REM python ..\..\..\..\.venv\Scripts\pyxbgen -u obj_well.xsd                         -m witsml1311_obj_well
@REM python ..\..\..\..\.venv\Scripts\pyxbgen -u obj_wellbore.xsd                     -m witsml1311_obj_wellbore

echo "done"

@REM pause