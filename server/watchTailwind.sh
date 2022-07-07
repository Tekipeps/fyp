#!/bin/bash
nodemon -e html -x 'tailwindcss -i ./static/src/main.css -o ./static/dist/main.css --minify'
