import socket

HOST = '127.0.0.1'
PORT = 12345

def udp_server(host=HOST, port=PORT):
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Bind the socket to the address and port
    server_socket.bind((host, port))
    
    print(f"UDP server listening on {host}:{port}")
    
    while True:
        try:
            # Receive data from the client
            data, client_address = server_socket.recvfrom(4096)
            print(f"Received message from {client_address}: {data.decode()}")
        except KeyboardInterrupt:
            server_socket.close()
            break
        else:
            # Send a response back to the client
            response = f"Server received: {data.decode()}"
            server_socket.sendto(response.encode(), client_address)

if __name__ == "__main__":
    udp_server()
