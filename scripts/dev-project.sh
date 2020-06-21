#!/bin/bash

# Exit in case of error
set -e

if [ ! -d ./fastapi-celery ] ; then
    echo "Run this script from outside the project, to generate a sibling dev project"
    exit 1
fi

rm -rf ./dev-fastapi-react

python -m cookiecutter --no-input -f ./fastapi-celery project_slug="dev-fastapi-celery"