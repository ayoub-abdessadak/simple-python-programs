from socket import *
from tcpfuncs import string_to_binary

def send_message(client_socket: socket, message:str):
    print(f"OUTGOING: {string_to_binary(message)}")
    return client_socket.send(message.encode())

def receive_message(client_socket: socket):
    response = client_socket.recv(1024)
    print(f"INCOMING: {string_to_binary(response.decode())}")
    print(f"Received from the server: {response.decode()}")
    return response


server_name = 'localhost'
keep_alive = "keep alive"
server_port = 12000
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_port))
while True:
    message = input("Write: ")
    send_message(client_socket=client_socket, message=message)
    receive_message(client_socket=client_socket)
    client_socket.send(keep_alive.encode())


