from nose.tools import *
from lamson.testing import *
import os
from lamson import server

relay = relay(port=8823)
client = RouterConversation("somedude@localhost", "requests_tests")
confirm_format = "testing-confirm-[0-9]+@"
noreply_format = "testing-noreply@"


def test_forwards_relay_host():
    """
    !!!!!! YOU MUST CONFIGURE YOUR config/settings.py OR THIS WILL FAIL !!!!!!
    Makes sure that your config/settings.py is configured to forward mail from
    localhost (or your direct host) to your relay.
    """
    client.begin()
    client.deliver("tester@localhost", "somedude@localhost", "Test that forward works.", "Test")

    #assert delivered("tester@localhost"), "Expected %r when sending to %r with '%s:%s' message." % ("tester@localhost", "somedude@localhost", "Test", "Test that forward works.")


def test_drops_open_relay_messages():
    """
    But, make sure that mail NOT for test.com gets dropped silently.
    """
    client.begin()
    client.say("tester@badplace.notinterwebs", "Relay should not happen")
    assert queue().count() == 0, "You are configured currently to accept everything.  You should change config/settings.py router_defaults so host is your actual host name that will receive mail."

def test_removes_prefix():
    """
    If I email anonymize-ckozak@localhost, an email is shot to ckozak@localhost
    """
    client.begin()
    client.say("anonymize-ckozak@localhost", "Test that redirect works", "ckozak@localhost")
    assert queue().count() == 1, "An email was not sent"

def test_changes_from_email():
    """
    If hcorbucc@localhost emails anonymize-ckozak@localhost, an email is shot from a hashed recipient
    """
    client = RouterConversation("hcorbucc@localhost", "requests_tests")
    client.begin()
    client.say("anonymize-ckozak@localhost", "Test that redirect works", "ckozak@localhost")
    incoming = queue()
    assert incoming.count() == 1, "An email was not sent"
    key, msg = incoming.pop()
    assert msg['from'] != 'hcorbucc@localhost', "hcorbucc@localhost should not be the sender of %s" % msg

def test_follows_up_existing_conversation():
    """
    If ckozak@localhost emails anonymizer-328764873256@localhost, an email is shot from to hcorbucc@localhost from anonymize-ckozak@localhost
    """
    client = RouterConversation("ckozak@localhost", "reply_tests")
    client.begin()
    client.say("anonymizer-328764873256@localhost", "Test that answer works", "hcorbucc@localhost")


#Remove extra to/cc