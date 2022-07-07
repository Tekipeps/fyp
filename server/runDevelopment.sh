#!/bin/bash

set -x

export FLASK_APP=app
export FLASK_ENV=development
export APPLICATION_SETTINGS=settings.cfg

# Run tailwindcss with watch mode and go to background
tailwindcss -w -i ./static/src/main.css -o ./static/dist/main.css --minify &

flask run

trap 'pkill -ef tailwind' exit
