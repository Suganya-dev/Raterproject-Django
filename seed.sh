#!/bin/bash
rm -rf raterprojectapi/migrations
rm db.sqlite3
python manage.py migrate
python manage.py makemigrations raterprojectapi
python manage.py migrate raterprojectapi
python manage.py loaddata users
python manage.py loaddata category
python manage.py loaddata games
python manage.py loaddata ratings