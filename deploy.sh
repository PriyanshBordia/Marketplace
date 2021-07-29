#!/bin/bash
git checkout .
git pull
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py collectstatic
python3 manage.py test circle
python3 manage.py makemigrations
python3 manage.py migrate
git add .
git commit -am "deploy"
git push
sleep 3
git push heroku main