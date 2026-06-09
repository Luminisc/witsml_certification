#!/bin/bash
# Initialize WSL Python virtual environment and install dependencies
# Run this from the repository root in WSL:
#   ./init_wsl.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$SCRIPT_DIR/.venv_wsl"
REQUIREMENTS="$SCRIPT_DIR/requirements.txt"

echo "=== Initializing WSL Python environment ==="
echo "Project root: $SCRIPT_DIR"
echo "Virtual env:  $VENV_DIR"
echo ""

# Check if python3 is available
if ! command -v python3 &> /dev/null; then
    echo "ERROR: python3 not found. Install Python 3 in WSL first."
    echo "  sudo apt update && sudo apt install -y python3 python3-venv"
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
    echo "Done."
else
    echo "Virtual environment already exists at $VENV_DIR"
fi
echo ""

# Install requirements
if [ -f "$REQUIREMENTS" ]; then
    echo "Installing packages from requirements.txt..."
    pip install -r "$REQUIREMENTS"
    echo ""
else
    echo "WARNING: requirements.txt not found at $REQUIREMENTS"
fi

echo "=== Done ==="
echo "Activate the environment with:  source .venv_wsl/bin/activate"