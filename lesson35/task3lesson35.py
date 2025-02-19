#task3lesson35.py


"""
Echo server with multiprocessing

Create a socket echo server that handles each connection using the multiprocessing library.
"""

import socket
import multiprocessing


def handle_connection(client_socket, client_address):
    """
    Handle a client connection.
    :param client_socket: Socket object for the client.
    :param client_address: Address of the client.
    """
    print(f"Connection established with {client_address}")
    try:
        while True:
            data = client_socket.recv(1024)  # Receive data from the client
            if not data:
                break  # If no data is received, close the connection
            print(f"Received from {client_address}: {data.decode('utf-8')}")
            client_socket.send(data)  # Echo the data back to the client
    except Exception as e:
        print(f"Error handling connection with {client_address}: {e}")
    finally:
        client_socket.close()
        print(f"Connection closed with {client_address}")
        
        
def start_server(host='127.0.0.1', port=12345):
    """
    Start the echo server.
    :param host: Host address to bind the server.
    :param port: Port to bind the server.
    """
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    try:
        while True:
            # Wait for a connection
            client_socket, client_address = server_socket.accept()
            print(f"Accepted connection from {client_address}")

            # Create a new process to handle the connection
            process = multiprocessing.Process(
                target=handle_connection,
                args=(client_socket, client_address)
            )
            process.start()

            # Close the client socket in the parent process
            client_socket.close()
    except KeyboardInterrupt:
        print("Server shutting down...")
    finally:
        server_socket.close()
        
        
if __name__ == "__main__":
    start_server()
