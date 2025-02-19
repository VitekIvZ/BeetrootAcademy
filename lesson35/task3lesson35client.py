#task3lesson35client.py


import socket
import random
import string

def generate_random_words(num_words=100, word_length=5):
    words = []
    for _ in range(num_words):
        word = ''.join(random.choice(string.ascii_lowercase) for _ in range(word_length))
        words.append(word)
    return words

def start_client(host='127.0.0.1', port=12345, max_iterations=10):
    """
    Start a TCP client to test the echo server.
    :param host: Server host address.
    :param port: Server port.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    try:
        for _ in range(max_iterations):
            message = generate_random_words()
            if not message:
                break
            for word in message:
                client_socket.send(word.encode('utf-8'))
                response = client_socket.recv(1024)
                print(f"Received from server: {response.decode('utf-8')}")
    finally:
        client_socket.close()
        
        

if __name__ == "__main__":
    start_client()
