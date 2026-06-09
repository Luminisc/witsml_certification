# WITSML Certification Tool — Developer Setup

## Prerequisites

- **Windows 11** with **WSL** (Windows Subsystem for Linux) installed
- **Python 3** in WSL (Ubuntu recommended)
- **VS Code** with the WSL extension

---

## 1. Initial Setup (One-Time)

### 1.1 Install Python 3 in WSL

```bash
sudo apt update && sudo apt install -y python3 python3-venv
```

### 1.2 Clone the Repository

```bash
cd /mnt/c/_Work/_Tools
git clone <repo-url> witsml_v1.4.1.1_certification
cd witsml_v1.4.1.1_certification
```

### 1.3 Create Virtual Environment & Install Dependencies

```bash
./init_wsl.sh
```

This creates `.venv_wsl/` and installs all packages from `requirements.txt`:
- `pyxb-x` — Python 3 fork of PyXB for XSD binding generation
- `suds-community` — SOAP client for WITSML store communication
- `lxml` — XML processing
- `iso8601` — date/time parsing
- `2to3`, `pyupgrade`, `tokenize_rt` — code migration tools

### 1.4 Activate the Environment

```bash
source .venv_wsl/bin/activate
```

---

## 2. Running the Tool

### 2.1 Activate the Environment (Every New Terminal)

```bash
cd /mnt/c/_Work/_Tools/witsml_v1.4.1.1_certification
source .venv_wsl/bin/activate
```

### 2.2 Run Tests

```bash
cd tool
python -m pytest test/
```

Or run individual test files:

```bash
python -m pytest test/test_globals.py -v
```

### 2.3 Run Certification Scripts

```bash
cd scripts/accepted
python test1c.py
```

---

## 3. Regenerating PyXB Bindings

The auto-generated object model files are created from WITSML XSD schemas using `pyxbgen` (from `pyxb-x`).

### 3.1 Regenerate All Objects for a Schema Version

```bash
# WITSML 1.3.1.1
./tool/src/wcmp/witsml1311/gen1311.sh

# WITSML 1.4.1.0
./tool/src/wcmp/witsml1410/gen1410.sh

# WITSML 1.4.1.1
./tool/src/wcmp/witsml1411/gen1411.sh
```

Each script:
1. Resolves the schema directory relative to the script location
2. Runs `pyxbgen` with `--strip-file-paths` (portable paths, no machine-specific locations)
3. Outputs generated `.py` files to the script's directory

### 3.2 Regenerate a Single Object

```bash
cd /mnt/c/_Work/_Tools/witsml_v1.4.1.1_certification
source .venv_wsl/bin/activate

# Example: regenerate only obj_well for 1.3.1.1
SCHEMA_DIR="tool/src/wsvt/schemas/WITSML_v1.3.1.1_Data_Schema"
BINDING_DIR="tool/src/wcmp/witsml1311"
pyxbgen --schema-root="$SCHEMA_DIR" --binding-root="$BINDING_DIR" --strip-file-paths \
  -u obj_well.xsd -m witsml1311_obj_well
```

### 3.3 Schema Directory Structure

| Schema Version | Path |
|----------------|------|
| 1.3.1.1 | `tool/src/wsvt/schemas/WITSML_v1.3.1.1_Data_Schema/` |
| 1.4.1.0 | `tool/src/wsvt/schemas/WITSML_v1.4.1.0_Data_Schema/witsml_v1.4.1_data/xsd_schemas/` |
| 1.4.1.1 | `tool/src/wsvt/schemas/WITSML_v1.4.1.1_Data_Schema/witsml_v1.4.1.1_data/xsd_schemas/` |

---

## 4. Code Migration (Python 2 → Python 3)

### 4.1 Run 2to3 (Windows)

```powershell
.venv\Scripts\2to3.exe -w ./
```

### 4.2 Run pyupgrade (Optional)

```powershell
.venv\Scripts\pyupgrade.exe --py3-plus ./**/*.py
```

---

## 5. Project Architecture

```
witsml_v1.4.1.1_certification/
├── init_wsl.sh                    # WSL environment setup
├── requirements.txt               # Python dependencies
├── MigrationPlan.md               # Migration status & blockers
├── DEV.README.md                  # This file
│
├── tool/
│   ├── setup.py                   # Package installer (WTL + WSVT)
│   ├── src/
│   │   ├── wcmp/                  # Object comparison engine
│   │   │   ├── witsml_obj_compare.py    # Main comparison logic
│   │   │   ├── witsml1311/              # PyXB bindings for 1.3.1.1
│   │   │   │   ├── gen1311.sh           # Regeneration script
│   │   │   │   └── witsml1311_obj_*.py  # Auto-generated objects
│   │   │   ├── witsml1410/              # PyXB bindings for 1.4.1.0
│   │   │   │   ├── gen1410.sh           # Regeneration script
│   │   │   │   └── witsml1410_obj_*.py  # Auto-generated objects
│   │   │   └── witsml1411/              # PyXB bindings for 1.4.1.1
│   │   │       ├── gen1411.sh           # Regeneration script
│   │   │       └── witsml1411_obj_*.py  # Auto-generated objects
│   │   ├── wsvt/                  # Schema Validation Tool
│   │   │   └── schemas/           # WITSML XSD schemas (3 versions)
│   │   ├── wtl/                   # WITSML Test Library
│   │   └── wtools/                # Utility tools
│   └── test/                      # Test suite
│
├── scripts/
│   └── accepted/                  # Certification test scripts
│
└── testplan/                      # Test plans & data model docs
```

---

## 6. Key Dependencies

| Package | Purpose | Python 3 Status |
|---------|---------|-----------------|
| `pyxb-x` | XSD schema → Python bindings | ✅ Python 3 fork of `pyxb` |
| `suds-community` | SOAP client for WITSML stores | ✅ Drop-in replacement for `suds` |
| `lxml` | XML parsing & validation | ✅ Python 3 native |
| `iso8601` | ISO 8601 date/time parsing | ✅ Python 3 native |

---

## 7. Troubleshooting

### `pyxbgen` fails on Windows

`pyxb-x` has a known issue on Windows: absolute paths like `C:\...` are incorrectly treated as URLs (scheme `c:`). **Always use WSL** for regeneration.

### Machine-specific paths in generated files

The `--strip-file-paths` flag ensures `_XSDLocation` entries use only filenames (e.g., `'obj_well.xsd'`) instead of full absolute paths. This is already configured in all `gen*.sh` scripts.

### Virtual environment not found

```bash
./init_wsl.sh    # Creates .venv_wsl/ if missing
source .venv_wsl/bin/activate