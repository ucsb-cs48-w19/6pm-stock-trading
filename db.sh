#!/bin/bash 


rm -r migrations
python manage.py db init
python manage.py db migrate
python manage.py db upgrade