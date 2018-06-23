# -*- coding: utf-8 -*-
import re
import requests
import conf


def extract_ticket_quota(ticket_quota_response):
    matches = re.findall(r'<quota>(\d+)<\/quota>', ticket_quota_response)
    return int(matches[0])


def get_ticket_quota(user, password):
    """Returns ticket quota for PoS (ППр).

    This method calls `getTicketQuota` method of Sirena WS.

    :param user: Sirena WS user with supervisor permission in the PoS.
    :param password: user password.
    :return: ticket quota.
    :rtype: int
    """
    rq = '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ser="http://service.swc.comtech/">
       <soapenv:Header/>
       <soapenv:Body>
          <ser:getTicketQuota>
             <dynamicId>0</dynamicId>
          </ser:getTicketQuota>
       </soapenv:Body>
    </soapenv:Envelope>'''
    r = requests.post(conf.gateway, auth=(user, password), data=rq)
    r.raise_for_status()
    return extract_ticket_quota(r.text)


if __name__ == '__main__':
    print('Debug. Trying to send request to Sirena.')
    account = conf.accounts[1]
    print(get_ticket_quota(account['user'], account['password']))
