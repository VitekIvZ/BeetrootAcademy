import socket

HOST = '127.0.0.1'  # Standard loop-back interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)

sock.setblocking(False)

while True:
    try:
        conn, addr = sock.accept()
        print('Connected by', addr)
    except socket.error:
        # print('no client')
        pass
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        result = conn.recv(1024)
        print('Message', result.decode('utf-8'))
        conn.send(result.upper())
        conn.close()

