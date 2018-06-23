# -*- coding: utf-8 -*-
import requests
import conf

rq = '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ser="http://service.swc.comtech/">
   <soapenv:Header/>
   <soapenv:Body>
      <ser:getTicketQuota>
         <dynamicId>0</dynamicId>
      </ser:getTicketQuota>
   </soapenv:Body>
</soapenv:Envelope>'''


def get_quota():
    r = requests.post(conf.gateway, auth=(conf.user, conf.password), data=rq)
    print(r.content)
    r.raise_for_status()


if __name__ == '__main__':
    print('Debug. Trying to send request to Sirena.')
    get_quota()
