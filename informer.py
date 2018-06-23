# -*- coding: utf-8 -*-
import time
from utils import db_execute
import conf


if __name__ == '__main__':
    rows = db_execute(
        conf.db_name,
        'SELECT account, quota, created_at FROM quota_check GROUP BY account HAVING MAX(created_at)'
    )
    info_items = list()
    for row in rows:
        if row[0] not in conf.accounts:
            continue  # unknown account code
        info_items.append({
            'code': row[0],
            'quota': row[1],
            'datetime': time.strftime('%Y-%m-%d %H:%M:%S (%Z)', time.localtime(row[2])),
            'alert': row[1] <= conf.accounts[row[0]].get('alert', 0),
        })
    print(info_items)
