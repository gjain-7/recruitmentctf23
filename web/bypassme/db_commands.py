import random
import string
from models import User
from db import connection_context

CREATE_TABLE_USER = """
CREATE TABLE IF NOT EXISTS users (
    id integer PRIMARY KEY,
    username varchar(100) UNIQUE NOT NULL,
    password varchar(100) NOT NULL
);
"""

USER_DATA = [
    User(1, username="guest", password="guest123"),
    User(2, username="admin", password=''.join(random.choices(string.ascii_uppercase + string.digits, k=12))),
]

def start_database():
    with connection_context() as cur:
        cur.execute(CREATE_TABLE_USER)

        for user in USER_DATA:
            insert_cmd = f"""
                INSERT INTO users (id, username, password)
                VALUES (
                    {user.id},
                    '{user.username}',
                    '{user.password}'
                )
                ON CONFLICT DO NOTHING
            """
            cur.execute(insert_cmd)