#!/usr/bin/env bash

set -e

if [ -z $1 ] ; then
	echo "No version specified"
	exit 1
fi

printf "\n====== Applying release updates ======\n"

perl -pi -e 's/DEBUG/INFO/g' api/configuration.py

printf "Done.\n"

printf "\n====== Pushing release updates ======\n"

git add -u
git commit -m "Prepare release $1"
git tag -a v$1 -m "v$1"
git revert -n HEAD
git commit -m "Prepare for next development iteration"
git push --tags origin master

printf "\n====== Deploying version ======\n"

git checkout HEAD~1
bash bin/deploy.sh $(git describe --tags $(git rev-list --tags --max-count=1))
git checkout -
