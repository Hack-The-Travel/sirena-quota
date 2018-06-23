# -*- coding: utf-8 -*-
from utils import db_execute
import conf


if __name__ == '__main__':
    rows = db_execute(
        conf.db_name,
        'SELECT account, quota, created_at FROM quota_check GROUP BY account HAVING MAX(created_at)'
    )
    print(rows)
