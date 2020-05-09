import socket
import random
import time

while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('172.17.137.85', 8081))
    r = random.randint(0,100)
    print('sending data %s' % r)
    sock.send(b'test data %s\n' % r)
    sock.close()
    time.sleep(1)