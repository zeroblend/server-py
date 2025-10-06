# server.py
import asyncio
import websockets

connected = set()

async def handler(websocket, path):
    # Add new client to the connected set
    connected.add(websocket)
    try:
        async for message in websocket:
            # Broadcast message to all connected clients
            for conn in connected:
                if conn != websocket:
                    await conn.send(message)
            print(message)
    except:
        pass
    finally:
        connected.remove(websocket)

# Run the server on 0.0.0.0 and port 10000
start_server = websockets.serve(handler, "0.0.0.0", 10000)

print("Server running on port 10000...")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
