# -*- coding: utf-8 -*-
from utils import db_execute
from conf import DB_NAME


def setup_db(db_name):
    db_execute(
        db_name,
        '''CREATE TABLE IF NOT EXISTS quota_check (
            id INTEGER PRIMARY KEY,
            quota INTEGER,
            created_at integer(4) not null default (strftime('%s','now'))
        )'''
    )


if __name__ == '__main__':
    setup_db(DB_NAME)
    print('`quota_check` db was created')
