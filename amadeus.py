# -*- coding: utf-8 -*-
import requests
import string
import random
import uuid
import base64
from hashlib import sha1
from datetime import datetime

AWS_GATE = 'https://production.webservices.amadeus.com'


def security_authenticate():
    headers = {
        'Content-Type': 'text/xml;charset=UTF-8',
        'SOAPAction': 'http://webservices.amadeus.com/1ASIWASIAER/VLSSLQ_06_1_1A',
    }
    rq = '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:def="http://webservices.amadeus.com/definitions" xmlns:vls="http://xml.amadeus.com/VLSSLQ_06_1_1A">
      <soapenv:Header>
        <Action>http://webservices.amadeus.com/1ASIWASTAER/VLSSLQ_06_1_1A</Action>
        <SessionId />
      </soapenv:Header>
      <soapenv:Body>
        <Security_Authenticate>
         <userIdentifier xmlns="http://xml.amadeus.com/VLSSLQ_06_1_1A">
           <originIdentification>
             <sourceOffice>{office}</sourceOffice>
           </originIdentification>
           <originatorTypeCode>U</originatorTypeCode>
           <originator>{user}</originator>
         </userIdentifier>
         <dutyCode xmlns="http://xml.amadeus.com/VLSSLQ_06_1_1A">
           <dutyCodeDetails>
             <referenceQualifier>DUT</referenceQualifier>
             <referenceIdentifier>SU</referenceIdentifier>
           </dutyCodeDetails>
         </dutyCode>
         <systemDetails xmlns="http://xml.amadeus.com/VLSSLQ_06_1_1A">
           <organizationDetails>
             <organizationId>{organization}</organizationId>
           </organizationDetails>
         </systemDetails>
         <passwordInfo xmlns="http://xml.amadeus.com/VLSSLQ_06_1_1A">
           <dataLength>10</dataLength>
           <dataType>E</dataType>
           <binaryData>{password}</binaryData>
         </passwordInfo>
        </Security_Authenticate>
        </soapenv:Body>
    </soapenv:Envelope>'''.format(user='', password='', office='', organization='')
    r = requests.post(AWS_GATE, headers=headers, data=rq)
    print(r.text)


def get_nonce(n=8):
    """Returns random byte string of length n

    :param n: int, length of the returned string
    :return: random string
    :rtype: bytes
    """
    chars = string.printable
    random_string = ''.join(random.SystemRandom().choice(chars) for _ in range(n))
    return random_string.encode('ascii')


def encode_base64(s):
    s = s if isinstance(s, (bytes, bytearray)) else s.encode('ascii')
    return base64.b64encode(s).decode('utf-8')


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
