#!/bin/bash
# Creates a folder that bundles all required libraries
# needed for GAE-SE deploys:
# https://cloud.google.com/appengine/docs/standard/python/tools/using-libraries-python-27#vendoring
# to run: $ source gae_install_libs.sh

# remove any files in the lib bundle folder
BUNDLE_FOLDER=lib
echo "FOLDER: $BUNDLE_FOLDER"
if [ -d $BUNDLE_FOLDER ]; then
    echo "removing current files/folders in $BUNDLE_FOLDER ..."
    rm -rf $BUNDLE_FOLDER/*
else
    echo "folder named $BUNDLE_FOLDER does not exist, creating it"
    mkdir $BUNDLE_FOLDER
fi

# install regular dependencies in requirements.txt
echo "installing requirements.txt dependencies to folder $BUNDLE_FOLDER... "
pip install -t $BUNDLE_FOLDER -r requirements.txt