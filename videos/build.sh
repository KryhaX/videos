#!/usr/bin/env bash
# exit on error
set -o errexit

pip3 install requirements.txt

python3 manage.py collectstatic --no-input
python3 manage.py migrate