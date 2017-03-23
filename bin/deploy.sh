#!/usr/bin/env bash

set -e

if [ -z $1 ] ; then
	echo "No version specified"
	exit 1
fi

echo "==== Configuring dependencies for production ===="

source venv/bin/activate
virtualenv --clear venv
pip install -r requirements.txt
rm -rf libs
linkenv venv/lib/python2.7/site-packages libs

echo "==== Deploying app to App Engine ===="

appcfg.py update api.yaml --no_cookies --env_variable=env:prod

gcloud app deploy \
    api.yaml \
    --account=TODO \
    --project=TODO \
    --version=$1 \
    --no-promote \
    --quiet

bash bin/dev.sh
