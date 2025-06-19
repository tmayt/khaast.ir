#!/bin/sh

python manage.py makemigrations
python manage.py migrate --noinput
python manage.py collectstatic --noinput

gunicorn --reload --bind 0.0.0.0:8000 khaast.wsgi:application
