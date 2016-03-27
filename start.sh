#!/bin/bash

apidoc -i controllers/ -o static/api/

python3 run.py --debug=True
