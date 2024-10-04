from socket import *
from tcpfuncs import string_to_binary

server_port = 12000
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', server_port))
server_socket.listen(1)
print("Lets receive some messages")
while True:
    # Three way handshake*
    connection_socket, addr = server_socket.accept()
    sentence = connection_socket.recv(1024).decode()
    capitalized_sentence = sentence.upper()
    print(f"INCOMING: {string_to_binary(sentence)}")
    print(f"INCOMING MESSAGE: {sentence}")
    connection_socket.send(capitalized_sentence.encode())
    print(f"OUTGOING: {string_to_binary(capitalized_sentence)}")
    print(f"OUTGOING MESSAGE: {capitalized_sentence}")
    print("----------------------------------------------\n")