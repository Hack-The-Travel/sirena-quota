# -*- coding: utf-8 -*-
import requests
import conf


def get_ticket_quota(user, password):
    """Returns ticket quota for PoS (ППр).

    This method calls `getTicketQuota` method of Sirena WS.

    :param user: Sirena WS user with supervisor permission in the PoS.
    :param password: user password.
    :return: ticket quota.
    :rtype: int
    """
    ticket_quota = 0
    rq = '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ser="http://service.swc.comtech/">
       <soapenv:Header/>
       <soapenv:Body>
          <ser:getTicketQuota>
             <dynamicId>0</dynamicId>
          </ser:getTicketQuota>
       </soapenv:Body>
    </soapenv:Envelope>'''
    r = requests.post(conf.gateway, auth=(user, password), data=rq)
    print(r.content)
    r.raise_for_status()
    return ticket_quota


if __name__ == '__main__':
    print('Debug. Trying to send request to Sirena.')
    account = conf.accounts[1]
    print(get_ticket_quota(account['user'], account['password']))
