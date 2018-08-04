# -*- coding: utf-8 -*-
import requests
import string
import random
import uuid
import base64
from hashlib import sha1
from datetime import datetime


def get_nonce(n: int=8) -> bytes:
    """Returns random byte string of length n

    :param n: int, length of the returned string
    :return: random string
    :rtype: bytes
    """
    chars = string.printable
    random_string = ''.join(random.SystemRandom().choice(chars) for _ in range(n))
    return random_string.encode('ascii')


def get_password_digest(nonce: bytes, timestamp: bytes, password: bytes) -> bytes:
    """Generates password digest

    :param nonce: bytes, random string.
    :param timestamp: bytes, current UTC timestamp in ISO format, e.g. '2018-08-04T17:13:14.105Z'.
    :param password: bytes, raw password obtained from Amadeus.
    :return: password digest.
    :rtype: bytes
    """
    return sha1(nonce + timestamp + sha1(password).digest()).digest()


def command_cryptic():
    headers = {
        'Content-Type': 'text/xml;charset=UTF-8',
        'SOAPAction': 'http://webservices.amadeus.com/1ASIWASIAER/HSFREQ_07_3_1A',
    }
    rq = '''<soapenv:Envelope xmlns:def="http://webservices.amadeus.com/definitions" xmlns:hsf="http://xml.amadeus.com/HSFREQ_07_3_1A" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
       <soapenv:Header>
           <def:SessionId>{session_id}|2</def:SessionId>
       </soapenv:Header>
       <soapenv:Body>
           <Command_Cryptic>
               <messageAction>
                   <messageFunctionDetails>
                       <messageFunction>M</messageFunction>
                   </messageFunctionDetails>
               </messageAction>
               <longTextString>
                   <textStringDetails>toqd/t-S7</textStringDetails>
               </longTextString>
           </Command_Cryptic>
       </soapenv:Body>
    </soapenv:Envelope>'''.format(session_id = '03GDRWTQT5')
    r = requests.post(AWS_GATE, headers=headers, data=rq)
    print(r.text)


if __name__ == '__main__':
    command_cryptic()
