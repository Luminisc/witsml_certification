#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCHEMA_DIR="$SCRIPT_DIR/../../wsvt/schemas/WITSML_v1.4.1.1_Data_Schema/witsml_v1.4.1.1_data/xsd_schemas"

PYXBGEN_OPTS="--schema-root=$SCHEMA_DIR --binding-root=$SCRIPT_DIR --strip-file-paths"

echo "SCRIPT_DIR: $SCRIPT_DIR"
echo "SCHEMA_DIR: $SCHEMA_DIR"

pyxbgen $PYXBGEN_OPTS -u obj_attachment.xsd                   -m witsml1411_obj_attachment
pyxbgen $PYXBGEN_OPTS -u obj_bhaRun.xsd                       -m witsml1411_obj_bhaRun
pyxbgen $PYXBGEN_OPTS -u obj_cementJob.xsd                    -m witsml1411_obj_cementJob
pyxbgen $PYXBGEN_OPTS -u obj_changeLog.xsd                    -m witsml1411_obj_changeLog
pyxbgen $PYXBGEN_OPTS -u obj_convCore.xsd                     -m witsml1411_obj_convCore
pyxbgen $PYXBGEN_OPTS -u obj_coordinateReferenceSystem.xsd    -m witsml1411_obj_coordinateReferenceSystem
pyxbgen $PYXBGEN_OPTS -u obj_drillReport.xsd                  -m witsml1411_obj_drillReport
pyxbgen $PYXBGEN_OPTS -u obj_fluidsReport.xsd                 -m witsml1411_obj_fluidsReport
pyxbgen $PYXBGEN_OPTS -u obj_formationMarker.xsd              -m witsml1411_obj_formationMarker
pyxbgen $PYXBGEN_OPTS -u obj_log.xsd                          -m witsml1411_obj_log
pyxbgen $PYXBGEN_OPTS -u obj_message.xsd                      -m witsml1411_obj_message
pyxbgen $PYXBGEN_OPTS -u obj_mudLog.xsd                       -m witsml1411_obj_mudLog
pyxbgen $PYXBGEN_OPTS -u obj_objectGroup.xsd                  -m witsml1411_obj_objectGroup
pyxbgen $PYXBGEN_OPTS -u obj_opsReport.xsd                    -m witsml1411_obj_opsReport
pyxbgen $PYXBGEN_OPTS -u obj_rig.xsd                          -m witsml1411_obj_rig
pyxbgen $PYXBGEN_OPTS -u obj_risk.xsd                         -m witsml1411_obj_risk
pyxbgen $PYXBGEN_OPTS -u obj_sidewallCore.xsd                 -m witsml1411_obj_sidewallCore
pyxbgen $PYXBGEN_OPTS -u obj_stimJob.xsd                      -m witsml1411_obj_stimJob
pyxbgen $PYXBGEN_OPTS -u obj_surveyProgram.xsd                -m witsml1411_obj_surveyProgram
pyxbgen $PYXBGEN_OPTS -u obj_target.xsd                       -m witsml1411_obj_target
pyxbgen $PYXBGEN_OPTS -u obj_toolErrorModel.xsd               -m witsml1411_obj_toolErrorModel
pyxbgen $PYXBGEN_OPTS -u obj_toolErrorTermSet.xsd             -m witsml1411_obj_toolErrorTermSet
pyxbgen $PYXBGEN_OPTS -u obj_trajectory.xsd                   -m witsml1411_obj_trajectory
pyxbgen $PYXBGEN_OPTS -u obj_tubular.xsd                      -m witsml1411_obj_tubular
pyxbgen $PYXBGEN_OPTS -u obj_wbGeometry.xsd                   -m witsml1411_obj_wbGeometry
pyxbgen $PYXBGEN_OPTS -u obj_well.xsd                         -m witsml1411_obj_well
pyxbgen $PYXBGEN_OPTS -u obj_wellbore.xsd                     -m witsml1411_obj_wellbore

echo "done"