#!/usr/bin/env python

import os
import sys
from collections import defaultdict

bindir = os.path.abspath(os.path.dirname(sys.argv[0]))
sys.path.append(bindir + "/../landale_python/lib")
from landale_python import *

books = defaultdict(mktdata.levelBook)

clientLoop = mktdata.clientLoop()

def tickCB(ts, tick):
    ourts = util.epochNanos()
    print(f"Got tick captured at {tick.captureTimeNanos} picked up at {ts} which we ultimately received at {ourts}")
    books[tick.id].update(tick)
    if (tick.flags & 8):
        # print book here
        print("Got consistent flag")
        
client = mktdata.client()
tickCBHolder = util.cbPython(tickCB)
client.setTickCB(tickCBHolder)
client.connect("localhost", 12345)

clientLoop.addClient(client) # client needs to be connected to add to loop

client.subscribeTicks("ETH/JPY", "KRAKEN")

while True:
    clientLoop.poll(0)
