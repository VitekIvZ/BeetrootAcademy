#task3lesson36.py


"""
Echo server with asyncio

Create a socket echo server which handles each connection using asyncio Tasks.
"""


import asyncio

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection('127.0.0.1', 12345)
    print(f"Sending: {message}")
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f"Received: {data.decode()}")

    writer.close()
    await writer.wait_closed()
    
    
if __name__ == "__main__":
    for i in range(1, 11):
        asyncio.run(tcp_echo_client(f"Hello, Server! number {i}"))
