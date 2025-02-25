#task1lesson37server.py


import asyncio
import signal

# Dictionary to store connected clients and their names
clients = {}

async def broadcast(message, sender_writer=None):
    """Send a message to all connected clients except the sender."""
    if not message:
        return

    for writer in clients:
        if writer != sender_writer:
            try:
                writer.write(message.encode('utf-8'))
                await writer.drain()
            except Exception as e:
                print(f"Error broadcasting message: {e}")
                # Remove the client if sending fails
                await remove_client(writer)

async def remove_client(writer):
    """Remove a client from the list and notify others."""
    if writer in clients:
        name = clients[writer]
        del clients[writer]
        await broadcast(f"{name} has left the chat.\n", writer)
        if not writer.is_closing():
            writer.close()
            await writer.wait_closed()

async def handle_client(reader, writer):
    """Handle communication with a single client."""
    try:
        # Ask the client for their name
        writer.write("Enter your name: ".encode('utf-8'))
        await writer.drain()
        name = (await reader.read(1024)).decode('utf-8').strip()
        clients[writer] = name
        await broadcast(f"{name} has joined the chat.\n", writer)

        while True:
            # Receive messages from the client
            message = (await reader.read(1024)).decode('utf-8').strip()
            if not message:
                break

            # Check if the message is a rename command
            if message.startswith("/rename"):
                new_name = message.split(" ", 1)[1]
                clients[writer] = new_name
                writer.write(f"Your name is now {new_name}\n".encode('utf-8'))
                await writer.drain()
            else:
                # Broadcast the message to all clients
                await broadcast(f"{name}: {message}\n", writer)
    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
        # Remove the client when they disconnect
        await remove_client(writer)

async def start_server():
    """Start the server and listen for incoming connections."""
    server = await asyncio.start_server(handle_client, '0.0.0.0', 12345)
    print("Server started. Waiting for connections...")

    async with server:
        await server.serve_forever()

async def stop_server(loop, server):
    """Stop the server gracefully."""
    for task in asyncio.all_tasks(loop):
        task.cancel()
    await asyncio.gather(*asyncio.all_tasks(loop), return_exceptions=True)
    server.close()
    await server.wait_closed()
    loop.stop()
    
    
if __name__ == "__main__":    

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    server = None

    try:
        server = loop.run_until_complete(start_server())
        # Register signal handlers for graceful shutdown
        for sig in (signal.SIGINT, signal.SIGTERM):
            loop.add_signal_handler(sig, lambda: loop.create_task(stop_server(loop, server)))

        loop.run_forever()
    except asyncio.CancelledError:
        pass
    finally:
        loop.close()
        print("Server stopped.")


    


