# -*- coding: utf-8 -*-
from .checker import Checker


class SirenaChecker(Checker):
    def __init__(self,
                 user: str, password: str, endpoint: str):
        Checker.__init__(self)
        self.user = user
        self.password = password
        self.endpoint = endpoint

    def get_quota(self):
        rq = '''<soapenv:Envelope
           xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
           xmlns:ser="http://service.swc.comtech/">
           <soapenv:Header/>
           <soapenv:Body>
              <ser:getTicketQuota>
                 <dynamicId>0</dynamicId>
              </ser:getTicketQuota>
           </soapenv:Body>
        </soapenv:Envelope>'''
        self.request(self.endpoint, auth=(self.user, self.password), data=rq)
        return self.last_sent, self.last_received
