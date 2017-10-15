from __future__ import unicode_literals
from hackathon import *

lastUpdateID = None
while True:
    updates = getUpdates(lastUpdateID)
    if len(updates["result"]) > 0:
        lastUpdateID = getLatestUpdateID(updates) + 1
        for update in updates["result"]:
            message,who = extract(update)
            try:
            	print "from", who, "message", message
            except:
            	pass
            reply = process(message)
            sendMessage(reply,who)
            print "reply sent"