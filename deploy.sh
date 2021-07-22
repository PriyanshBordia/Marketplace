#!/bin/bash
git pull
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py test circle
python3 manage.py migrate