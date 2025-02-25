#task1lesson37client.py


import asyncio

async def receive_messages(reader):
    """Receive and display messages from the server."""
    while True:
        try:
            message = await reader.read(1024)
            if not message:
                print("Disconnected from the server.")
                break
            print(message.decode('utf-8'), end='')
        except:
            print("Disconnected from the server.")
            break

async def send_messages(writer):
    """Send messages to the server."""
    while True:
        message = await asyncio.get_event_loop().run_in_executor(None, input)
        if message.lower() == "/quit":
            break
        writer.write(message.encode('utf-8'))
        await writer.drain()

    writer.close()
    await writer.wait_closed()

async def start_client():
    """Start the client and connect to the server."""
    reader, writer = await asyncio.open_connection('127.0.0.1', 12345)

    # Start tasks to receive and send messages
    receive_task = asyncio.create_task(receive_messages(reader))
    send_task = asyncio.create_task(send_messages(writer))

    await asyncio.gather(receive_task, send_task)

if __name__ == "__main__":
    asyncio.run(start_client())
