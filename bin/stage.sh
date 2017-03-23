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

echo "==== Configuration app for production ===="

perl -pi -e "s/'dev'/'staging'/g" api.yaml

echo "==== Deploying app to App Engine ===="

gcloud app deploy \
    api.yaml \
    --account=TODO \
    --project=TODO \
    --version=$1 \
    --quiet

perl -pi -e "s/'staging'/'dev'/g" api.yaml
bash bin/dev.sh
