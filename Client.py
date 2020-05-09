# Client
import socket
print('starting client application...')
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('172.17.137.85', 8081))
while True:
    serv.listen(5)
    conn, addr = serv.accept()
    from_client = ''
    while True:
        data = conn.recv(4096)
        if not data: break
        from_client += data
    print(from_client)
    conn.close()