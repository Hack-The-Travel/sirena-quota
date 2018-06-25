# -*- coding: utf-8 -*-
db_name = 'db/quota.db'
accounts = {
    'OTA.TCH': {
        'user': 'ota_grs101',
        'password': 'secret',
    },
    'OTA.UT': {
        'user': 'ota_grs102',
        'password': 'newsecret',
    },
}
sender = ('Anton Yakovlev', 'anton.yakovlev@a.gentlemantravel.club')
smtp_gateway= 'email-smtp.eu-west-1.amazonaws.com'
smtp_port = 587
smtp_user = 'aws_ses_user'
smtp_password = 'aws_ses_user_password'
