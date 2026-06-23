#!/bin/bash
set -e

if [ -n "${BUILT_PRODUCTS_DIR}" ]; then
    RESOURCES_DIR="${BUILT_PRODUCTS_DIR}/${CONTENTS_FOLDER_PATH}/Resources"
else
    # Local fallback for testing
    RESOURCES_DIR="${PWD}/build/Resources"
fi

RUNTIME_DIR="${RESOURCES_DIR}/python_runtime"
REQUIREMENTS_FILE="${PWD}/backend/requirements.txt"

if [ -d "${RUNTIME_DIR}" ]; then
    echo "Python runtime already exists at ${RUNTIME_DIR}. Skipping build."
    exit 0
fi

echo "Building standalone Python runtime at ${RUNTIME_DIR}"
mkdir -p "${RUNTIME_DIR}"
cd "${RUNTIME_DIR}"

PYTHON_VERSION="3.11.9"
RELEASE_TAG="20240415"
TARBALL="cpython-${PYTHON_VERSION}+${RELEASE_TAG}-aarch64-apple-darwin-install_only.tar.gz"
DOWNLOAD_URL="https://github.com/indygreg/python-build-standalone/releases/download/${RELEASE_TAG}/${TARBALL}"

echo "Downloading ${DOWNLOAD_URL}"
curl -L -o python.tar.gz "${DOWNLOAD_URL}"

echo "Extracting Python..."
tar -xf python.tar.gz
rm python.tar.gz

mv python/* .
rm -rf python

echo "Installing requirements..."
./bin/python3 -m pip install -r "${REQUIREMENTS_FILE}"

echo "Stripping unnecessary files..."
rm -rf lib/python3.11/test
rm -rf lib/python3.11/tkinter
rm -rf lib/python3.11/idlelib
rm -rf lib/python3.11/pydoc_data
find . -type d -name "__pycache__" -exec rm -rf {} +
find . -type f -name "*.pyc" -delete

echo "Standalone Python runtime build complete."
