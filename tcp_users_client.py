import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ("localhost", 12345)
client_socket.connect(server_address)

message = "Привет, серверdas!"
client_socket.send(message.encode())

history = client_socket.recv(4096).decode()
if history:
    print(history + '\n')


response = client_socket.recv(1024).decode()
print(f'{response}')

client_socket.close()