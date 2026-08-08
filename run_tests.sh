#!/bin/bash

set +e

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

echo "Cleaning previous test reports..."

rm -rf test-reports/allure-results
rm -rf test-reports/allure-report

mkdir -p test-reports/allure-results

MARKER="$1"
WORKERS="${WORKERS:-2}"
RERUNS="${RERUNS:-0}"
RERUN_DELAY="${RERUN_DELAY:-1}"

echo "Running tests..."
echo "Workers: $WORKERS"
echo "Retries: $RERUNS"
echo "Retry delay: ${RERUN_DELAY}s"

if [ -z "$MARKER" ]; then
    echo "Running all tests with $WORKERS workers... ${RERUNS} retries."
    pytest -n "$WORKERS" \
        --reruns "$RERUNS" \
        --reruns-delay "$RERUN_DELAY" \
        --alluredir=test-reports/allure-results 
else
    echo "Running suite: $MARKER with $WORKERS workers... ${RERUNS} retries."
    pytest -n "$WORKERS" -m "$MARKER" \
        --reruns "$RERUNS" \
        --reruns-delay "$RERUN_DELAY" \
        --alluredir=test-reports/allure-results
fi

TEST_EXIT_CODE=$?

echo "Generating Allure report..."

allure generate test-reports/allure-results \
    -o test-reports/allure-report \
    --clean

exit $TEST_EXIT_CODE