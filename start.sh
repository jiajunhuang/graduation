#!/bin/bash

apidoc -i controllers/ -o static/api/

python run.py --debug=True
