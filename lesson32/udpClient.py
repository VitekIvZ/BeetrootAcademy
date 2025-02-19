import socket

HOST = '127.0.0.1'
PORT = 12345

def udp_client(server_host=HOST, server_port=PORT):
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Send a message to the server
    message = "Hello, UDP Server!"
    client_socket.sendto(message.encode(), (server_host, server_port))
    
    print(f"Sent message to {server_host}:{server_port}")
    
    # Receive the server's response
    data, server_address = client_socket.recvfrom(4096)
    print(f"Received response from {server_address}: {data.decode()}")
    
    # Close the socket
    client_socket.close()

if __name__ == "__main__":
    udp_client()
