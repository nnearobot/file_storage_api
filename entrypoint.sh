#!/bin/sh
export FLASK_APP=./filestorage.py
pipenv run flask --debug run -h 0.0.0.0 -p 5000
