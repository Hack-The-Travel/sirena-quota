# -*- coding: utf-8 -*-
import time
from utils import db_execute
import conf


def prepare_body_text(accounts_info, sender):
    status_msg = ''
    alert_accounts = list()
    for account in accounts_info:
        if account['alert']:
            alert_accounts.append(account['code'])
        status_msg += '{account} - {quota}, проверено {dt}\r\n'\
            .format(account=account['code'], quota=account['quota'], dt=account['datetime'])
    alert_msg = ''
    if len(alert_accounts):
        alert_msg = 'Срочно запросите квоту для: ' + ', '.join(alert_accounts) + '!\r\n\r\n'
    body_text = (
        'Приветствую\r\n\r\n'
        '{alert}'
        'Состояние стоков:\r\n{status_msg}'
        '\r\n\r\n'
        '--\r\n'
        'Дружески,\r\n'
        '{sender}'
    )
    return body_text.format(alert=alert_msg, status_msg=status_msg, sender=sender)


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
    print(prepare_body_text(info_items, conf.sender[0]))
