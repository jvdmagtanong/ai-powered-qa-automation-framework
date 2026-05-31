#!/bin/bash

set -e

echo "Detecting environment..."

if [[ "$(uname -m)" == "arm64" ]]; then
    export PATH="/opt/homebrew/bin:$PATH"
elif [[ "$(uname -m)" == "x86_64" ]]; then
    export PATH="/usr/local/bin:$PATH"
fi

# Safety check
if ! command -v allure &> /dev/null
then
    echo "Allure CLI not found. Please install Allure."
    exit 1
fi

echo "Running tests..."
pytest --alluredir=test-reports/allure-results || true

echo "Generating Allure report..."
allure generate test-reports/allure-results \
  -o test-reports/allure-report \
  --clean

# echo "Report ready:"
# echo "test-reports/allure-report/index.html"