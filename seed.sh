#!/bin/bash
rm -rf raterprojectapi/migrations
rm db.sqlite3
python manage.py migrate
python manage.py makemigrations raterprojectapi
python manage.py migrate raterprojectapi
python manage.py loaddata categories
python manage.py loaddata users
python manage.py loaddata player
python manage.py loaddata games

# Create a seed.sh file in your project directory
# Place the code below in the file.
# Run chmod +x seed.sh in the terminal.
# Then run ./seed.sh in the terminal to run the commands.

#order matters for load data
#If it has no dependency it can go first
