# -*- coding: utf-8 -*-
from .checker import Checker


class SirenaChecker(Checker):
    def __init__(self, user: str, password: str, endpoint: str):
        Checker.__init__(self, template_dir='templates')
        self.user = user
        self.password = password
        self.endpoint = endpoint

    def get_quota(self):
        rq = self.render_template('sirena_get_ticket_quota.xml', context=None)
        self.request(self.endpoint, auth=(self.user, self.password), data=rq)
        return self.last_sent, self.last_received
