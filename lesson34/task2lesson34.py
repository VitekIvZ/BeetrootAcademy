#task2lesson34.py


"""
    Echo server with threading

Create a socket echo server which handles each connection in a separate Thread
"""


import socket
import threading

HOST = '127.0.0.1'  # Standard loop-back interface address (localhost)
PORT = 12345       # Port to listen on (non-privileged ports are > 1023)

# Функція для обробки клієнтських підключень
def handle_client(client_socket):
    while True:
        # Отримання даних від клієнта
        data = client_socket.recv(1024)
        if not data:
            break
        # Відправка отриманих даних назад клієнту (ехо)
        client_socket.sendall(data)
    # Закриття підключення
    client_socket.close()

def main():
    # Створення сокета
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Сервер запущено і слухає на порту {PORT}")

    while True:
        try:
            # Прийняття нового підключення
            client_socket, addr = server_socket.accept()
            print(f"Підключено клієнта: {addr}")
        except KeyboardInterrupt:
            client_socket.close()
            break
        else:
            # Створення нового потоку для обробки підключення
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.start()

if __name__ == "__main__":
    main()