# -*- coding: utf-8 -*-
import random
import uuid
import base64
from hashlib import sha1
from datetime import datetime

from .checker import Checker


def get_nonce(n: int=8) -> bytes:
    """Returns random byte string of length n

    :param n: int, length of the returned string
    :return: random string
    :rtype: bytes
    """
    chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
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


class AmadeusChecker(Checker):
    def __init__(self,
                 user: str, password: str, office_id: str, duty_code: str, endpoint: str):
        Checker.__init__(self)
        self.user = user
        self.password = password
        self.office_id = office_id
        self.duty_code = duty_code
        self.endpoint = endpoint

    def get_quota(self):
        soap_action = 'http://webservices.amadeus.com/HSFREQ_07_3_1A'
        timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.105Z')
        nonce = get_nonce()
        password_digest = get_password_digest(nonce, timestamp.encode('ascii'), self.password.encode('ascii'))
        headers = {
            'Content-Type': 'text/xml;charset=UTF-8',
            'SOAPAction': soap_action,
        }
        rq = '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sec="http://xml.amadeus.com/2010/06/Security_v1" xmlns:typ="http://xml.amadeus.com/2010/06/Types_v1" xmlns:iat="http://www.iata.org/IATA/2007/00/IATA2010.1" xmlns:app="http://xml.amadeus.com/2010/06/AppMdw_CommonTypes_v3" xmlns:ses="http://xml.amadeus.com/2010/06/Session_v3">
        <soap:Header xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
          <add:MessageID xmlns:add="http://www.w3.org/2005/08/addressing">{message_id}</add:MessageID>
          <add:Action xmlns:add="http://www.w3.org/2005/08/addressing">{soap_action}</add:Action>
          <add:To xmlns:add="http://www.w3.org/2005/08/addressing">{endpoint}</add:To>
          <link:TransactionFlowLink xmlns:link="http://wsdl.amadeus.com/2010/06/ws/Link_v1" />
          <oas:Security xmlns:oas="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
            <oas:UsernameToken xmlns:oas1="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd" oas1:Id="UsernameToken-1">
              <oas:Username>{username}</oas:Username>
              <oas:Nonce EncodingType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-soap-message-security-1.0#Base64Binary">{nonce}</oas:Nonce>
              <oas:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordDigest">{password}</oas:Password>
              <oas1:Created>{created}</oas1:Created>
            </oas:UsernameToken>
          </oas:Security>
          <AMA_SecurityHostedUser xmlns="http://xml.amadeus.com/2010/06/Security_v1">
            <UserID POS_Type="1" PseudoCityCode="{pseudo_city_code}" RequestorType="U" />
          </AMA_SecurityHostedUser>
        </soap:Header>
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
            </soapenv:Envelope>'''.format(
            message_id=str(uuid.uuid4()), soap_action=soap_action, endpoint=self.endpoint,
            username=self.user, password=base64.b64encode(password_digest).decode('utf-8'),
            nonce=base64.b64encode(nonce).decode('utf-8'),
            created=timestamp,
            duty_code=self.duty_code, pseudo_city_code=self.office_id,
        )
        self.request(self.endpoint, headers=headers, data=rq)
        return self.last_sent, self.last_received
