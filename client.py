import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8') 
            if message:
                print(message)
            else:
                break
        except:
            print("Connection closed")
            client_socket.close() 
            break

def send_messages(client_socket):
    while True:
        message = input()
        client_socket.send(message.encode('utf-8')) 

def start_client():
    client = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
    client.connect(('127.0.0.1',  12345))

    threading.Thread(target=receive_messages, args=(client,)).start()
    send_messages(client)

start_client()