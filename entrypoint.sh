#!/bin/sh
export FLASK_APP=./api/api.py
pipenv run flask --debug run -h 0.0.0.0