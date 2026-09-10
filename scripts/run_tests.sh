#!/bin/bash

echo "Starting Python tests..."

python -m pytest

if [ $? -eq 0 ]; then
    echo "Tests PASSED"
else
    echo "Tests FAILED"
    exit 1
fi