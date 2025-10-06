# client.py
import asyncio
import websockets

async def chat():
    username = input("Enter your username: ")
    server_ip = input("Enter server IP or hostname (Render example: your-server.onrender.com): ")
    port = 10000

    uri = f"ws://{server_ip}:{port}"
    async with websockets.connect(uri) as websocket:
        print(f"Connected to {server_ip}:{port} as {username}")
        print("Type messages. Type EXIT to quit.\n")

        async def send_messages():
            while True:
                msg = input()
                if msg.upper() == "EXIT":
                    break
                await websocket.send(f"{username}: {msg}")

        async def receive_messages():
            async for message in websocket:
                print(message)

        await asyncio.gather(send_messages(), receive_messages())

asyncio.run(chat())
