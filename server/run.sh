#!/bin/bash

set -x

# Run tailwindcss with watch mode and go to background
tailwindcss -w -i ./app/static/src/main.css -o ./app/static/dist/main.css --minify &

flask run

trap 'pkill -ef tailwind' exit
