# -*- coding: utf-8 -*-
import requests


class Checker(object):
    def __init__(self):
        self.last_sent = None
        self.last_received = None

    def request(self, url: str, auth=None, headers=None, data=None):
        r = requests.post(url, auth=auth, headers=headers, data=data)
        self.last_sent = data
        self.last_received = r.content
        r.raise_for_status()
