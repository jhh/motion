#!/bin/bash
SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
export FLASK_APP=$SCRIPTPATH/flask_server.py
export FLASK_ENV=production

flask run --host=0.0.0.0

