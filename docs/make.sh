#!/bin/bash
# description: Command file for Sphinx documentation
# file-name: make.{ext}
# file-id: 5cd428a9-d748-46e7-9391-9c2290b4b870
# file-version: 2025.0.1

SPHINXBUILD=${SPHINXBUILD:-sphinx-build}
SOURCEDIR=.
BUILDDIR=_build

# Check if sphinx-build is available
if ! command -v "$SPHINXBUILD" &> /dev/null; then
    echo
    echo "The 'sphinx-build' command was not found. Make sure you have Sphinx"
    echo "installed, then set the SPHINXBUILD environment variable to point"
    echo "to the full path of the 'sphinx-build' executable. Alternatively, you"
    echo "may add the Sphinx directory to PATH."
    echo
    echo "If you don't have Sphinx installed, grab it from"
    echo "https://www.sphinx-doc.org/"
    exit 1
fi

# Display help if no arguments are provided
if [ -z "$1" ]; then
    "$SPHINXBUILD" -M help "$SOURCEDIR" "$BUILDDIR" $SPHINXOPTS $O
    exit 0
fi

# Run the specified Sphinx build command
"$SPHINXBUILD" -M "$1" "$SOURCEDIR" "$BUILDDIR" $SPHINXOPTS $O
