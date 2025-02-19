import socket

HOST = '127.0.0.1'
PORT = 12345

def caesar_cipher_encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Encrypt only alphabetic characters
            shift = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift + key) % 26 + shift)
        else:
            encrypted_text += char  # Leave non-alphabetic characters unchanged
    return encrypted_text

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
        
            # Extract the key and message from the received data
            try:
                key, message = data.decode().split(':', 1)  # Split into key and message
                key = int(key)  # Convert key to integer
            except ValueError:
                response = "Invalid format. Send data as 'key:message'."
                server_socket.sendto(response.encode(), client_address)
                continue
        except KeyboardInterrupt:
            server_socket.close()
            break
        
        else:
            # Encrypt the message using the Caesar cipher
            encrypted_message = caesar_cipher_encrypt(message, key)
        
            # Send the encrypted message back to the client
            server_socket.sendto(encrypted_message.encode(), client_address)

if __name__ == "__main__":
    udp_server()
