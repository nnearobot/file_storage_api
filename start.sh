#!/bin/sh
service nginx start
uwsgi --ini uwsgi.ini