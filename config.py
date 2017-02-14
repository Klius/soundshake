import os
basedir = os.path.abspath(os.path.dirname(__file__))
WTF_CSRF_ENABLED = True
SECRET_KEY = 'password'
HOST="0.0.0.0"
PORT=33507
SQLALCHEMY_DATABASE_URI = 'mysql://ikwvc64s2hjr10hv:x0ocwlmw0o6v4zbb@onnjomlc4vqc55fw.chr7pe7iynqr.eu-west-1.rds.amazonaws.com:3306/yornoznhmhb5pcen'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')