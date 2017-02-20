#Disclaimer
Only works on linux

# Requeriments

Install gcc ->[sudo] apt-get install gcc
Remove virtualenv with: rm -R flask
Add virtualenv with: python -m venv flask
Add all dependencies: flask/bin/pip install -r requeriments.txt

# Run soundshake

gunicorn app:app
