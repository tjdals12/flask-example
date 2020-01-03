import os

DEBUG = os.environ.get("DEBUG", True)
HOST = os.environ.get("HOST", "127.0.0.1")
PORT = os.environ.get("PORT", 4000)
SECRET_KEY = "flasknotewithsqlalchemy"

mysql_config = {
    "user": os.environ.get("DB_USER", "root"),
    "pass": os.environ.get("DB_PASS", "1234"),
    "host": os.environ.get("DB_HOST", "localhost"),
    "db": os.environ.get("DB_NAME", "mysql"),
}

SQLALCHEMY_DATABASE_URI = "mysql://%s:%s@%s/%s?charset=utf8" % (
    mysql_config["user"],
    mysql_config["pass"],
    mysql_config["host"],
    mysql_config["db"],
)
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
