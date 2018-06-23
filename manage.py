# -*- coding: utf-8 -*-
import sqlite3
from conf import DB_NAME


def setup_db(db_name=DB_NAME):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS quota_check (
        id INTEGER PRIMARY KEY,
        quota INTEGER,
        created_at integer(4) not null default (strftime('%s','now'))
    )''')
    conn.commit()
    conn.close()


if __name__ == '__main__':
    setup_db()
