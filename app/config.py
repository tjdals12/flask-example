import os

DEBUG = os.environ.get("DEBUG", True)
HOST = os.environ.get("HOST", "127.0.0.1")
PORT = os.environ.get("PORT", 4000)
DB_TYPE = os.environ.get("PROTOCOL", "oracle")
SECRET_KEY = "flasknotewithsqlalchemy"

# MySql
mysql_config = {
    "protocol": "mysql",
    "user": os.environ.get("DB_USER", "root"),
    "pass": os.environ.get("DB_PASS", "1234"),
    "host": os.environ.get("DB_HOST", "localhost"),
    "db": os.environ.get("DB_NAME", "mysql"),
}

mysql_uri = "%s://%s:%s@%s/%s?charset=utf8" % (
    mysql_config["protocol"],
    mysql_config["user"],
    mysql_config["pass"],
    mysql_config["host"],
    mysql_config["db"],
)

# Oracle
oracle_config = {
    "protocol": "oracle",
    "user": os.environ.get("DB_USER", "root"),
    "pass": os.environ.get("DB_PASS", "1234"),
    "host": os.environ.get("DB_HOST", "localhost"),
    "db": os.environ.get("DB_NAME", "ORCL"),
}

oracle_uri = "%s://%s:%s@%s/%s" % (
    oracle_config["protocol"],
    oracle_config["user"],
    oracle_config["pass"],
    oracle_config["host"],
    oracle_config["db"],
)

SQLALCHEMY_DATABASE_URI = DB_TYPE == "oracle" and oracle_uri or mysql_uri
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
