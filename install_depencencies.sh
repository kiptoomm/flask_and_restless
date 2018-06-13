#!/bin/bash
# Installs dependencies needed for local development and GAE-flex deploys:
# https://cloud.google.com/python/getting-started/using-cloud-sql
# to run: $ source install_dependencie.sh

# install regular dependencies in requirements.txt
echo "installing requirements.txt dependencies to this venv"
pip install -r requirements.txt