# -*- coding: utf-8 -*-
import pytest
import base64
from amadeus import get_password_digest


class TestAmadeus:
    # Check values from AWS Implementation Guide
    nonce = 'secretnonce10111'
    timestamp = '2015-09-30T14:12:15Z'
    password = 'AMADEUS'
    password_digest_64 = '+LzcaRc+ndGAcZIXmq/N7xGes+k='

    def test_get_password_digest(self):
        nonce = self.nonce.encode('ascii')
        timestamp = self.timestamp.encode('ascii')
        password = self.password.encode('ascii')
        password_digest = get_password_digest(nonce, timestamp, password)
        password_digest_64 = base64.b64encode(password_digest).decode('utf-8')
        assert password_digest_64 == self.password_digest_64
