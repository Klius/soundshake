#!/bin/bash
echo 'activate virtual environment'
. flask/bin/activate
echo 'Run Forrest, RUN!'
gunicorn app:app