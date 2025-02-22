#task3lesson36.py


"""
Echo server with asyncio

Create a socket echo server which handles each connection using asyncio Tasks.
"""


import asyncio

# Define the echo server logic
async def handle_echo(reader, writer):
    """Handle client connections and echo back received data."""
    addr = writer.get_extra_info('peername')
    print(f"Connection from {addr}")

    while True:
        # Read data from the client
        data = await reader.read(100)  # Read up to 100 bytes
        if not data:
            break  # Client disconnected

        # Echo the data back to the client
        message = data.decode()
        print(f"Received from {addr}: {message}")
        writer.write(data)
        await writer.drain()  # Ensure the data is sent

    # Close the connection
    print(f"Closing connection with {addr}")
    writer.close()
    await writer.wait_closed()

# Start the server
async def start_server(host='127.0.0.1', port=12345):
    """Start the echo server."""
    server = await asyncio.start_server(handle_echo, host, port)
    addr = server.sockets[0].getsockname()
    print(f"Serving on {addr}")

    async with server:
        await server.serve_forever()  # Keep the server running


if __name__ == "__main__":
    try:
        asyncio.run(start_server())
    except KeyboardInterrupt:
        print("Server stopped.")
