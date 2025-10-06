# server.py
import socket
import threading

clients = []

def handle_client(client):
    while True:
        try:
            msg = client.recv(1024).decode()
            if msg:
                print(msg)
                for c in clients:
                    if c != client:
                        c.send(msg.encode())
            else:
                clients.remove(client)
                client.close()
                break
        except:
            clients.remove(client)
            client.close()
            break

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5000))
server.listen(5)
print("Server listening on port 5000...")

while True:
    client, addr = server.accept()
    clients.append(client)
    threading.Thread(target=handle_client, args=(client,)).start()
