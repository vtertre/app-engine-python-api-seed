#!/usr/bin/env bash

set -e

echo "==== Initializing environment ===="

rm -rf venv libs
virtualenv venv
source venv/bin/activate
bash bin/dev.sh
