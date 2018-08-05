# -*- coding: utf-8 -*-
import requests


class Checker(object):
    def __init__(self):
        #: String contains text of HTTP body request
        self.last_sent = None

        #: Content of the response, in bytes
        self.last_received = None

    def request(self, url: str, method: str = 'post', auth=None, headers=None, data=None):
        r = requests.request(method, url, auth=auth, headers=headers, data=data)
        self.last_sent = data
        self.last_received = r.content
        r.raise_for_status()
