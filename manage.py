# -*- coding: utf-8 -*-
import argparse
from utils import db_execute
from conf import DB_NAME


def setup_db(db_name):
    db_execute(
        db_name,
        '''CREATE TABLE IF NOT EXISTS quota_check (
            id INTEGER PRIMARY KEY,
            account VARCHAR,
            quota INTEGER,
            created_at integer(4) not null default (strftime('%s','now'))
        )'''
    )


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', type=str, choices=['setup', 'drop'],
                        help='what to do with `quota_check` database')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    if args.command == 'setup':
        setup_db(DB_NAME)
