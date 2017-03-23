#!/usr/bin/env bash

set -e

echo "==== Configuring dependencies for development ===="

source venv/bin/activate
virtualenv --clear venv
pip install -r dev_requirements.txt
rm -rf libs
linkenv venv/lib/python2.7/site-packages libs
