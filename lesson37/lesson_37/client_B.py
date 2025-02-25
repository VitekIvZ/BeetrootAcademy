import socket
from threading import Thread


HOST = '127.0.0.1'
PORT = 65432


owner_name = 'user_B'

users = {}


def read_message(server):
    while True:
        data = server.recv(1024)
        # data = "user_name:message"
        print("\033[A\033[J")
        print(f"Received <= {data.decode()}")
        print("Send to=>", end='', flush=True)


def run_receive_thread(server):
    thread = Thread(target=read_message, args=(server, ), daemon=True)
    thread.start()


def run_chat():
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.connect((HOST, PORT))
        server.send(owner_name.encode())
        data = None
        run_receive_thread(server)
        while data !='!QUIT':
            incomming_data = input("Send to=>")

            server.sendall(incomming_data.encode())
            data = incomming_data.upper()


if __name__ == '__main__':
    run_chat()

