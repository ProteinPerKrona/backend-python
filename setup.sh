#!/bin/bash

# Setup venv
python3 -m pip install virtualenv
virtualenv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt

# Start server
python3 main.py