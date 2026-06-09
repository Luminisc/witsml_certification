# WITSML v1.4.1.1 Certification

Fork of
[WITSML Certification Tool](https://bitbucket.org/energistics/witsml_v1.4.1.1_certification).

Experimental try to convert repository from Python2 to Python3

## Setup

### Prerequisites

- Python 3.10+
- Windows (with WSL for PyXB binding regeneration) or Linux

### Initial Setup

```bash
# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate      # Windows
# source .venv/bin/activate  # Linux

# Install dependencies
pip install -r requirements.txt

# Install the tool packages
pip install -e tool/
```

### Server Configuration

1. Copy `scripts/datamodel/default_server.py` to `my_server.py` in the project root
2. Edit `my_server.py` with your WITSML server details:

```python
server_URL = 'http://your-server:port/wmls'
server_username = 'your-username'
server_password = 'your-password'
server_schema_version = '1.4.1.1'  # or '1.4.1.0' / '1.3.1.1'
```

3. Create `wtl_cfg.py` in the project root:

```python
server_file_name = 'my_server'
```

### PyXB Bindings (WSL only)

If you need to regenerate the auto-generated PyXB binding files from XSD schemas:

```bash
# From WSL terminal
cd /mnt/c/_Work/_Tools/witsml_v1.4.1.1_certification

# Initialize WSL venv (first time only)
./init_wsl.sh

# Activate WSL venv
source .venv_wsl/bin/activate

# Regenerate bindings for each schema version
./tool/src/wcmp/witsml1311/gen1311.sh
./tool/src/wcmp/witsml1410/gen1410.sh
./tool/src/wcmp/witsml1411/gen1411.sh
```

## Running Tests

### Single Test

```bash
.venv\Scripts\activate
python scripts/accepted/test1a.py
```

### Full Test Suite

```bash
.venv\Scripts\activate
python scripts/accepted/testsuite.py
```

### Command-Line Options

| Flag | Effect |
|------|--------|
| `-s<filename>` | Use `<filename>.py` as server config (overrides `wtl_cfg.py`) |
| `-v` | Enable XML schema validation |
| `-V` | Disable schema validation (default) |
| `-l` | Log SOAP responses (default: on) |
| `-L` | Disable response logging |
| `-r` | Log SOAP requests |
| `-R` | Disable request logging (default) |

### Results

Test results are written to `results/witsml_result.txt` by default.