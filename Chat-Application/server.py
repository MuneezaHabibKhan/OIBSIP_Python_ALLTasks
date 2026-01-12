import socket
import threading

host = '127.0.0.1'
port = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
names = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            name = names[index]
            names.remove(name)
            broadcast(f"{name} left the chat.".encode())
            break

def receive_connections():
    print("Server is running...")
    while True:
        client, address = server.accept()
        print(f"Connected with {address}")

        client.send("NAME".encode())
        name = client.recv(1024).decode()
        names.append(name)
        clients.append(client)

        print(f"Name of the client is {name}")
        broadcast(f"{name} joined the chat!".encode())
        client.send("Connected to server.".encode())

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

receive_connections()
