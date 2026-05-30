#!/bin/bash

set -e

echo "🧪 Running tests..."
pytest --alluredir=test-reports/allure-results

echo "📊 Generating Allure report..."
allure generate test-reports/allure-results -o test-reports/allure-report --clean

#echo "🌐 Opening report..."
#open test-reports/allure-report/index.html