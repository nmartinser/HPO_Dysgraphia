#!/bin/bash

# Verifica si pip está instalado
if command -v pip >/dev/null 2>&1; then
    echo "pip found. Continuing..."
else
    echo "pip not found. Please install pip before running this script."
    exit 1
fi

# Instala las dependencias desde requirements.txt
pip install -r requirements.txt

# Verifica si la instalación fue exitosa
if [ $? -eq 0 ]; then
    echo "Dependencies installed successfully."
else
    echo "Failed to install dependencies. See error messages above for details."
    exit 1
fi

echo "Setup complete."