#!/bin/bash

cd /usr/src/app
cp $GITHUB_WORKSPACE/secrets.test.yaml $GITHUB_WORKSPACE/secrets.yaml
/usr/local/bin/python -m homeassistant --config $GITHUB_WORKSPACE --script check_config --info all
