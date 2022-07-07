#!/bin/bash

set -x

export FLASK_APP=app
export FLASK_ENV=development
export APPLICATION_SETTINGS=settings.cfg

tailwindcss -i ./static/src/main.css -o ./static/dist/main.css --minify

flask run