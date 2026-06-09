### Tools
- 2to3
    `.venv\Scripts\2to3.exe -w ./`
- pybxgen
    (not working) From '.\tool\src\wcmp\witsml1311': `python ..\..\..\..\.venv\Scripts\pyxbgen -u obj_well.xsd -m witsml1311_obj_well`
    pybxgen does not work on Windows, so run `tool/src/wcmp/witsml1311/gen1311.sh` (and rest) from within WSL
    - `tool/src/wcmp/witsml1311/gen1311.sh`
    - `tool/src/wcmp/witsml1410/gen1410.sh`
    - 