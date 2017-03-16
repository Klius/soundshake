#Disclaimer
Only works on linux

# Requeriments

GCC -> sudo apt-get install gcc
librarias de mysql -> sudo apt-get install python-dev libmysqlclient-dev
Python3 -> sudo apt-get install python3
pip -> sudo apt-get install python3-pip
Virtualenv -> sudo pip3 install virtualenv

Remove virtualenv with: rm -R flask
Add virtualenv with: virtualenv flask
Add all dependencies: flask/bin/pip install -r requeriments.txt

# Run soundshake
1- activate virtual environment: source flask/bin/activate
2- Run: gunicorn app:app
