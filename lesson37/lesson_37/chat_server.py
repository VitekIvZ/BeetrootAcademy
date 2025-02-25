import socket
from threading import Thread


HOST = '127.0.0.1'
PORT = 65432
clients_conn = {}  #  "user_name": conn
clients_name = {}


def init_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(10)
    server.setblocking(False)
    return server


def handle_client(conn):
    data = ''
    conn.setblocking(True)
    while True:
        received_data = conn.recv(1024)
        data = received_data.decode()
        if data.upper() == '!QUIT':
            conn.close()
            break
        
        user_message = data.split(':')
        if len(user_message)>1:
            user, message = user_message
            if user in clients_conn:
                message_to_send = f"{clients_name[conn]}:{message}"
                #print('Message', result.decode('utf-8'))
                cl_conn = clients_conn[user]
                cl_conn.send(message_to_send.encode())
            else:
                conn.send(f"Client with name '{user}' does not exists".encode())
        else:
            conn.send(b"Enter client name, please") 


def run_client_thread(conn):
    thread = Thread(target=handle_client, args=(conn, ), daemon=True)
    thread.start()


def run_chat_server():
    server = init_server()
    while True:
        try:
            conn, addr = server.accept()
            print('Connected by', addr)
            user_name = conn.recv(1024).decode()
            if user_name not in clients_conn:
                clients_conn[user_name] = conn
                clients_name[conn] = user_name
        except socket.error:
            # print('no client')
            pass
        except KeyboardInterrupt:

            server.close()
            break
        else:
            run_client_thread(conn)


if __name__ == '__main__':
    run_chat_server()