@echo off
python3 ./manage.py runserver  192.168.0.69:8000 --insecure
timeout 2 > NUL