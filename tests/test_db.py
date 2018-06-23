# -*- coding: utf-8 -*-
import sqlite3
import os
import pytest
from manage import setup_db


class TestDB():
    db_name = 'db/test.db'

    def test_init_db(self):
        try:
            os.remove(self.db_name)
        except OSError:
            pytest.fail('Unexpected error trying to delete {}'.format(self.db_name), pytrace=True)
        conn = sqlite3.connect(self.db_name)
        conn.close()
        assert os.path.isfile(self.db_name)

    def test_setup_db(self):
        try:
            setup_db(db_name=self.db_name)
        except sqlite3.Error:
            pytest.fail('Unexpected error trying to setup DB', pytrace=True)
