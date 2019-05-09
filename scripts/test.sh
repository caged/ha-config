#!/bin/bash

cd /usr/src/app
echo "some_password: welcome" > secrets.yaml
/usr/local/bin/python -m homeassistant --config / --script check_config --info all
