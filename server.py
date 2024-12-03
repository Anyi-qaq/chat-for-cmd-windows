import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8') 
            if message:
                print(f"Received: {message}")
                broadcast(message, client_socket)
            else:
                remove(client_socket)
                break
        except:
            continue

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8')) 
            except:
                client.close() 
                remove(client)

def remove(client_socket):
    if client_socket in clients:
        clients.remove(client_socket) 

def start_server():
    server = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
    server.bind(('0.0.0.0',  12345))
    server.listen(5) 
    print("Server started on port 12345")

    while True:
        client_socket, addr = server.accept() 
        print(f"Connection from {addr}")
        clients.append(client_socket) 
        threading.Thread(target=handle_client, args=(client_socket,)).start()

clients = []
start_server()