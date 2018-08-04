# -*- coding: utf-8 -*-
import pytest
from amadeus import get_password_digest, encode_base64


class TestAmadeus:
    # Control values are from AWS Implementation Guide
    nonce = 'secretnonce10111'
    nonce_encoded = 'c2VjcmV0bm9uY2UxMDExMQ=='
    password = 'AMADEUS'
    timestamp = '2015-09-30T14:12:15Z'
    password_digest = '+LzcaRc+ndGAcZIXmq/N7xGes+k='

    def test_encode_base64(self):
        assert encode_base64(self.nonce) == self.nonce_encoded

    def test_get_password_digest(self):
        assert get_password_digest(self.nonce, self.timestamp, self.password) == self.password_digest
