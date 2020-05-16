#! /bin/bash
python3 server/manage.py makemigrations computation_core
python3 server/manage.py migrate computation_core
python3 server/manage.py runserver
