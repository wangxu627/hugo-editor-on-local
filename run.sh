#!/bin/bash

source venv/bin/activate

export FLASK_APP=app.py
nohup flask run -p 3201 &
