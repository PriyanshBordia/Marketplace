#!/bin/sh
git pull
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
# python3 manage.py collectstatic
# echo "yes"
python3 manage.py test circle
# if [python3 manage.py test circle] then
# python3 manage.py makemigrations
python3 manage.py migrate
git add .
git commit -am "deploy"
git push
# sleep 3
git push heroku main
# fi 