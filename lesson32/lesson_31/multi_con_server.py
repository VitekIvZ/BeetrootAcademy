import socket
import selectors
import types


HOST = '127.0.0.1' 
PORT = 65432


def accept_wrapper(sock):
    conn, addr = sock.accept()
    print('Connected by', addr)
    conn.setblocking(False)

    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)


def selvice_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        resv_data = sock.recv(1024)
        if resv_data:
            data.outb += resv_data
        else:
            print("Closeing conn")
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            sent = sock.send(data.outb)
            data.outb = data.outb[sent:]


if __name__ == '__main__':
    sel = selectors.DefaultSelector()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(1)

    sock.setblocking(False)
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(sock, events, data=None)

    try:
        while True:
            events = sel.select(timeout=0.5)
            for key, mask in events:
                if key.data is None:
                    accept_wrapper(key.fileobj)
                else:
                    selvice_connection(key, mask)
    except KeyboardInterrupt:
        print("Keyboard Interrupt")
    finally:
        sel.close()