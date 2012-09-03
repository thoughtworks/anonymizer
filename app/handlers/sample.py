import logging
from lamson.routing import route, route_like, stateless
from config.settings import relay
from lamson import view

START_PREFIX='anonymize-'
REPLY_PREFIX='anonymizer-'

@route("%s(address)@(host)" % START_PREFIX, address=".+")
def START(message, address=None, host=None):
    message['from'] = 'anonymizer-328764873256@localhost'
    recipient = message['to']
    address, host = recipient[len(START_PREFIX):].split('@')
    return NEW_USER(message)

@route("%s(address)@(host)" % REPLY_PREFIX, address=".+")
def REPLY(message, address=None, host=None):
    message['from'] = START_PREFIX + message['from']
    message['to'] = 'hcorbucc@localhost'
    address, host = message['to'].split('@')
    return NEW_USER(message)

@route("(address)@(host)", address=".+")
def NEW_USER(message, address=None, host=None):
    relay.deliver(message, message['to'], message['from'])
    return NEW_USER

@route_like(NEW_USER)
def END(message, address=None, host=None):
    return NEW_USER(message, address, host)
