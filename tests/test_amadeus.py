# -*- coding: utf-8 -*-
import pytest
import base64
from checkers import get_password_digest, get_nonce


class TestAmadeus:
    @pytest.mark.parametrize(
        'nonce, timestamp, password, password_digest_64', (
            ('secretnonce10111', '2015-09-30T14:12:15Z', 'AMADEUS', '+LzcaRc+ndGAcZIXmq/N7xGes+k='),
        ))
    def test_get_password_digest(self, nonce, timestamp, password, password_digest_64):
        nonce = nonce.encode('ascii')
        timestamp = timestamp.encode('ascii')
        password = password.encode('ascii')
        password_digest = get_password_digest(nonce, timestamp, password)
        password_digest_64 = base64.b64encode(password_digest).decode('utf-8')
        assert password_digest_64 == password_digest_64

    def test_get_nonce_lenght(self):
        assert len(get_nonce(100)) == 100
