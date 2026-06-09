#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# But probably should use 1.4.1 objects, as not all of this is part of 1.3.1.1
SCHEMA_DIR="$SCRIPT_DIR/../../wsvt/schemas/WITSML_v1.3.1.1_Data_Schema"

PYXBGEN_OPTS="--schema-root=$SCHEMA_DIR --binding-root=$SCRIPT_DIR --strip-file-paths"

echo "SCRIPT_DIR: $SCRIPT_DIR"
echo "SCHEMA_DIR: $SCHEMA_DIR"

pyxbgen $PYXBGEN_OPTS -u obj_bhaRun.xsd                     -m witsml1311_obj_bhaRun
pyxbgen $PYXBGEN_OPTS -u obj_cementJob.xsd                  -m witsml1311_obj_cementJob
pyxbgen $PYXBGEN_OPTS -u obj_convCore.xsd                   -m witsml1311_obj_convCore
pyxbgen $PYXBGEN_OPTS -u obj_coordinateReferenceSystem.xsd  -m witsml1311_obj_coordinateReferenceSystem
pyxbgen $PYXBGEN_OPTS -u obj_drillReport.xsd                -m witsml1311_obj_drillReport
pyxbgen $PYXBGEN_OPTS -u obj_fluidsReport.xsd               -m witsml1311_obj_fluidsReport
pyxbgen $PYXBGEN_OPTS -u obj_formationMarker.xsd            -m witsml1311_obj_formationMarker
pyxbgen $PYXBGEN_OPTS -u obj_log.xsd                        -m witsml1311_obj_log
pyxbgen $PYXBGEN_OPTS -u obj_message.xsd                    -m witsml1311_obj_message
pyxbgen $PYXBGEN_OPTS -u obj_mudLog.xsd                     -m witsml1311_obj_mudLog
pyxbgen $PYXBGEN_OPTS -u obj_objectGroup.xsd                -m witsml1311_obj_objectGroup
pyxbgen $PYXBGEN_OPTS -u obj_opsReport.xsd                  -m witsml1311_obj_opsReport
pyxbgen $PYXBGEN_OPTS -u obj_rig.xsd                        -m witsml1311_obj_rig
pyxbgen $PYXBGEN_OPTS -u obj_risk.xsd                       -m witsml1311_obj_risk
pyxbgen $PYXBGEN_OPTS -u obj_sidewallCore.xsd               -m witsml1311_obj_sidewallCore
pyxbgen $PYXBGEN_OPTS -u obj_stimJob.xsd                    -m witsml1311_obj_stimJob
pyxbgen $PYXBGEN_OPTS -u obj_surveyProgram.xsd              -m witsml1311_obj_surveyProgram
pyxbgen $PYXBGEN_OPTS -u obj_target.xsd                     -m witsml1311_obj_target
pyxbgen $PYXBGEN_OPTS -u obj_toolErrorModel.xsd             -m witsml1311_obj_toolErrorModel
pyxbgen $PYXBGEN_OPTS -u obj_toolErrorTermSet.xsd           -m witsml1311_obj_toolErrorTermSet
pyxbgen $PYXBGEN_OPTS -u obj_trajectory.xsd                 -m witsml1311_obj_trajectory
pyxbgen $PYXBGEN_OPTS -u obj_tubular.xsd                    -m witsml1311_obj_tubular
pyxbgen $PYXBGEN_OPTS -u obj_wbGeometry.xsd                 -m witsml1311_obj_wbGeometry
pyxbgen $PYXBGEN_OPTS -u obj_well.xsd                       -m witsml1311_obj_well
pyxbgen $PYXBGEN_OPTS -u obj_wellbore.xsd                   -m witsml1311_obj_wellbore

echo "done"
