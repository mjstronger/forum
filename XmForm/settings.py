import os

import peewee_async

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

settings = {
    "static_path":"E:\pythonxingmu\XmForm\static",
    "static_url_prefix": "/static/",
    "template_path": "templates",
    "secret_key": "EMpHv8EKuVt2!@&H",
    "jwt_expire": 7 * 24 * 3600,
    "MEDIA_ROOT": os.path.join(BASE_DIR, "media"),
    "SITE_URL": "http://127.0.0.1:8000",
    "db": {
        "host": "127.0.0.1",
        "user": "root",
        "password": "root",
        "name": "message",
        "port": 3306
    },
    "redis":{
    "host":"127.0.0.1",
}
}
database = peewee_async.MySQLDatabase(
    "xmform", host="127.0.0.1", port=3306, user="root", password="root"
)