#!/bin/bash

python manage.py makemigrations
python manage.py migrate --noinput
python manage.py collectstatic --noinput

# Start uWSGI
uwsgi --ini ./uwsgi.ini