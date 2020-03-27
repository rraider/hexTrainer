#!/bin/sh

echo "Running migrations"
python3 manage.py migrate
echo "Starting app"
gunicorn mathtrainer.wsgi:application --bind 0.0.0.0:8000 --workers 3
