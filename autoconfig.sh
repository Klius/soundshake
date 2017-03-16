#!/bin/bash
echo 'installing dependencies'
sudo apt-get install gcc python-dev libmysqlclient-dev python3 python3-pip
echo 'installing virtual environment'
sudo pip3 install virtualenv
echo 'removing old virtual environment'
rm -R flask
echo 'creating new virtualenvironment'
virtualenv flask
echo 'installing app libraries'
flask/bin/pip3 install -r requirements.txt
echo 'all done'
