import socket

HOST = '127.0.0.1'
PORT = 4000

client = socket.socket()

client.connect((HOST, PORT))

client.sendall(b'Hello world')
data = client.recv(1024)
client.close()
print("Receved: ", repr(data))